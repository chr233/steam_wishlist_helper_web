# -*- coding: UTF-8 -*-
'''
# @Author       : Chr_
# @Date         : 2020-06-21 15:41:24
# @LastEditors  : Chr_
# @LastEditTime : 2020-12-17 15:08:35
# @Description  : 读取Steam愿望单信息
'''

from re import findall
from time import strptime, mktime
from logging import getLogger
from json import JSONDecodeError
from bs4 import BeautifulSoup

from requests import Session
from requests.cookies import RequestsCookieJar
from soupsieve import select
from .static import HEADERS, URLs, Norst, STEAM_COOKIES_CN, STEAM_COOKIES_EN
from .basic import retry_get, get_timestamp
# from app.models import GameInfo
# from django.conf import settings
# UPDATE_PERIOD = settings.SWH_SETTINGS['INFO_UPDATE_PERIOD']

UPDATE_PERIOD = 10 * 86400

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

    # 锁区,锁偏好,以及其他错误
    if bool(soup_cn.select_one('.error')):
        return None

    # 游戏名称
    name = (soup_en.select_one('.apphub_AppName') or Norst).text
    name_cn = (soup_cn.select_one('.apphub_AppName') or Norst).text

    # 是否锁偏好
    audlt = bool(soup_cn.select_one('.mature_content_notice'))

    # 右侧信息框
    info_en = soup_en.select_one('.glance_ctn')
    info_cn = soup_cn.select_one('.glance_ctn')
    # 开发商和发行商
    d = info_cn.select('#developers_list>a') or []
    develop = [x.text for x in d]
    p = info_cn.select('div.dev_row:last-child>div.summary>a') or []
    publish = [x.text for x in p]
    # 标签
    t_en = [x.text.strip() for x in info_en.select('a.app_tag') or []]
    t_cn = [x.text.strip() for x in info_cn.select('a.app_tag') or []]
    tags = list(dict(zip(t_cn, t_en)).items())
    # 是否已发行
    release = not(soup_en.select_one('.not_yet'))
    if release:
        # 发行日期
        tr = info_cn.select_one('.date')
        trelease = int(mktime(strptime(tr.text, '%Y年%m月%d日')))
        # 用户评测信息
        r = info_cn.select_one('meta[itemprop="reviewCount"]') or {
            'content': 0}
        rtotal = r.get('content')
        r = info_cn.select_one('meta[itemprop="ratingValue"]') or {
            'content': 0}
        rscore = r.get('content')
        r = info_cn.select('div.user_reviews_summary_row') or [
            {'data-tooltip-html': ''}]
        raw = r[-1].get('data-tooltip-html')
        rpercent = int((findall(r'\d+', raw) or [0])[-1])
    else:
        trelease = 0
        rtotal = 0
        rpercent = 0
        rscore = 0
        rpercent = 0

    tmodify = get_timestamp()
    tuinfo = get_timestamp() + UPDATE_PERIOD

    return {'name': name, 'name_cn': name_cn, 'audlt': audlt, 'release': release,
            'rscore': rscore, 'rtotal': rtotal, 'rpercent': rpercent,
            'trelease': trelease, 'tuinfo': tuinfo, 'tmodify': tmodify,
            'tags': tags, 'develop': develop, 'publish': publish}
