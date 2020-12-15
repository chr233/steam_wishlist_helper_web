# -*- coding: UTF-8 -*-
'''
# @Author       : Chr_
# @Date         : 2020-12-11 20:24:13
# @LastEditors  : Chr_
# @LastEditTime : 2020-12-16 03:15:31
# @Description  : 序列化器
'''

from rest_framework import serializers
from rest_framework.utils import serializer_helpers
from .models import Company, GameInfo, Tags


class TagsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tags
        fields = ['id', 'name', 'name_cn']
        extra_kwargs = {
            'id': {'read_only': True},
        }


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'name_cn']
        extra_kwargs = {
            'id': {'read_only': True},
        }


class GameInfoSerializer(serializers.ModelSerializer):
    rtags = serializers.SlugRelatedField(
        read_only=True, many=True, source='tags', slug_field='name')
    rdevelop = serializers.SlugRelatedField(
        read_only=True, many=True, source='develop', slug_field='name')
    rpublish = serializers.SlugRelatedField(
        read_only=True, many=True, source='publish', slug_field='name')

    class Meta:
        model = GameInfo
        fields = ['appid', 'name', 'name_cn',
                  'ready', 'card', 'free',
                  'release', 'rscore', 'rtotal', 'rpercent',
                  'pcurrent', 'porigin', 'plowest', 'pcut', 'plowestcut',
                  'tadd', 'tlowest', 'tupdate', 'tmodify', 'trelease',
                  'cview', 'cupdate', 'cerror', 'tags', 'rtags',
                  'develop', 'rdevelop', 'publish', 'rpublish']
        extra_kwargs = {
            'tags': {'write_only': True},
            'develop': {'write_only': True},
            'publish': {'write_only': True},
            'rtags': {'read_only': True},
            'rdevelop': {'read_only': True},
            'rpublish': {'read_only': True},
        }
