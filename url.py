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
from handlers.people.people import CommitPeopleHandler, GetCreationPeopleSample, GetPeopleHandler, UpdatePeopleHandler
from handlers.people.people_description import CommitPeopleDescriptionHandler, UpdatePeopleDescriptionHandler, DeletePeopleDescriptionHandler
from handlers.people.people_description import GetPeopleDescriptionHandler
from handlers.people.people_description import GetPeopleDescriptionFromDraftHandler
from handlers.draft.draft_people import InsertDraftPeopleHandler, UpdateDraftPeopleHandler, GetDraftPeopleSample, GetDraftPeopleHandler
from handlers.draft.draft_people_description import DraftPeopleDescriptionHandler
from handlers.people.people_events import CommitPeopleEventsHandler, UpdatePeopleEventsHandler
from handlers.draft.draft_people_event import CommitDraftPeopleDescriptionHandler, UpdateDraftPeopleDescriptionHandler
from handlers.people.people_events import GetPeopleEventFromDraftHandler, GetPeopleEventHandler
from handlers.public.AboutFile import UploadFileHandler,DeleteFileHandler
from handlers.account.getAccountInfo import GetAccountInfoHandler

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
    # ===========人物描述相关======
    # 提交人物描述
    (r'/people/commit/description', CommitPeopleDescriptionHandler),
    # 更新人物描述
    (r'/people/update/description', UpdatePeopleDescriptionHandler),
    # 删除人物描述
    (r'/people/delete/description', DeletePeopleDescriptionHandler),
    # 提交或更新人物描述草稿
    (r'/draft/people/description', DraftPeopleDescriptionHandler),
    # 获取提交的人物描述
    (r'/people/get/description', GetPeopleDescriptionHandler),
    # 获取草稿中的的人物描述
    (r'/people/get/description_from_draft', GetPeopleDescriptionFromDraftHandler),
    # 删除草稿中的人物描述
    (r'/people/delete/description_from_draft', DeletePeopleDescriptionFromDraftHandler),

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
    (r'/people/get/event_from_draft', GetPeopleEventFromDraftHandler)# OK
]