#!/usr/bin/env Python
# coding=utf-8
import tornado.web
import methods.db as mdb
import json
import url
import logging
class InsertDraftPeopleHandler(tornado.web.RequestHandler):
    def post(self):
        global cover_url
        files = self.request.files
        if not files:
            cover_url = ""
        else:
            img_cover = files.get("cover")
            for img in img_cover:
                with open('./statics/draft/cover/people/' + img['filename'], 'wb') as f:
                    f.write(img['body'])
                    cover_url = url.base_url + '/statics/draft/cover/people/' + img['filename']

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
        time_stamp = self.get_argument("time_stamp")
        data = {}
        try:
            draft_people_id = mdb.insert_draft_people(uploader=uploader, name=name, time_stamp=time_stamp,
                                                      cover_url=cover_url, nationality=nationality, birthplace=birthplace, residence=residence, grave_place=grave_place, birth_day=birth_day, death_day=death_day, motto=motto, industry=industry)
        except BaseException as e:
            logging.exception(e)
            data['code'] = -1
            data['msg'] = "save people draft fail"
        else:
            data['code'] = 0
            data['msg'] = "save people draft success"
            data['draft_people_id'] = draft_people_id
        self.write(json.dumps(data))
class UpdateDraftPeopleHandler(tornado.web.RequestHandler):
    def post(self):
        global cover_url
        files = self.request.files
        if not files:
            cover_url = ""
        else:
            img_cover = files.get("cover")
            for img in img_cover:
                with open('./statics/draft/cover/people/' + img['filename'], 'wb') as f:
                    f.write(img['body'])
                    cover_url = url.base_url + '/statics/draft/cover/people/' + img['filename']
        draft_people_id = self.get_argument("draft_people_id")
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
        time_stamp = self.get_argument("time_stamp")
        data = {}
        try:
            draft_people_id = mdb.update_draft_people(draft_people_id=draft_people_id, uploader=uploader, name=name, time_stamp=time_stamp,
                                                      cover_url=cover_url, nationality=nationality,
                                                      birthplace=birthplace, residence=residence,
                                                      grave_place=grave_place, birth_day=birth_day, death_day=death_day,
                                                      motto=motto, industry=industry)
        except BaseException as e:
            logging.exception(e)
            data['code'] = -1
            data['msg'] = "update people draft fail"
        else:
            data['code'] = 0
            data['msg'] = "update people draft success"
            data['draft_people_id'] = draft_people_id
        self.write(json.dumps(data))