# -*- coding: UTF-8 -*-
import psycopg2


def db_connect():
   # 建立数据库连接
   #conn = psycopg2.connect(database="flow", user="postgres", password="postgres", host="10.44.99.16",
    #                       port="5432")
   conn = psycopg2.connect(database="situation", user="postgres", password="postgres", host="39.96.15.249",
                           port="5432")
   return conn






'''
   # 执行的添加sql语句
   sql = """INSERT INTO "public"."docker" ("id","container_name", "container_id", "image_name", "container_status", 
   "container_createtime", "container_ip", "container_port1", "container_port2", "container_port3",
    "container_process_status", "container_group") 
   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);   """
   
   # 测试使用，手动给值
   id = 2
   container_name = "v3061_centos7.4_11"
   container_id = "1ced0758cab9"
   image_name = "v3061/postgres:s1"
   container_status = "Up"
   container_createtime = datetime.datetime.now()
   container_ip = "172.0.0.3"
   container_port1 = "11433->5432"
   container_port2 = "11223->22"
   container_port3 = "container_port3"
   container_process_status = "running"
   container_group = "container_group"
   
   # 将上面的值赋给变量
   values = (id, container_name, container_id, image_name, container_status,
    container_createtime, container_ip, container_port1, container_port2, container_port3,
    container_process_status, container_group)
   
   # 执行sql
   cur.execute(sql, values)
   
   # 提交，并关闭连接
   conn.commit()


'''

