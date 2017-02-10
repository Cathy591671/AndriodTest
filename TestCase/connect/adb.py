# -*- coding: utf-8 -*-

import os
import datetime
import time
import subprocess

'''ip和配置的文件--close()是为了释放资源。
如果不close()，那就要等到垃圾回收时，自动释放资源。垃圾回收的时机是不确定的，也无法控制的。
如果程序是一个命令，很快就执行完了，那么可能影响不大（注意：并不是说就保证没问题）。
但如果程序是一个服务，或是需要很长时间才能执行完，或者很大并发执行，就可能导致资源被耗尽，也有可能导致死锁。
'''
iptxt=os.getcwd()+"\\ip.txt"
f=open(iptxt)
lines=f.readlines()
f.close()

configtxt=os.getcwd()+"\\config.txt"
f1=open(configtxt)
lines1=f1.readlines()
f1.close()

logdaystr = datetime.date.today().strftime('%Y.%m.%d')

packageName = lines1[0].strip("\n")

#activity = lines1[1].strip("\n")
appiumpid=''
#apkname='777'

#logcat目录
log_path=os.getcwd()+"\\logcat"

#安装包目录
file_path=os.getcwd()+"\\file"

#错误截图目录
photo_path=os.getcwd()+"\\screenPhoto"

#appium日志目录
appiumlog_path=os.getcwd()+"\\appiumlog"

#获取新包apk
def splitstr(packageName):
    #svn更新语句
    updatecmd = 'svn update '+file_path
    print updatecmd
    updateinfo=os.popen(updatecmd)
    time.sleep(5)
    x=str(updateinfo.read())
    print '打印的日志是'+x
    if ".apk" in x:
        xsp=x.split('A    file\\')[1].split('.apk')[0]
        print 'xsp是'+xsp
        #global apkname
        apkname=str(xsp)+'.apk'
        print '更新的包是:'+apkname
        return apkname


#检查路径
def checkpath():
    if os.path.exists(log_path):
        pass
    else:
        os.mkdir(log_path)
    if os.path.exists(file_path):
        pass
    else:
        os.mkdir(file_path)
    if os.path.exists(photo_path):
        pass
    else:
        os.mkdir(photo_path)
    if os.path.exists(appiumlog_path):
        pass
    else:
        os.mkdir(appiumlog_path)

#启动appium
def runserver(port,ip):

    bpport=int(port)+1
    cmd = "start appium -a 127.0.0.1 -p " + port + " --bootstrap-port " + str(bpport)+" --session-override"
    print cmd
    os.popen(cmd)

#杀appium进程
def killserver():

    cmd = "taskkill /F /im node.exe"
    print "kill the node.exe task"
    os.popen(cmd)

#杀adb进程
def killadb():
    cmd="taskkill /F /im adb.exe"
    print "kill the adb.exe"
    os.popen(cmd)


# 连接设备
def many_connect(ip):

    connect_str = "adb connect %s" % ip
    print connect_str
    #os.popen(connect_str)
    is_connect = os.popen(connect_str).read()
    print 'info is:'
    print is_connect
    if 'unable' in is_connect:
        print 'unable'
        return False
    else:
        devices_info=os.popen('adb devices').read()
        print devices_info
        if "unauthorized" in devices_info or "offline" in devices_info:
            print 'offline'
            many_connect(ip)
        else:
            print '1234'
        #return 要卸载外边的else下，才有返回值，如果卸载内部
        return True

#批量安装
def manyinstall(ip,apk):
    print 'ready to install'
    print apk
    install_cmd = 'adb -s %s:5555 install -r %s\\%s' % (ip ,file_path,apk)
    print "the install cmd is " + install_cmd
    print time.strftime("%H:%M:%S",time.localtime(time.time()))+'----is installing on %s '%(ip)
    is_install=os.popen(install_cmd).read()
    print is_install
    print time.strftime("%H:%M:%S",time.localtime(time.time()))+'----is completely installed on %s '%(ip)
    if 'Success' in is_install:
        return True
    else:
        return False




#检查安装环境、卸载
def adbuninstall(ip,packageName,apk):
    find_cmd='adb -s %s:5555 shell pm list package|findstr %s'%(ip,packageName)
    find_info=os.popen(find_cmd)
    install_str = len(find_info.read())
    print find_info
    print install_str

    if install_str > 0:
        uninstall_cmd='adb -s %s:5555 shell pm uninstall %s'%(ip,packageName)

        print time.strftime("%H:%M:%S",time.localtime(time.time()))+'----already installed on %s ，uninstalling...'%(ip)
        os.popen(uninstall_cmd)
        x=manyinstall(ip,apk)
        if x is True:
            return True
        else:
            return False

    else:
        x=manyinstall(ip,apk)
        if x is True:
            return True
        else:
            return False


#生成日志
def error_log(ip,packageName):
    #日志文件命名
    filename =log_path+"\\"+ip+'-'+logdaystr+".log"
    logcat_file = open(filename, 'w')

    #根据包名和ip获取程序的pid
    #pid_cmd = "adb -s %s:5555:5555 shell busybox pgrep %s"%(ip,packageName)
    pid_cmd = "adb -s %s:5555 shell  pgrep %s"%(ip,packageName)

    print "the pid search cmd is "+ pid_cmd
    pid_info=os.popen(pid_cmd)
    #pids=pid_info.read().strip()
    #print pids
    pidstr =''
    print pid_info
    for pid in pid_info:
        #print pid
        pidstr =' '.join([pidstr,pid.strip()])
    print pidstr

    #判断是否有pid

    iplen=len(pidstr)
    print iplen
    #程序启动了 存在pid
    if iplen > 1:
        #log_cmd = 'adb -s %s:5555 logcat -v time | findstr "%s" >%s\%s-%s.txt'%(ip,pidstr,log_path,ip,logdaystr)
        #log_cmd = 'adb -s %s:5555:5555 logcat -v time *:I | findstr "%s"'%(ip,pidstr)
        log_cmd = 'adb -s %s:5555 logcat -v time *:W | findstr "%s"'%(ip,pidstr)

        print log_cmd
        #此处不能用os.system,阻塞，外部命令不停止无法继续进行
        process=subprocess.Popen(log_cmd, stdout=logcat_file, stderr=subprocess.PIPE,shell=True)
        time.sleep(5)
        process.kill()
        print('%s log has been finished'%(ip))
        logcat_file.close()






