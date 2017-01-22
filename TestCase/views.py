# coding:utf-8
from django.shortcuts import render

import os
import time
from connect import adb
from django import forms
from django. shortcuts import render_to_response
from django. shortcuts import render
from django.http import request
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django. contrib import auth
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from connect import scripts
from multiprocessing import Process
from multiprocessing import Pool

iptxt=os.getcwd()+"\\ip.txt"
f=open(iptxt)
lines=f.readlines()


iptxt=os.getcwd()+"\\config.txt"
f=open(iptxt)
configinfo=f.readlines()
packageName= configinfo[0].strip("\n")
apk= configinfo[1].strip("\n")
paramList=[]
#resultList=[]

# Create your views here.
def index(request):
    return render(request, "index.html")
def connect(ip):
    result=adb.many_connect(ip)
    print result
    if result:
        connectInfo='device'+ip+'connected successfully'
        return connectInfo

    else:
        connectInfo='device'+ip+'connected failed'
        return connectInfo



def nomalinstall(ip,packageName,apk):

    result=adb.adbuninstall(ip,packageName,apk)
    print 'result is：'
    print result
    if result is True:
        installinfo='device'+ip+'normal installed successfully'
        return installinfo
    else:
        installinfo='device'+ip+'normal installed failed'
        return installinfo


def coverinstall(ip,apk):
    result=adb.manyinstall(ip,apk)
    if result is True:
        installinfo='device'+ip+'cover installed successfully'
        return installinfo
    else:
        installinfo='device'+ip+'cover installed failed'
        return installinfo

def manyFunction(ip,apk,port,packageName,install_checked,function_checked):
    resultList=[]
    connectInfo=connect(ip)
    resultList.append(connectInfo)
    if 'connected successfully' in connectInfo:
        if install_checked=='2':
            x=coverinstall(ip,apk)
            resultList.append(x)
        elif install_checked=='1':
            x=nomalinstall(ip,packageName,apk)
            resultList.append(x)
        fs=scripts.function_scripts()
        fs.setUp(ip,port,apk)
        if 'guide' in function_checked:
            swiptinfo=fs.test_swipe()
            resultList.append(swiptinfo)
        if 'login' in function_checked:
            logininfo=fs.test_login()
            resultList.append(logininfo)
        fs.tearDown()
        print 'resultList:'
        print resultList
        return resultList

def run(request):
    resultList=[]
    sumlist=[]
    install_checked = request. POST. get('install' , ' ' )
    function_checked= request. POST. getlist('function' , ' ' )
    print '==='+install_checked
    #paramList.append(install_checked)
    p = Pool(processes=5)
    for ipline in lines:
        i=ipline.strip("\n")
        ip=i.split("|")[0]
        port=i.split("|")[1]
        resultList.append(p.apply_async(manyFunction, (ip,apk,port,packageName,install_checked,function_checked,)))
    p.close()
    p.join()
    for res in resultList:
        print '=============='
        result=res.get()
        print result
        sumlist.append(result)
        print sumlist
    #return render_to_response('result.html',{'connectinfo':result[0], 'installinfo':installres,'welcomeinfo':welcomeres,'logininfo':loginres})
    return render_to_response('result.html',{'result':sumlist})

'''
def run(request):
    connectInfo=connect()
    installinfo=''
    swiptinfo=''
    logininfo=''
    #如果连接手机成功，可以继续装包
    if connectInfo=='connect successful':
        install_checked = request. POST. get('install' , ' ' )
        if install_checked=='2':
            print install_checked
            installinfo=coverinstall()
        elif install_checked=='1':
            print install_checked
            installinfo=nomalinstall()
    function_checked= request. POST. getlist('function' , ' ' )
    print 'function_checked:'
    print function_checked
    fs=scripts.function_scripts()
    fs.setUp(ip,port,apk)
    if 'guide' in function_checked:
        swiptinfo=fs.test_swipe()
    if 'login' in function_checked:
        logininfo=fs.test_login()
    fs.tearDown()


    return render_to_response('result.html',{'connectInfo': connectInfo, 'installinfo': installinfo, 'swiptinfo': swiptinfo, 'logininfo':logininfo} )

'''





def uploadfile(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理
        apk =request.FILES.get("apk", None)
        ip =request.FILES.get("ip", None)
        config =request.FILES.get("config", None)
        # 获取上传的文件，如果没有文件，则默认为None
        if not apk and not ip and not config:
            return render_to_response('index.html', {'error': 'no fileno'})
            #raise forms.ValidationError(u"请选择要上传的文件")
        apk_destination = open(os.path.join("C:\Users\Cathy\PycharmProjects\connect",apk.name),'wb+')    # 打开特定的文件进行二进制的写操作
        for chunk in apk.chunks():      # 分块写入文件
            apk_destination.write(chunk)
        apk_destination.close()

        ip_destination = open(os.path.join("C:\Users\Cathy\PycharmProjects\connect",ip.name),'wb+')    # 打开特定的文件进行二进制的写操作
        for chunk in ip.chunks():      # 分块写入文件
            ip_destination.write(chunk)
        ip_destination.close()

        config_destination = open(os.path.join("C:\Users\Cathy\PycharmProjects\connect",config.name),'wb+')    # 打开特定的文件进行二进制的写操作
        for chunk in config.chunks():      # 分块写入文件
            config_destination.write(chunk)
        config_destination.close()
        return render_to_response('index.html', {'upload success'})
