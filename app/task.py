# -*- coding: UTF-8 -*-
'''
# @Author       : Chr_
# @Date         : 2020-12-15 00:09:43
# @LastEditors  : Chr_
# @LastEditTime : 2020-12-17 16:47:49
# @Description  : 定时调度器
'''

import time

from .spider import steam



def flush_steam_info():
    # 具体要执行的代码
    print(f'任务运行成功！{time.strftime("%Y-%m-%d %H:%M:%S")}')


def flush_price_info():
    # 具体要执行的代码
    print(f'任务运行成功！{time.strftime("%Y-%m-%d %H:%M:%S")}')

