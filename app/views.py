# -*- coding: UTF-8 -*-
'''
# @Author       : Chr_
# @Date         : 2020-12-11 20:05:41
# @LastEditors  : Chr_
# @LastEditTime : 2020-12-18 12:59:46
# @Description  : 视图函数
'''
from sys import argv
from django.conf import settings
from django.http.response import Http404, JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
# from django.contrib import requests
from app.serializers import GameInfoSerializer, TagsSerializer, CompanySerializer

from .models import GameInfo, Tags, Company

from .spider.itad import get_plains, get_prices,Session

TIME_DECREASE = settings.SWH_SETTINGS['TIME_DECREASE']


def test(requests):
    ss=Session()
    a = get_plains(ss,[379720, 730, 236850, 1167700])
    b = get_prices(ss,a.values())

    result = {'A':a,'B':b}

    return JsonResponse({'result': result})


class GameInfoViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not request.user.is_authenticated:
            qs = queryset.filter(ready=True)
        else:
            qs = queryset
        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(qs, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def retrieve(self, request,  *args, **kwargs):
        try:
            game = self.get_object()
        except Http404:
            try:
                pk = int(kwargs['pk'])
            except ValueError:
                raise Http404
            game = GameInfo(appid=pk)
            game.save()

        if not game.visable:
            if not request.user.is_authenticated:
                raise Http404
        else:
            game.cview += 1
            t = game.tuinfo
            if t >= TIME_DECREASE:
                game.tuinfo = t-TIME_DECREASE
            t = game.tuprice
            if t >= TIME_DECREASE:
                game.tuprice = t-TIME_DECREASE
            game.save()

        serializer = GameInfoSerializer(game)
        return Response(serializer.data)

    queryset = GameInfo.objects.all()
    serializer_class = GameInfoSerializer


class CompantViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
