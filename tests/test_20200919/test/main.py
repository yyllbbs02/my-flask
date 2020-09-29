# -*- coding: UTF-8 -*-

from docker_sis import docker_sis
from docker_addDb import docker_addDb

if __name__ == "__main__":

    # 定义要使用的镜像名
    image_name = "v3061/automation:s1"

    #创建对象：docker_sis.py是自动创建容器的脚本
    d_sis = docker_sis()
    #创建容器，获取字典
    docker_dict = d_sis.exec_create(image_name)
	
    #调用添加方法，将获取的docker字典信息写入数据库
    docker_addDb.docker_add(docker_dict)
	
