#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import methods.db as mdb
import json;
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world")
