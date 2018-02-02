#!/usr/bin/env Python
# coding=utf-8
import tornado.web
import methods.db as mdb
import json
import url
class CommitPeopleHandler(tornado.web.RequestHandler):
    def post(self):
        uploader = self.get_argument("username")
        name = self.get_argument("name")
        nationality = self.get_argument("nationality", default=None)
        birthplace = self.get_argument("birthplace", default=None)
        residence = self.get_argument("residence", default=None)
        grave_place = self.get_argument("grave_place", default=None)
        birth_day = self.get_argument("birth_day", default=None)
        death_day = self.get_argument("death_day", default=None)
        # TODO 相关文章id
        # article_ids = self.get_argument("article_ids")
        # TODO 声望
        reputation = 0
        # TODO 评论数
        comment_count = 0
        #description = self.get_argument("description")
        motto = self.get_argument("motto", default=None)
        industry = self.get_argument("industry", default=None)
        #event_ids = self.get_argument("event_ids")
        #TODO 封面图片url地址
        files = self.request.files
        if not files:
            cover_url = ""
        else:
            img_cover = files.get("cover")
            for img in img_cover:
                with open('./statics/cover/people/' + img['filename'], 'wb') as f:
                    f.write(img['body'])
                    cover_url = url.base_url + '/statics/cover/people/' + img['filename']
        time_stamp = self.get_argument("time_stamp")

        people_id = mdb.insert_people(uploader, name, time_stamp, cover_url, nationality, birthplace, residence, grave_place, birth_day, death_day, motto, industry)

        data = {}
        data['code'] = 0
        data['msg'] = "insert success"
        data['people_id'] = people_id
        self.write(json.dumps(data))