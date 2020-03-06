from django.contrib import admin
from .models import CallingPlan, CVSUpload
from .forms import CVSUploadForm
import csv

@admin.register(CallingPlan)
class CallingPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'calling_plan')
    list_display_links = ('id', 'company', 'calling_plan')
    search_fields = ['calling_plan']
    list_filter = ['brand']

@admin.register(CVSUpload)
class CVSUploadAdmin(admin.ModelAdmin):
    list_display = ('id','file','date')
    list_display_links = ('file','date')
    # def save_form(self, request, form, change):
        
    # def insert_data(self,request):
    #     if request.method == "POST" in request.POST:
    #         form = CVSUploadForm(request.POST, request.FILES)
    #         if form.is_valid():
    #             CSV_PATH = request.FILES
    #             with open(CSV_PATH, encoding='utf-8-sig') as csvfile:
    #                 data_reader = csv.DictReader(csvfile)
    #                 for row in data_reader:
    #                     print(row['company'])
