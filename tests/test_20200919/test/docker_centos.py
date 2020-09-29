# -*- coding: UTF-8 -*-
import commands
import subprocess
import os
import datetime
import time


def create_file(file_conf):
	if (os.path.exists(file_conf)):
        	print (file_conf,' is exists')
	else:
		fp = open(file_conf, 'w')
        	if (os.path.exists(file_conf)):
			print(file_conf,'create success')
	return file_conf

#封装执行shell命令的方法，有返回值，如果返回值不赋值给变量，则代表只执行shell命令
#os.popen()可以实现一个“管道”，从这个命令获取的值可以继续被调用
def shell_cmd(cmd):
	result = os.popen(cmd).read()
	return result


#封装获取最大值的方法，每次创建容器时进行调用
def get_maxsingle(docker_name, awk_param):
	# 获取行数
	line_cmd="docker ps |grep " + docker_name + " |awk -F '" + awk_param +"' '{print $2}' |cut -b 1-2 | wc -l"
	line_result = shell_cmd(line_cmd)


	max=0
	for i in (1,int(line_result)):

		#依次获取每个 num 从1开始，从line_cmd的结果结束
		single_cmd="docker ps |grep " + docker_name + " |awk -F '" + awk_param +"' '{print $2}' |cut -b 1-2 | head -" + str(i) + " | tail -1"
		single_result = shell_cmd(single_cmd)
		#如果获取不到，就是line_cmd为0，single_cmd为空的时候，给最大值1个初始值为
		#if single_result == "" or single_result == " ":
		if len(single_result) == 0:
		   single_result = '10'
		num=int(single_result)
	    #比较上面的所有数，获取最大值
		if num > max:
			max=num
		else:
			print "else .... name:",docker_name, "awk_param: ",awk_param, "max: ",max,"num: ",num
	return max

#封装获取docker容器名称后缀的最大值docker ps |grep v3061_automation |awk -F 'v3061_automation_' '{print $2}'

# 定义字典，接收docker容器信息
docker_dict = {}	
		


#22端口的封装
def get_port22(dockerNameA):
    maxsingle = get_maxsingle(dockerNameA,"0.0.0.0:")
    port_22 = str(maxsingle + 1) + '222'
	# 将映射的端口1加入字典
    docker_dict['port_22'] = port_22
    return port_22

#5432端口的封装
def get_port920(dockerNameA):
	maxsingle = get_maxsingle(dockerNameA,"0.0.0.0:")
	port_920 = str(maxsingle + 1) + '920'
	# 将映射的端口2加入字典
	docker_dict['port_920'] = port_920
	return port_920

#921端口的封装
def get_port921(dockerNameA):
	maxsingle = get_maxsingle(dockerNameA,"0.0.0.0:")
	port_921 = str(maxsingle + 1) + '921'
	# 将映射的端口3加入字典
	docker_dict['port_921'] = port_921
	return port_921
	
#docker容器名的封装
def get_vesselName(dockerNameA, dockerNameAA):
    maxsingle = get_maxsingle(dockerNameA,dockerNameAA)
    vessel_name = dockerNameAA + str(maxsingle + 1)
    docker_dict['vessel_name'] = vessel_name
    return vessel_name


def create_docker(docker_image, dockerNameA, dockerNameAA):
     
	# 将镜像名加入字典
    docker_dict['docker_image'] = docker_image
	# 将创建时间加入字典
    create_time = datetime.datetime.now()
    docker_dict['create_time'] = create_time
	
	
	
	#获取容器名赋值给变量
    vesselName = get_vesselName(dockerNameA,dockerNameAA)
	

	#创建postgres容器
    dynamic_cmd='sudo docker run -d -p ' + get_port22(dockerNameA) + ':22 -p ' + get_port920(dockerNameA) + ':9200 -p ' + get_port921(dockerNameA) + ':9201 --name ' + vesselName + ' -m 4G --memory-swap 5G --privileged --cap-add=SYS_ADMIN ' + docker_image + ' /usr/sbin/init /usr/sbin/sshd -D'
    shell_cmd(dynamic_cmd)
    return vesselName
	
#写内容到文件，传递文件名和内容
def write_file(file_name, file_content):
	fp = open(file_name,'a')
	fp.write("{}\n".format(file_content))
	fp.close()	

#删除文件的方法
def os_removefile(file_rm):
	if os.path.exists(file_rm):
     		os.remove(file_rm)
                print file_rm," file remove success"
	else:
		print "file is not exists"


def situation_init():
    #创建shell文件
    file_name = "situation_init.sh"
    os_removefile(file_name)
    create_file(file_name)
        
    # 将脚本内容写入shell文件中
    write_file(file_name, "#!/bin/bash")	
    write_file(file_name, "supervisord -c /etc/supervisord.conf")	
    write_file(file_name, "supervisorctl start web:nginx")	
    write_file(file_name, "mkdir /data10/log")	
    write_file(file_name, "chown -R website:website /data10/log")
    write_file(file_name, "supervisorctl start redis6379")	
	

    
    #拷贝shell文件到docker容器中
    docker_cpcmd = "docker cp situation_init.sh " + vesselName + ":/root"
    shell_cmd(docker_cpcmd)
    
    #清理宿主机上创建的shell文件    
    os_removefile(file_name)
    
    #在容器内执行shell脚本    
    docker_cmd_execsh="docker exec -it " + vesselName + " /bin/bash -c 'sh /root/situation_init.sh'"
    shell_cmd(docker_cmd_execsh)
	


# docker inspect --format='{{.NetworkSettings.IPAddress}}' v3061_centos7.4_12
# 获取容器创建后的id
def container_id(vesselName):
	docker_cmd_execsh="docker ps  |grep " + vesselName + " | awk '{print $1}'"
	container_id = shell_cmd(docker_cmd_execsh)
	return container_id


# 获取容器创建后的状态
def container_status(vesselName):
	docker_cmd_execsh="docker ps  |grep " + vesselName + " | awk '{print $8}'"
	container_status = shell_cmd(docker_cmd_execsh)
	return container_status



# 获取容器内运行的服务状态 
def container_process_status(vesselName):
	docker_cmd_execsh="docker exec -it " + vesselName + " /bin/bash -c 'supervisorctl status web:webcgi | awk '{print $2}''"
	container_status = shell_cmd(docker_cmd_execsh)
	return container_process_status

# 获取容器的所属组，每次关联的时候，添加到分组，然后将分组信息写到本地配置文件，获取时从配置文件中读取

# 目前直接返回2
def container_group():
	return 2

if __name__ == "__main__":

    #传参镜像名称，执行方法创建容器,同时获取容器创建的容器名
	vesselName = create_docker("v3061/centos7.4:s1","v3061_centos7.4","v3061_centos7.4_")
'''	
	# 容器内业务初始化
	print "starting situation_init...... please wait ...."
	situation_init()


	time.sleep(3)
	# 将容器id加入字典
    docker_dict['container_id'] = container_id(vesselName)
	# 将状态加入字典
	docker_dict['container_status'] = container_status(vesselName)
	# 将分组加入字典
	docker_dict['container_group'] = container_group()
	
	# 打印字典
	for key,value in docker_dict.items:
		print "key: ",key," value: ",value
'''
	













