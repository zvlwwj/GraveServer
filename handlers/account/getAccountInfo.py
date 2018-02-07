#!/usr/bin/env Python
# coding=utf-8
import logging

import tornado.web
import methods.db as mdb
import json
class GetAccountInfoHandler(tornado.web.RequestHandler):
    def post(self):
        user_id = self.get_argument("user_id")
        try:
            data = {}
            user_infos = mdb.select_table(table="user", column="*", condition="user_id", value=user_id)
            nick_name = user_infos[0][3]
            avatar_url = user_infos[0][4]
            draft_people_ids = user_infos[0][5]
            draft_thing_ids = user_infos[0][6]
            draft_event_ids = user_infos[0][7]
            people_ids = user_infos[0][8]
            thing_ids = user_infos[0][9]
            event_ids = user_infos[0][10]
            collection_people_ids = user_infos[0][11]
            collection_thing_ids = user_infos[0][12]
            collection_event_ids = user_infos[0][13]

        except BaseException as e:
            data['code'] = -1
            data['msg'] = "select error"
            logging.exception(e)
        else:
            data['code'] = 0
            data['msg'] = "select success"
            info = {}
            info['nick_name'] = nick_name
            info['avatar_url'] = avatar_url
            info['draft_people_ids'] = draft_people_ids
            info['draft_thing_ids'] = draft_thing_ids
            info['draft_event_ids'] = draft_event_ids
            info['people_ids'] = people_ids
            info['thing_ids'] = thing_ids
            info['event_ids'] = event_ids
            info['collection_people_ids'] = collection_people_ids
            info['collection_thing_ids'] = collection_thing_ids
            info['collection_event_ids'] = collection_event_ids
            data['info'] = info
        json_data = json.dumps(data)
        self.write(json_data)