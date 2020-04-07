from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.http import  Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question


#需要导入HttpResponse模块
'''
def hello(request):
    context = {}
    context['hello'] = 'Hello World'
    return render(request,'hello.html',context)
    #request参数必须有，名字类似self的默认规则，可以修改，它封装了用户请求的所有内容
   # return HttpResponse("Hello world ! ")    #不能直接字符串，必须是由这个类封装，此为Django规则

'''

def login(request):
    return render(request, 'login.html')


def login_action(request):
#这是一个通过跳转的url，所以不能直接访问，但是可以通过跳转post后的数据访问。
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if username == 'admin' and password == 'admin123':
            return HttpResponse('login success!')
        else:
            return render(request, 'index.html', {'error': 'username or passowrd error!'})

def detail(request,question_id):
    try:
        # 给question 赋值，获取的是 Question object (4) ,其中，4为 question_id
        question= Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        #抛出404错误
        raise Http404("Question does not exist")
    return render(request, 'myapp/detail.html', {'question':question})


def results(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'myapp/results.html', {'question': question})


def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST 是一个类字典对象，让你可以通过关键字的名字获取提交的数据。 request.POST['choice'] 以字符串形式返回选择的Choice 的ID.
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # 如果 request.POST['choice '] 数据中没有提供 choice ,POST 将引发一个KeyError . 上面的代码检查 KeyError ,
        # 如果没有给出choice 将重新显示Question 表单和一个错误信息。

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'myapp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

        #在增加Choice 得票数之后，代码返回一个HttpResponseRedirect 而不是常用的 HttpResponse , HttpResponseRedirect 只接收一个参数：
        # 用户将要被重定向的URL (
        # reverse 调用，返回一个这样的URL    '/myapp/3/results/'
        return HttpResponseRedirect(reverse('myapp:results', args=(question.id,)))


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('myapp/index.html')
    context = {'latest_question_list': latest_question_list,}
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(template.render(context,request))

    return render(request, 'myapp/index.html', context)