# -*- coding: UTF-8 -*-
'''
# @Author       : Chr_
# @Date         : 2020-05-03 23:20:00
# @LastEditors  : Chr_
# @LastEditTime : 2021-01-13 23:39:40
# @Description  : 静态常量
'''

# 近史低标准
ALMOST_LOWEST = 0.05

# 网络超时时间
TIMEOUT = 10


HEADERS = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Steam_Wishlist_Helper",
}


STEAM_COOKIES_CN = {'wants_mature_content': '1',
                    'birthtime': '22503171', 'Steam_Language': 'schinese'}
STEAM_COOKIES_EN = {'wants_mature_content': '1',
                    'birthtime': '22503171', 'Steam_Language': 'english'}


class URLs():
    '''URL常量'''
    Steam_Store = 'https://store.steampowered.com/'
    Steam_Store_App = 'https://store.steampowered.com/app/%s'
    Steam_Wishlist = 'https://store.steampowered.com/wishlist/profiles/%s/#sort=%s'
    Steam_Wishlist_XHR = 'https://store.steampowered.com/wishlist/profiles/%s/wishlistdata/?p=%s'
    Steam_Game_Pic_SM = 'https://steamcdn-a.akamaihd.net/steam/apps/%s/capsule_sm_120.jpg'
    Steam_Game_Pic_MD = 'https://steamcdn-a.akamaihd.net/steam/apps/%s/header_292x136.jpg'

    ITAD_ID_To_Plain = 'https://api.isthereanydeal.com/v01/game/plain/id/'
    ITAD_Get_Current_Prices = 'https://api.isthereanydeal.com/v01/game/prices/'
    ITAD_Get_Lowest_Prices = 'https://api.isthereanydeal.com/v01/game/lowest/'
    ITAD_Get_Game_Info = 'https://api.isthereanydeal.com/v01/game/info/'
    ITAD_Get_Overview_Prices = 'https://api.isthereanydeal.com/v01/game/overview/'

    Keylol_Get_Game_Info = 'https://steamdb.keylol.com/app/%s/data.js?v=38'

    Github_Releases = 'https://github.com/chr233/steam_wishlist_helper/releases'
    Github_Releases_API = 'https://api.github.com/repos/chr233/steam_wishlist_helper/releases/latest'


class Norst():
    '''未找到结果'''
    text = ''


class AppNotFound(Exception):
    '''App不存在'''
    msg: str

    def __init__(self, msg='App不存在'):
        self.msg = msg

    def __str__(self) -> str:
        return self.msg

    def __repr__(self) -> str:
        return self.msg


Review2Num = {
    'Error': -1,
    'No user reviews': 0,
    'Overwhelmingly Negative': 1,
    'Very Negative': 2,
    'Negative': 3,
    'Mostly Negative': 4,
    'Mixed': 5,
    'Mostly Positive': 6,
    'Positive': 7,
    'Very Positive': 8,
    'Overwhelmingly Positive': 9
}

Num2Review = {
    -1: '【解析出错】',
    0: '评测数量不足',
    1: '差评如潮',
    2: '特别差评',
    3: '差评',
    4: '多半差评',
    5: '褒贬不一',
    6: '多半好评',
    7: '好评',
    8: '特别好评',
    9: '好评如潮'
}

Num2GameType = {
    0: '【解析错误】',
    1: '游戏',
    2: '软件',
    3: 'DLC',
    4: '视频'
}
