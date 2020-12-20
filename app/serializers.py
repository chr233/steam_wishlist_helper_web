# -*- coding: UTF-8 -*-
'''
# @Author       : Chr_
# @Date         : 2020-12-11 20:24:13
# @LastEditors  : Chr_
# @LastEditTime : 2020-12-20 22:42:14
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
    appid = serializers.IntegerField()

    class Meta:
        model = GameAddList
        fields = ['appid', 'tadd', 'cview']


class GameBanListSerializer(serializers.ModelSerializer):
    appid = serializers.IntegerField()

    class Meta:
        model = GameBanList
        fields = ['appid', 'tadd', 'cview']


class GameSimpleInfoSerializer(serializers.ModelSerializer):
    tag = serializers.SlugRelatedField(
        read_only=True, many=True,  source='tags', slug_field='name')
    developer = serializers.SlugRelatedField(
        read_only=True, many=True,  source='develop', slug_field='name')
    publisher = serializers.SlugRelatedField(
        read_only=True, many=True, source='publish', slug_field='name')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update(gtype=instance.get_gtype_display(),
                    source=instance.get_source_display())
        return data

    class Meta:
        model = GameInfo
        fields = ['appid', 'name', 'name_cn', 'gtype', 'source',
                  'eupdate',  'card', 'limit', 'adult', 'free', 'release',
                  'rscore', 'rtotal', 'rpercent',
                  'pcurrent', 'porigin', 'plowest', 'pcut', 'plowestcut',
                  'trelease', 'tlowest', 'tmodify',
                  'tag', 'developer',  'publisher']
        extra_kwargs = {
            'appid': {'read_only': True},
        }


class GameFullInfoSerializer(serializers.ModelSerializer):
    appid = serializers.IntegerField()

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
