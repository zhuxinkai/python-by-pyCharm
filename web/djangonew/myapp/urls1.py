from django.urls import path
from . import views2
# 使用命名空间后，url 的格式使用  myapp:detail   myapp:vote   myapp:result 格式。
app_name = 'myapp'


urlpatterns = [

    # ex: /polls/
    #继承来上层的文件，条状到views的index .
    path('', views2.index, name='index'),

    # ex: /polls/5/

    # 对应 http://127.0.0.1:8000/myapp/4/ ，其中 views 的detail  返回到 detail2.html。 detail2.html 中代码为 {{question}} 中，获取的是 view 的detail 中
    # return render(request,'myapp/detail2.html',{'question':question})   ,返回时，确认返回的目标路径和，返回的值。


    # 其中的 name = 'detail' 可以，写在html模板中的 {%url 'detail' } 中的位置。这样使得，形成的url，可以自动更改。

    path('special/<int:question_id>/', views2.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views2.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views2.vote, name='vote'),


]