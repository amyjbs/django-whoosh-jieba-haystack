# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from  hello_app.models import Publisher
from django.contrib.auth.models import User
from forms import contactform
from  django.core.mail import send_mail
from django.views.decorators.csrf import csrf_protect

# Create your views here.
p = Publisher.address
def hello(request):
    url_list = User.objects.all()
    user = request.path
    return render(request,'table.html',{'url_list':url_list,'user':user})

def userform(requset):
    form = contactform()
    data = requset.META
    return render(requset,'form.html',{'form': form,'data':data})
@csrf_protect
def contact(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            content = '内容：%s，邮箱：%s' %(cd['message'],cd['email'])
            send_mail(
                cd['subject'],
                content,
                'yangyong@findourlove.com',
                ['yangyong@findourlove.com',],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = contactform()
    return render(request,'form.html',{'form': form})

def thanks(request):
    return HttpResponse('信息提交成功！')




# def mail(request):
#
#     send_mail(
#                 'Django测试',
#                 'test1',
#                 'yangyong@findourlove.com',
#                 ['1937320874@qq.com',],
#
#     )
#     return HttpResponse("ok")


