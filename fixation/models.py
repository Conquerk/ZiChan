from django.db import models
from cotegory.models import *

FIXADD = (
    ('A','自购资产'),
    ('B','其它资产'),
)
EMPLOY = (
    ('1','在用'),
    ('2','闲置'),
    ('3','在途'),
    ('4','已处置'),
)

# Create your models here.
class Fixation(models.Model):
    cartID = models.CharField(max_length=50,unique=True,verbose_name='卡片编号',null=True)
    fixID = models.CharField(max_length=50,unique=True,verbose_name='固定资产编号',null=True)
    fixname = models.CharField(max_length=50,verbose_name='固定资产名称')
    cotename = models.ForeignKey(Cote,verbose_name='类别名称')
    cote= models.CharField(max_length=20,verbose_name='类别编号',)
    spmodels = models.CharField(max_length=50,verbose_name='规格型号',null=True)
    serialnum = models.CharField(max_length=50,verbose_name='产品序列号',null=True)
    fixadd = models.CharField(verbose_name='资产来源',choices=FIXADD,null=False,max_length=20)
    date = models.DateField(verbose_name='开始使用日期',null=False)
    user = models.CharField(verbose_name='使用人',max_length=20,null=False)
    place = models.CharField(verbose_name='存放地点',max_length=50)
    employ = models.CharField(verbose_name='使用状况',choices=EMPLOY,max_length=20)
    value = models.DecimalField(verbose_name='原值',max_digits=10,decimal_places=2)
    currency = models.CharField(verbose_name='币种',max_length=10)
    demeth = models.ForeignKey(Depreciation,verbose_name='折旧方法')
    year = models.CharField(verbose_name='折旧年限',max_length=200,default='5')
    stmonth = models.DateField(verbose_name='开始折旧月份')
    monmoney = models.DecimalField(verbose_name='月折旧额',max_digits=10,decimal_places=2)
    addZ = models.DecimalField(verbose_name='累计折旧',max_digits=10,decimal_places=2)
    JanZ = models.DecimalField(verbose_name='减值准备',max_digits=10,decimal_places=2,default=0)
    ZhM = models.DecimalField(verbose_name='账面价值',max_digits=10,decimal_places=2,null=True)
    ZhZ = models.CharField(verbose_name='折旧状态',max_length=20)
    Jing = models.TextField(verbose_name='净残值率',max_length=20,default='5%')
    JingC = models.CharField(verbose_name='净残值',max_length=20,null=True)
    JinS = models.DecimalField(verbose_name='进项税',max_digits=10,decimal_places=2)
    BZ = models.TextField(verbose_name='备注',max_length=2000,null=True)

    def __str__(self):
        return self.fixname

    def to_dict(self):
        dic = {
            'cartID':self.cartID,
            'fixID':self.fixID,
            'fixname':self.fixname,
            'cotename':self.cotename.coteName,
            'fixadd':self.fixadd,
            'user':self.user,
            'place':self.place,
            'value':self.value,
            'demeth':self.demeth.method,
            'addZ':self.addZ,
            'ZhM':self.ZhM,
            'BZ':self.BZ,

        }
        return dic

    class Meta:
        db_table = 'fixation'
        verbose_name = '资产卡片'
        verbose_name_plural = verbose_name


