#!/usr/bin/env Python
# coding=utf-8
import logging

import tornado.web
import methods.db as mdb
import json
import url

#提交人物事件
class CommitPeopleEventsHandler(tornado.web.RequestHandler):
    def post(self):
        uploader = self.get_argument("username")
        time_stamp = self.get_argument("time_stamp")
        draft_people_id = self.get_argument("draft_people_id")
        event_text = self.get_argument("event_text")
        event_title = self.get_argument("event_title")
        data = {}
        try:
            #插入数据到people_event表
            people_event_id_new = mdb.insert_people_event(uploader=uploader,
                                                          time_stamp=time_stamp,
                                                          event_text=event_text,
                                                          event_title=event_title,
                                                          draft_people_id=draft_people_id)
            people_event_id_old = mdb.select_draft_people_event_ids(draft_people_id)
            if people_event_id_old[0] is None:
                people_event_id = people_event_id_new
            else:
                people_event_id = people_event_id_old[0] + "," + str(people_event_id_new)
            #TODO 确认返回的格式

            # 更新数据表
            mdb.update_draft_people_event_id(draft_people_id=draft_people_id,
                                             time_stamp=time_stamp,
                                             event_ids=people_event_id)
        except BaseException as e:
            data['code'] = -1
            data['msg'] = "commit people event error"
            logging.exception(e)
        else:
            # 删除草稿中的数据
            try:
                mdb.delete_draft_people_event(draft_people_id)
            except BaseException as e:
                logging.exception(e)
            else:
                data['code'] = 0
                data['msg'] = "commit people event success"
                data['people_event_id'] = people_event_id_new
        self.write(json.dumps(data))

#从人物事件草稿中获取人物事件文本和标题
class GetPeopleEventFromDraftHandler(tornado.web.RequestHandler):
    def post(self):
        draft_people_event_id = self.get_argument("draft_people_event_id")
        data = {}
        try:
            lines = mdb.select_draft_people_event(draft_people_event_id)
        except BaseException as e:
            data['code'] = -1
            data['msg'] = "get people event draft error"
            logging.exception(e)
        else:
            data['code'] = 0
            data['msg'] = "get people event draft success"
            # TODO 确认返回的格式
            data['event_title'] = lines[0][2]
            data['event_text'] = lines[0][3]
        self.write(json.dumps(data))

#从人物描述中获取人物描述文本
class GetPeopleEventHandler(tornado.web.RequestHandler):
    def post(self):
        people_event_id = self.get_argument("people_event_id")
        data = {}
        try:
            lines = mdb.select_people_event(people_event_id=people_event_id)
        except BaseException as e:
            data['code'] = -1
            data['msg'] = "commit people event error"
            logging.exception(e)
        else:
            data['code'] = 0
            data['msg'] = "commit people event success"
            # TODO 确认返回的格式
            data['event_title'] = lines[0][2]
            data['event_text'] = lines[0][3]
        self.write(json.dumps(data))