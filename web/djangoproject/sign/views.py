from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def login_actionfront(request):
    return render(request,"login.html")
# Create your views here.
def login_action(request):
#这是一个通过跳转的url，所以不能直接访问，但是可以通过跳转post后的数据访问。
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)

       # if username == 'admin' and password == 'admin123':
            response = HttpResponseRedirect('/event_manage/')
            #response.set_cookie('user',username,3600) # 添加浏览器cookie
            request.session['user'] = username # 将session 信息记录到浏览器

            return response

        else:
            return render(request, 'index.html', {'error': 'username or passowrd error!'})

#发布会管理
@login_required()
def event_manage(request):
    #username = request.COOKIES.get('user','') # 读取浏览器cookie
    username = request.session.get('user','') # 读取浏览器 session
    return render(request,"event_manage.html",{"user":username})