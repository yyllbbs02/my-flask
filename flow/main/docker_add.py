# -*- coding: UTF-8 -*-

import sqlconnect
import docker_ssh



def docker_add():
    conn = sqlconnect.db_connect()

    cur = conn.cursor()

    # 执行的添加sql语句
    sql = """INSERT INTO "public"."docker" ("container_name", "container_id", "image_name", "container_status", 
    "container_createtime", "container_ip", "container_port1", "container_port2", "container_port3",
     "container_process_status", "container_group") 
    VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);   """



    # 获取python执行后返回的字典信息
    docker_dict = docker_ssh.docker_ssh_exec()

    print(type(docker_dict))


    # 传递参数到字典
    container_name = docker_dict['container_name']
    container_id = docker_dict['container_id']
    image_name = docker_dict['image_name']
    container_status = docker_dict['container_status']
    container_createtime = docker_dict['container_createtime']
    container_ip = docker_dict['container_ip']
    container_port1 = docker_dict['container_port1']
    container_port2 = docker_dict['container_port2']
    container_port3 = docker_dict['container_port3']
    container_process_status = docker_dict['container_process_status']
    container_group = docker_dict['container_group']


    # 将上面的值赋给变量
    values = (container_name, container_id, image_name, container_status,
              container_createtime, container_ip, container_port1, container_port2, container_port3,
              container_process_status, container_group)

    # 执行sql
    cur.execute(sql, values)

    # 提交，并关闭连接
    conn.commit()

    cur.close()
    conn.close()


if __name__ == '__main__':
    docker_add()
