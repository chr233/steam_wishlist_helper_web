# -*- coding: UTF-8 -*-
'''
# @Author       : Chr_
# @Date         : 2020-12-11 20:24:13
# @LastEditors  : Chr_
# @LastEditTime : 2020-12-20 21:16:31
# @Description  : 序列化器
'''

from rest_framework import serializers
from .models import AccessStats, Company, GameAddList, GameBanList, GameInfo, Status, Tag


class AccessStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessStats
        fields = ['id', 'ip', 'ban', 'path']
        extra_kwargs = {
            'id': {'read_only': True},
        }


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'desc']
        extra_kwargs = {
            'id': {'read_only': True},
        }


class GameAddListSerializer(serializers.ModelSerializer):
    appid=serializers.IntegerField()
    class Meta:
        model = GameAddList
        fields = ['appid', 'tadd', 'cview']


class GameBanListSerializer(serializers.ModelSerializer):
    appid=serializers.IntegerField()
    class Meta:
        model = GameBanList
        fields = ['appid', 'tadd', 'cview']


class GameSimpleInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameInfo
        fields = ['appid', 'name', 'name_cn', 'gtype', 'source',
                  'eupdate',  'card', 'limit', 'adult', 'free', 'release',
                  'rscore', 'rtotal', 'rpercent',
                  'pcurrent', 'porigin', 'plowest', 'pcut', 'plowestcut',
                  'trelease', 'tlowest', 'tmodify',
                  'tags', 'develop',  'publish']
        extra_kwargs = {
            'appid': {'read_only': True},
        }


class GameFullInfoSerializer(serializers.ModelSerializer):
    appid=serializers.IntegerField()
    class Meta:
        model = GameInfo
        fields = ['appid', 'name', 'name_cn', 'gtype', 'source',
                  'eupdate',  'card', 'limit', 'adult', 'free', 'release',
                  'rscore', 'rtotal', 'rpercent',
                  'pcurrent', 'porigin', 'plowest', 'pcut', 'plowestcut',
                  'tadd', 'trelease', 'tlowest', 'tmodify', 'tuprice', 'tuinfo',
                  'cview', 'cupdate', 'cerror', 'tags',  'develop',  'publish']


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'name', 'value']
        extra_kwargs = {
            'id': {'read_only': True},
        }


class TagSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tag
        fields = ['id', 'name', 'name_en']
        extra_kwargs = {
            'id': {'read_only': True},
        }
