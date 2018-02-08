#!/usr/bin/env Python
# coding=utf-8

import MySQLdb

conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="grave_server_db", port=3306, charset="utf8")    #连接对象

cur = conn.cursor()    #游标对象

def select_table(table, column, condition, value):
    sql = "select " + column + " from " + table + " where " + condition + "='" + value + "'"
    cur.execute(sql)
    lines = cur.fetchall()
    return lines

#插入数据到people数据表
def insert_people(uploader,name,time_stamp,cover_url=None,nationality=None,birthplace=None,residence=None,grave_place=None,birth_day=None,death_day=None,motto=None,industry=None,event_ids=None,description_id=None):
    sql = "insert into people (uploader,name,time_stamp,cover_url,nationality,birthplace,residence,grave_place,birth_day,death_day,motto,industry,event_ids,description_id) " \
          "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(sql, (uploader, name, time_stamp, cover_url, nationality, birthplace, residence, grave_place, birth_day, death_day, motto, industry, event_ids, description_id))
    conn.commit()
    return cur.lastrowid

#插入数据到draft_people数据表
def insert_draft_people(uploader,name,time_stamp,cover_url=None,nationality=None,birthplace=None,residence=None,grave_place=None,birth_day=None,death_day=None,motto=None,industry=None):
    sql = "insert into draft_people (uploader,name,time_stamp,cover_url,nationality,birthplace,residence,grave_place,birth_day,death_day,motto,industry) " \
          "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(sql, (uploader, name, time_stamp, cover_url, nationality, birthplace, residence, grave_place, birth_day, death_day, motto, industry))
    conn.commit()
    return cur.lastrowid

#更新数据到draft_people数据表
def update_draft_people(draft_people_id,uploader,name,time_stamp,cover_url=None,nationality=None,birthplace=None,residence=None,grave_place=None,birth_day=None,death_day=None,motto=None,industry=None):
    sql = "update draft_people set uploader = %s , name =  %s , time_stamp =  %s ," \
                                         " cover_url =  %s , nationality =  %s , birthplace =  %s , residence =  %s ," \
                                         " grave_place =  %s , birth_day =  %s , death_day =  %s , motto =  %s , industry =  %s where draft_people_id = %s"
    cur.execute(sql,(uploader,name,time_stamp,cover_url,nationality,birthplace,residence,grave_place,birth_day,death_day,motto,industry,draft_people_id))
    conn.commit()

# 更新数据到draft_people数据表的description_id
def update_draft_people_description_id(draft_people_id, time_stamp, description_id):
    sql = "update draft_people set description_id =  %s ,time_stamp = %s where draft_people_id = %s"
    cur.execute(sql, (description_id, time_stamp, draft_people_id))
    conn.commit()

# 更新数据到draft_people数据表的event_id
def update_draft_people_event_id(draft_people_id, time_stamp, event_ids):
    sql = "update draft_people set event_ids =  %s ,time_stamp = %s where draft_people_id = %s"
    cur.execute(sql, (event_ids, time_stamp, draft_people_id))
    conn.commit()


#插入数据到draft_people_description数据表
def insert_draft_people_description(uploader,time_stamp,draft_people_id,description_text):
    sql = "insert into draft_people_description (uploader,time_stamp,draft_people_id,description_text) " \
          "values (%s,%s,%s,%s)"
    cur.execute(sql, (uploader, time_stamp, draft_people_id, description_text))
    conn.commit()
    return cur.lastrowid

#插入数据到draft_people_event数据表
def insert_draft_people_event(uploader,time_stamp,draft_people_id,title,event_text):
    sql = "insert into draft_people_event (uploader,time_stamp,draft_people_id,title,event_text) " \
          "values (%s,%s,%s,%s,%s)"
    cur.execute(sql, (uploader, time_stamp, draft_people_id, title, event_text))
    conn.commit()
    return cur.lastrowid

#更新数据到draft_people_description数据表
def update_draft_people_description(uploader,time_stamp,description_text,draft_people_id):
    sqlUpdate = "update draft_people_description set uploader = %s , time_stamp = %s , description_text = %s where draft_people_id = %s"
    cur.execute(sqlUpdate, (uploader, time_stamp, description_text, draft_people_id))
    conn.commit()
    sqlSelect = "select draft_people_description_id from draft_people_description where draft_people_id = " + draft_people_id
    cur.execute(sqlSelect)
    return cur.fetchone()[0]

#更新数据到draft_people_event数据表
def update_draft_people_event(uploader,time_stamp,event_title, event_text,draft_people_event_id):
    sqlUpdate = "update draft_people_event set uploader = %s , time_stamp = %s , title = %s , event_text = %s where draft_people_event_id = %s"
    cur.execute(sqlUpdate, (uploader, time_stamp, event_title, event_text, draft_people_event_id))
    conn.commit()

