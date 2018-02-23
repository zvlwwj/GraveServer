#!/usr/bin/env Python
# coding=utf-8
import logging

import tornado.web
import methods.db as mdb
import json
import url
# 提交人物事件的草稿
class CommitDraftPeopleDescriptionHandler(tornado.web.RequestHandler):
    def post(self):
        uploader = self.get_argument("username")
        time_stamp = self.get_argument("time_stamp")
        draft_people_id = self.get_argument("draft_people_id")
        people_id = self.get_argument("people_id")
        event_title = self.get_argument("event_title")
        event_text = self.get_argument("event_text")
        data = {}

        try:
            draft_people_event_id = mdb.insert_draft_people_event(uploader=uploader,
                                                                  time_stamp=time_stamp,
                                                                  draft_people_id=draft_people_id,
                                                                  title=event_title,
                                                                  event_text=event_text,
                                                                  people_id=people_id)
        except BaseException as e:
            data['code'] = -1
            data['msg'] = "save people event draft error"
            logging.exception(e)
        else:
            data['code'] = 0
            data['msg'] = "save people event draft success"
            data['draft_people_event_id'] = draft_people_event_id
        self.write(json.dumps(data))

# 更新人物事件的草稿
class UpdateDraftPeopleDescriptionHandler(tornado.web.RequestHandler):
    def post(self):
        uploader = self.get_argument("username")
        time_stamp = self.get_argument("time_stamp")
        draft_people_event_id = self.get_argument("draft_people_event_id")
        event_title = self.get_argument("event_title")
        event_text = self.get_argument("event_text")
        people_id = self.get_argument("people_id")
        data = {}
        try:
            mdb.update_draft_people_event(uploader=uploader,
                                          time_stamp=time_stamp,
                                          draft_people_event_id=draft_people_event_id,
                                          event_title=event_title,
                                          event_text=event_text,
                                          people_id=people_id)
        except BaseException as e:
            data['code'] = -1
            data['msg'] = "save people description draft error"
            logging.exception(e)
        else:
            data['code'] = 0
            data['msg'] = "save people description draft success"
        self.write(json.dumps(data))