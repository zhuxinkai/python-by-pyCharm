from django.db import models
import datetime
from django.utils import timezone


# Create your models here.

class Question(models.Model): # model.Model ,每个模型表示为， django.db.models.Model 类的子类。
    #每个字段都是Field 类的实例-比如 ，CharField 表示为字符字段。
    # question_text , pub_date 为字段名。
    # 字段名，最好使用机器友好的格式。
    # 定义某些Field实例，需要参数。例如 CharField 需要参数 max_length参数。
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    was_published_recently = models.BooleanField(max_length=1)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'



class Choice(models.Model):
    # ForeignKey 定义了一个关系。这将告诉Django ,每个chice 对象都关联到一个Question 对象。
    # Django 支持所有常用数据库关系： 多对一 ，多对多， 一对一
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
