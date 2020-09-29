# -*- coding: UTF-8 -*-
from flow import app
from flask import render_template
import psycopg2
import sqlconnect


@app.route('/')
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



if __name__ == '__main__':

    #建立临时站点
    app.debug = True
    app.run(port=8006)
