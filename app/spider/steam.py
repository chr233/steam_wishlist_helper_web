# -*- coding: UTF-8 -*-
'''
# @Author       : Chr_
# @Date         : 2020-06-21 15:41:24
# @LastEditors  : Chr_
# @LastEditTime : 2020-12-16 04:52:26
# @Description  : 读取Steam愿望单信息
'''

# from soupsieve import select
# from app import serializers

from logging import getLogger
from json import JSONDecodeError
from bs4 import BeautifulSoup

from requests import Session
from requests.cookies import RequestsCookieJar
from .static import HEADERS, URLs, STEAM_COOKIES_CN, STEAM_COOKIES_EN
from .basic import retry_get

logger = getLogger('Steam')


def get_store_soup(session: Session, url: str, language: str = 'EN') -> BeautifulSoup:
    cookies = STEAM_COOKIES_EN if language == 'EN' else STEAM_COOKIES_CN

    resp = retry_get(session=session, url=url, cookies=cookies)
    if resp:
        resp.encoding = 'utf-8'
        soup = BeautifulSoup(resp.text, 'lxml')
        return soup
    else:
        logger.warning('请求失败,结束')
        return None


def get_soup_key(soup: BeautifulSoup, selector: str, key: str) -> str:
    s = soup.select_one(selector)
    return s.get(key) if s else ''


def get_game_info_base(appid: int):
    ss = Session()
    url = URLs.Steam_Store_App % appid
    soup_en = get_store_soup(session=ss, url=url, language='EN')
    soup_cn = get_store_soup(session=ss, url=url, language='CN')

    n = soup_en.select_one('.apphub_AppName')
    n_cn = soup_cn.select_one('.apphub_AppName')

    name = n.text if n else ''
    name_cn = n_cn.text if n_cn else ''

    print(name,name_cn)
