# -*- coding: utf-8 -*-
import os
import time

#运行功能
def function(ip,packageName,activity):
    openactivity = 'adb -s %s:5555 shell am start %s/%s'%(ip,packageName,activity)
    os.system(openactivity)
    print time.strftime("%H:%M:%S",time.localtime(time.time()))+'----%s 上的app被打开了'%(ip)