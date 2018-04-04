#!/usr/bin/env Python
# coding=utf-8

import mysql.connector
# conn = mysql.connector.connect(host="localhost", user="root", passwd="zv63108412", db="grave_server_db", port=3306, charset="utf8")    #连接对象
conn = mysql.connector.connect(host="35.229.220.81", user="root", passwd="zv63108412", db="grave_server_db", port=3306, charset="utf8")
cur = conn.cursor()    #游标对象

def select_table(table, column, condition, value):
    sql = "select " + column + " from " + table + " where " + condition + "='" + value + "'"
    cur.execute(sql)
    lines = cur.fetchall()
    return lines

#插入数据到people数据表
def insert_people(uploader,name,time_stamp,cover_url=None,nationality=None,birthplace=None,residence=None,grave_place=None,birth_day=None,death_day=None,motto=None,industry=None,event_ids=None,description_id=None,alive=0,draft_people_description_id=None,draft_people_event_ids=None):
    sql = "insert into people (uploader,name,time_stamp,cover_url,nationality,birthplace,residence,grave_place,birth_day,death_day,motto,industry,event_ids,description_id,alive,draft_people_description_id,draft_people_event_ids) " \
          "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(sql, (uploader, name, time_stamp, cover_url, nationality, birthplace, residence, grave_place, birth_day, death_day, motto, industry, event_ids, description_id, alive, draft_people_description_id, draft_people_event_ids))
    conn.commit()
    return cur.lastrowid

# 更新数据到people数据表
def update_people(people_id, uploader,name,time_stamp,cover_url=None,nationality=None,birthplace=None,residence=None,grave_place=None,birth_day=None,death_day=None,motto=None,industry=None,alive=0):
    sql = "update people set uploader = %s , name = %s , time_stamp = %s , cover_url = %s , nationality = %s , birthplace = %s , residence = %s , grave_place = %s , birth_day = %s , death_day = %s , motto = %s , industry = %s  , alive = %s where people_id = %s"
    cur.execute(sql, (uploader, name, time_stamp, cover_url, nationality, birthplace, residence, grave_place, birth_day, death_day, motto,industry, alive, people_id))
    conn.commit()
    return cur.lastrowid

# 删除people中的数据
def delete_people(people_id):
    sql = "delete from people where people_id = "+str(people_id)
    cur.execute(sql)
    conn.commit()

#从people数据表中删除描述
def delete_people_description_from_people(people_id):
    sql = "update people set description_id = null where people_id = "+people_id
    cur.execute(sql)
    conn.commit()

#从people数据表中删除描述草稿
def delete_draft_people_description_from_people(people_id):
    sql = "update people set draft_people_description_id = null where people_id = "+str(people_id)
    cur.execute(sql)
    conn.commit()

#从draft_people数据表中删除描述
def delete_people_description_from_draft_people(draft_people_id):
    sql = "update draft_people set description_id = null where draft_people_id = "+draft_people_id
    cur.execute(sql)
    conn.commit()

#从draft_people数据表中删除描述草稿
def delete_draft_people_description_from_draft_people(draft_people_id):
    sql = "update draft_people set draft_people_description_id = null where draft_people_id = "+draft_people_id
    cur.execute(sql)
    conn.commit()

#插入数据到draft_people数据表
def insert_draft_people(uploader,name,time_stamp,cover_url=None,nationality=None,birthplace=None,residence=None,grave_place=None,birth_day=None,death_day=None,motto=None,industry=None,alive=0,event_ids=None,description_id=None):
    sql = "insert into draft_people (uploader,name,time_stamp,cover_url,nationality,birthplace,residence,grave_place,birth_day,death_day,motto,industry,alive,event_ids,description_id) " \
          "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(sql, (uploader, name, time_stamp, cover_url, nationality, birthplace, residence, grave_place, birth_day, death_day, motto, industry, alive, event_ids, description_id))
    conn.commit()
    return cur.lastrowid

