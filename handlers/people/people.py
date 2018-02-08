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
            data = {}
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
            # 插入people表中
            people_id = mdb.insert_people\
                (uploader, name, time_stamp, cover_url, nationality, birthplace, residence, grave_place, birth_day, death_day, motto, industry, event_ids, description_id)
            # 将people_id 更新到user表中
            old_people_ids = mdb.select_user_people_ids(condition="user_name", value=uploader)
            if old_people_ids is None:
                new_people_ids = draft_people_id
            else:
                new_people_ids = old_people_ids[0]+","+people_id
            mdb.update_user_people_ids(new_people_ids)
            # 删除draft_people数据
            mdb.delete_draft_people(draft_people_id=draft_people_id)
            # 更新user表中的draft_people_ids
            old_people_draft_ids = mdb.select_user_draft_people(user_name=uploader)[0]
            if old_people_draft_ids is not None:
                new_people_draft_ids = old_people_draft_ids.repalce(","+draft_people_id, '')
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

class GetCreationPeopleSample(tornado.web.RequestHandler):
    def post(self):
        try:
            data = {}
            user_id = self.get_argument("user_id")
            people_ids = mdb.select_user_people_ids(condition="user_id", value=user_id)
            print(people_ids)
            ids = people_ids.split(',')
            infos = []
            for id in ids:
                line = mdb.select_people_info(id)
                name = line[1]
                description_id = line[11]
                description_text = mdb.select_people_description(description_id)
                info = {"name": name, "description_text": description_text}
                infos.append(info)
            data['infos'] = infos
        except BaseException as e:
            data['code'] = -1
            data['msg'] = "get creation people sample error"
            logging.exception(e)
        else:
            data['code'] = 0
            data['msg'] = "get creation people sample success"
