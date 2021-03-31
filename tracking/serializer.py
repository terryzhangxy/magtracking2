from rest_framework import serializers
from .models import Tracking,MagOrder



class TrackingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tracking
        fields = '__all__'

class MagOrderSerializer(serializers.ModelSerializer):
    #用于json输出时，包含某个订单的快递单号列表数据
    tracking = TrackingSerializer(many=True)

    class Meta:
        model = MagOrder
        fields = '__all__'


class ExcelOrderSerializer(serializers.ModelSerializer):
    #主要用于excel数据导入，无法解决is_validated报错中tracking为空的问题
    class Meta:
        model = MagOrder
        fields = '__all__'


