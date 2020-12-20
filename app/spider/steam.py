# -*- coding: UTF-8 -*-
'''
# @Author       : Chr_
# @Date         : 2020-06-21 15:41:24
# @LastEditors  : Chr_
# @LastEditTime : 2020-12-21 00:20:21
# @Description  : 爬取Steam商店信息
'''

from re import findall
from time import strptime, mktime
from bs4 import BeautifulSoup
from requests import Session
from soupsieve import select

from .static import URLs, Norst, AppNotFound, STEAM_COOKIES_CN, STEAM_COOKIES_EN
from .basic import print_log, retry_get


def __get_soup(session: Session, url: str, language: str = 'CN') -> BeautifulSoup:
    cookies = STEAM_COOKIES_EN if language == 'EN' else STEAM_COOKIES_CN
    resp = retry_get(session=session, url=url, cookies=cookies)
    if resp:
        soup = BeautifulSoup(resp.text, 'lxml')
        return soup
    else:
        print_log('请求失败,结束')
        return None


def __judge_type(strlist: list) -> int:
    '''判断游戏类型'''
    if 'All Games' in strlist:
        if 'Downloadable Content' not in strlist:
            return 'G'
        else:
            return 'D'
    elif 'All Software' in strlist:
        return 'S'
    elif 'All Videos' in strlist:
        return 'V'
    else:
        return ''


def get_game_info(session: Session, appid: int):
    url = URLs.Steam_Store_App % appid
    soup_en = __get_soup(session=session, url=url, language='EN')
    soup_cn = __get_soup(session=session, url=url, language='CN')

    # 锁区,需要登录,以及其他错误
    emsg = (soup_cn.select_one('.error')
            or soup_cn.select_one('#error_box') or Norst).text
    if emsg != '':
        print_log(f'读取APP {appid} 出错 {emsg}')
        return None  # 返回空值,通过其他方式获取信息

    # 游戏名称
    name = (soup_en.select_one('.apphub_AppName') or Norst).text
    name_cn = (soup_cn.select_one('.apphub_AppName') or Norst).text

    # 下架,被ban,直接跳转到首页获取不到标题
    if name == '':
        print_log(f'读取APP {appid} 出错')
        raise AppNotFound(f'读取APP {appid} 出错')

    bgs = [x.text for x in (soup_en.select('.blockbg>a') or [])]
    gtype = __judge_type(bgs)

    category = soup_cn.select_one('#category_block')
    if category:
        card = bool(category.select_one('img[src$="ico_cards.png"]'))
        limit = bool(category.select_one('div.learning_about'))
    else:
        card = limit = False
    # 是否锁偏好
    adult = bool(soup_cn.select_one('.mature_content_notice'))

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
    release = not(bool(soup_en.select_one('.not_yet')) or bool(
        soup_en.select_one('div.game_area_comingsoon')))

    # 发行日期
    tr = info_cn.select_one('.date') or Norst
    trelease = 0

    if release:
        try:
            trelease = int(mktime(strptime(tr.text, '%Y年%m月%d日')))
        except Exception:
            print_log(f'app {appid} 读取发型日期出错 {tr.text}')
            release = False

    if release:
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
        rscore = 0
        rtotal = 0
        rpercent = 0
        trelease = 0

    return {'name': name, 'name_cn': name_cn,
            'gtype': gtype, 'source': 'S',
            'card': card, 'limit': limit,
            'adult': adult, 'release': release,
            'rscore': rscore, 'rtotal': rtotal,
            'rpercent': rpercent,  'trelease': trelease,
            'tags': tags, 'develop': develop, 'publish': publish}
