#encoding:utf-8
import sys
import requests,os

from flask import Blueprint, redirect, render_template, request, url_for, session
main = Blueprint('/', __name__)
from model import case_list,case

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# @main.before_request
# def before_request():
#     ip = request.remote_addr
#     url = request.url
#     form = request.form
#     args = request.args
#     values = request.values
#     headers = request.headers
#     method = request.method
#     path = request.path
#     base_url = request.base_url
#     url_root = request.url_root
#     print(url)


@main.route('/case/',methods=['GET','POST',"PUT"])
def case_():
    title = '测试用例'
    if request.method=="GET":
        case_list_ = case_list.query.all()
        # session["case_list"]=case_list_
        return render_template('case.html',locals=locals())
    if request.method == 'PUT':
        case_steps=request.form.get('case_steps',None)
        case_type=request.form.get('case_type',None)
        case_name= request.form.get('case_name',None)
        case_id =request.form.get('case_id',None)
        default_result=request.form.get('default_result',None)




    if request.method=="POST":
        case_steps=request.form.get('case_steps',None)
        case_type=request.form.get('case_type',None)
        case_name= request.form.get('case_name',None)
        case_id =request.form.get('case_id',None)
        default_result=request.form.get('default_result',None)
        if not case_name or not case_steps:
            msg = "必要参数不能为空:case_name or case_steps"
            case_list_ = case_list.query.all()
            return render_template('case.html', locals=locals())
        else:
            case_list_obj = case_list(case_id=case_id,
                                      case_name=case_name,
                                      case_steps=case_steps,
                                      case_type=case_type,
                                      default_result=default_result
                                      )
            case_list_obj.save()
            case_list_ = case_list.query.all()
            # session["case_list"] = case_list_
            msg = "用例添加成功！"
            return render_template('case.html',locals=locals())


@main.route('/')
def home():
    title = "主页"
    result = case.query.all()
    case_mulit=[]
    for obj in result:
        case_mulit.append({"case_name":obj.case_name,'case_type':obj.case_type})
    session['case_mulit']=case_mulit
    return render_template("main.html", locals=locals())


@main.route('/test/', methods=['GET', 'POST'])
def test():
    title = "测试"
    test_type_list=['基础测试']
    result=session['case_mulit']
    if request.method == "POST":
        test_url = request.form.get('test_url')
        test_select = request.form.get("test_select")
        # print(test_select,test_url,)
        if "http://" in test_url:
            pass
        else:
            test_url="http://"+test_url
        for i in result:
            i=i.get('case_name')
            if request.form.get(u"%s"%i) == "on":
                test_type_list.append(i)
        try:
            doing_test(test_type_list,test_url,test_select)
            # path = os.path.abspath(os.curdir)
            fa_path = os.path.abspath('.').replace('\\', '\\\\')
            # print(fa_path)
            # os.system("move /Y %s\\templates\\assets\style.css %s\\static"%(fa_path,fa_path))
            f = open('%s\\templates\\report.html'%fa_path,'r')
            fr = f.readlines()
            f.close()
            f = open('%s\\templates\\report.html'%fa_path,'w')

            for j in fr:
                if "<link href=\"assets/style.css\"" in str(j):
                    j = "<link href='../static/style.css' rel='stylesheet' type='text/css'/></head>"
                f.write(j)
            f.close()
        except Exception as e:
            print(e)
            msg = e
            return render_template('main.html',locals=locals())
        return render_template('main.html',locals=locals())

    if request.method == "GET":
        return render_template('report.html',locals=locals())
        # return render_template('main.html',locals=locals())

def doing_test(test_list,url,methods):

    # data_list = []
    data_list = ''
    for j in test_list:
        print("...调用" + u'%s'%j + "测试用例ing...")
        case_l= case_list.query.filter(case_list.case_type==u'%s'%j).all()
        for i in case_l:
            data_1 = str(methods)+','+str(url)+','+str(i.case_steps)+';'
            # data_list.append(data_1)
            data_list+=data_1
    # print(data_list)
    os.system("python D:\\MyDownloads\\Download\\test_tools\\tool\\test_sample.py %s"%data_list)
    #         result = requests.post(url, data={'data': i.case_steps})
    #         test_result.append({'case':i.case_steps,'status':result.status_code})
    #     dict.setdefault(j ,test_result)
    # print(dict)
    # return dict