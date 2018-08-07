import sqlite3
import hashlib
import sys

if len(sys.argv)!=2:
    print "usage: {} <password file>\n\tAdd hash of passwords into the database.".format(sys.argv[0])
    exit()
path=sys.argv[-1]
conn=sqlite3.connect('hashlib.db')
cur=conn.cursor()
f=open(path,'r')
for password in f.readlines():
    password=password.strip()
    try:
        sql="insert into hash (str,md5,sha1,sha256) values('{}','{}','{}','{}')".format(password,hashlib.md5(password).hexdigest(),hashlib.sha1(password).hexdigest(),hashlib.sha256(password).hexdigest())
        # print sql
        cur.execute(sql)
    except:
        pass
conn.commit()
f.close()
cur.close()
conn.close()