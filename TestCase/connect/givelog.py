import logging
from adb import *
import os
appiumlog_path=os.getcwd()+"\\appiumlog"
logday = datetime.date.today()
logdaystr = logday.strftime('%Y.%m.%d')

logging.basicConfig(level=logging.ERROR,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename=appiumlog_path+'\\'+logdaystr+".log",
                filemode='w')

def errorlog(msg):
    logging.error(msg)