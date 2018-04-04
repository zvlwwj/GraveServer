#!/usr/bin/env Python
# coding=utf-8
import logging

import tornado.web
import methods.db as mdb
import json
class GetRecommendListHandler(tornado.web.RequestHandler):
    def post(self):
        data = {}
        try:
            user_id = self.get_argument("user_id")
            lines_people = mdb.select_peoples()
            infos = []
            for line in lines_people:
                type = "people"
                people_id = line[0]
                name = line[1]
                cover_url = line[2]
                description_id = line[12]
                description_text = None
                if description_id is not None:
                    description_text = mdb.select_people_description(description_id)[2]
                info = {"type": type, "id": people_id, "name": name, "coverUrl": cover_url, "descriptionText": description_text}
                infos.append(info)
                data["infos"] = infos
        except BaseException as e:
            data['code'] = -1
            data['msg'] = "get recommend error"
            logging.exception(e)
        else:
            data['code'] = 0
            data['msg'] = "get creation people sample success"
        self.write(json.dumps(data))