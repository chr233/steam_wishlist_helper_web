from django.db import models

# Create your models here.


class Plainid(models.Model):
    appid = models.IntegerField(primary_key=True, unique=True,
                                null=False, help_text='AppID')
    plainid = models.CharField(max_length=50, unique=True, help_text='PlainID')


class GameInfo(models.Model):
    appid = models.IntegerField(primary_key=True, unique=True,
                                null=False, help_text='AppID')
    has_card = models.BooleanField(null=True, help_text='有无卡牌')
    is_free = models.BooleanField(null=True, help_text='是否免费')

    p_current = models.IntegerField(null=True, help_text='当前价格*100')
    p_origin = models.IntegerField(null=True, help_text='原始价格*100')
    p_lowest = models.IntegerField(null=True, help_text='史低价格*100')
    p_lowcut = models.IntegerField(null=True, help_text='史低折扣%')
    p_cut = models.IntegerField(null=True, help_text='当前折扣%')

    addtime = models.IntegerField(null=True, help_text='添加时间戳')
    lowtime = models.IntegerField(null=True, help_text='史低时间戳')
    updatetime = models.IntegerField(null=True, help_text='更新时间戳')
    nexttime = models.IntegerField(null=True, help_text='下次更新时间戳')

    r_score = models.IntegerField(null=True, help_text='评测分数0-10')
    r_total = models.IntegerField(null=True, help_text='评测总人数')
    r_percent = models.IntegerField(null=True, help_text='好评率')

    name = models.CharField(max_length=50, help_text='游戏名')
    tags = models.CharField(null=True, max_length=100, help_text='标签')
