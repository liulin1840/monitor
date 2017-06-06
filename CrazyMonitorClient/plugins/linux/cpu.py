#!/usr/bin/env python
#coding:utf-8

#apt-get install sysstat

import commands,re
import subprocess

def monitor(frist_invoke=1):
    shell_command = 'sar -u 1 1 |grep "all"'
    status,result = commands.getstatusoutput(shell_command)
    #result = subprocess.Popen(shell_command,shell=True,stdout=subprocess.PIPE).stdout.read()
    if status != 0:
        value_dic = {'status': status}
    else:
        value_dic = {}
        re_resullt = re.sub(r"\s+"," ",result)#\s匹配任何空格字符串
        print(re_resullt)
        user,nice,system,irq,iowait,steal,idle = re_resullt.split(' ')[2:]#以空格拆分成列表,取第三个到最后面的
        value_dic= {
            'user': user,    #显示在用户级别(application)运行使用 CPU 总时间的百分比
            'nice': nice,    #显示在用户级别，用于nice操作，所占用 CPU 总时间的百分比。
            'system': system,#在核心级别(kernel)运行所使用 CPU 总时间的百分比
            'irq':irq,
            'iowait': iowait,#显示用于等待I/O操作占用 CPU 总时间的百分比。
            'steal': steal,  #管理程序(hypervisor)为另一个虚拟进程提供服务而等待虚拟 CPU 的百分比。
            'idle': idle,    #显示 CPU 空闲时间占用 CPU 总时间的百分比。
            'status': status
        }
    return value_dic
if __name__ == "__main__":
    monitor()


