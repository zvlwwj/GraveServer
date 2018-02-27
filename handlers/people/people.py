#!/usr/bin/env Python
# coding=utf-8
import logging

import tornado.web
import methods.db as mdb
import json
import url
class CommitPeopleHandler(tornado.web.RequestHandler):
    def post(self):
        data = {}
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
            draft_people_id = self.get_argument("draft_people_id", default=None)
            alive = self.get_argument("alive", default=0)
            event_ids = None
            description_id = None
            draft_people_description_id = None
            draft_people_event_ids = None
            if draft_people_id is not None:
                line = mdb.select_draft_people(draft_people_id)
                event_ids = line[13]
                description_id = line[14]
                draft_people_description_id = line[16]
                draft_people_event_ids = line[17]
            # 插入people表中
            people_id = mdb.insert_people(uploader=uploader, name=name, time_stamp=time_stamp, cover_url=cover_url, nationality=nationality, birthplace=birthplace
                                          , residence=residence, grave_place=grave_place, birth_day=birth_day, death_day=death_day, motto=motto, industry=industry
                                          , event_ids=event_ids, description_id=description_id, alive=alive, draft_people_description_id=draft_people_description_id
                                          , draft_people_event_ids=draft_people_event_ids)
            # 更新原本绑定在草稿中的事件和描述(从绑定草稿到绑定people)
            if draft_people_id is not None:
                mdb.update_people_event_use_draft_people_id(draft_people_id=draft_people_id, people_id=people_id)
                mdb.update_draft_people_event_use_draft_people_id(draft_people_id=draft_people_id, people_id=people_id)

            # 将people_id 更新到user表中
            old_people_ids = mdb.select_user_people_ids(condition="user_name", value=uploader)
            if old_people_ids[0] is not None:
                new_people_ids = str(old_people_ids[0]) + "," + str(people_id)
            else:
                new_people_ids = str(people_id)

            print(new_people_ids)
            mdb.update_user_people_ids(new_people_ids)
            # 删除draft_people数据
            if draft_people_id is not None:
                mdb.delete_draft_people(draft_people_id=draft_people_id)
                # 更新user表中的draft_people_ids
                old_people_draft_ids = mdb.select_user_draft_people(user_name=uploader)[0]
                print("old_people_draft_ids"+str(old_people_draft_ids))
                if old_people_draft_ids is not None:
                    new_people_draft_ids = None
                    if "," not in old_people_draft_ids:
                        new_people_draft_ids = None
                    else:
                        if ","+str(draft_people_id) in old_people_draft_ids:
                            new_people_draft_ids = old_people_draft_ids.replace(","+str(draft_people_id), '')
                        elif str(draft_people_id)+"," in old_people_draft_ids:
                            new_people_draft_ids = old_people_draft_ids.replace(str(draft_people_id)+",", '')
                    print("new_people_draft_ids" + str(new_people_draft_ids))
                    mdb.update_user_draft_people(user_name=uploader, draft_people_ids=new_people_draft_ids)
        except BaseException as e:
            data['code'] = -1
            data['msg'] = "insert error"
            logging.exception(e)
        else:
            data['code'] = 0
            data['msg'] = "insert success"
            data['people_id'] = people_id
        self.write(json.dumps(data))

class UpdatePeopleHandler(tornado.web.RequestHandler):
    def post(self):
        data = {}
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
            alive = self.get_argument("alive", default=0)
            people_id = self.get_argument("people_id")
            # 更新people表
            mdb.update_people(uploader=uploader, name=name, time_stamp=time_stamp, cover_url=cover_url, nationality=nationality, birthplace=birthplace, residence=residence, grave_place=grave_place, birth_day=birth_day, death_day=death_day, motto=motto, industry=industry, alive=alive, people_id=people_id)
        except BaseException as e:
            data['code'] = -1
            data['msg'] = "insert error"
            logging.exception(e)
        else:
            data['code'] = 0
            data['msg'] = "insert success"
            data['people_id'] = people_id
        self.write(json.dumps(data))

class GetCreationPeopleSample(tornado.web.RequestHandler):
    def post(self):
        data = {}
        try:
            user_id = self.get_argument("user_id")
            people_ids = mdb.select_user_people_ids(condition="user_id", value=user_id)
            print(people_ids)
            if people_ids[0] is not None:
                ids = people_ids[0].split(',')
                infos = []
                for id in ids:
                    line = mdb.select_people_info(id)
                    people_id = line[0]
                    name = line[1]
                    cover_url = line[2]
                    description_id = line[12]
                    print("description_id"+str(description_id))
                    description_text = None
                    if description_id is not None:
                        description_text = mdb.select_people_description(description_id)[2]
                    info = {"name": name, "coverUrl": cover_url, "descriptionText": description_text, "people_id": people_id}
                    infos.append(info)
                print(infos)
                data['infos'] = infos
        except BaseException as e:
            data['code'] = -1
            data['msg'] = "get creation people sample error"
            logging.exception(e)
        else:
            data['code'] = 0
            data['msg'] = "get creation people sample success"
        self.write(json.dumps(data))

class GetPeopleHandler(tornado.web.RequestHandler):
    def post(self):
        data = {}
        try:
            people_id = self.get_argument("people_id")
            line = mdb.select_people_info(people_id=people_id)
            name = line[1]
            cover_url = line[2]
            alive = line[3]
            nationality = line[4]
            birthplace = line[5]
            residence = line[6]
            grave_place = line[7]
            birth_day = line[8]
            death_day = line[9]
            article_ids = line[10]
            reputation = line[11]
            description_id = line[12]
            description_text = None
            if description_id is not None:
                description_text = mdb.select_people_description(description_id)[2]
            description = {"description_id": description_id, "description_text": description_text}
            comment_count = line[13]
            motto = line[14]
            industry = line[15]
            event_ids = line[16]
            events = []
            if event_ids is not None:
                ids = event_ids.split(",")
                for event_id in ids:
                    title = mdb.select_people_event(event_id)[2]
                    event_text = mdb.select_people_event(event_id)[3]
                    event = {"event_id": event_id, "event_title": title, "event_text": event_text}
                    events.append(event)
            uploader = line[18]
            draft_people_description_id = line[19]
            draft_people_event_ids = line[20]
            draft_events = []
            if draft_people_event_ids is not None and len(draft_people_event_ids) > 0:
                ids = draft_people_event_ids.split(",")
                print("ids"+str(ids))
                for draft_event_id in ids:
                    title = mdb.select_draft_people_event(draft_event_id)[4]
                    event_text = mdb.select_draft_people_event(draft_event_id)[5]
                    draft_event = {"draft_event_id": draft_event_id, "draft_event_title": title, "draft_event_text": event_text}
                    draft_events.append(draft_event)
            info = {"name": name, "cover_url":cover_url, "alive":alive, "nationality":nationality, "birthplace":birthplace, "residence":residence
                ,"grave_place":grave_place,"birth_day":birth_day,"death_day":death_day,"article_ids":article_ids,"reputation":reputation
                ,"description":description,"comment_count":comment_count,"motto":motto,"industry":industry,"events":events,"uploader":uploader
                ,"draft_people_description_id":draft_people_description_id,"draftEvents":draft_events}
            print(info)
            data['info'] = info
        except BaseException as e:
            data['code'] = -1
            data['msg'] = "get people error"
            logging.exception(e)
        else:
            data['code'] = 0
            data['msg'] = "get people success"
        self.write(json.dumps(data))