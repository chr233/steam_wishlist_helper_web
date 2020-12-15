'''
# @Author       : Chr_
# @Date         : 2020-12-16 04:15:38
# @LastEditors  : Chr_
# @LastEditTime : 2020-12-16 04:53:33
# @Description  : 测试专用
'''

import sys
sys.path.append("/home/dev/steam_wishlist_helper_web/app/spider")

from app.spider import steam

steam.get_game_info_base(1256610)