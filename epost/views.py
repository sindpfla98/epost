import csv, os
import requests
from .models import CallingPlan, CVSUpload
from .forms import CVSUploadForm
from .serializers import *
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models.base import ObjectDoesNotExist
from django.urls import reverse
from django.conf import settings
from rest_framework import views
from rest_framework.response import Response

def insert_data(request):
    CSV_PATH = './epost/calling-plan-data.csv'
    with open(CSV_PATH, encoding='utf-8-sig') as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            print(row['company'])
            # data = CallingPlan.objects.create(
            #     company = row['company'],
            #     brand = row['brand'],
            #     homepage = row['homepage'],
            #     calling_plan = row['calling_plan'],
            #     mobile_carrier = row['mobile_carrier'],
            #     category = row['category'],
            #     data_speed = row['data_speed'],
            #     data_category = row['data_category'],
            #     data_unit = row['data_unit'],
            #     call = row['call'],
            #     call_unit = row['call_unit'],
            #     unlimited_free = row['unlimited_free'],
            #     message = row['message'],
            #     message_unit = row['message_unit'],
            #     data1 = row['data1'],
            #     data2 = row['data2'],
            #     pay = row['pay'],
            #     promo_pay = row['promo_pay'],
            #     # saled_pay1 = row['saled_pay1'],
            #     # saled_pay2 = row['saled_pay2'],
            #     # saled_pay3 = row['saled_pay3'],
            #     # sales_pay1 = row['sales_pay1'],
            #     # condition1 = row['condition1'],
            #     # sales_pay2 = row['sales_pay2'],
            #     # condition2 = row['condition2'],
            #     # sales_pay3 = row['sales_pay3'],
            #     # condition3 = row['condition3'],
            #     # etc1 = row['etc1'],
            #     # etc2 = row['etc2'],
            #     # etc3 = row['etc3'],
            #     activation = row['activation'],
            #     update_date = row['update_date'],
            #     create_date = row['create_date']
            # )
    return render(request, 'epost/epost.html')

# csv 업로드
def cvs_upload(request):
    if request.method == "POST":
        form = CVSUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            CSV_PATH = settings.MEDIA_ROOT +str(CVSUpload.objects.last().file)
            with open(CSV_PATH, encoding='utf-8-sig') as csvfile:
                data_reader = csv.DictReader(csvfile)
                for row in data_reader:
                    print(row['calling_plan'], '있음')
                    try:
                        plan = CallingPlan.objects.get(calling_plan=row['calling_plan'], mobile_carrier=row['mobile_carrier'])
                        if plan:
                            plan.company=row['company']
                            plan.brand=row['brand']
                            plan.homepage=row['homepage']
                            plan.calling_plan=row['calling_plan']
                            plan.mobile_carrier=row['mobile_carrier']
                            plan.category=row['category']
                            plan.data_speed=row['data_speed']
                            plan.data_category=row['data_category']
                            plan.data_unit=row['data_unit']
                            plan.call=row['call']
                            plan.call_unit=row['call_unit']
                            plan.unlimited_free=row['unlimited_free']
                            plan.message=row['message']
                            plan.message_unit=row['message_unit']
                            plan.data1=row['data1']
                            plan.data2=row['data2']
                            plan.pay=row['pay']
                            plan.promo_pay=row['promo_pay']
                                # calling_plan.saled_pay1 = row['saled_pay1']
                                # calling_plan.saled_pay2 = row['saled_pay2']
                                # calling_plan.saled_pay3 = row['saled_pay3']
                                # calling_plan.sales_pay1 = row['sales_pay1']
                                # calling_plan.condition1 = row['condition1']
                                # calling_plan.sales_pay2 = row['sales_pay2']
                                # calling_plan.condition2 = row['condition2']
                                # calling_plan.sales_pay3 = row['sales_pay3']
                                # calling_plan.condition3 = row['condition3']
                                # calling_plan.etc1 = row['etc1']
                                # calling_plan.etc2 = row['etc2']
                                # calling_plan.etc3 = row['etc3']
                            plan.activation=row['activation']
                            plan.update_date= timezone.localtime()
                            plan.save()
                    except ObjectDoesNotExist:
                        print(row['calling_plan'], '추가')
                        data = CallingPlan.objects.create(
                            company = row['company'],
                            brand = row['brand'],
                            homepage = row['homepage'],
                            calling_plan = row['calling_plan'],
                            mobile_carrier = row['mobile_carrier'],
                            category = row['category'],
                            data_speed = row['data_speed'],
                            data_category = row['data_category'],
                            data_unit = row['data_unit'],
                            call = row['call'],
                            call_unit = row['call_unit'],
                            unlimited_free = row['unlimited_free'],
                            message = row['message'],
                            message_unit = row['message_unit'],
                            data1 = row['data1'],
                            data2 = row['data2'],
                            pay = row['pay'],
                            promo_pay = row['promo_pay'],
                            # saled_pay1 = row['saled_pay1'],
                            # saled_pay2 = row['saled_pay2'],
                            # saled_pay3 = row['saled_pay3'],
                            # sales_pay1 = row['sales_pay1'],
                            # condition1 = row['condition1'],
                            # sales_pay2 = row['sales_pay2'],
                            # condition2 = row['condition2'],
                            # sales_pay3 = row['sales_pay3'],
                            # condition3 = row['condition3'],
                            # etc1 = row['etc1'],
                            # etc2 = row['etc2'],
                            # etc3 = row['etc3'],
                            activation = row['activation'],
                            update_date = '',
                            create_date = timezone.localtime()
                        )
            return render(request, 'epost/cvs_uploaded.html')
    else:
        form = CVSUploadForm()
    return render(request, 'epost/cvs_upload.html', {'form': form})