#更新数据到draft_people数据表
def update_draft_people(draft_people_id,uploader,name,time_stamp,cover_url=None,nationality=None,birthplace=None,residence=None,grave_place=None,birth_day=None,death_day=None,motto=None,industry=None, alive=0):
    sql = "update draft_people set uploader = %s , name =  %s , time_stamp =  %s ," \
                                         " cover_url =  %s , nationality =  %s , birthplace =  %s , residence =  %s ," \
                                         " grave_place =  %s , birth_day =  %s , death_day =  %s , motto =  %s , industry =  %s , alive = %s where draft_people_id = %s"
    cur.execute(sql, (uploader, name, time_stamp, cover_url, nationality, birthplace, residence, grave_place, birth_day, death_day, motto, industry, alive, draft_people_id))
    conn.commit()

# 更新数据到draft_people数据表的description_id
def update_draft_people_description_id(draft_people_id, time_stamp, description_id):
    sql = "update draft_people set description_id =  %s ,time_stamp = %s where draft_people_id = %s"
    cur.execute(sql, (description_id, time_stamp, draft_people_id))
    conn.commit()

# 更新数据到draft_people数据表的draft_people_description_id
def update_draft_people_draft_people_description_id(draft_people_id, time_stamp, draft_people_description_id):
    sql = "update draft_people set draft_people_description_id =  %s ,time_stamp = %s where draft_people_id = %s"
    cur.execute(sql, (draft_people_description_id, time_stamp, draft_people_id))
    conn.commit()

# 更新数据到people数据表的description_id
def update_people_description_id(people_id, time_stamp, description_id):
    sql = "update people set description_id =  %s ,time_stamp = %s where people_id = %s"
    cur.execute(sql, (description_id, time_stamp, people_id))
    conn.commit()

# 更新数据到people数据表的draft_people_description_id
def update_people_draft_description_id(people_id, time_stamp, draft_people_description_id):
    sql = "update people set draft_people_description_id =  %s ,time_stamp = %s where people_id = %s"
    cur.execute(sql, (draft_people_description_id, time_stamp, people_id))
    conn.commit()

# 更新数据到people数据表的draft_event_ids
def update_people_draft_event_ids(people_id, time_stamp, draft_people_event_ids):
    sql = "update people set draft_people_event_ids =  %s ,time_stamp = %s where people_id = %s"
    cur.execute(sql, (draft_people_event_ids, time_stamp, people_id))
    conn.commit()

# 更新数据到draft_people数据表的draft_event_ids
def update_draft_people_draft_event_ids(draft_people_id, time_stamp, draft_people_event_ids):
    sql = "update draft_people set draft_people_event_ids =  %s ,time_stamp = %s where draft_people_id = %s"
    cur.execute(sql, (draft_people_event_ids, time_stamp, draft_people_id))
    conn.commit()


# 更新数据到draft_people数据表的event_id
def update_draft_people_event_id(draft_people_id, time_stamp, event_ids):
    sql = "update draft_people set event_ids =  %s ,time_stamp = %s where draft_people_id = %s"
    cur.execute(sql, (event_ids, time_stamp, draft_people_id))
    conn.commit()

# 更新数据到draft_people数据表的event_id
def update_people_event_id(people_id, time_stamp, event_ids):
    sql = "update people set event_ids =  %s ,time_stamp = %s where people_id = %s"
    cur.execute(sql, (event_ids, time_stamp, people_id))
    conn.commit()

#插入数据到draft_people_description数据表
def insert_draft_people_description(uploader,time_stamp,draft_people_id,description_text,people_id):
    sql = "insert into draft_people_description (uploader,time_stamp,draft_people_id,description_text,people_id) " \
          "values (%s,%s,%s,%s,%s)"
    cur.execute(sql, (uploader, time_stamp, draft_people_id, description_text, people_id))
    conn.commit()
    return cur.lastrowid

#插入数据到draft_people_event数据表
def insert_draft_people_event(uploader,time_stamp,draft_people_id,title,event_text,people_id):
    sql = "insert into draft_people_event (uploader,time_stamp,draft_people_id,title,event_text,people_id) " \
          "values (%s,%s,%s,%s,%s,%s)"
    cur.execute(sql, (uploader, time_stamp, draft_people_id, title, event_text,people_id))
    conn.commit()
    return cur.lastrowid

