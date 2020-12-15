# -*- coding: UTF-8 -*-
'''
# @Author       : Chr_
# @Date         : 2020-12-11 20:05:41
# @LastEditors  : Chr_
# @LastEditTime : 2020-12-15 20:03:02
# @Description  : 视图函数
'''

from django.http.response import Http404
from rest_framework import viewsets
from rest_framework.response import Response
from app.serializers import GameInfoSerializer, TagsSerializer, CompanySerializer

from .models import GameInfo, Tags, Company

from .task import init_scheduler
init_scheduler()

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

        if not game.ready:
            if not request.user.is_authenticated:
                raise Http404
        else:
            game.cview += 1
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
