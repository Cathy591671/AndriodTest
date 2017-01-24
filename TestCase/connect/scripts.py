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
        x=None
        try:
            x=self.base.findele('id','com.djr.zichanjia:id/btn_login1')
            x.click()
            print 'elementx is:'
            print x
            return 'device '+self.ip+' swipe success'
        except Exception as e:
            return x


    def tearDown(self):
        self.base.quite()
        print 'done'


    def test_login(self):
        x=None
        try:
            x=self.base.findele('id','com.djr.zichanjia:id/main_me')
            x.click()
            time.sleep(1)
            x=self.base.findele('id','com.djr.zichanjia:id/tv_dianzixieyi')
            text=x.get_attribute('text')
            check=self.base.checkText('《资产家平台服务协议》',text)
            if check:
                return check
            print text
            x=self.base.findele('id','com.djr.zichanjia:id/login_user_name_ed')
            x.send_keys('18511302741')
            time.sleep(2)
            x=self.base.findele('id','com.djr.zichanjia:id/login_user_pad_ed')
            x.send_keys('qweasd123')
            x=self.base.findele('id','com.djr.zichanjia:id/login_btn')
            x.click()
            time.sleep(2)
            return 'device '+self.ip+' login success'
        except Exception as e:
            return x







