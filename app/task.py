# -*- coding: UTF-8 -*-
'''
# @Author       : Chr_
# @Date         : 2020-12-15 00:09:43
# @LastEditors  : Chr_
# @LastEditTime : 2020-12-16 07:12:32
# @Description  : 定时调度器
'''

from sys import argv

import time
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_job, register_events

from .spider import steam

def flush_steam_info():
    # 具体要执行的代码
    steam.g
    print(f'任务运行成功！{time.strftime("%Y-%m-%d %H:%M:%S")}')

def flush_price_info():
    # 具体要执行的代码
    print(f'任务运行成功！{time.strftime("%Y-%m-%d %H:%M:%S")}')

def init_scheduler():
    if not(argv and 'run' in argv[-1] ):
        return
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    
    scheduler.add_job(flush_steam_info,"interval",minutes=5,id="flush_steam_info")
    scheduler.add_job(flush_price_info,"interval",minutes=5,id="flush_price_info")
    
    register_events(scheduler)
    scheduler.start()
