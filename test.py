'''
# @Author       : Chr_
# @Date         : 2020-12-16 04:15:38
# @LastEditors  : Chr_
# @LastEditTime : 2020-12-18 10:39:12
# @Description  : 测试专用
'''

from app.spider import keylol as steam  # ,itad
import sys

from rest_framework.fields import JSONField
sys.path.append("/home/dev/steam_wishlist_helper_web/app/spider")


ss = steam.Session()

print(steam.get_game_info(ss, 873290))
print(steam.get_game_info(ss, 880250))
print(steam.get_game_info(ss, 1386650))
print(steam.get_game_info(ss, 1256610))
print(steam.get_game_info(ss, 730))
print(steam.get_game_info(ss, 812140))
print(steam.get_game_info(ss, 263280))
print(steam.get_game_info(ss, 1167700))
print(steam.get_game_info(ss, 1477440))
print(steam.get_game_info(ss, 1058500))
print(steam.get_game_info(ss, 1082040))

# import re

# txt='''proc({"id":"730","type":"app","path":"app\/730","name":"Counter-Strike: Global Offensive","description":"\u300a\u53cd\u6050\u7cbe\u82f1\uff1a\u5168\u7403\u653b\u52bf\u300b\uff08CS: GO\uff09\u5ef6\u7eed\u4e86 1999 \u5e74\u539f\u4f5c\u5728\u56e2\u961f\u7ade\u6280\u7c7b\u6e38\u620f\u4e0a\u53d6\u5f97\u7684\u6210\u5c31\u3002 CS: GO \u7684\u7279\u8272\u5305\u542b\u5168\u65b0\u7684\u5730\u56fe\u3001\u4eba\u7269\u3001\u6b66\u5668\u3001\u5168\u65b0\u7684\u6e38\u620f\u6a21\u5f0f\uff0c\u5e76\u63d0\u4f9b\u7ffb\u65b0\u540e\u7684 CS \u7ecf\u5178\u5185\u5bb9\uff08de_dust2 \u7b49\uff09\u3002","language":{"sc":[1,0,0],"en":[1,1,0],"tc":[1,0,0]},"genre":["\u52a8\u4f5c","\u514d\u8d39\u6e38\u73a9"],"developer":["Valve","Hidden Path Entertainment"],"publisher":["Valve"],"release":"2012\u5e748\u670821\u65e5","categories":[["22","Steam \u6210\u5c31"],["28","\u5b8c\u5168\u652f\u6301\u63a7\u5236\u5668"],["29","Steam \u96c6\u6362\u5f0f\u5361\u724c"],["30","Steam \u521b\u610f\u5de5\u574a"],["35","\u5e94\u7528\u5185\u8d2d\u4e70"],["8","\u542f\u7528 Valve \u53cd\u4f5c\u5f0a\u4fdd\u62a4"],["15","\u7edf\u8ba1\u6570\u636e"],["41","\u5728\u624b\u673a\u4e0a\u8fdc\u7a0b\u7545\u73a9"],["42","\u5728\u5e73\u677f\u4e0a\u8fdc\u7a0b\u7545\u73a9"],["43","\u5728\u7535\u89c6\u4e0a\u8fdc\u7a0b\u7545\u73a9"]],"score":{"metacritic":{"score":83,"link":"https:\/\/www.metacritic.com\/game\/pc\/counter-strike-global-offensive","userscore":7.6},"review":87.9,"review_positive":4287870,"review_negative":589296,"opencritic":{"link":"https:\/\/opencritic.com\/game\/9752\/counter-strike-global-offensive","score":82}},"tags":["\u7b2c\u4e00\u4eba\u79f0\u5c04\u51fb","\u5c04\u51fb","\u591a\u4eba","\u7ade\u6280","\u52a8\u4f5c"],"platforms":["win","mac","linux"],"price_steam":{"price":0},"highlights":["81958","ss_34090867f1a02b6c17652ba9043e3f622ed985a9","ss_1d30c9a215fd621e2fd74f40d93b71587bf6409c","ss_baa02e979cd3852e3c4182afcd603ab64e3502f9","ss_ffe584c163a2b16e9c1b733b1c8e2ba669fb1204","ss_d87c102d028d545c877363166c9d8377014f0c23","ss_9d0735a5fbe523fd39f2c69c047019843c326cea","ss_9d889bec419cf38910ccf72dd80f9260227408ee","ss_ccc4ce6edd4c454b6ce7b0757e633b63aa93921d","ss_9db552fd461722f1569e3292d8f2ea654c8ffdef"],"price_history":{"price":{"store":"Steam","cut":0,"price":0,"url":"https:\/\/store.steampowered.com\/app\/730\/"},"lowest":{"store":"Steam","cut":0,"price":0,"recorded":1539214278},"last":null,"bundles":{"count":0,"active":[],"url":"https:\/\/isthereanydeal.com\/game\/counterstrikeglobaloffensive\/info\/"},"steam":{"cut":0,"recorded":1539214278},"history":"https:\/\/isthereanydeal.com\/game\/counterstrikeglobaloffensive\/history\/"},"mydb":1604022249,"name_cn":"\u53cd\u6050\u7cbe\u82f1\uff1a\u5168\u7403\u653b\u52bf^CSGO^\u53cd\u6050\u7cbe\u82f1\uff1a\u5168\u7403\u7a81\u51fb","card":{"booster":0.15,"normal":{"count":5,"average":0.07},"foil":{"count":5,"average":0.36}}});'''

# pattern = re.findall(r'(\{.+\})',txt, re.MULTILINE)
# print(pattern)