#更新数据到draft_people_description数据表
def update_draft_people_description(uploader,time_stamp,description_text,draft_people_id,people_id):
    if draft_people_id is not None:
        sqlUpdate = "update draft_people_description set uploader = %s , time_stamp = %s , description_text = %s where draft_people_id = %s"
        cur.execute(sqlUpdate, (uploader, time_stamp, description_text, draft_people_id))
        conn.commit()
        sqlSelect = "select draft_people_description_id from draft_people_description where draft_people_id = " + draft_people_id
        cur.execute(sqlSelect)
        return cur.fetchone()[0]
    elif people_id is not None:
        sqlUpdate = "update draft_people_description set uploader = %s , time_stamp = %s , description_text = %s where people_id = %s"
        cur.execute(sqlUpdate, (uploader, time_stamp, description_text, people_id))
        conn.commit()
        sqlSelect = "select draft_people_description_id from draft_people_description where people_id = " + people_id
        cur.execute(sqlSelect)
        return cur.fetchone()[0]

#更新数据到draft_people_event数据表
def update_draft_people_event(uploader,time_stamp,event_title, event_text,draft_people_event_id):
    sqlUpdate = "update draft_people_event set uploader = %s , time_stamp = %s , title = %s , event_text = %s where draft_people_event_id = %s"
    cur.execute(sqlUpdate, (uploader, time_stamp, event_title, event_text, draft_people_event_id))
    conn.commit()

#查询数据库中是否存在指定draft_people_id/people_id的事件草稿
def is_draft_people_description_exist(draft_people_id,people_id):
    if draft_people_id is not None:
        sql = "select draft_people_description_id from draft_people_description where draft_people_id = "+str(draft_people_id)
        cur.execute(sql)
        lines = cur.fetchall()
        return len(lines) != 0
    elif people_id is not None:
        sql = "select draft_people_description_id from draft_people_description where people_id = " + str(people_id)
        cur.execute(sql)
        lines = cur.fetchall()
        return len(lines) != 0

# 查询数据库中是否存在指定draft_people_id/people_id的事件草稿
def is_people_description_exist(draft_people_id, people_id):
    if draft_people_id is not None:
        sql = "select people_description_id from people_description where draft_people_id = " + str(draft_people_id)
        cur.execute(sql)
        lines = cur.fetchall()
        return len(lines) != 0
    elif people_id is not None:
        sql = "select people_description_id from people_description where people_id = " + str(people_id)
        cur.execute(sql)
        lines = cur.fetchall()
        return len(lines) != 0


#查询数据库中是否存在指定draft_people_id的事件草稿
def is_draft_people_event_exist(draft_people_id):
    sql = "select draft_people_event_id from draft_people_event where draft_people_id = "+str(draft_people_id)
    cur.execute(sql)
    lines = cur.fetchall()
    return len(lines) != 0

#从人物描述草稿中查询人物描述文本
def select_draft_people_description(draft_people_description_id):
    sql = "select * from draft_people_description where draft_people_description_id = " + str(draft_people_description_id)
    cur.execute(sql)
    lines = cur.fetchone()
    return lines

#从人物描述中查询人物描述文本
def select_people_description(people_description_id):
    sql = "select * from people_description where people_description_id = " + str(people_description_id)
    cur.execute(sql)
    lines = cur.fetchone()
    return lines

#查询人物事件
def select_people_event(people_event_id):
    sql = "select * from people_event where people_event_id = " + str(people_event_id)
    cur.execute(sql)
    lines = cur.fetchone()
    return lines

#查询人物事件草稿
def select_draft_people_event(draft_people_event_id):
    sql = "select * from draft_people_event where draft_people_event_id = " + str(draft_people_event_id)
    cur.execute(sql)
    lines = cur.fetchone()
    return lines

#插入数据到people_description数据表
def insert_people_description(uploader,time_stamp,description_text,draft_people_id,people_id):
    sql_insert = "insert into people_description (uploader,time_stamp,description_text,draft_people_id,people_id) " \
          "values (%s,%s,%s,%s,%s)"
    cur.execute(sql_insert, (uploader, time_stamp, description_text, draft_people_id,people_id))
    conn.commit()
    return cur.lastrowid

