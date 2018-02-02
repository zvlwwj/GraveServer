#!/usr/bin/env Python
# coding=utf-8
import logging

import tornado.web
import methods.db as mdb
import json
import url

#提交人物描述
class CommitPeopleDescriptionHandler(tornado.web.RequestHandler):
    def post(self):
        uploader = self.get_argument("username")
        time_stamp = self.get_argument("time_stamp")
        draft_people_id = self.get_argument("draft_people_id")
        description_text = self.get_argument("description_text")
        data = {}
        try:
            #插入数据到people_description表
            people_description_id = mdb.insert_people_description(uploader=uploader,
                                                                  time_stamp=time_stamp,
                                                                  description_text=description_text,
                                                                  draft_people_id=draft_people_id)
            # 更新数据表
            mdb.update_draft_people_description_id(draft_people_id=draft_people_id,
                                                   time_stamp=time_stamp,
                                                   description_id=people_description_id)
        except BaseException as e:
            data['code'] = -1
            data['msg'] = "commit people description error"
            logging.exception(e)
        else:
            # 删除草稿中的数据
            try:
                mdb.delete_draft_people_description(draft_people_id)
            except BaseException as e:
                logging.exception(e)
            else:
                data['code'] = 0
                data['msg'] = "commit people description success"
                data['people_description_id'] = people_description_id
        self.write(json.dumps(data))

#从人物描述草稿中获取人物描述文本
class GetPeopleDescriptionFromDraftHandler(tornado.web.RequestHandler):
    def post(self):
        draft_people_description_id = self.get_argument("draft_people_description_id")
        data = {}
        try:
            lines = mdb.select_draft_people_description(draft_people_description_id)
        except BaseException as e:
            data['code'] = -1
            data['msg'] = "commit people description error"
            logging.exception(e)
        else:
            data['code'] = 0
            data['msg'] = "commit people description success"
            print(lines)
            data['description_text'] = lines[0][3]
        self.write(json.dumps(data))

#从人物描述中获取人物描述文本
class GetPeopleDescriptionHandler(tornado.web.RequestHandler):
    def post(self):
        people_description_id = self.get_argument("people_description_id")
        data = {}
        try:
            lines = mdb.select_people_description(people_description_id)
        except BaseException as e:
            data['code'] = -1
            data['msg'] = "commit people description error"
            logging.exception(e)
        else:
            data['code'] = 0
            data['msg'] = "commit people description success"
            print(lines)
            data['description_text'] = lines[0][2]
        self.write(json.dumps(data))