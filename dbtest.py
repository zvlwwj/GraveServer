#!/usr/bin/env Python
# coding=utf-8

import MySQLdb

conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="grave_server_db", port=3306, charset="utf8")    #连接对象

cur = conn.cursor()    #游标对象

sql = "select " + "draft_people_description_id" + " from " + "draft_people_description" + " where " + "draft_people_id" + "='" + "6" + "'"
cur.execute(sql)
lines = cur.fetchall()
print(len(lines))