#插入数据到people_event数据表
def insert_people_event(uploader,time_stamp,event_title,event_text,draft_people_id,people_id):
    sql_insert = "insert into people_event (uploader,time_stamp,title,event_text,draft_people_id,people_id) " \
                 "values (%s,%s,%s,%s,%s,%s)"
    cur.execute(sql_insert, (uploader, time_stamp, event_title, event_text, draft_people_id, people_id))
    conn.commit()
    return cur.lastrowid

#更新数据到people_event数据表
def update_people_event(uploader,time_stamp,event_title,event_text,people_event_id):
    sql_insert = "update people_event set uploader = %s , time_stamp = %s , title = %s , event_text = %s where people_event_id = %s"
    cur.execute(sql_insert, (uploader, time_stamp, event_title, event_text, people_event_id))
    conn.commit()

#将people_event中的数据绑定从draft_people更新到people
def update_people_event_use_draft_people_id(draft_people_id,people_id):
    sql = "update people_event set draft_people_id=null , people_id = %s where draft_people_id = %s"
    cur.execute(sql, (people_id, draft_people_id))
    conn.commit()

#将people_description中的数据绑定从draft_people更新到people
def update_people_description_use_draft_people_id(draft_people_id,people_id):
    sql = "update people_description set draft_people_id=null , people_id = %s where draft_people_id = %s"
    cur.execute(sql, (people_id, draft_people_id))
    conn.commit()

#将draft_people_event中的数据绑定从draft_people更新到people
def update_draft_people_event_use_draft_people_id(draft_people_id,people_id):
    sql = "update draft_people_event set draft_people_id=null , people_id = %s where draft_people_id = %s"
    cur.execute(sql, (people_id, draft_people_id))
    conn.commit()

#将draft_people_description中的数据绑定从draft_people更新到people
def update_draft_people_description_use_draft_people_id(draft_people_id,people_id):
    sql = "update draft_people_description set draft_people_id=null , people_id = %s where draft_people_id = %s"
    cur.execute(sql, (people_id, draft_people_id))
    conn.commit()

#更新数据到people_description数据表
def update_people_description_use_id(uploader,time_stamp,description_text,people_description_id):
    sql_insert = "update people_description set uploader = %s , time_stamp = %s , description_text = %s where people_description_id = %s"
    cur.execute(sql_insert, (uploader, time_stamp, description_text, people_description_id))
    conn.commit()

#更新数据到people_description数据表
def update_people_description(uploader,time_stamp,description_text,draft_people_id,people_id):
    if draft_people_id is not None:
        sql_update = "update people_description set uploader = %s , time_stamp = %s , description_text = %s where draft_people_id = %s"
        cur.execute(sql_update, (uploader, time_stamp, description_text, draft_people_id))
        conn.commit()
        sql_select = "select people_description_id from people_description where draft_people_id = "+draft_people_id
        cur.execute(sql_select)
        line = cur.fetchone()
        return line[0]
    elif people_id is not None:
        sql_update = "update people_description set uploader = %s , time_stamp = %s , description_text = %s where people_id = %s"
        cur.execute(sql_update, (uploader, time_stamp, description_text, people_id))
        conn.commit()
        sql_select = "select people_description_id from people_description where people_id = " + people_id
        cur.execute(sql_select)
        line = cur.fetchone()
        return line[0]

#删除人物描述草稿
def delete_draft_people_description(draft_people_id=None,people_id=None):
    if draft_people_id is not None:
        sql_delete = "delete from draft_people_description where draft_people_id="+draft_people_id
        cur.execute(sql_delete)
        conn.commit()
        delete_draft_people_description_from_draft_people(draft_people_id=draft_people_id)
    elif people_id is not None:
        sql_delete = "delete from draft_people_description where people_id="+people_id
        cur.execute(sql_delete)
        conn.commit()
        delete_draft_people_description_from_people(people_id=people_id)

# 删除人物描述
def delete_people_description(people_description_id):
    sql = "delete from people_description where people_description_id="+people_description_id
    cur.execute(sql)
    conn.commit()

# 删除人物描述
def delete_people_description_use_people_id(people_id):
    sql = "delete from people_description where people_id="+str(people_id)
    cur.execute(sql)
    conn.commit()

# 删除人物事件
def delete_people_event_use_people_id(people_id):
    sql = "delete from people_event where people_id="+str(people_id)
    cur.execute(sql)
    conn.commit()

