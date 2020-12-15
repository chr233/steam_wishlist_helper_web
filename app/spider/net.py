# -*- coding: UTF-8 -*-
'''
# @Author       : Chr_
# @Date         : 2020-12-15 00:35:49
# @LastEditors  : Chr_
# @LastEditTime : 2020-12-15 20:19:02
# @Description  : 带自动重试的请求器
'''

import re
import json
from logging import getLogger
from time import sleep
from bs4 import BeautifulSoup
from requests import Session, Response

from.static import HEADERS, TREAD_CD, TIMEOUT

logger = getLogger('Net')




async def get_html(session: Session, url: str, params: dict = None,
                   headers: dict = None, retrys: int = 3) -> BeautifulSoup:
    if not headers:
        headers = HEADERS
    for _ in range(0, retrys):
        try:
            resp = session.get(url=url, params=params,
                               headers=headers, timeout=TIMEOUT)
            resp.encoding = 'utf-8'
            soup = BeautifulSoup(resp.text, 'lxml')
            return soup
        except Exception:
            if _ == 0:
                logger.debug('网络错误,暂停5秒')
                sleep(5)
            else:
                logger.warning('网络错误,暂停15秒')
                sleep(15)
    return None


def k_get_json(session: Session, url: str, params: dict = None,
               headers: dict = None, retrys: int = 3) -> Response:
    if not headers:
        headers = HEADERS
    for _ in range(0, retrys):
        try:
            resp = session.get(url=url, params=params,
                               headers=headers, timeout=TIMEOUT)
            pattern = re.compile(r'(\{.+\})', re.MULTILINE)
            matchobj = pattern.search(resp.text)
            jd = json.loads(matchobj.group(1))
            sleep(TREAD_CD)
            return (jd)
        except Exception:
            if _ == 0:
                logger.debug('网络错误,暂停8秒')
                sleep(8)
            else:
                logger.warning('网络错误,暂停30秒')
                sleep(30)
    logger.error('网络错误,请求失败')
    return {}


def get_json(session: Session, url: str, params: dict = None,
             headers: dict = None, retrys: int = 3) -> dict:
    if not headers:
        headers = HEADERS
    for _ in range(0, retrys):
        try:
            resp = session.get(url=url, params=params,
                               headers=headers, timeout=TIMEOUT)
            jd = resp.json()
            return jd
        except Exception:
            if _ == 0:
                logger.debug('网络错误,暂停8秒')
                sleep(8)
            else:
                logger.warning('网络错误,暂停30秒')
                sleep(30)
    logger.error('网络错误,请求失败')
    return {}
