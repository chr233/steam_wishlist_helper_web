'''
# @Author       : Chr_
# @Date         : 2020-12-16 04:15:38
# @LastEditors  : Chr_
# @LastEditTime : 2020-12-16 15:47:05
# @Description  : 测试专用
'''

import sys
sys.path.append("/home/dev/steam_wishlist_helper_web/app/spider")

from app.spider import steam

steam.get_game_info_base(1256610)
steam.get_game_info_base(730)
steam.get_game_info_base(812140)
steam.get_game_info_base(263280)
steam.get_game_info_base(1167700)