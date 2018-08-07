import sqlite3
import sys
import os
#创建数据库
if os.path.exists('hashlib.db'):
    print "hashlib.db is already exist."
    exit()
conn=sqlite3.connect('hashlib.db')
sql='''create table hash(
    str text primary key,
    md5 text,
    sha1 text,
    sha256 text,
    other text)'''
conn.cursor().execute(sql)
conn.close()
