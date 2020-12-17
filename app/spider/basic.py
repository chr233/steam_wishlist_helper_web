# -*- coding: UTF-8 -*-
'''
# @Author       : Chr_
# @Date         : 2020-12-15 00:35:49
# @LastEditors  : Chr_
# @LastEditTime : 2020-12-18 00:49:41
# @Description  : 带自动重试的请求器
'''

from json.decoder import JSONDecodeError
from logging import getLogger
from time import sleep
from re import findall, MULTILINE
from time import time
from json import loads
from requests import Session, Response

from.static import HEADERS, TIMEOUT

logger = getLogger('Basic')


def get_timestamp():
    return int(time())


def retry_get(session: Session, url: str, params: dict = None,
              headers: dict = None, cookies: dict = None, retrys: int = 3) -> Response:
    if not headers:
        headers = HEADERS

    for _ in range(0, retrys):
        try:
            resp = session.get(url=url, params=params, headers=headers,
                               cookies=cookies, timeout=TIMEOUT)
            if resp.status_code == 200:
                resp.encoding = 'utf-8'
                return resp
        except Exception as e:
            logger.warning(e)
            if _ == 0:
                logger.warning('网络错误,暂停3秒')
                sleep(3)
            else:
                logger.warning('网络错误,暂停10秒')
                sleep(10)


def retry_get_json(session: Session, url: str, params: dict = None,
                   headers: dict = None, cookies: dict = None, retrys: int = 3) -> dict:
    if not headers:
        headers = HEADERS

    for _ in range(0, retrys):
        try:
            resp = session.get(url=url, params=params, headers=headers,
                               cookies=cookies, timeout=TIMEOUT)
            if resp.status_code == 200:
                resp.encoding = 'utf-8'
                jd = resp.json()
                return jd
        except JSONDecodeError:
            logger.warning('JSON解析失败')
        except Exception as e:
            logger.warning(e)
            if _ == 0:
                logger.warning('网络错误,暂停3秒')
                sleep(3)
            else:
                logger.warning('网络错误,暂停10秒')
                sleep(10)
    return {}


def retry_get_json_keylol(session: Session, url: str, params: dict = None,
                          headers: dict = None, cookies: dict = None, retrys: int = 3) -> dict:
    if not headers:
        headers = HEADERS

    for _ in range(0, retrys):
        try:
            resp = session.get(url=url, params=params, headers=headers,
                               cookies=cookies, timeout=TIMEOUT)
            if resp.status_code == 200:
                resp.encoding = 'utf-8'
                raw = findall(r'(\{.+\})', resp.text, MULTILINE)
                jd = loads(raw)
                return jd
        except JSONDecodeError:
            logger.warning('JSON解析失败')
        except Exception as e:
            logger.warning(e)
            if _ == 0:
                logger.warning('网络错误,暂停3秒')
                sleep(3)
            else:
                logger.warning('网络错误,暂停10秒')
                sleep(10)
    return {}
