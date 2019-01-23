import json

from django.http import HttpResponse
from django.shortcuts import render
from fixation.models import *
import datetime
import time
# Create your views here.
def Caltime(date1,date2):
    # date1 = time.strptime(date1,'%Y-%m-%d')
    # date2 = time.strptime(date2,'%Y-%m-%d')
    # date1 = datetime.datetime(date1[0],date1[1],date1[2])
    # date2 = datetime.datetime(date2[0], date2[1], date2[2])
    # return date2 - date1
    year1 = datetime.datetime.strptime(date1[0:10], "%Y-%m-%d").year
    year2 = datetime.datetime.strptime(date2[0:10], "%Y-%m-%d").year
    month1 = datetime.datetime.strptime(date1[0:10], "%Y-%m-%d").month
    month2 = datetime.datetime.strptime(date2[0:10], "%Y-%m-%d").month
    num = (year1 - year2) * 12 + (month1 - month2)
    return num


def index(request):
    fixs = Fixation.objects.all()
    l=[]
    for x in fixs:
        l.append(x.to_dict())
    return render(request,'index.html',locals())


def Check(request):
    l=[]
    cartID = request.GET.get('cartID')
    fix = Fixation.objects.get(cartID=cartID)
    year = str(fix.stmonth)
    nowyear = str(datetime.date.today())
    monthC = Caltime(nowyear, year)
    monmoney = fix.monmoney
    value = int(fix.value)
    JingC = int(fix.JingC)
    zheJY = int(fix.year)
    monmoney = (value-JingC)/(zheJY * 12)
    ZhM = value - monmoney * monthC
    fix.ZhM = ZhM
    fix.monmoney = monmoney
    fix.addZ = monmoney * monthC
    fix.save()

    fix2 = Fixation.objects.get(cartID=cartID)
    l.append(fix2.to_dict())
    return render(request, 'exmp.html', locals())

