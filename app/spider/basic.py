# -*- coding: UTF-8 -*-
'''
# @Author       : Chr_
# @Date         : 2020-12-15 00:35:49
# @LastEditors  : Chr_
# @LastEditTime : 2020-12-20 21:20:32
# @Description  : 带自动重试的请求器
'''

from json.decoder import JSONDecodeError
from logging import getLogger
from time import sleep, strftime
from re import findall, MULTILINE
from time import time
from json import loads
from requests import Session, Response

from.static import HEADERS, TIMEOUT


def get_timestamp():
    return int(time())


def print_log(message: str):
    '''打印日志'''
    print(f'{strftime("%Y-%m-%d %H:%M:%S")} {message}')


def retry_get(session: Session, url: str, params: dict = None,
              headers: dict = None, cookies: dict = None, retrys: int = 3) -> Response:
    '''带自动重试的请求器,返回soup'''
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
            print_log(e)
            if _ == 0:
                print_log('网络错误,暂停3秒')
                sleep(3)
            else:
                print_log('网络错误,暂停10秒')
                sleep(10)


def retry_get_json(session: Session, url: str, params: dict = None,
                   headers: dict = None, cookies: dict = None, retrys: int = 3) -> dict:
    '''带自动重试的请求器,返回json'''
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
            print_log('JSON解析失败')
        except Exception as e:
            print_log(e)
            if _ == 0:
                print_log('网络错误,暂停3秒')
                sleep(3)
            else:
                print_log('网络错误,暂停10秒')
                sleep(10)
    return {}


def retry_get_json_keylol(session: Session, url: str, params: dict = None,
                          headers: dict = None, cookies: dict = None, retrys: int = 3) -> dict:
    '''带自动重试的请求器,返回json,keylol专用'''
    if not headers:
        headers = HEADERS

    for _ in range(0, retrys):
        try:
            resp = session.get(url=url, params=params, headers=headers,
                               cookies=cookies, timeout=TIMEOUT)
            if resp.status_code == 200:
                resp.encoding = 'utf-8'
                raw = findall(r'(\{.+\})', resp.text, MULTILINE)
                if raw:
                    jd = loads(raw[0])
                    return jd
        except JSONDecodeError:
            print_log('JSON解析失败')
        except Exception as e:
            print_log(e)
            if _ == 0:
                print_log('网络错误,暂停3秒')
                sleep(3)
            else:
                print_log('网络错误,暂停10秒')
                sleep(10)
    return {}
