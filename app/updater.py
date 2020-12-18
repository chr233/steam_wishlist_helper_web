from django.conf import settings

from .models import GameInfo, Tags, Company
from .spider.basic import get_timestamp, Session
from .spider.steam import get_game_info as steam_info
from .spider.keylol import get_game_info as keylol_info

INFO_PERIOD = settings.SWH_SETTINGS['INFO_UPDATE_PERIOD']
PRICE_PERIOD = settings.SWH_SETTINGS['PRICE_UPDATE_PERIOD']

def update_base_info():
    ts = get_timestamp()
    qs = GameInfo.objects.filter(tuinfo_lte=ts)[:10]
    for g in qs:
        appid = g.appid
        ss = Session()
        info = steam_info(ss, appid) or keylol_info(ss, appid)
        if not info:
            g.cerror +=1
            g.save()
