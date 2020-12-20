from django.conf import settings

from .models import GameInfo, Tag, Company, GameAddList, GameBanList
from .spider.basic import get_timestamp, Session
from .spider.steam import get_game_info as steam_info
from .spider.keylol import get_game_info as keylol_info
from .spider.itad import get_plains, get_prices
from .spider.static import AppNotFound
from .spider.basic import print_log

INFO_PERIOD = settings.SWH_SETTINGS['INFO_UPDATE_PERIOD']
PRICE_PERIOD = settings.SWH_SETTINGS['PRICE_UPDATE_PERIOD']
MAX_ERROR = settings.SWH_SETTINGS['MAX_ERROR']


def __gen_tag_list(tags: list) -> list:
    '''生成标签列表'''
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


def __gen_tag_list_k(tags: list) -> list:
    '''生成标签列表'''
    ts = []
    for name, _ in tags:
        try:
            t = Tag.objects.get(name=name)
        except Tag.DoesNotExist:
            try:
                t = Tag.objects.get(name_en=name)
            except Tag.DoesNotExist:
                print_log(f'未找到标签{name}')
                continue
                # t = Tag(name=name, name_en=name_en)
                # t.save()
        finally:
            ts.append(t.id)
    return ts


def __gen_company_list(tags: list) -> list:
    '''生成发行商/开发商列表'''
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


def __modify_game_info(appid, info, g: GameInfo = None):
    '''修改模型字段'''
    try:
        if not g:
            try:
                g = GameInfo.objects.get(appid=appid)
            except GameInfo.DoesNotExist:
                g = GameInfo(appid=appid)
                g.save()
        g.name = info.get('name', g.name)
        g.name_cn = info.get('name_cn', g.name_cn)
        g.gtype = info.get('gtype', g.gtype)
        g.source = info.get('source', g.source)
        g.card = info.get('card', g.card)
        g.limit = info.get('card', g.limit)
        g.adult = info.get('adult', g.adult)
        g.release = info.get('release', g.release)
        g.rscore = info.get('rscore', g.rscore)
        g.rtotal = info.get('rtotal', g.rtotal)
        g.rpercent = info.get('rpercent', g.rpercent)
        g.trelease = info.get('trelease', g.trelease)
        g.tmodify = get_timestamp()
        g.tuinfo = get_timestamp() + INFO_PERIOD
        t = info.get('tags')
        if t:
            if g.source == 'S':
                g.tags.set(__gen_tag_list(t))
            elif g.source == 'K':
                g.tags.set(__gen_tag_list_k(t))
        d = info.get('develop')
        if d:
            g.develop.set(__gen_company_list(d))
        p = info.get('publish')
        if p:
            g.publish.set(__gen_company_list(p))
        g.cupdate += 1
        return g
    except Exception as e:
        print_log(f'出错了 {e}')


def __modify_game_price(appid, price, g: GameInfo = None):
    '''修改模型字段'''
    if not g:
        try:
            g = GameInfo.objects.get(appid=appid)
        except GameInfo.DoesNotExist:
            g = GameInfo(appid=appid)
    g.free = price.get('free', g.free)
    g.pcurrent = price.get('pcurrent', g.pcurrent)
    g.porigin = price.get('porigin', g.porigin)
    g.pcut = price.get('pcut', g.source)
    g.plowest = price.get('plowest', g.card)
    g.plowestcut = price.get('plowestcut', g.limit)
    g.tlowest = price.get('tlowest', g.adult)
    g.tmodify = get_timestamp()
    g.tuprice = get_timestamp() + INFO_PERIOD
    g.cupdate += 1
    return g


def add_new_games():
    '''添加新游戏'''
    print_log('添加新游戏')
    qs = GameAddList.objects.all()[:500]
    print_log(f'开始执行任务,共{len(qs)}个游戏')
    ss = Session()
    for ag in qs:
        appid = ag.appid
        try:
            print_log(f'开始处理app {appid} 信息')
            info = steam_info(ss, appid) or keylol_info(ss, appid)
            if info:
                print_log(f'app {appid} 信息读取成功')
                # print_log(f'app {appid} {info}')
                try:
                    g = __modify_game_info(appid, info, None)
                    g.save()
                    ag.delete()
                except Exception:
                    print_log(f'app {appid} 修改失败')
                    ag.cerror += 1
                    ag.save()
            else:
                # 所有渠道都获取失败
                print_log(f'app {appid} 信息获取失败')
                ag.cerror += 1
                if ag.cerror >= MAX_ERROR:
                    raise AppNotFound
                else:
                    ag.save()
        except AppNotFound:
            # 下架或者被ban
            try:
                g = GameInfo.objects.all().last()
                maxid = g.appid
            except GameInfo.DoesNotExist:
                maxid = 9999999
            if appid < maxid:
                print_log(f'app {appid} 被禁用')
                bg = GameBanList(appid=appid, tadd=get_timestamp(),
                                 cview=ag.cview, cerror=ag.cerror)
                bg.save()
                ag.delete()
            else:
                ag.tadd = get_timestamp() + INFO_PERIOD
                ag.save()


def update_current_games_info():
    '''更新现有游戏'''
    print_log('更新游戏基本信息')
    ts = get_timestamp()
    qs = GameInfo.objects.filter(eupdate=True, tuinfo__lte=ts)[:50]
    ss = Session()
    print_log(f'开始执行任务,共{len(qs)}个游戏')
    for g in qs:
        appid = g.appid
        try:
            print_log(f'开始处理app {appid} 信息')
            info = steam_info(ss, appid) or keylol_info(ss, appid)
            if info:
                print_log(f'app {appid} 信息读取成功')
                # print_log(f'app {appid} {info}')
                __modify_game_info(appid, info, g)
            else:
                # 所有渠道都获取失败
                print_log(f'app {appid} 信息获取失败')
                g.cerror += 1
                if g.cerror >= MAX_ERROR:
                    raise AppNotFound
        except AppNotFound:
            # 下架或者被ban,无数失败次数,直接禁用更新
            print_log(f'app {appid} 禁用更新')
            g.eupdate = False
        finally:
            try:
                g.save()
            except Exception:
                print_log(f'app {appid} 保存失败')


def update_current_games_price():
    '''更新现有游戏'''
    print_log('更新游戏价格信息')
    ts = get_timestamp()
    qs = GameInfo.objects.filter(eupdate=True, tuprice__lte=ts)[:50]
    ss = Session()
    print_log(f'开始执行任务,共{len(qs)}个游戏')

    a2p_map = {}  # appid和plains对照表
    appidlist = []
    for g in qs:  # 为没有plains的条目添加plains
        plains = g.plains
        appid = g.appid
        if not plains:
            appidlist.append(appid)
        a2p_map[appid] = plains
    newplains = get_plains(ss, appidlist)  # 获取plains
    a2p_map.update(newplains)
    vaildplains = list(filter(None, a2p_map.values()))
    pricesdic = get_prices(ss, vaildplains)
    for g in qs:
        appid = g.appid
        plains = a2p_map[appid]
        if plains in pricesdic:
            price = pricesdic.get(plains)
            g.plains = plains
            __modify_game_price(appid, price, g)
        else:
            print_log(f'app {appid} 价格获取失败')
            g.cerror += 1
            g.plains = ''
            if g.cerror >= MAX_ERROR:
                print_log(f'app {appid} 禁用更新')
                g.eupdate = False
        try:
            g.save()
        except Exception:
            print_log(f'app {appid} 保存失败')
