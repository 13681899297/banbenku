# coding=utf-8
# 编译日期：2020-05-08 14:40:55
# 版权所有：www.i-search.com.cn
import time
import pdb
from ubpa.ilog import ILog
from ubpa.base_img import *
import getopt
from sys import argv
import sys
import ubpa.ibrowse as ibrowse
import ubpa.ikeyboard as ikeyboard

class YeHongJun_KaoShi:
     
    def __init__(self,**kwargs):
        self.__logger = ILog(__file__)
        self.path = set_img_res_path(__file__)
        self.robot_no = ''
        self.proc_no = ''
        self.job_no = ''
        self.input_arg = ''
        if('robot_no' in kwargs.keys()):
            self.robot_no = kwargs['robot_no']
        if('proc_no' in kwargs.keys()):
            self.proc_no = kwargs['proc_no']
        if('job_no' in kwargs.keys()):
            self.job_no = kwargs['job_no']
        if('input_arg' in kwargs.keys()):
            self.input_arg = kwargs['input_arg']
            self.input_arg = self.input_arg.replace("\\","/")
      
    def LoginCSM(self):
        url='http://122.112.200.222:9080/login.action'
        #打开浏览器
        self.__logger.debug('Flow:LoginCSM,StepNodeTag:0814383211710,Note:打开CSM')
        ibrowse.open_browser(browser_type='ie',url=url)
        # 热键输入
        self.__logger.debug('Flow:LoginCSM,StepNodeTag:0814400306515,Note:最大化窗口')
        ikeyboard.key_send_cs(text='#{UP}',waitfor=10)
      
    def Main(self):
        pass
 
if __name__ == '__main__':
    robot_no = ''
    proc_no = ''
    job_no = ''
    input_arg = ''
    try:
        argv = sys.argv[1:]
        opts, args = getopt.getopt(argv,"hr:p:j:i:",["robot = ","proc = ","job = ","input = "])
    except getopt.GetoptError:
        print ('robot.py -r <robot> -p <proc> -j <job>')
    for opt, arg in opts:
        if opt == '-h':
            print ('robot.py -r <robot> -p <proc> -j <job>')
        elif opt in ("-r", "--robot"):
            robot_no = arg
        elif opt in ("-p", "--proc"):
            proc_no = arg
        elif opt in ("-j", "--job"):
            job_no = arg
        elif opt in ("-i", "--input"):
            input_arg = arg
    pro = YeHongJun_KaoShi(robot_no=robot_no,proc_no=proc_no,job_no=job_no,input_arg=input_arg)
    pro.LoginCSM()
    ___logger = ILog(__file__)
    ___logger.debug('Class:Main,ProTag:Quit,Note:Exit')
