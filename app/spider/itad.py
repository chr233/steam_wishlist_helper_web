# -*- coding: UTF-8 -*-
'''
# @Author       : Chr_
# @Date         : 2020-07-08 19:48:26
# @LastEditors  : Chr_
# @LastEditTime : 2020-12-20 21:58:09
# @Description  : 对接ITAD的API接口
'''

from random import choice
from requests import Session
from .static import URLs
from .basic import retry_get_json, print_log

from django.conf import settings

TOKENS = settings.SWH_SETTINGS['ITAD_TOKENS']
REGION = settings.SWH_SETTINGS['REGION']
COUNTRY = settings.SWH_SETTINGS['COUNTRY']


def __api_interface(session: Session, url: str, params: dict):
    p = {'key': choice(TOKENS), **params}
    jd = retry_get_json(session=session, url=url, params=p,
                        headers=None, cookies=None)
    return jd


def get_plains(session: Session, ids: list) -> dict:
    '''把appid转换成IsThereAnyDeal使用的plainid'''
    url = URLs.ITAD_ID_To_Plain
    result = {}
    subs = [ids[i:i+5] for i in range(0, len(ids), 5)]
    for sub in subs:
        params = {'shop': 'steam',
                  'ids': ','.join([f'app/{x}' for x in sub])}
        jd = __api_interface(session=session, url=url, params=params)
        if jd:
            data = jd.get('data', {})
            for id_ in ids:
                plain = data.get(f'app/{id_}', None)
                if plain:
                    result[id_] = plain
                else:
                    # result[id_] = ''
                    print_log(f'读取App {id_} 出错')
    return result


def __get_current_prices(session: Session, plains: list) -> dict:
    '''获取Steam商店当前价格'''
    params = {'plains': ','.join(plains), 'shops': 'steam',
              'country': COUNTRY, 'region': REGION}
    url = URLs.ITAD_Get_Current_Prices
    result = {}
    jd = __api_interface(session=session, url=url, params=params)
    if jd:
        data = jd.get('data', {})
        for plain in data.keys():
            d = data[plain].get('list', [])
            if len(d) > 1:
                print_log(f'{plain} {d}')
            if d:
                p_new = d[0]['price_new']
                p_old = d[0]['price_old']
                p_cut = d[0]['price_cut']
            else:
                # 未发售游戏,没有价格,标记为-1
                p_new, p_old, p_cut = -1, -1, 0
            result[plain] = (p_new, p_old, p_cut)
    return result


def __get_lowest_prices(session: Session, plains: list) -> dict:
    '''获取Steam商店史低价格'''
    params = {'plains': ','.join(plains), 'shops': 'steam',
              'country': COUNTRY, 'region': REGION}
    url = URLs.ITAD_Get_Lowest_Prices
    result = {}
    jd = __api_interface(session=session, url=url, params=params)
    if jd:
        data = jd.get('data', {})
        for plain in data.keys():
            d = data[plain]
            if 'shop' in d:
                p_low = d['price']
                p_cut = d['cut']
                p_time = d['added']
            else:
                # 未发售游戏,没有价格,标记为-1
                p_low, p_cut, p_time = -1, 0, 0
            result[plain] = (p_low, p_cut, p_time)
    return result


def get_prices(session: Session, plains: list) -> dict:
    subs = [plains[i:i+4] for i in range(0, len(plains), 4)]
    result = {}
    for sub in subs:
        current = __get_current_prices(session, sub)
        lowest = __get_lowest_prices(session, sub)
        for p in sub:
            p_new, p_old, p_cut = current.get(p) or [-1, -1, 0]
            p_low, p_lcut, p_time = lowest.get(p) or [-1, 0, 0]
            free = p_old == 0
            result[p] = {'free': free,
                         'pcurrent': p_new,
                         'porigin': p_old,
                         'pcut': p_cut,
                         'plowest': p_low,
                         'plowestcut': p_lcut,
                         'tlowest': p_time}
    return result
