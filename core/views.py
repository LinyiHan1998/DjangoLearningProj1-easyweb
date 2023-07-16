from django.shortcuts import render , HttpResponse, redirect
from core.models import UserInfo,department

# Create your views here.

def index(request):
    return HttpResponse("welcome")

def user_list(request):
    return render(request,'user_list.html')

def user_add(request):
    return render(request,'user_add.html')

def tpl(request):
    name = "John"
    roles = ["manager","boss","security","cat","mouse"]
    user_info = {"name":"Jane","salary":10000,"role":"boss"}

    data_list = [
        {"name": "Tom", "salary": 30000, "role": "cat"},
        {"name": "Jerry", "salary": 60000, "role": "mouse"},
        {"name": "Brave", "salary": 90000, "role": "manager"}
    ]
    return render(request,'tpl.html',{"n1":name,"n2":roles,"n3":user_info,"n4":data_list})

def news(request):
    return render(request,'news.html')


def sth(request):
    return HttpResponse('sth')

def login(request):
    if request.method == "GET":
        return render(request,'login.html')

    username = request.POST.get("user")
    password = request.POST.get("password")
    if username =='1' and password == '1':
        return HttpResponse("login succeed")
    error_msg = 'login failed'
    return render(request,'login.html',{"error_msg":error_msg})

def info_list(request):
    #UserInfo.objects.create('name' ='Tom','password'='123','age'='19')
    #create('name' = Tom,'password'='123',age='19')
    data_list = UserInfo.objects.all()

    return render(request,'info.html',{"data_list" : data_list})

def info_add(request):
    if request.method == "GET":
        return render(request,'info_add.html')
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")

    UserInfo.objects.create(name = user, password = pwd,age = age)

    return redirect('/info/list')

def info_delete(request):
    nid = request.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()
    return HttpResponse('succeed')

