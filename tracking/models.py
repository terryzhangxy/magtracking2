from django.db import models

# Create your models here.
class MagOrder(models.Model):
    order_numb = models.CharField(max_length=30,null=True,blank=True, verbose_name='订单编号')
    order_receiving_time = models.DateField(null=True,blank=True,verbose_name='接单时间')
    product = models.CharField(null=True,blank=True,max_length=30,verbose_name='杂志名称')
    customer_name = models.CharField(null=True,blank=True,max_length=30, verbose_name='客户名称')
    customer_tel = models.CharField(null=True,blank=True,max_length=30, verbose_name='客户电话')
    customer_add = models.CharField(null=True,blank=True,max_length=100, verbose_name='客户地址')
    distributor = models.CharField(null=True,blank=True,max_length=30, verbose_name='分销商')
    remark = models.CharField(null=True,blank=True,max_length=100, verbose_name='备注')

class Tracking(models.Model):
    magorder = models.ForeignKey(MagOrder,on_delete=models.CASCADE,related_name='tracking',null=True,blank=True,verbose_name='订单编号')
    express_comp = models.CharField(max_length=30,null=True,blank=True,verbose_name='快递公司')
    deliverly_time = models.DateField(null=True,blank=True,verbose_name='发货时间')
    tracking_numb = models.CharField(max_length=30,null=True,blank=True,verbose_name='快递单号')
    deliverly_detail = models.CharField(max_length=100, null=True,blank=True,verbose_name='发货明细')




