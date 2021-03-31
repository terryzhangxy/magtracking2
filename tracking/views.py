from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import MagOrder,Tracking
from .serializer import MagOrderSerializer,TrackingSerializer,ExcelOrderSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,generics,mixins
from .forms import FileUploadForm
from datetime import date,datetime
from rest_framework import serializers
import xlrd

# Create your views here.
class TrackingList(generics.ListCreateAPIView):
    queryset = Tracking.objects.all()
    serializer_class = TrackingSerializer

class MagOrderList(generics.ListCreateAPIView):
    queryset = MagOrder.objects.all()
    serializer_class = MagOrderSerializer

def excel(request):
    if request.method =='POST':
        file = request.FILES.get('my_file')
        f_type = file.name.split('.')[-1]

        if f_type in ['xls','xlsx']:
            workbook = xlrd.open_workbook(file_contents=file.read())
            sheet_data = workbook.sheet_by_index(0)
            rows = sheet_data.nrows
            for i in range(1,rows):
                row_value = sheet_data.row_values(i)
                data=dict(order_numb='%d' %row_value[0],
                          order_receiving_time=date(*xlrd.xldate_as_tuple(row_value[1],workbook.datemode)[:3]),
                          order_time=date(*xlrd.xldate_as_tuple(row_value[2],workbook.datemode)[:3]),
                          purchaser=row_value[3],
                          product_numb=row_value[4],
                          product=row_value[5],
                          Subscription_cycle=row_value[6],
                          customer_name=row_value[7],
                          customer_tel=row_value[8],
                          customer_add=row_value[9],
                          distributor=row_value[10],
                          remark=row_value[11],
                          attention=row_value[12],)
                serlializer = ExcelOrderSerializer(data=data)
                if serlializer.is_valid():
                    serlializer.save()
                    print(serlializer.validated_data)
                else:
                   print(serlializer.errors)
        return HttpResponseRedirect('/order/list/')

    else:
        order_form = FileUploadForm()
        return render(request, 'tracking/fileloader.html', context={'form': order_form, 'what': "文件传输"})


