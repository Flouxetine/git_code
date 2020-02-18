#-*- encoding: utf-8 -*-
import logging
import wmi
import os
import time
from ConfigParser import ConfigParser
import smtplib
from email.mime.text import MIMEText
import socket
from datetime import datetime
import re
import sys
import time
import string
import psutil
import threading
from threading import Timer
import logging
# 创建一个logger
logger = logging.getLogger('Monitor')
logger.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log')
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

reload(sys)  # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')
# 读取配置文件中的进程名和系统路径，这2个参数都可以在配置文件中修改
ProList = []
# 定义一个列表
c = wmi.WMI()


#获取进程所用内存
def countProcessMemoey(processName):
    try:
        CONFIGFILE = 'config.ini'
        config = ConfigParser()
        config.read(CONFIGFILE)

        pattern = re.compile(r'([^\s]+)\s+(\d+)\s.*\s([^\s]+\sK)')
        cmd = 'tasklist /fi "imagename eq ' + processName + '"' + ' | findstr.exe ' + processName
        result = os.popen(cmd).read()
        resultList = result.split("\n")
        totalMem = 0.0
        totalCpu = 0.0

        print "*" * 80
        for srcLine in resultList:
            srcLine = "".join(srcLine.split('\n'))
            if len(srcLine) == 0:
                break
            m = pattern.search(srcLine)
            if m == None:
                continue
            #由于是查看python进程所占内存，因此通过pid将本程序过滤掉
            if str(os.getpid()) == m.group(2):
                continue
            p = psutil.Process(int(m.group(2)))
            cpu = p.cpu_percent(interval=1)
            ori_mem = m.group(3).replace(',', '')
            ori_mem = ori_mem.replace(' K', '')
            ori_mem = ori_mem.replace(r'\sK', '')
            memEach = string.atoi(ori_mem)
            totalMem += (memEach * 1.0 / 1024)
            totalCpu += cpu
            print 'ProcessName:' + m.group(1) + '\tPID:' + m.group(
                2) + '\tmemory size:%.2f' % (
                    memEach * 1.0 / 1024), 'M' + ' CPU:' + str(cpu) + '%'
        print 'ProcessName:' + m.group(1) + ' TotalMemory:' + str(
            totalMem) + 'M' + ' totalCPU:' + str(totalCpu) + '%'
        logger.info('ProcessName:' + m.group(1) + ' TotalMemory:' +
                    str(totalMem) + 'M' + ' totalCPU:' + str(totalCpu) + '%')
        print "*" * 80

        if totalMem > float(config.get('MonitorProcessValue', 'Memory')):
            print 'Memory Exceed!'
            IP = socket.gethostbyname(socket.gethostname())
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            subject = IP + ' ' + processName + '内存使用量过高！'
            content = now + ' ' + IP + ' ' + processName + '内存使用量过高,达到' + str(
                totalMem) + 'M\n请尽快处理！'
            logger.info(processName + '内存使用量过高,达到' + str(totalMem) + 'M')
            send_mail(['sunwei_work@163.com', 'sunweiworkplace@gmail.com'],
                      subject, content)
        if totalCpu > float(config.get('MonitorProcessValue', 'CPU')):
            print 'CPU Exceed!'
            IP = socket.gethostbyname(socket.gethostname())
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            subject = IP + ' ' + processName + 'CPU使用率过高！'
            content = now + ' ' + IP + ' ' + processName + 'CPU使用率过高,达到' + str(
                totalCpu) + '%\n请尽快处理！'
            logger.info(processName + 'CPU使用率过高,达到' + str(totalMem) + 'M')
            send_mail(['sunwei_work@163.com', 'sunweiworkplace@gmail.com'],
                      subject, content)
    except Exception, e:
        print str(e)
        logger.info(str(e))


#判断进程是否存活
def judgeIfAlive(ProgramPath, ProcessName):
    try:
        print datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for process in c.Win32_Process():
            ProList.append(str(process.Name))
        #把所有任务管理器中的进程名添加到列表

        if ProcessName in ProList:
            countProcessMemoey(ProcessName)
            #判断进程名是否在列表中，如果是True，则所监控的服务正在 运行状态，
            #打印服务正常运行
            print ''
            print ProcessName + " Server is running..."
            print ''
            logger.info(ProcessName + " Server is running...")
        else:
            #如果进程名不在列表中，即监控的服务挂了，则在log文件下记录日志
            #日志文件名是以年月日为文件名
            IP = socket.gethostbyname(socket.gethostname())
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            subject = IP + ' ' + ProcessName + '已停止运行！'
            logger.info(ProcessName + '已停止运行！')
            content = now + ' ' + IP + ' ' + ProcessName + '已停止运行！' + '\n请尽快处理！'
            send_mail(['sunwei_work@163.com', 'sunweiworkplace@gmail.com'],
                      subject, content)
            print ProcessName + ' Server is not running...'
            #打印服务状态
            logger.info('\n' +
                        'Server is not running,Begining to Restart Server...' +
                        '\n' + (time.strftime('%Y-%m-%d %H:%M:%S --%A--%c',
                                              time.localtime()) + '\n'))
            #写入时间和服务状态到日志文件中
            os.startfile(ProgramPath)
            #调用服务重启
            logger.info(
                ProcessName + 'Restart Server Success...' + '\n' +
                time.strftime('%Y-%m-%d %H:%M:%S --%A--%c', time.localtime()))
            print ProcessName + 'Restart Server Success...'
            print time.strftime('%Y-%m-%d %H:%M:%S --%A--%c', time.localtime())
        del ProList[:]
        #清空列表，否则列表会不停的添加进程名，会占用系统资源
    except Exception, e:
        print str(e)
        logger.info(str(e))


def startMonitor(ProgramPathDict, ProcessNameDict):
    for i in range(0, len(ProcessNameDict)):
        judgeIfAlive(ProgramPathDict[i], ProcessNameDict[i])


if __name__ == "__main__":
    CONFIGFILE = 'config.ini'
    config = ConfigParser()
    config.read(CONFIGFILE)
    ProgramPathDict = config.get('MonitorProgramPath',
                                 'ProgramPath').split("|")
    ProcessNameDict = config.get('MonitorProcessName',
                                 'ProcessName').split("|")
    while True:
        startMonitor(ProgramPathDict, ProcessNameDict)
        time.sleep(int(config.get('MonitorProcessValue', 'Time')))
