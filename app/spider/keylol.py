# -*- coding: UTF-8 -*-
'''
# @Author       : Chr_
# @Date         : 2020-06-30 05:08:57
# @LastEditors  : Chr_
# @LastEditTime : 2020-12-20 20:27:40
# @Description  : 对接Keylol的API接口
'''

from time import strptime, mktime
from requests import Session

from .static import URLs
from .basic import retry_get_json_keylol, print_log


def calc_rscore(total: int, percent: int):
    if total < 10:
        score = 0
    if percent < 30:
        score = 3
    elif percent <= 70:
        score = 5
    else:
        score = 7
    return score
    # if total < 10:
    #     score = 0
    # elif total < 200:
    #     if percent < 30:
    #         score = 3
    #     elif percent <= 70:
    #         score = 5
    #     else:
    #         score = 7
    # elif total < 500:
    #     if percent <30:
    #         score=2
    #     elif percent <45:
    #         score=4
    #     elif percent <70:
    #         score=5
    #     else:
    #         score=6
    # elif total < 1000:
    #     if percent <20:
    #         score=1
    #     if percent <30:
    #         score=2
    #     elif percent <45:
    #         score=4
    #     elif percent <70:
    #         score=5
    #     elif percent <70:
    #         score=6
    # if percent >= 96:
    #     if total:
    #         pass
    # return score


def get_game_info(session: Session, appid: int) -> dict:
    '''读取steam游戏信息'''
    url = URLs.Keylol_Get_Game_Info % appid
    jd = retry_get_json_keylol(session=session, url=url)
    if jd:
        name = name_cn = jd.get('name', '无法显示游戏信息')
        if name == '无法显示游戏信息':
            print_log(f'读取APP {appid} 出错')
            return None
        gtype = 'G'  # TODO API未提供相关信息
        card = bool(jd.get('card'))
        adult = False
        cate = [x[0] for x in jd.get('categories', [])]
        limit = 'learning' in cate
        tags = [(x, '')for x in jd.get('tags', [])]
        develop = jd.get('developer', [])
        publish = jd.get('publisher', [])
        release = bool(jd.get('price_steam'))
        if release:
            t = jd.get('release')
            try:
                trelease = int(mktime(strptime(t, '%Y年%m月%d日')))
            except Exception:
                trelease = 0
            s = jd.get('score', {})
            rtotal = s.get('review_positive', 0)+s.get('review_negative', 0)
            rpercent = int(s.get('review', 0))
            rscore = calc_rscore(rtotal, rpercent)
        else:
            rscore = 0
            rtotal = 0
            rpercent = 0
            trelease = 0
    else:
        print_log(f'读取APP {appid} 出错')
        return None

    return {'name': name, 'name_cn': name_cn,
            'gtype': gtype, 'source': 'K',
            'card': card, 'limit': limit,
            'adult': adult, 'release': release,
            'rscore': rscore, 'rtotal': rtotal,
            'rpercent': rpercent, 'trelease': trelease,
            'tags': tags, 'develop': develop, 'publish': publish}
