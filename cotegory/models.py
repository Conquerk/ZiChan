from django.db import models

# Create your models here.

class Cote(models.Model):
    coteId = models.CharField(max_length=10,unique=True,verbose_name='类别编号')
    coteName = models.CharField(max_length=30,verbose_name='类别名字')


    def __str__(self):
        return self.coteName

    class Meta:
        db_table = 'Cote'
        verbose_name = '类别'
        verbose_name_plural = verbose_name

class Depreciation(models.Model):
    method = models.CharField(max_length=50,verbose_name='折旧方法')

    def __str__(self):
        return self.method

    class Meta:
        db_table = 'depreciation'
        verbose_name='折旧方法'
        verbose_name_plural = verbose_name

