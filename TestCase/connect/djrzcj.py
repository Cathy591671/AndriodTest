# -*- coding: utf-8 -*-
from app import *
import sys
import HTMLTestRunner
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

global ip
global port
global apkname
ip = None
port = None
apkname = None

class zcj(unittest.TestCase):

    def setUp(self):
        self.ip=ip
        self.port=port
        self.apkname=apkname
        self.base=andriodScript(self.ip,self.port,self.apkname)
        self.base.zichanjia(self.ip,self.port,self.apkname)
        print '初始化成功'

    def test_swipe(self):

        self.base.swipeToLeft()
        time.sleep(1)
        self.base.findele('id','com.djr.zichanjia:id/btn_login').click()

    def test_login(self):
        print "登录"

        self.base.swipeToLeft()
        time.sleep(1)
        self.base.findele('id','com.djr.zichanjia:id/btn_login').click()

        time.sleep(1)
        self.base.findele('id','com.djr.zichanjia:id/main_me').click()
        time.sleep(1)
        text=self.base.findele('id','com.djr.zichanjia:id/tv_dianzixieyi').get_attribute('text')
        self.base.checkText('《资产家平台服务协议》',text)
        print text


        self.base.findele('id','com.djr.zichanjia:id/login_user_name_ed2').send_keys('18511302741')
        time.sleep(2)
        self.base.findele('id','com.djr.zichanjia:id/login_user_pad_ed').send_keys('qweasd123')
        self.base.findele('id','com.djr.zichanjia:id/login_btn').click()
        time.sleep(2)
        self.base.findele('id','com.djr.zichanjia:id/negativeButton').click()
        time.sleep(2)
        print "******"



    def tearDown(self):
        self.base.quite()
        print '结束'

def runit(ip):

    print "ip如下："
    print ip
    filePath = adb.log_path+"/"+ip+"-pyResult.html"
    fp = file(filePath, 'wb')
    testsuite=unittest.TestSuite()

    #testsuite.addTest(zcj("test_swipe"))
    testsuite.addTest(zcj("test_login"))

    #runner=unittest.TextTestRunner()
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='测试结果',
                description='测试报告'
                )

    runner.run(testsuite)
    print "run被执行了"