host = 'http://localhost:8000'

class Keyword(views.APIView):
    """
    키워드 검색
    """
    def get(self, request, format=None):
        keyword = self.request.query_params.get('keyword')

        queryset = CallingPlan.objects.all()
        if keyword:
            queryset = queryset.filter(calling_plan__icontains=keyword)
        serializer = SearchSerializer(queryset, many=True)

        return Response(serializer.data)



from django.http import HttpResponseRedirect


# 검색
def keyword_search(request):
    path = '/epost/keyword'

    keyword = request.GET.get('keyword', '')
    params = {'keyword':keyword}

    url = host + path
    response = requests.get(url, params=params).json()

    count = len(response)

    return render(request, 'epost/keyword_search.html', {
        'plans' : response,
        'keyword':keyword,
        'count':count,
    })

class Listing(views.APIView):
    """
    조건 검색
    """
    def get(self, request, format=None):
        mobile_carrier = self.request.query_params.getlist('mobile_carrier')
        category = self.request.query_params.get('category')
        data_speed = self.request.query_params.getlist('data_speed')
        call = self.request.query_params.get('call')
        message = self.request.query_params.get('message')
        data1 = self.request.query_params.get('data1')

        queryset = CallingPlan.objects.all()

        if mobile_carrier:
            queryset = queryset.filter(mobile_carrier=mobile_carrier[0])
            if len(mobile_carrier)>1:
                for i in range(1, len(mobile_carrier)):
                    queryset = queryset|CallingPlan.objects.filter(mobile_carrier=mobile_carrier[i])

        if category:
            queryset = queryset.filter(category=category)

        if data_speed:
            queryset = queryset.filter(data_speed=data_speed[0])
            if len(data_speed)>1:
                for i in range(1, len(data_speed)):
                    queryset = queryset|CallingPlan.objects.filter(data_speed=data_speed[i])

        if call:
            if call == "0":
                queryset = queryset.filter(call__lte=50)
            elif call == "1":
                queryset = queryset.filter(call__gt=50, call__lte=100)
            elif call == "2":
                queryset = queryset.filter(call__gt=100, call__lte=250)
            elif call == "3":
                queryset = queryset.filter(call__gt=250)
            elif call == "4":
                queryset = queryset.filter(call=999999)

        if message:
            if message == "0":
                queryset = queryset.filter(message__lte=50)
            elif message == "1":
                queryset = queryset.filter(message__gt=50, message__lte=100)
            elif message == "2":
                queryset = queryset.filter(message__gt=100, message__lte=200)
            elif message == "3":
                queryset = queryset.filter(message__gt=200)
            elif message == "4":
                queryset = queryset.filter(message=999999)

        if data1:
            if data1 == "0":
                queryset = queryset.filter(data1__lte=100)
            elif data1 == "1":
                queryset = queryset.filter(data1__gt=100, data1__lte=1000)
            elif data1 == "2":
                queryset = queryset.filter(data1__gt=1000, data1__lte=5000)
            elif data1 == "3":
                queryset = queryset.filter(data1__gt=5000)
            elif data1 == "4":
                queryset = queryset.filter(data2__contains='계속')

        serializer = ListingSerializer(queryset, many=True)

        return Response(serializer.data)

def listing_search(request):
    path = '/epost/listing'

    mobile_carrier = request.GET.getlist("mobile_carrier", [])
    category = request.GET.get("category", "")
    data_speed = request.GET.getlist("data_speed", [])
    call = request.GET.get("call", "")
    message = request.GET.get("message", "")
    data1 = request.GET.get("data1", "")

    params = {'mobile_carrier':mobile_carrier, 'category':category, 'data_speed':data_speed,
              'call':call, 'message':message, 'data1':data1 }

    url = host + path
    response = requests.get(url, params=params).json()

    count = len(response)
    return render(request, 'epost/listing_search.html',
                    { 'plans':response, 'count':count, })

def detail(request, pk):
    plan = get_object_or_404(CallingPlan, pk=pk)
    return render(request, 'epost/detail.html',{'plan':plan})
