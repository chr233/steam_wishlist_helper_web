# -*- coding: UTF-8 -*-
'''
# @Author       : Chr_
# @Date         : 2020-12-15 00:09:43
# @LastEditors  : Chr_
# @LastEditTime : 2020-12-18 17:15:26
# @Description  : 定时调度器
'''

from .updater import add_new_games, update_current_games_info, update_current_games_price

def flush_steam_info():
    # 具体要执行的代码
    add_new_games()
    update_current_games_info()


def flush_price_info():
    # 具体要执行的代码
     update_current_games_price()

