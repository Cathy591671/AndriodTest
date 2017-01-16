# -*- coding: utf-8 -*-
from multiprocessing import Process

from adb import *
import djrzcj


global apkname
def func(ip,port,apk):

    djrzcj.ip=ip
    djrzcj.port=port
    djrzcj.apkname=apk
    try:
        #checkpath()
        many_connect(ip)
        #runserver(port,ip)
        #time.sleep(30)
        #time.sleep(3)
        #function(ip,packageName,activity)
        #time.sleep(3)
        djrzcj.runit(ip)
        #oneapp.zichanjia(ip,port)
        #appiumTest.runit(ip)

    finally:
        error_log(ip,packageName)

def func2(ip,port,packageName,apk):
    djrzcj.ip=ip
    djrzcj.port=port
    djrzcj.apkname=apk
    try:
        #checkpath()
        many_connect(ip)
        #runserver(port,ip)
        #time.sleep(30)
        adbuninstall(ip,packageName,apk)
        #time.sleep(3)
        #function(ip,packageName,activity)
        #time.sleep(3)
        djrzcj.runit(ip)
        #appiumTest.runit(ip)
    finally:
        error_log(ip,packageName)

if __name__ == "__main__":
    #killserver()
    killadb()
    #通过更新本地的svn获取到apkname
    apkname=splitstr(packageName)
    print apkname
    print "============="
    #如果有新包，把apkname更新到配置文件
    if apkname is not None:
        f=open(configtxt,'r+')
        info=f.readlines()
        info[1]=apkname
        f=open(configtxt,'w+')
        f.writelines(info)
        f.close()
        fn=open(configtxt)
        newinfo=fn.readlines()
        apk= newinfo[1].strip("\n")
        fn.close()
        for ip in lines:
            i=ip.strip("\n")
            #使用multiprocessing多进程包
            p = Process(target=func2, args=(i.split("|")[0],i.split("|")[1],packageName,apk))
            p.start()
    else:
        fx=open(configtxt)
        newinfo=fx.readlines()
        apkx= newinfo[1].strip("\n")
        fx.close()
        for ip in lines:
            i=ip.strip("\n")
            p = Process(target=func, args=(i.split("|")[0],i.split("|")[1],apkx))
            p.start()



