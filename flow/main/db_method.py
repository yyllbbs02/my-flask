# -*- coding: UTF-8 -*-
import sqlconnect



class db_method:

    @staticmethod
    def insert(username,password):
        sql = "insert into user (username,password) values ('%s','%s')"%(username,password)
        conn = sqlconnect.db_connect()
        cur = conn.cursor()
        cur.execute(sql)

        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def select(username,password):
        # username ='%s' and
        sql = "select username, password from public.user where username ='%s' and password ='%s'"%(username,password)
        conn = sqlconnect.db_connect()
        cur = conn.cursor()
        cur.execute(sql)

        result = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        if(len(result)==0):
            print ("用户名和密码不正确")
            return False
        else:
            return True