# 删除人物描述草稿
def delete_draft_people_description_use_people_id(people_id):
    sql = "delete from draft_people_description where people_id="+str(people_id)
    cur.execute(sql)
    conn.commit()

# 删除人物事件草稿
def delete_draft_people_event_use_people_id(people_id):
    sql = "delete from draft_people_event where people_id="+str(people_id)
    cur.execute(sql)
    conn.commit()

# 删除人物事件草稿
def delete_draft_people_event(draft_people_event_id):
    sql_delete = "delete from draft_people_event where draft_people_event_id=" + str(draft_people_event_id)
    cur.execute(sql_delete)
    conn.commit()

#从人物草稿中查询event_ids
def select_draft_people_event_ids(draft_people_id):
    sql = "select event_ids from draft_people where draft_people_id = "+draft_people_id
    cur.execute(sql)
    lines = cur.fetchone()
    return lines

#从人物中查询event_ids
def select_people_event_ids(people_id):
    sql = "select event_ids from people where people_id = " + people_id
    cur.execute(sql)
    lines = cur.fetchone()
    return lines

#从人物中查询draft_event_ids
def select_people_draft_event_ids(people_id):
    sql = "select draft_people_event_ids from people where people_id = " + people_id
    cur.execute(sql)
    lines = cur.fetchone()
    return lines

#从人物中查询draft_event_ids
def select_draft_people_draft_event_ids(draft_people_id):
    sql = "select draft_people_event_ids from draft_people where draft_people_id = " + draft_people_id
    cur.execute(sql)
    lines = cur.fetchone()
    return lines

#从人物草稿中查询event_ids和description_id
def select_draft_people(draft_people_id):
    sql = "select * from draft_people where draft_people_id = " + draft_people_id
    cur.execute(sql)
    line = cur.fetchone()
    return line

#从用户表中查询该用户的人物草稿
def select_user_draft_people(user_name):
    sql = "select draft_people_ids from user where user_name = " + user_name
    cur.execute(sql)
    line = cur.fetchone()
    return line

#从用户表中更新该用户的人物草稿
def update_user_draft_people(user_name,draft_people_ids):
    sql = "update user set draft_people_ids = %s where user_name = %s"
    cur.execute(sql, (draft_people_ids, user_name))
    conn.commit()

# 从用户表中查询该用户创建的people_ids
def select_user_people_ids(condition, value):
    sql = "select people_ids from user where "+condition+" = "+value
    cur.execute(sql)
    people_ids = cur.fetchone()
    return people_ids

# 从people表中查询所有的people
def select_peoples():
    sql = "select * from people"
    cur.execute(sql)
    lines = cur.fetchall()
    return lines

# 从用户表中查询该用户创建的draft_people_ids
def select_user_draft_people_ids(condition, value):
    sql = "select draft_people_ids from user where "+condition+" = "+value
    cur.execute(sql)
    people_ids = cur.fetchone()
    return people_ids

def select_people_info(people_id):
    sql = "select * from people where people_id = "+people_id
    cur.execute(sql)
    return cur.fetchone()

def select_draft_people_info(draft_people_id):
    sql = "select * from draft_people where draft_people_id = "+draft_people_id
    cur.execute(sql)
    return cur.fetchone()

# 更新用户表的昵称和头像
def edit_user_info(nickname, avatar_url, user_id):
    if avatar_url is not None:
        sql = "update user set nick_name = %s , avatar_url = %s where user_id = %s"
        cur.execute(sql, (nickname, avatar_url, user_id))
    else:
        sql = "update user set nick_name = %s where user_id = %s"
        cur.execute(sql, (nickname, user_id))
    conn.commit()

# 更新用户表的people_ids
def update_user_people_ids(people_ids,user_name):
    sql = "update user set people_ids = %s where user_name = %s"
    cur.execute(sql, (people_ids, user_name))
    conn.commit()

# 从draft_people表中删除
def delete_draft_people(draft_people_id):
    sql = "delete from draft_people where draft_people_id = "+draft_people_id
    cur.execute(sql)
    conn.commit()

# 删除人物描述
def delete_people_description_use_draft_people_id(draft_people_id):
    sql = "delete from people_description where draft_people_id = "+str(draft_people_id)
    cur.execute(sql)
    conn.commit()

