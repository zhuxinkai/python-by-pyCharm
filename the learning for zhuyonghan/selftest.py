# coding=utf-8
class person():

#带有两个下划线开头的函数，声明该属性为私有，不能再类的外部被直接使用或者访问
#相当于java的构造器 __init__的第一个参数必须是self


    def __init__(self,name,gender,birth,**kw):
        self.name=name
        self.gender=gender
        self.birth=birth
#可使用 **kw定义关键参数，代表任意参数，python函数可变参数及关键字参数定义参考见下文。

        for k,w in kw.iteritems():
            setattr(self,k,w)
    def sayhi(self):
#在类中，直接使用self时，调用怎会调用对象本身的属性。
        print "my name is "+ self.name
#解决出现None的问题，当函数没有返回的时候，出现None;
        exit()


xiaoming = person('Xiao Ming', 'Male', '1991-1-1',job='student',tel='18089355',stdid='15010')
xiaohong = person('Xiao Hong', 'Female', '1992-2-2')


print xiaoming.name
print xiaohong.birth
print xiaoming.job
print xiaoming.tel
print xiaoming.stdid
print xiaohong.sayhi()
