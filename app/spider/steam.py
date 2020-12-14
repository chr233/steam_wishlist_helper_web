# -*- coding: UTF-8 -*-
'''
# @Author       : Chr_
# @Date         : 2020-06-21 15:41:24
# @LastEditors  : Chr_
# @LastEditTime : 2020-12-15 01:14:20
# @Description  : 读取Steam愿望单信息【异步】
'''

from requests import Session
from logging import getLogger
from bs4 import BeautifulSoup
from json import JSONDecodeError
from.static import HEADERS,URLs


async def get_game_info(appid:int) -> dict:
    '''
    获取steam愿望单单页详情

    参数:
        client: httpx异步client对象
        steamid: 64位steamid
        page: 页码
    返回:
        dict: 愿望单信息字典,key:{游戏信息}
    '''
    url = URLs.Steam_Wishlist_XHR % (steamid, page)
    headers = {
        'Referer': URLs.Steam_Wishlist % (steamid, 'order')
    }
    resp = await adv_http_get(client=client, url=url, headers=headers)
    wishlist = {}
    if resp:
        try:
            datajson = resp.json()
        except (JSONDecodeError, AttributeError):
            logger.error('Json解析失败')
            logger.error(resp.content)
            return {}

        for key in datajson.keys():
            data = datajson[key]
            review_score = int(data.get('review_score', -1))
            key = int(key)
            wishlist[key] = {
                'name': data.get('name', '【解析出错】'),
                'picture': PIC_URL % key,
                'review': {
                    'score': review_score,
                    'result': Num2Review.get(review_score, 'Error'),
                    'total': int(data.get('reviews_total', '0').replace(',', '')),
                    'percent': int(data.get('reviews_percent', 0)),
                },
                'release_date': int(data.get('release_date', 0)),
                'subs': [s['id'] for s in data.get('subs', [])],
                'free': data.get('is_free_game', False),
                'type': GameType2Num.get(data.get('type', 'Error'), 0),
                'priority': data.get('priority', 0),
                'tags': data.get('tags', []),
                'add_date': int(data.get('added', 0)),
                # 'rank': int(data.get('rank', 0)),
                'price': {},
                'platform': (
                    data.get('win', 0) == 1,
                    data.get('mac', 0) == 1,
                    data.get('linux', 0) == 1
                ),
                "card": False
            }
            if wishlist[key]['name'] == '【解析出错】':
                logger.debug(f'数据解析失败 {data}')
    return (wishlist)
