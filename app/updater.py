from django.conf import settings

from .models import GameInfo, Tag, Company
from .spider.basic import get_timestamp, Session
from .spider.steam import get_game_info as steam_info
from .spider.keylol import get_game_info as keylol_info
from .spider.static import AppNotFound
from .spider.basic import print_log

INFO_PERIOD = settings.SWH_SETTINGS['INFO_UPDATE_PERIOD']
PRICE_PERIOD = settings.SWH_SETTINGS['PRICE_UPDATE_PERIOD']
MAX_ERROR = settings.SWH_SETTINGS['MAX_ERROR']


def gen_tag_list(tags: list) -> list:
    ts = []
    for name, name_en in tags:
        try:
            t = Tag.objects.get(name=name)
        except Tag.DoesNotExist:
            t = Tag(name=name, name_en=name_en)
            t.save()
        finally:
            ts.append(t.id)
    return ts


def gen_company_list(tags: list) -> list:
    cs = []
    for name in tags:
        try:
            c = Company.objects.get(name=name)
        except Company.DoesNotExist:
            c = Company(name=name)
            c.save()
        finally:
            cs.append(c.id)
    return cs


def update_base_info():
    print_log('开始执行任务')
    ts = get_timestamp()
    qs = GameInfo.objects.filter(tuinfo__lte=ts, eupdate=True)[:10]
    for g in qs:
        appid = g.appid
        ss = Session()
        try:
            print_log(f'开始处理app {appid} 信息')
            info = steam_info(ss, appid) or keylol_info(ss, appid)
            if not info:
                # 所有渠道都获取失败
                print_log(f'app {appid} 信息获取失败')
                g.cerror += 1
                if g.cerror >= MAX_ERROR:
                    g.eupdate = False
            else:
                print_log(f'app {appid} {info}')
                g.name = info.get('name')
                g.name_cn = info.get('name_cn')
                g.source = info.get('source', 0)
                g.card = info.get('card', False)
                g.adult = info.get('adult', False)
                g.release = info.get('release', False)
                g.rscore = info.get('rscore', 0)
                g.rtotal = info.get('rtotal', 0)
                g.rpercent = info.get('rpercent', 0)
                g.trelease = info.get('trelease', 0)
                g.tmodify = get_timestamp()
                g.tuinfo = get_timestamp() + INFO_PERIOD
                g.visible = True
                g.tags.set(gen_tag_list(info.get('tags', [])))
                g.develop.set(gen_company_list(info.get('develop', [])))
                g.publish.set(gen_company_list(info.get('publish', [])))
                g.cupdate+=1
        except AppNotFound:
            # 下架或者被ban
            print_log(f'app {appid} 商店页不存在,停止自动更新')
            g.eupdate = False
            g.cerror += 1
        finally:
            g.save()
