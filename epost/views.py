from django.shortcuts import render
from django.http import HttpResponseRedirect
import csv, os
from .models import CallingPlan, CVSUpload
from datetime import datetime
from .forms import CVSUploadForm
from django.utils import timezone
from django.db.models.base import ObjectDoesNotExist

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

# 검색
def keyword_search(request):
    plans = CallingPlan.objects.all()

    keyword = request.GET.get('keyword', '') # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    if keyword: # q가 있으면
        plans = plans.filter(calling_plan__icontains=keyword) # 제목에 q가 포함되어 있는 레코드만 필터링

    return render(request, 'epost/keyword_search.html', {
        'plans' : plans,
        'keyword' : keyword,
    })

# csv 업로드
def cvs_upload(request):
    if request.method == "POST":
        form = CVSUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            CSV_PATH = './mysite/media/'+str(CVSUpload.objects.last().file)
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



















