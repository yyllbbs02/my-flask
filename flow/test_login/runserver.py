# -*- coding: UTF-8 -*-
from login import userRoute
from model import create_app

DEFAULT_MODULES = [userRoute]

# 这里config.py 的相对路径，是以model目录下的文件作为对象进行计算的
app = create_app('../config.py')

for module in DEFAULT_MODULES:
    app.register_blueprint(module)


@app.before_request
def before_request():
    pass


if __name__ == '__main__':
    app.run(debug=True)