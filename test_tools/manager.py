#encoding:utf-8
import sys
import os
from flask import Flask

from flask_script import Manager
from app import main
from model import db
BASE_DIR = os.getcwd()  # 执行脚本的初始路径
static_dir = os.path.join(BASE_DIR, 'static')
templates_dir = os.path.join(BASE_DIR, 'templates')
print(static_dir,templates_dir)
app = Flask(__name__, static_folder=static_dir, template_folder=templates_dir)
app.config["SECRET_KEY"]="\xe5\xc3\x7f\xd9\xa1\xd2es\xec\xac\x13y^{\xdas\xb1\xfd\xe0\xc2\x89\xbaS"
app.config["DEBUG"]=True
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///' + os.path.join(BASE_DIR, 'data.sqlite') + '?check_same_thread=False' + '?charset=utf8'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
app.register_blueprint(blueprint=main,url_prefix = "/")


db.init_app(app=app)
# app_ctx = app.app_context()
# with app_ctx:
#     for db in [db,]:
#         db.drop_all()
#         db.create_all()

manager = Manager(app)



if __name__ == '__main__':

    #run   python manager.py runserver -h 192.168.1.156 -p 9000
    manager.run()