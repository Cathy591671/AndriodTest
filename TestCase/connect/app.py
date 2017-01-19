# -*- coding: utf-8 -*-
import os
import unittest
from appium import webdriver
import time
import adb
import givelog

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)

)

class andriodScript():

    def __init__(self,ip,port,apkname):
        self.ip=ip
        self.port=port
        self.apkname=apkname

    #定位元素
    def findele(self,*loc):
        el=''
        if loc[0] == 'id':
            el=self.driver.find_element_by_id(loc[1])
        elif loc[0] == 'name':
            el=self.driver.find_element_by_name(loc[1])
        assert el
        return el
    '''
        except Exception as e:
            print e
            #givelog.errorlog(e)
            errorinfo="device"+self.ip+"，element"+loc[1]+"is not exist"
            print errorinfo
            return errorinfo

            givelog.errorlog("设备"+self.ip+"中，元素"+loc[1]+"不存在")
            self.takephoto(self.ip)
            '''

    #截屏
    def takephoto(self,ip):
        photoname=adb.photo_path+"\\"+ip+"-"+adb.logdaystr+".jpg"
        self.driver.get_screenshot_as_file(photoname)

    #向左滑屏
    def swipeToLeft(self):
        width=self.driver.get_window_size()['width']
        height=self.driver.get_window_size()['height']

        self.driver.swipe(width * 3 / 4, height * 3 / 4, width * 1 / 4, height  * 3 / 4,300)
        print 'swipe successful'

    #返回
    def back(self):
        self.driver.press_keycode("4")

    #检查文本
    def checkText(self,exp,real):
        print "check 了"
        try:
            assert exp == real
        except Exception as e:
            givelog.errorlog(e)
        #except AssertionError,  e:
            print("设备"+self.ip+"中，预期显示"+exp+",实际显示的是"+real)
            givelog.errorlog("设备"+self.ip+"中，预期显示"+exp+",实际显示的是"+real)
            self.takephoto(self.ip)
            #raise e


    def zichanjia(self,ip,port,apkname):
        print "基本配置"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = ip+':5555'
        #esired_caps['appPackage'] = adb.packageName
        #desired_caps['appActivity'] = adb.activity
        desired_caps['appWaitActivity'] = '.activity.WelcomeActivity'
        desired_caps['app'] = adb.file_path+'\\'+self.apkname
        desired_caps['udid'] =  ip+':5555'
        self.driver = webdriver.Remote('http://127.0.0.1:'+port+'/wd/hub',desired_caps)
        print "配置中的apkname是："+self.apkname

    def quite(self):
        self.driver.quit()




