# -*- coding: UTF-8 -*-
from flask import Flask
from flask import request,render_template,redirect,session,url_for,flash
from db_method import db_method
from flow import app
import sqlconnect
from wtforms import Form,StringField,PasswordField,BooleanField, validators
from wtforms.validators import DataRequired,Length
import docker_ssh
import functools

class LoginForm(Form):
    username = StringField("username",validators=[DataRequired()])
    password = PasswordField("password",validators=[DataRequired(),Length(5,128)])

# 如果访问/根目录，则跳转到登录页面
@app.route('/')
def index():
    return redirect('/login')

'''
# 定义装饰器函数，判断是否登录了
def is_login(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        user = session.get('user')
        if not user:
            return redirect('login')
        return func(*args,**kwargs)
    return inner
'''

# 登录页面
@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm(request.form)
    if request.method =='POST' and form.validate():
        if (db_method.select(form.username.data, form.password.data)):
            print "使用用户名和密码查询数据库有结果"
            return redirect('success')
            #return redirect(url_for('success'))
        else:
            return "Login Failed"

    return render_template("login.html", form=form)





# 成功页面
@app.route('/success')
def situation_docker():
    conn = sqlconnect.db_connect()

    cur = conn.cursor()

    # 待执行的查询sql语句
    sql = """select id, container_name, container_id, image_name, container_status,
container_createtime, container_ip, container_port1, container_port2, container_port3,
container_process_status, container_group from docker;"""

    # 执行语句
    cur.execute(sql)
    # fetchall返回多个记录
    result_dict = cur.fetchall()

    # 提交并关闭连接
    conn.commit()
    cur.close()
    conn.close()
    print (type(result_dict))
    # 将结果返回到html页面中，并传递包含值的结果集u
    return render_template('success.html', result_dict=result_dict)

@app.route('/more')
def create():
    docker_ssh.docker_ssh_exec()
    data ="create success"
    return render_template('success.html', data)



if __name__ == '__main__':

    #建立临时站点
    app.debug = True
    app.run(port=8010)