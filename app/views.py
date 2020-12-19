# -*- coding: UTF-8 -*-
'''
# @Author       : Chr_
# @Date         : 2020-12-11 20:05:41
# @LastEditors  : Chr_
# @LastEditTime : 2020-12-20 02:30:05
# @Description  : 视图函数
'''
from app.spider.basic import get_timestamp
from sys import argv
from django.conf import settings
from django.http.response import Http404, HttpResponse, JsonResponse
from rest_framework import views, viewsets
from rest_framework.response import Response
from rest_framework import permissions
# from django.contrib import requests
from app.serializers import GameSimpleInfoSerializer, GameFullInfoSerializer, GameBanListSerializer, GameAddListSerializer
from app.serializers import TagSerializer, CompanySerializer, StatusSerializer, AccessStatsSerializer

from .models import AccessStats, GameInfo, GameAddList, GameBanList, Tag, Company

from .updater import update_base_info

TIME_DECREASE = settings.SWH_SETTINGS['TIME_DECREASE']


def test(requests):
    permission_classes = (permissions.IsAdminUser,)
    update_base_info()

    return HttpResponse('done')


class AccessStatsViewSet(viewsets.ModelViewSet):
    queryset = AccessStats.objects.all()
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = AccessStatsSerializer


class GameAddListViewSet(viewsets.ModelViewSet):
    queryset = GameAddList.objects.all()
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = GameAddListSerializer


class GameBanListViewSet(viewsets.ModelViewSet):
    queryset = GameBanList.objects.all()
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = GameBanListSerializer


class GameFullInfoViewSet(viewsets.ModelViewSet):
    queryset = GameInfo.objects.all()
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = GameFullInfoSerializer


class CompantViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class GameSimpleInfoViewSet(viewsets.ModelViewSet):
    def retrieve(self, request,  *args, **kwargs):
        try:
            game = self.get_object()
        except Http404:
            try:
                pk = int(kwargs['pk'])
            except ValueError:
                raise Http404
            if pk <= 0:
                try:
                    bangame = GameBanList.objects.get(appid=pk)
                    bangame.cview += 1
                    bangame.save()
                except GameBanList.DoesNotExist:
                    try:
                        newgame = GameAddList.objects.get(appid=pk)
                        newgame.cview += 1
                    except GameAddList.DoesNotExist:
                        newgame = GameAddList(appid=pk)
                        newgame.tadd = get_timestamp()
                    finally:
                        newgame.save()
            raise Http404
        else:
            game.cview += 1
            t = game.tuinfo
            if t >= TIME_DECREASE:
                game.tuinfo = t - TIME_DECREASE
            t = game.tuprice
            if t >= TIME_DECREASE:
                game.tuprice = t - TIME_DECREASE
            game.save()

        serializer = GameSimpleInfoSerializer(game)
        return Response(serializer.data)

    queryset = GameInfo.objects.all()
    serializer_class = GameSimpleInfoSerializer
