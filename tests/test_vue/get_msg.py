# -*- coding: UTF-8 -*-
from flask import Flask
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/getMsg": {"origins": "*"}})

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/getMsg',methods=['GET','POST'])
def home():
    response = {
        ##这里面填写和后台交互的代码
        'msg': 'Hello, Python !'
    }
    return jsonify(response)

##启动运行
if __name__ == '__main__':
    app.run()