#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import methods.db as mdb
import json;
class IndexHandler(tornado.web.RequestHandler):
    # def get(self):
    #     self.write("hello world")

    def get(self, filename):
        print('i download file handler : ', filename)
        # Content-Type这里我写的时候是固定的了，也可以根据实际情况传值进来
        self.set_header('Content-Type', 'application/octet-stream')
        self.set_header('Content-Disposition', 'attachment; filename=' + filename)
        # 读取的模式需要根据实际情况进行修改
        with open(filename, 'rb') as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                self.write(data)
        # 记得有finish哦
        self.finish()