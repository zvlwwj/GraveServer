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
        draft_people_id = self.get_argument("draft_people_id", default=None)
        people_id = self.get_argument("people_id", default=None)
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
            print("draft_people_event_id"+str(draft_people_event_id))
            if people_id is not None:
                old_draft_event_ids = mdb.select_people_draft_event_ids(people_id=people_id)[0]
                if old_draft_event_ids is not None and len(str(old_draft_event_ids))>0:
                    new_draft_event_ids = old_draft_event_ids + "," + str(draft_people_event_id)
                else:
                    new_draft_event_ids = draft_people_event_id
                mdb.update_people_draft_event_ids(people_id=people_id, time_stamp=time_stamp, draft_people_event_ids=new_draft_event_ids)

            if draft_people_id is not None:
                old_draft_event_ids = mdb.select_draft_people_draft_event_ids(draft_people_id=draft_people_id)[0]
                print("old_draft_event_ids" + str(old_draft_event_ids))
                if old_draft_event_ids is not None and len(str(old_draft_event_ids))>0:
                    new_draft_event_ids = old_draft_event_ids + "," + str(draft_people_event_id)
                else:
                    new_draft_event_ids = draft_people_event_id
                print("new_draft_event_ids" + str(new_draft_event_ids))
                mdb.update_draft_people_draft_event_ids(draft_people_id=draft_people_id, time_stamp=time_stamp, draft_people_event_ids=new_draft_event_ids)
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
        data = {}
        try:
            mdb.update_draft_people_event(uploader=uploader,
                                          time_stamp=time_stamp,
                                          draft_people_event_id=draft_people_event_id,
                                          event_title=event_title,
                                          event_text=event_text)
        except BaseException as e:
            data['code'] = -1
            data['msg'] = "save people description draft error"
            logging.exception(e)
        else:
            data['code'] = 0
            data['msg'] = "save people description draft success"
        self.write(json.dumps(data))