# -*- coding: UTF-8 -*-
import psycopg2

class docker_sqlconnect():
	
    @staticmethod
    def db_connect():
   	# 建立数据库连接
   	conn = psycopg2.connect(database="flow", user="postgres", password="postgres", host="10.44.99.16",
                           port="5432")
   	return conn