# 删除人物事件
def delete_people_event_use_draft_people_id(draft_people_id):
    sql = "delete from people_event where draft_people_id = "+str(draft_people_id)
    cur.execute(sql)
    conn.commit()

# 删除人物事件
def delete_people_event(people_event_id):
    sql = "delete from people_event where people_event_id = " + str(people_event_id)
    cur.execute(sql)
    conn.commit()

# 删除人物描述草稿
def delete_draft_people_description_use_draft_people_id(draft_people_id):
    sql = "delete from draft_people_description where draft_people_id = "+str(draft_people_id)
    cur.execute(sql)
    conn.commit()

# 删除人物事件草稿
def delete_draft_people_event_use_draft_people_id(draft_people_id):
    sql = "delete from draft_people_event where draft_people_id = "+str(draft_people_id)
    cur.execute(sql)
    conn.commit()

# 查询user表中的draft_people_ids
def select_draft_people_ids_from_user(uploader):
    sql = "select draft_people_ids from user where user_name = "+uploader
    cur.execute(sql)
    return cur.fetchone()

# 查询user表中的people_ids
def select_people_ids_from_user(uploader):
    sql = "select people_ids from user where user_name = "+uploader
    cur.execute(sql)
    return cur.fetchone()

# 添加新的评论
def insert_comment(text,uploader_id,previous_id,type,type_id,time_stamp):
    sql_insert = "insert into comment (text,uploader_id,previous_id,type,type_id,time_stamp) " \
                 "values (%s,%s,%s,%s,%s,%s)"
    cur.execute(sql_insert, (text, uploader_id, previous_id, type, type_id,time_stamp))
    conn.commit()
    return cur.lastrowid

# 更新评论中的next_id
def update_comment_next_id(next_ids,comment_id):
    sql = "update comment set next_ids = %s where comment_id = %s"
    cur.execute(sql, (next_ids, comment_id))
    conn.commit()


# 查询评论
def select_comment(type, type_id):
    sql = "select * from comment where type = %s and type_id = %s"
    cur.execute(sql, (type, type_id))
    return cur.fetchall()

# 查询评论
def select_comment_use_id(comment_id):
    sql = "select * from comment where comment_id = "+comment_id
    cur.execute(sql)
    return cur.fetchone()

# 查询评论(使用comment_id)
def select_comment_use_id(comment_id):
    sql = "select * from comment where comment_id = "+comment_id
    cur.execute(sql)
    return cur.fetchone()

# 查询用户信息
def select_user_info(user_id):
    sql = "select * from user where user_id = "+str(user_id)
    cur.execute(sql)
    return cur.fetchone()

# 删除评论
def delete_comment(comment_id):
    sql = "delete from comment where comment_id = "+str(comment_id)
    cur.execute(sql)
    conn.commit()

# 用户点赞评论
def insert_comment_upvote(comment_id, upvote_user_id):
    sql = "insert into comment_upvote (comment_id,upvote_user_id) values(%s,%s)"
    cur.execute(sql, (comment_id, upvote_user_id))
    conn.commit()

# 更新comment表中的upvote数量
def update_comment_upvote(comment_id, upvote):
    sql = "update comment set upvote = %s where comment_id = %s"
    cur.execute(sql, (upvote, comment_id))
    conn.commit()

# 删除点赞记录
def delete_comment_upvote(comment_id, upvote_user_id):
    if upvote_user_id is not None:
        sql = "delete from comment_upvote where comment_id = %s and upvote_user_id = %s"
        cur.execute(sql, (comment_id, upvote_user_id))
    else:
        sql = "delete from comment_upvote where comment_id ="+comment_id
        cur.execute(sql)
    conn.commit()

# 查询该user_id 是否upvote
def select_comment_upvote(comment_id, upvote_user_id):
    sql = "select * from comment_upvote where comment_id = %s and upvote_user_id = %s"
    cur.execute(sql, (comment_id, upvote_user_id))
    return cur.fetchone()

# 查询next_ids
def select_comment_next_ids(comment_id):
    sql = "select next_ids from comment where comment_id = "+str(comment_id)
    cur.execute(sql)
    return cur.fetchone()