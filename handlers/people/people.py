#!/usr/bin/env Python
# coding=utf-8
import logging

import tornado.web
import methods.db as mdb
import json
import url
class CommitPeopleHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            uploader = self.get_argument("username")
            name = self.get_argument("name")
            nationality = self.get_argument("nationality", default=None)
            birthplace = self.get_argument("birthplace", default=None)
            residence = self.get_argument("residence", default=None)
            grave_place = self.get_argument("grave_place", default=None)
            birth_day = self.get_argument("birth_day", default=None)
            death_day = self.get_argument("death_day", default=None)
            motto = self.get_argument("motto", default=None)
            industry = self.get_argument("industry", default=None)
            cover_url = self.get_argument("cover_url", default=None)
            time_stamp = self.get_argument("time_stamp")
            draft_people_id = self.get_argument("draft_people_id")
            line = mdb.select_draft_people(draft_people_id)
            event_ids = line[12]
            description_id = line[13]
            people_id = mdb.insert_people\
                (uploader, name, time_stamp, cover_url, nationality, birthplace, residence, grave_place, birth_day, death_day, motto, industry, event_ids, description_id)
            data = {}
        except BaseException as e:
            data['code'] = -1
            data['msg'] = "insert error"
            logging.exception(e)
        else:
            data['code'] = 0
            data['msg'] = "insert success"
            data['people_id'] = people_id
        self.write(json.dumps(data))