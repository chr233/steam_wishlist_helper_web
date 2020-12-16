# Generated by Django 3.1.4 on 2020-12-16 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(db_index=True, help_text='公司ID', primary_key=True, serialize=False, unique=True, verbose_name='公司ID')),
                ('name', models.CharField(db_index=True, help_text='公司英文名', max_length=20, unique=True, verbose_name='英文名')),
                ('desc', models.CharField(blank=True, default='', help_text='公司备注', max_length=20, verbose_name='备注')),
            ],
            options={
                'verbose_name': '公司信息',
                'verbose_name_plural': '公司信息',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='项目的名称', max_length=20, unique=True, verbose_name='名称')),
                ('value', models.IntegerField(default=0, help_text='项目的数值', verbose_name='数值')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(db_index=True, help_text='标签ID', primary_key=True, serialize=False, unique=True, verbose_name='标签ID')),
                ('name', models.CharField(db_index=True, help_text='标签中文名', max_length=20, unique=True, verbose_name='标签名')),
                ('name_en', models.CharField(blank=True, db_index=True, default='*', help_text='标签英文名', max_length=20, verbose_name='英文名')),
            ],
            options={
                'verbose_name': '标签信息',
                'verbose_name_plural': '标签信息',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='GameInfo',
            fields=[
                ('appid', models.IntegerField(db_index=True, help_text='游戏的AppID', primary_key=True, serialize=False, unique=True, verbose_name='appid')),
                ('ready', models.BooleanField(default=False, help_text='数据是否可用', verbose_name='可用')),
                ('card', models.BooleanField(default=False, help_text='有无卡牌', verbose_name='卡牌')),
                ('audlt', models.BooleanField(default=False, help_text='是否被标记为仅限成人', verbose_name='“仅限成人')),
                ('free', models.BooleanField(default=False, help_text='是否为免费游戏', verbose_name='免费')),
                ('release', models.BooleanField(default=False, help_text='是否已发行', verbose_name='发行')),
                ('rscore', models.SmallIntegerField(default=0, help_text='评测分数0-10', verbose_name='评价')),
                ('rtotal', models.IntegerField(default=0, help_text='评测总人数', verbose_name='评测总数')),
                ('rpercent', models.IntegerField(default=0, help_text='好评率', verbose_name='好评率%')),
                ('pcurrent', models.IntegerField(default=-1, help_text='当前价格 * 100', verbose_name='现价')),
                ('porigin', models.IntegerField(default=-1, help_text='原始价格 * 100', verbose_name='原价')),
                ('plowest', models.IntegerField(default=-1, help_text='史低价格 * 100', verbose_name='史低')),
                ('pcut', models.IntegerField(default=0, help_text='当前折扣,0:未打折', verbose_name='当前折扣%')),
                ('plowestcut', models.IntegerField(default=0, help_text='史低折扣,0:未打折', verbose_name='史低折扣%')),
                ('tadd', models.IntegerField(default=0, help_text='添加时间戳', verbose_name='添加时间')),
                ('tlowest', models.IntegerField(default=0, help_text='史低时间戳', verbose_name='史低时间')),
                ('tupdate', models.IntegerField(db_index=True, default=0, help_text='下次更新时间戳', verbose_name='更新时间')),
                ('tmodify', models.IntegerField(default=0, help_text='上次修改时间戳', verbose_name='修改时间')),
                ('trelease', models.IntegerField(default=0, help_text='游戏发行时间戳', verbose_name='发行时间')),
                ('cview', models.IntegerField(default=0, help_text='访问计数器', verbose_name='访问')),
                ('cupdate', models.IntegerField(default=0, help_text='更新计数器', verbose_name='更新')),
                ('cerror', models.IntegerField(default=0, help_text='出错计数器', verbose_name='出错')),
                ('name', models.CharField(default='*', help_text='游戏英文名', max_length=100, verbose_name='英文名')),
                ('name_cn', models.CharField(default='*', help_text='游戏中文名', max_length=100, verbose_name='中文名')),
                ('plains', models.CharField(default='', help_text='查询价格数据需要用到', max_length=200, verbose_name='PlainID')),
                ('develop', models.ManyToManyField(blank=True, help_text='开发商', related_name='develop', to='app.Company', verbose_name='开发商')),
                ('publish', models.ManyToManyField(blank=True, help_text='发行商', related_name='publish', to='app.Company', verbose_name='发行商')),
                ('tags', models.ManyToManyField(blank=True, help_text='游戏标签', related_name='tags', to='app.Tags', verbose_name='标签')),
            ],
            options={
                'ordering': ('appid',),
            },
        ),
    ]
