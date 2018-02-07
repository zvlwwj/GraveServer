#!/usr/bin/env Python
# coding=utf-8

import json
data = {}
data['code'] = 0
data['msg'] = "select success"
info = {}
info['nick_name'] = "hello"
info['draft_people_ids'] = "123,123,12334"
data['info'] = info

json_data = json.dumps(data)
print(json_data)