#!/usr/bin/env Python
# coding=utf-8
import tornado.web
import methods.db as mdb
import json
class LoginHandler(tornado.web.RequestHandler):
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_infos = mdb.select_table(table="user",column="*",condition="user_name",value=username)
        data = {}
        if user_infos:
            db_pwd = user_infos[0][2]
            if db_pwd == password:
                data['code'] = 0
                data['msg'] = "login success!"
                json_data = json.dumps(data)

                self.write(json_data)
            else:
                data['code'] = -1
                data['msg'] = "login fail ,pwd is wrong"
                json_data = json.dumps(data)
                self.write(json_data)
        else:
            data['code'] = -2
            data['msg'] = "no user"
            json_data = json.dumps(data)
            self.write(json_data)