# -*- coding: utf-8 -*-
from app import *
import sys
import HTMLTestRunner
import sys
import app
reload(sys)
sys.setdefaultencoding('utf-8')

global ip
global port
global apkname
ip = None
port = None
apkname = None

class function_scripts():

    def setUp(self,ip,port,apkname):
        self.ip=ip
        self.port=port
        self.apkname=apkname
        self.base=andriodScript(self.ip,self.port,self.apkname)
        self.base.zichanjia(self.ip,self.port,self.apkname)
        print 'init successful'

    def test_swipe(self):
        self.base.swipeToLeft()
        idnum='com.djr.zichanjia:id/btn_login'
        try:
            elementx=self.base.findele('id',idnum)
            elementx.click()
            print 'elementx is:'
            print elementx
            return 'success'
        except Exception as e:
            print idnum
            return 'element '+idnum+' is not exist'


    def tearDown(self):
        self.base.quite()
        print 'done'


    def test_login(self):
        try:
            self.base.findele('id','com.djr.zichanjia:id/main_me').click()
            time.sleep(1)
            text=self.base.findele('id','com.djr.zichanjia:id/tv_dianzixieyi').get_attribute('text')
            self.base.checkText('《资产家平台服务协议》',text)
            print text
            self.base.findele('id','com.djr.zichanjia:id/login_user_name_ed').send_keys('18511302741')
            time.sleep(2)
            self.base.findele('id','com.djr.zichanjia:id/login_user_pad_ed').send_keys('qweasd123')
            self.base.findele('id','com.djr.zichanjia:id/login_btn').click()
            time.sleep(2)
            return 'success'
        except Exception as e:
            return 'fail'







