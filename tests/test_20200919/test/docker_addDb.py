# -*- coding: UTF-8 -*-

from docker_sqlconnect import docker_sqlconnect


class docker_addDb():
    @staticmethod
    def docker_add(docker_dict):
		# 获取连接
		conn = docker_sqlconnect.db_connect()
		cur = conn.cursor()
		
		# 执行的添加sql语句
		sql = """INSERT INTO "public"."docker" ("container_name", "container_id", "image_name", "container_status", 
                "container_createtime", "container_ip", "container_port1", "container_port2", "container_port3",
                "container_group") 
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);   """
		
		# 传递参数到字典
		container_name_value = docker_dict['container_name']
		container_id_value = docker_dict['container_id']
		image_name_value = docker_dict['image_name']
		container_status_value = docker_dict['container_status']
		container_createtime_value = docker_dict['container_createtime']
		container_ip_value = docker_dict['container_ip']
		container_port1_value = docker_dict['container_port1']
		container_port2_value = docker_dict['container_port2']
		container_port3_value = docker_dict['container_port3']
		#container_process_status = docker_dict['container_process_status']
		container_group_value = docker_dict['container_group']
		
                #cursor.execute("insert into people values (%s, %s)", (who, age))
		#print ("container_name:",container_name)                

		# 将上面的值赋给变量
		#values = (container_name, container_id, image_name, container_status,
		#		  container_createtime, container_ip, container_port1, container_port2, container_port3,
		#		  container_process_status, container_group)
				  
		values =  (container_name_value, container_id_value, image_name_value, container_status_value,container_createtime_value, container_ip_value,
		 container_port1_value, container_port2_value, container_port3_value, container_group_value)
				  
		#'insert into Login values(%s, %s)' % \
        #     (user_id, password)

		# 执行sql,提交字典中数据到数据库
		cur.execute(sql,values)
		# 提交
		conn.commit()
                print ("sql execute finish......................................")
		# 关闭连接
		cur.close()
		conn.close()


