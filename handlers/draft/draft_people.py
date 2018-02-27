#!/usr/bin/env Python
# coding=utf-8
import tornado.web
import methods.db as mdb
import json
import url
import logging
class InsertDraftPeopleHandler(tornado.web.RequestHandler):
    def post(self):
        cover_url = self.get_argument("cover_url", default=None)
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
        alive = self.get_argument("alive")
        event_ids = self.get_argument("event_ids", default=None)
        description_id = self.get_argument("description_id", default=None)
        data = {}
        try:
            draft_people_id = mdb.insert_draft_people(uploader=uploader, name=name, time_stamp=time_stamp,
                                                      cover_url=cover_url, nationality=nationality, birthplace=birthplace,
                                                      residence=residence, grave_place=grave_place, birth_day=birth_day,
                                                      death_day=death_day, motto=motto, industry=industry, alive=alive,
                                                      event_ids=event_ids, description_id=description_id)
            # 从用户表中查询该用户的人物草稿
            old_draft_people_ids = mdb.select_user_draft_people(user_name=uploader)[0]
            print("old_draft_people_ids" + str(old_draft_people_ids))
            if old_draft_people_ids is None:
                new_draft_people_ids = str(draft_people_id)
            else:
                new_draft_people_ids = old_draft_people_ids+","+str(draft_people_id)
            print("new_draft_people_ids"+str(new_draft_people_ids))
            # 将新的草稿id更新到用户表
            mdb.update_user_draft_people(user_name=uploader, draft_people_ids=new_draft_people_ids)
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
        cover_url = self.get_argument("cover_url", default=None)
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
        alive = self.get_argument("alive")
        data = {}
        try:
            draft_people_id = mdb.update_draft_people(draft_people_id=draft_people_id, uploader=uploader, name=name, time_stamp=time_stamp,
                                                      cover_url=cover_url, nationality=nationality,
                                                      birthplace=birthplace, residence=residence,
                                                      grave_place=grave_place, birth_day=birth_day, death_day=death_day,
                                                      motto=motto, industry=industry,alive=alive)
        except BaseException as e:
            logging.exception(e)
            data['code'] = -1
            data['msg'] = "update people draft fail"
        else:
            data['code'] = 0
            data['msg'] = "update people draft success"
            data['draft_people_id'] = draft_people_id
        self.write(json.dumps(data))

class GetDraftPeopleSample(tornado.web.RequestHandler):
    def post(self):
        try:
            data = {}
            user_id = self.get_argument("user_id")
            draft_people_ids = mdb.select_user_draft_people_ids(condition="user_id", value=user_id)
            print(draft_people_ids)
            if draft_people_ids[0] is not None:
                ids = draft_people_ids[0].split(',')
                infos = []
                for id in ids:
                    line = mdb.select_draft_people_info(id)
                    name = line[2]
                    cover_url = line[3]
                    description_id = line[14]
                    if description_id is not None:
                        description_text = mdb.select_people_description(description_id)[2]
                    else:
                        description_text = None
                    info = {"name": name, "coverUrl": cover_url, "descriptionText": description_text, "draft_people_id": id}
                    infos.append(info)
                data['infos'] = infos
        except BaseException as e:
            data['code'] = -1
            data['msg'] = "get creation people sample error"
            logging.exception(e)
        else:
            data['code'] = 0
            data['msg'] = "get creation people sample success"
        self.write(json.dumps(data))

class GetDraftPeopleHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            data = {}
            draft_people_id = self.get_argument("draft_people_id")
            line = mdb.select_draft_people_info(draft_people_id=draft_people_id)
            uploader = line[1]
            name = line[2]
            cover_url = line[3]
            alive = line[4]
            nationality = line[5]
            birthplace = line[6]
            residence = line[7]
            grave_place = line[8]
            birth_day = line[9]
            death_day = line[10]
            motto = line[11]
            industry = line[12]
            event_ids = line[13]
            events = []
            if event_ids is not None:
                ids = event_ids.split(",")
                for event_id in ids:
                    title = mdb.select_people_event(event_id)[2]
                    event_text = mdb.select_people_event(event_id)[3]
                    event = {"event_id": event_id, "event_title": title, "event_text": event_text}
                    events.append(event)
            description_id = line[14]
            description_text = None
            if description_id is not None:
                description_text = mdb.select_people_description(description_id)[2]
            description = {"description_id": description_id, "description_text": description_text}
            draft_people_description_id = line[16]
            draft_people_event_ids = line[17]
            print("draft_people_event_ids"+str(draft_people_event_ids))
            draft_events = []
            if draft_people_event_ids is not None:
                ids = draft_people_event_ids.split(",")
                print("ids" + str(ids))
                for draft_event_id in ids:
                    title = mdb.select_draft_people_event(draft_event_id)[4]
                    event_text = mdb.select_draft_people_event(draft_event_id)[5]
                    draft_event = {"draft_event_id": draft_event_id, "draft_event_title": title,
                                   "draft_event_text": event_text}
                    draft_events.append(draft_event)
            info = {"name": name,"cover_url":cover_url,"alive":alive,"nationality":nationality,"birthplace":birthplace,"residence":residence
                ,"grave_place":grave_place,"birth_day":birth_day,"death_day":death_day,"description":description,"motto":motto,"industry":industry,"events":events
                ,"uploader":uploader,"draft_people_description_id":draft_people_description_id,"draftEvents":draft_events}
            data['info'] = info
        except BaseException as e:
            data['code'] = -1
            data['msg'] = "get people error"
            logging.exception(e)
        else:
            data['code'] = 0
            data['msg'] = "get people success"
        self.write(json.dumps(data))