from .models import Category, Brand , Shop, Invoice, Quantity, Shift
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    category_id = serializers.ReadOnlyField()
    class Meta:
        model = Category
        fields = ['category_id','category_name','category_description']


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    brand_id = serializers.ReadOnlyField()
    category_id = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Category.objects.all())
    class Meta:
        model = Brand
        fields =  ['brand_id','brand_name','brand_description','category_id','brand_p_cost','brand_q_cost','brand_n_cost','brand_d_cost','brand_l_cost','brand_xg_cost','brand_y_cost','brand_p_sale','brand_q_sale','brand_n_sale','brand_d_sale','brand_l_sale','brand_xg_sale','brand_y_sale']

class ShopSerializer(serializers.HyperlinkedModelSerializer):
    shop_id = serializers.ReadOnlyField()
    class Meta:
        model = Shop
        fields =   ['shop_id','shop_name', 'shop_owner', 'shop_address']

class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    invoice_transaction_id = serializers.ReadOnlyField()
    brand_id = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Brand.objects.all())
    class Meta:
        model = Invoice
        fields =   ['invoice_transaction_id','brand_id','category_id','invoice_brand_size','invoice_brand_qty','invoice_rate_per_case','invoice_no_of_bottles','invoice_total']

class QuantitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quantity
        fields = ['quantity_name','quantity_bottles']

class ShiftSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        brand_id = serializers.ReadOnlyField()
        model = Shift
        fields = ['brand_id','stock_shift_date','stock_shift_from','stock_shift_to','stock_shift_p','stock_shift_q','stock_shift_n','stock_shift_d','stock_shift_l','stock_shift_xg','stock_shift_y']