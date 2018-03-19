#!/usr/bin/env Python
# coding=utf-8
import tornado.web
import methods.db as mdb
import json
import logging
class CommitCommentHandler (tornado.web.RequestHandler):
    def post(self):
        text = self.get_argument("text")
        uploader_id = self.get_argument("uploader_id")
        reply_id = self.get_argument("reply_id", default=-1)
        type = self.get_argument("type")
        type_id = self.get_argument("type_id")
        time_stamp = self.get_argument("time_stamp", default=None)
        data = {}
        try:
            comment_id = mdb.insert_comment(text=text, uploader_id=uploader_id, reply_id=reply_id, type=type, type_id=type_id, time_stamp=time_stamp)
        except BaseException as e:
            logging.exception(e)
            data['code'] = -1
            data['msg'] = "add comment fail"
        else:
            data['code'] = 0
            data['msg'] = "add comment success"
            data['comment_id'] = comment_id
        self.write(json.dumps(data))

class GetCommentHandler (tornado.web.RequestHandler):
    def post(self):
        type = self.get_argument("type")
        type_id = self.get_argument("type_id")
        data = {}
        try:
            lines = mdb.select_comment(type=type, type_id=type_id)
        except BaseException as e:
            logging.exception(e)
            data["code"] = -1
            data['msg'] = "get comment error"
        else:
            data["code"] = 0
            data['msg'] = "get comment success"
            infos = []
            for line in lines:
                comment_id = line[0]
                text = line[1]
                uploader_id = line[2]
                upvote = line[3]
                reply_id = line[4]
                type = line[5]
                type_id = line[6]
                time_stamp = line[7]
                line = mdb.select_user_info(user_id=uploader_id)
                nick_name = line[3]
                avatar_url = line[4]
                info = {"comment_id": comment_id, "text": text, "uploader_id": uploader_id, "nick_name": nick_name, "avatar_url": avatar_url, "upvote": upvote, "reply_id": reply_id, "type": type, "type_id": type_id, "time_stamp": time_stamp}
                infos.append(info)
            data['infos'] = infos
        self.write(json.dumps(data))