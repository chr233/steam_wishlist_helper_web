
'''
# @Author       : Chr_
# @Date         : 2020-12-11 20:24:13
# @LastEditors  : Chr_
# @LastEditTime : 2020-12-14 20:34:48
# @Description  : 序列化器
'''

from rest_framework import serializers
from .models import Company, GameInfo, Tags


class TagsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tags
        fields = ['id','name', 'name_cn']
        read_only_fields = ['id']


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['id','name', 'name_cn']
        read_only_fields = ['id']


class GameInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameInfo
        fields = ['appid', 'name', 'name_cn',
                  'ready', 'card', 'free',
                  'release', 'rscore', 'rtotal', 'rpercent',
                  'pcurrent', 'porigin', 'plowest', 'pcut', 'plowestcut',
                  'tadd', 'tlowest', 'tupdate', 'tmodify', 'trelease',
                  'cview', 'cupdate', 'cerror',
                  'tags', 'develop', 'publish']
