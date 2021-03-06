

#!/usr/bin/env Python
# coding=utf-8
import logging

import tornado.web
import methods.db as mdb
import json
import url
class DraftPeopleDescriptionHandler(tornado.web.RequestHandler):
    def post(self):
        uploader = self.get_argument("username")
        time_stamp = self.get_argument("time_stamp")
        draft_people_id = self.get_argument("draft_people_id", default=None)
        people_id = self.get_argument("people_id", default=None)
        description_text = self.get_argument("description_text")
        data = {}
        # 保存或更新人物描述的草稿
        try:
            if mdb.is_draft_people_description_exist(draft_people_id=draft_people_id, people_id=people_id):
                draft_people_description_id = mdb.update_draft_people_description(uploader=uploader,
                                                                                  time_stamp=time_stamp,
                                                                                  draft_people_id=draft_people_id,
                                                                                  description_text=description_text,
                                                                                  people_id=people_id)
                print("update_draft_people_description")
            else:
                draft_people_description_id = mdb.insert_draft_people_description(uploader=uploader,
                                                                                  time_stamp=time_stamp,
                                                                                  draft_people_id=draft_people_id,
                                                                                  description_text=description_text,
                                                                                  people_id=people_id)
                if people_id is not None:
                    mdb.update_people_draft_description_id(people_id=people_id, time_stamp=time_stamp, draft_people_description_id=draft_people_description_id)
                elif draft_people_id is not None:
                    mdb.update_draft_people_draft_people_description_id(draft_people_id=draft_people_id, time_stamp=time_stamp, draft_people_description_id=draft_people_description_id)
                print("insert_draft_people_description")
        except BaseException as e:
            data['code'] = -1
            data['msg'] = "save people description draft error"
            logging.exception(e)
        else:
            data['code'] = 0
            data['msg'] = "save people description draft success"
            data['draft_people_description_id'] = draft_people_description_id
        self.write(json.dumps(data))

#删除人物描述草稿
class DeleteDraftPeopleDescriptionHandler(tornado.web.RequestHandler):
    def post(self):
        draft_people_description_id = self.get_argument("draft_people_description_id")
        data = {}
        try:
            line = mdb.select_draft_people_description(draft_people_description_id)
            people_id = line[3]
            draft_people_id = line[2]
            mdb.delete_draft_people_description(people_id=people_id,draft_people_id=draft_people_id)
        except BaseException as e:
            data['code'] = -1
            data['msg'] = "delete people description draft error"
            logging.exception(e)
        else:
            data['code'] = 0
            data['msg'] = "delete people description draft success"
        self.write(json.dumps(data))