#查询数据库中是否存在指定draft_people_id的事件草稿
def is_draft_people_description_exist(draft_people_id):
    sql = "select draft_people_description_id from draft_people_description where draft_people_id = "+draft_people_id
    cur.execute(sql)
    lines = cur.fetchall()
    return len(lines) != 0

#查询数据库中是否存在指定draft_people_id的事件草稿
def is_draft_people_event_exist(draft_people_id):
    sql = "select draft_people_event_id from draft_people_event where draft_people_id = "+draft_people_id
    cur.execute(sql)
    lines = cur.fetchall()
    return len(lines) != 0

#从人物描述草稿中查询人物描述文本
def select_draft_people_description(draft_people_description_id):
    sql = "select * from draft_people_description where draft_people_description_id = " + draft_people_description_id
    cur.execute(sql)
    lines = cur.fetchone()
    return lines

#从人物描述草稿中查询人物描述文本
def select_draft_people_event(draft_people_event_id):
    sql = "select * from draft_people_event where draft_people_event_id = " + draft_people_event_id
    cur.execute(sql)
    lines = cur.fetchone()
    return lines

#从人物描述中查询人物描述文本
def select_people_description(people_description_id):
    sql = "select * from people_description where people_description_id = " + people_description_id
    cur.execute(sql)
    lines = cur.fetchall()
    return lines

#从人物描述中查询人物描述文本
def select_people_event(people_event_id):
    sql = "select * from people_event where people_event_id = " + people_event_id
    cur.execute(sql)
    lines = cur.fetchone()
    return lines

#插入数据到people_description数据表
def insert_people_description(uploader,time_stamp,description_text,draft_people_id):
    sql_insert = "insert into people_description (uploader,time_stamp,description_text,draft_people_id) " \
          "values (%s,%s,%s,%s)"
    cur.execute(sql_insert, (uploader, time_stamp, description_text, draft_people_id))
    conn.commit()
    return cur.lastrowid

#插入数据到people_event数据表
def insert_people_event(uploader,time_stamp,event_title,event_text,draft_people_id):
    sql_insert = "insert into people_event (uploader,time_stamp,title,event_text,draft_people_id) " \
                 "values (%s,%s,%s,%s,%s)"
    cur.execute(sql_insert, (uploader, time_stamp, event_title, event_text, draft_people_id))
    conn.commit()
    return cur.lastrowid

#更新数据到people_event数据表
def update_people_event(uploader,time_stamp,event_title,event_text,people_event_id):
    sql_insert = "update people_event set uploader = %s , time_stamp = %s , title = %s , event_text = %s where people_event_id = %s"
    cur.execute(sql_insert, (uploader, time_stamp, event_title, event_text, people_event_id))
    conn.commit()

#更新数据到people_description数据表
def update_people_description(uploader,time_stamp,description_text,people_description_id):
    sql_insert = "update people_description set uploader = %s , time_stamp = %s , description_text = %s where people_description_id = %s"
    cur.execute(sql_insert, (uploader, time_stamp, description_text, people_description_id))
    conn.commit()

#删除人物描述草稿
def delete_draft_people_description(draft_people_id):
    if is_draft_people_description_exist(draft_people_id):
        sql_delete = "delete from draft_people_description where draft_people_id="+draft_people_id
        cur.execute(sql_delete)
        conn.commit()

# 删除人物事件草稿
def delete_draft_people_event(people_event_id_new):
    if is_draft_people_event_exist(people_event_id_new):
        sql_delete = "delete from draft_people_event where people_event_id=" + people_event_id_new
        cur.execute(sql_delete)
        conn.commit()

#从人物草稿中查询event_ids
def select_draft_people_event_ids(draft_people_id):
    sql = "select event_ids from draft_people where draft_people_id = "+draft_people_id
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

#从用户表中查询该用户的人物草稿
def update_user_draft_people(user_name,draft_people_ids):
    sql = "update user set draft_people_ids = %s where user_name = %s"
    cur.execute(sql, (draft_people_ids, user_name))
    line = cur.fetchone()
    return line

# 从用户表中查询该用户创建的people_ids
def select_user_people_ids(condition, value):
    sql = "select people_ids from user where %s = %s"
    cur.execute(sql, (condition, value))
    people_ids = cur.fetchone()
    return people_ids

def select_people_info(people_id):
    sql = "select * from people where people_id = "+people_id
    cur.execute(sql)
    cur.fetchone()

# 更新用户表的people_ids
def update_user_people_ids(people_ids):
    sql = "update user set people_ids = "+people_ids
    cur.execute(sql)

# 从draft_people表中删除
def delete_draft_people(draft_people_id):
    sql = "delete from draft_people where draft_people_id = "+draft_people_id
    cur.execute(sql)