# -*- coding: UTF-8 -*-
'''
# @Author       : Chr_
# @Date         : 2020-12-15 00:35:49
# @LastEditors  : Chr_
# @LastEditTime : 2020-12-16 04:52:43
# @Description  : 带自动重试的请求器
'''

from logging import getLogger
from time import sleep
from requests import Session, Response

from.static import HEADERS, TIMEOUT

logger = getLogger('Basic')


def retry_get(session: Session, url: str, params: dict = None,
              headers: dict = None, cookies: dict = None, retrys: int = 3) -> Response:
    if not headers:
        headers = HEADERS

    for _ in range(0, retrys):
        try:
            resp = session.get(url=url, params=params, headers=headers,
                               cookies=cookies, timeout=TIMEOUT)
            if resp.status_code == 200:
                return resp
        except Exception as e:
            logger.warning(e)
            if _ == 0:
                logger.warning('网络错误,暂停5秒')
                sleep(5)
            else:
                logger.warning('网络错误,暂停15秒')
                sleep(15)
