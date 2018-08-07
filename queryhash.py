import sqlite3
import hashlib
import sys

if len(sys.argv)!=3:
    print("usage: {} <md5|sha1|sha256|other> <your string> ".format(sys.argv[0]))
    exit()
hashtype=sys.argv[1]
string=sys.argv[2]
conn=sqlite3.connect('hashlib.db')
cur=conn.cursor()
sql="select str from hash where {}='{}'".format(hashtype,string)
re=cur.execute(sql)
print re.fetchall()


