from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):   #必须加上request
    return HttpResponse("欢迎使用")

def user_list(request):   #必须加上request
    #默认会去app01目录的下template目录下寻找html文件，注意会根据所有的注册app下的templates去寻找
    #注意这部分去寻找的位置应该是结合setting配置文件中的templates定义的配置；
    return render(request,"user_list.html")    #使用render的模式返回给用户请求html；

def useradd(request):   #必须加上request
    return render(request,"user_add.html")

def tpl(request):
    name='学习计划一' #如果这个值想从数据库获取，这样定义变量
    roles=['cto','ceo','cfo']
    dic={"role":"cissp","age":18,"sal":20000}
    data_list = [
        {"role": "csp", "age": 19, "sal": 20000},
        {"role": "osp", "age": 18, "sal": 290000},
        {"role": "cpi", "age": 28, "sal": 2880000}
    ]
    return render(request,'tpl.html',{"n1":name,"n2":roles,"n3":dic,"n4":data_list})

def news(req):
    #1、不想去写数据也不想去查询数据，直接去爬虫
    #2、向这个地址发起请求：https://bj.122.gov.cn/m/page/news/getDetails
    #3、requests 模块使用
    import requests
    res = requests.get("https://www.chinanews.com.cn/scroll-news/news2.html")
    data_list = res.json()  #这种方式存在错误情况
    print(data_list)
    return render(req,"news.html")