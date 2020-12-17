# -*- coding: UTF-8 -*-
'''
# @Author       : Chr_
# @Date         : 2020-06-30 05:08:57
# @LastEditors  : Chr_
# @LastEditTime : 2020-12-18 00:38:09
# @Description  : 对接Keylol的API接口
'''


from logging import getLogger
from requests import Session

from .static import URLs
from .basic import retry_get_json_keylol


logger = getLogger('Keylol')

async def get_game_info(session: Session, appid: int) -> dict:
    '''读取steam游戏信息'''
    url = URLs.Keylol_Get_Game_Info % appid

    jd = retry_get_json_keylol(session=session, url=url)
    result = {}
    if jd:
        result[appid] = {
            # 'tags': set(jd.get('tags', []) + jd.get('genre', [])),
            # 'categories': [(int(x[0]), x[1])for x in raw.get('categories', [])],
            'card': len(jd.get('card', [])) > 0,
            # 'description': jd.get('description', '')
        }
    return (result)
