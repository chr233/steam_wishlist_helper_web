# -*- coding: UTF-8 -*-
'''
# @Author       : Chr_
# @Date         : 2020-12-15 00:09:43
# @LastEditors  : Chr_
# @LastEditTime : 2020-12-15 00:35:23
# @Description  : 定时调度器
'''

import time
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_job, register_events

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")


@register_job(scheduler, "interval", minutes=5, id='flush_steam_info')
def flush_steam_info():
    # 具体要执行的代码
    print(f'任务运行成功！{time.strftime("%Y-%m-%d %H:%M:%S")}')


@register_job(scheduler, "interval", minutes=5, id='flush_price_info')
def flush_price_info():
    # 具体要执行的代码
    print(f'任务运行成功！{time.strftime("%Y-%m-%d %H:%M:%S")}')


def init_scheduler():
    '''初始化调度器'''
    register_events(scheduler)
    # 调度器开始运行
    scheduler.start()
