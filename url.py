#!/usr/bin/env Python
# coding=utf-8
"""
the url structure of website
"""

import sys     #utf-8，兼容汉字
from importlib import reload

import tornado

reload(sys)
from handlers.index import IndexHandler
from handlers.account.login import LoginHandler
from handlers.people.people import CommitPeopleHandler, GetCreationPeopleSample, GetPeopleHandler, UpdatePeopleHandler, DeletePeopleHandler
from handlers.people.people_description import CommitPeopleDescriptionHandler, UpdatePeopleDescriptionHandler, DeletePeopleDescriptionHandler,GetPeopleDescriptionHandler,GetPeopleDescriptionFromDraftHandler
from handlers.draft.draft_people import InsertDraftPeopleHandler, UpdateDraftPeopleHandler, GetDraftPeopleSample, GetDraftPeopleHandler, DeleteDraftPeopleHandler
from handlers.draft.draft_people_description import DraftPeopleDescriptionHandler,DeleteDraftPeopleDescriptionHandler
from handlers.people.people_events import CommitPeopleEventsHandler, UpdatePeopleEventsHandler
from handlers.draft.draft_people_event import CommitDraftPeopleDescriptionHandler, UpdateDraftPeopleDescriptionHandler, DeleteDraftPeopleEventHandler
from handlers.people.people_events import GetPeopleEventFromDraftHandler, GetPeopleEventHandler, DeletePeopleEventHandler
from handlers.public.AboutFile import UploadFileHandler,DeleteFileHandler
from handlers.account.getAccountInfo import GetAccountInfoHandler

# base_url ="http://35.229.220.81:8000"
base_url ="http://172.16.4.32:8000"
url = [
    (r'/', IndexHandler),
    # ===========用户相关===========
    # 登录
    (r'/login', LoginHandler),
    # 获取用户信息
    (r'/get/accountInfo', GetAccountInfoHandler),

    # ===========文件相关=========
    # 上传文件
    (r'/uploadFile', UploadFileHandler),
    # 删除文件
    (r'/deleteFile', DeleteFileHandler),

    # ===========人物相关=========
    # 提交人物
    (r'/people/commit', CommitPeopleHandler),
    # 更新人物
    (r'/people/update', UpdatePeopleHandler),
    # 提交人物草稿
    (r'/draft/people/commit', InsertDraftPeopleHandler),# OK
    # 更新人物草稿
    (r'/draft/people/update', UpdateDraftPeopleHandler),# OK
    # 获取人物草稿（简单）
    (r'/people/get/draft_sample', GetDraftPeopleSample),# OK
    # 获取提交的人物（简单）
    (r'/people/get/creation_sample', GetCreationPeopleSample),
    # 获取提交的人物（详细）
    (r'/people/get', GetPeopleHandler),
    # 获取人物草稿（详细）
    (r'/draft/people/get', GetDraftPeopleHandler),
    # 删除人物
    (r'/people/delete', DeletePeopleHandler),
    # 删除人物草稿
    (r'/draft/people/delete', DeleteDraftPeopleHandler),

    # ===========人物描述相关======
    # 提交人物描述
    (r'/people/commit/description', CommitPeopleDescriptionHandler),
    # 更新人物描述
    (r'/people/update/description', UpdatePeopleDescriptionHandler),
    # 提交或更新人物描述草稿
    (r'/draft/people/description', DraftPeopleDescriptionHandler),
    # 获取提交的人物描述
    (r'/people/get/description', GetPeopleDescriptionHandler),
    # 获取人物描述草稿
    (r'/draft/people_description/get', GetPeopleDescriptionFromDraftHandler),
    # 删除人物描述
    (r'/people/delete/description', DeletePeopleDescriptionHandler),
    # 删除人物描述草稿
    (r'/draft/people_description/delete', DeleteDraftPeopleDescriptionHandler),


    # ===========人物事件相关========
    # 提交人物事件
    (r'/people/commit/event', CommitPeopleEventsHandler),# OK
    # 更新人物事件
    (r'/people/update/event', UpdatePeopleEventsHandler),# OK
    # 提交人物事件草稿
    (r'/draft/people/commit/event', CommitDraftPeopleDescriptionHandler),# OK
    # 更新人物事件草稿
    (r'/draft/people/update/event', UpdateDraftPeopleDescriptionHandler),# OK
    # 获取提交的人物事件
    (r'/people/get/event', GetPeopleEventHandler),# OK
    # 获取草稿中的的人物描述
    (r'/draft/people_event/get', GetPeopleEventFromDraftHandler),# OK
    # 删除人物事件
    (r'/people/event/delete', DeletePeopleEventHandler),
    # 删除人物事件草稿
    (r'/draft/people_events/delete', DeleteDraftPeopleEventHandler)
]