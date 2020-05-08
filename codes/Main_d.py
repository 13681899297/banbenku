# coding=utf-8
# 编译日期：2020-05-08 15:03:39
# 版权所有：www.i-search.com.cn
import time
import pdb
from ubpa.ilog import ILog
from ubpa.base_img import *
import getopt
from sys import argv
import sys
import pandas as pd
import ubpa.ibrowse as ibrowse
import ubpa.iie as iie
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
      
    def GetData(self,pv_key=None):
        lv_totalResult=None
        lv_pageResult=None
        # 代码块
        self.__logger.debug('Flow:GetData,StepNodeTag:0815030114185,Note:')
        lv_totalResult = pd.DataFrame()
        # While循环
        self.__logger.debug('Flow:GetData,StepNodeTag:0814504953647,Note:')
        while True:
            # IE拾取表格(web)
            self.__logger.debug('Flow:GetData,StepNodeTag:0814522186952,Note:')
            lv_pageResult = iie.get_ie_table(title=r'理财管理',selector=r'#boxTable',waitfor=10)
            # 代码块
            self.__logger.debug('Flow:GetData,StepNodeTag:0815024293883,Note:')
            
      
    def LoginCSM(self):
        password='TVlUqIwIyp0eXB=='
        userName='ceshi001'
        url='http://122.112.200.222:9080/login.action'
        #打开浏览器
        self.__logger.debug('Flow:LoginCSM,StepNodeTag:0814383211710,Note:打开CSM')
        ibrowse.open_browser(browser_type='ie',url=url)
        # 热键输入
        self.__logger.debug('Flow:LoginCSM,StepNodeTag:0814400306515,Note:最大化窗口')
        ikeyboard.key_send_cs(text='#{UP}',waitfor=10)
        # 设置文本
        self.__logger.debug('Flow:LoginCSM,StepNodeTag:0814403727417,Note:')
        iie.set_text(url=r'http://122.112.200.222:9080/login.action',selector=r'#loginWrap > UL:nth-of-type(1) > LI:nth-of-type(1) > INPUT:nth-of-type(1)',text=userName,waitfor=10)
        # 设置文本
        self.__logger.debug('Flow:LoginCSM,StepNodeTag:0814423516022,Note:')
        iie.set_text(url=r'http://122.112.200.222:9080/login.action',selector=r'#loginWrap > UL:nth-of-type(1) > LI:nth-of-type(2) > INPUT:nth-of-type(1)',text=password,waitfor=10)
        # 鼠标点击
        self.__logger.debug('Flow:LoginCSM,StepNodeTag:0814432656329,Note:')
        iie.do_click_pos(win_title=r'双录系统-录音、录像、录屏 - Internet Explorer',url=r'http://122.112.200.222:9080/login.action',selector=r'#loginWrap > UL:nth-of-type(1) > LI:nth-of-type(2) > INPUT:nth-of-type(2)',button=r'left',curson=r'center',times=1,run_mode=r'unctrl',continue_on_error=r'break',waitfor=10)
      
    def ProductsPage(self):
        # 鼠标点击
        self.__logger.debug('Flow:ProductsPage,StepNodeTag:0814463326434,Note:')
        iie.do_click_pos(win_title=r'双录系统-录音、录像、录屏 - Internet Explorer',url=r'http://122.112.200.222:9080/login.action',selector=r'#frame-nav > UL:nth-of-type(1) > LI:nth-of-type(1) > A:nth-of-type(1)',button=r'left',curson=r'center',times=1,run_mode=r'unctrl',continue_on_error=r'break',waitfor=10)
        # 鼠标点击
        self.__logger.debug('Flow:ProductsPage,StepNodeTag:0814464601036,Note:')
        iie.do_click_pos(win_title=r'双录系统-录音、录像、录屏 - Internet Explorer',url=r'http://122.112.200.222:9080/login.action',selector=r'#MenuContext > TABLE:nth-of-type(1) > TBODY:nth-of-type(1) > TR:nth-of-type(1) > TD:nth-of-type(2) > LI:nth-of-type(5) > A:nth-of-type(1)',button=r'left',curson=r'center',times=1,run_mode=r'unctrl',continue_on_error=r'break',waitfor=10)
      
    def Main(self):
        # 子流程:LoginCSM
        self.__logger.debug('Flow:Main,StepNodeTag:0814440592931,Note:登录到CSM系统')
        (temptemp)=self.LoginCSM()
        # 子流程:ProductsPage
        self.__logger.debug('Flow:Main,StepNodeTag:0814473839038,Note:')
        (temptemp)=self.ProductsPage()
 
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
    pro.Main()
    ___logger = ILog(__file__)
    ___logger.debug('Class:Main,ProTag:Quit,Note:Exit')
