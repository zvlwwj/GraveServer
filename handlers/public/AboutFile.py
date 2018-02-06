#!/usr/bin/env Python
# coding=utf-8
import logging

import tornado.web
import json
import os
from astropy.io.fits import file

import url
class UploadFileHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            data = {}
            img_url = self.get_argument("url")
            relative_url = img_url.replace(url.base_url, ".")
            files = self.request.files
            file = files.get("file")
            for img in file:
                with open(relative_url + img['filename'], 'wb') as f:
                    f.write(img['body'])
                    cover_url = img_url + img['filename']

        except BaseException as e:
            data['code'] = -1
            data['msg'] = "upload file error"
            logging.exception(e)
        else:
            data['code'] = 0
            data['msg'] = "upload file success"
        self.write(json.dumps(data))

class DeleteFileHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            data = {}
            delete_url = self.get_argument("url")
            relative_url = delete_url.replace(url.base_url, ".")
            os.remove(relative_url)
        except BaseException as e:
            data['code'] = -1
            data['msg'] = "upload file error"
            logging.exception(e)
        else:
            data['code'] = 0
            data['msg'] = "upload file success"
        self.write(json.dumps(data))