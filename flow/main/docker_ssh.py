# -*- coding: UTF-8 -*-


import paramiko,time



def docker_ssh_exec():
    # 创建SSH对象
    ssh = paramiko.SSHClient()

    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # 连接服务器
    ssh.connect(hostname='10.44.99.16', port=22, username='root', password='jbj!HHZS@tsl#')


    # 执行命令
    stdin, stdout, stderr = ssh.exec_command('python /tools/docker_s1/docker_a1/test/main.py')

    # 获取命令结果
    docker_py_result = stdout.read()
    print("docker_py_result : ", docker_py_result)  # 如果有输出的话
    print("docker_py_result(type) : ",type(docker_py_result))  # 如果有输出的话
    docker_py_result = eval(docker_py_result)

    print("docker_py_result(type2) : ", type(docker_py_result))

    # 关闭连接
    ssh.close()
    return docker_py_result