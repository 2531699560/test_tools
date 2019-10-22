#-*- encoding:utf-8 -*-
import pytest,sys
import requests

"""安装：
pip install -U pytest
pip install -U pytest-html
pip install -U pytest-xdist
pip install -U pytest-rerunfailures
"""


"""pytest测试样例：
测试文件                         ：以test_开头（以_test结尾也可以）
测试类                           ：以Test开头，并且不能带有 init 方法
测试函数                         ：以test_开头
断言使用基本的assert即可
"""


"""run:
    pytest                          : 运行当前目录下的测试。                              
    pytest -q                       : 减少冗长，不再展示pytest的版本信息。（pytest --version）
    pytest --html=report.html       : 生成html测试报告。                                
    pytest test_se.py               ： 直接运行test_se.py文件中的所有cases。
    pytest test_se.py::TestClassOne ： 运行test_se.py文件中的TestClassOne这个class下的两个cases。
    pytest test_se.py::TestClassTwo::test_one
                                    ： 运行test_se.py文件中的TestClassTwo这个class下的test_one函数。
    pytest test_se.py -n 5          ： 5线程运行测试。                                    
    pytest test_se.py --reruns 5    ： 意外重试5次。                                      
    pytest test_se.py -s            ： 打印测试函数的print内容。
"""

class TestClass():
    caseInfo = []
    list = str(sys.argv[1]).split(';')
    for i in list:
        list2 = str(i).split(',')
        if len(list2) > 1:
            # print(list2)
            caseInfo.append(tuple(list2))
    # print(caseInfo)
    @pytest.mark.parametrize('methods,url,data',caseInfo)
    def test_post(self,methods,url,data):
        header = {
            "User-Agent":"Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
        }
        if methods == "POST":
            result = requests.post(url, data={'data': data})
            assert result.status_code == 200
            print("POST ojbk")

        if methods == "GET":
            result = requests.get(url,headers=header,data=data)
            assert result.status_code == 200
            print("GET ojbk")
        if methods == "DELETE":
            result = requests.delete(url,headers=header,data=data)
            assert result.status_code == 200
            print("DELETE ojbk")
        if methods == "PUT":
            result = requests.put(url,headers=header,data=data)



    # @pytest.mark.parametrize('methods,url,data', caseInfo)
    # def test_get(self,methods,url,data):
    #     x = "hello"
    #     assert hasattr(x, 'check')


if __name__ == '__main__':
    pytest.main(['-q','--html=./templates/report.html'])