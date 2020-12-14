
'''
# @Author       : Chr_
# @Date         : 2020-12-11 20:05:41
# @LastEditors  : Chr_
# @LastEditTime : 2020-12-14 20:16:00
# @Description  : 数据库模型
'''

from django.db import models


class Status(models.Model):
    '''服务器状态信息'''

    name = models.CharField(max_length=20, unique=True, db_index=True,
                            verbose_name='名称', help_text='项目的名称')
    value = models.IntegerField(default=0,
                                verbose_name='数值', help_text='项目的数值')


class Tags(models.Model):
    '''标签'''
    id = models.AutoField(primary_key=True, unique=True, db_index=True,
                          verbose_name='标签ID', help_text='标签ID',)
    name = models.CharField(max_length=20, unique=True, db_index=True,
                            verbose_name='英文名', help_text='标签英文名')

    name_cn = models.CharField(max_length=20, default='*', blank=True, db_index=True,
                               verbose_name='中文名', help_text='标签中文名')

    def __str__(self) -> str:
        if self.name_cn != '*':
            return f'{self.name_cn} | {self.name}'
        else:
            return self.name

    class Meta:
        ordering = ('id',)
        verbose_name = "标签信息"
        verbose_name_plural = verbose_name


class Company(models.Model):
    '''发行商或者发行商'''
    id = models.AutoField(primary_key=True, unique=True, db_index=True,
                          verbose_name='公司ID', help_text='公司ID',)
    name = models.CharField(max_length=20, unique=True, db_index=True,
                            verbose_name='英文名', help_text='公司英文名')

    name_cn = models.CharField(max_length=20, default='*', blank=True, db_index=True,
                               verbose_name='中文名', help_text='公司中文名')

    def __str__(self) -> str:
        if self.name_cn != '*':
            return f'{self.name_cn} | {self.name}'
        else:
            return self.name

    class Meta:
        ordering = ('id',)
        verbose_name = "公司信息"
        verbose_name_plural = verbose_name


class GameInfo(models.Model):
    '''游戏信息'''
    appid = models.IntegerField(primary_key=True, unique=True, db_index=True,
                                verbose_name='appid', help_text='游戏的AppID')

    ready = models.BooleanField(default=False,
                                verbose_name='可用', help_text='True代表数据存在,False代表等待爬虫获取')
    card = models.BooleanField(default=False,
                               verbose_name="卡牌", help_text='有无卡牌')
    free = models.BooleanField(default=False,
                               verbose_name='免费', help_text='是否为免费游戏')
    release = models.BooleanField(default=False,
                                  verbose_name='发行', help_text='是否已发行')
    rscore = models.SmallIntegerField(default=0,
                                      verbose_name='评价', help_text='评测分数0-10')
    rtotal = models.IntegerField(default=0,
                                 verbose_name='评测总数', help_text='评测总人数')
    rpercent = models.IntegerField(default=0,
                                   verbose_name='好评率%', help_text='好评率')

    pcurrent = models.IntegerField(default=-1,
                                   verbose_name='现价', help_text='当前价格 * 100')
    porigin = models.IntegerField(default=-1,
                                  verbose_name='原价', help_text='原始价格 * 100')
    plowest = models.IntegerField(default=-1,
                                  verbose_name='史低', help_text='史低价格 * 100')
    pcut = models.IntegerField(default=0,
                               verbose_name='当前折扣%', help_text='当前折扣,0:未打折')
    plowestcut = models.IntegerField(default=0,
                                     verbose_name='史低折扣%', help_text='史低折扣,0:未打折')

    tadd = models.IntegerField(default=0,
                               verbose_name='添加时间', help_text='添加时间戳')
    tlowest = models.IntegerField(default=0,
                                  verbose_name='史低时间', help_text='史低时间戳')
    tupdate = models.IntegerField(default=0, db_index=True,
                                  verbose_name='更新时间', help_text='下次更新时间戳')
    tmodify = models.IntegerField(default=0,
                                  verbose_name='修改时间', help_text='上次修改时间戳')
    trelease = models.IntegerField(default=0,
                                   verbose_name='发行时间', help_text='游戏发行时间戳')

    cview = models.IntegerField(default=0,
                                verbose_name='访问', help_text='访问计数器')
    cupdate = models.IntegerField(default=0,
                                  verbose_name='更新', help_text='更新计数器')
    cerror = models.IntegerField(default=0,
                                 verbose_name='出错', help_text='出错计数器')

    tags = models.ManyToManyField(Tags, related_name='tags', blank=True,
                                  verbose_name='标签', help_text='游戏标签')
    develop = models.ManyToManyField(Company, related_name='develop', blank=True,
                                     verbose_name='开发商', help_text='开发商')
    publish = models.ManyToManyField(Company, related_name='publish', blank=True,
                                     verbose_name='发行商', help_text='发行商')

    name = models.CharField(default='*', max_length=100,
                            verbose_name='英文名', help_text='游戏英文名')
    name_cn = models.CharField(default='*', max_length=100,
                               verbose_name='中文名', help_text='游戏中文名')
    plains = models.CharField(default='', max_length=200,
                              verbose_name='PlainID', help_text='查询价格数据需要用到')

    def __str__(self):
        return f'{self.appid} | {self.name_cn if self.name_cn != "*" else self.name}'

    class Meta:
        ordering = ('appid',)
