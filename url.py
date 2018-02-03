#!/usr/bin/env Python
# coding=utf-8
"""
the url structure of website
"""

import sys     #utf-8，兼容汉字
from importlib import reload
reload(sys)
from handlers.index import IndexHandler
from handlers.login import LoginHandler
from handlers.people.people import CommitPeopleHandler
from handlers.people.people_description import CommitPeopleDescriptionHandler
from handlers.people.people_description import GetPeopleDescriptionHandler
from handlers.people.people_description import GetPeopleDescriptionFromDraftHandler
from handlers.draft.draft_people import InsertDraftPeopleHandler
from handlers.draft.draft_people import UpdateDraftPeopleHandler
from handlers.draft.draft_people_description import DraftPeopleDescriptionHandler
from handlers.people.people_events import CommitPeopleEventsHandler
from handlers.draft.draft_people_event import CommitDraftPeopleDescriptionHandler, UpdateDraftPeopleDescriptionHandler
from handlers.people.people_events import GetPeopleEventFromDraftHandler,GetPeopleEventHandler

base_url ="http://172.16.4.32:8000"

url = [
    (r'/', IndexHandler),
    # 登录
    (r'/login', LoginHandler),

    # 人物相关################
    # 提交人物
    (r'/people/commit', CommitPeopleHandler),
    # 提交人物草稿
    (r'/draft/people/commit', InsertDraftPeopleHandler),
    # 更新人物草稿
    (r'/draft/people/update', UpdateDraftPeopleHandler),


    # 人物描述相关################
    # 提交人物描述
    (r'/people/commit/description', CommitPeopleDescriptionHandler),
    # 提交或更新人物描述草稿
    (r'/draft/people/description', DraftPeopleDescriptionHandler),
    # 获取提交的人物描述
    (r'/people/get/description', GetPeopleDescriptionHandler),
    # 获取草稿中的的人物描述
    (r'/people/get/description_from_draft', GetPeopleDescriptionFromDraftHandler),


    # 人物事件相关################
    # 提交人物事件
    (r'/people/commit/event', CommitPeopleEventsHandler),
    # 提交人物事件草稿
    (r'/draft/people/commit/event', CommitDraftPeopleDescriptionHandler),
    # 更新人物事件草稿
    (r'/draft/people/update/event', UpdateDraftPeopleDescriptionHandler),
    # 获取提交的人物事件
    (r'/people/get/event', GetPeopleEventHandler),
    # 获取草稿中的的人物描述
    (r'/people/get/event_from_draft', GetPeopleEventFromDraftHandler)
]