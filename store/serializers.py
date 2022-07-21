from rest_framework import serializers
from store.models import Product
import datetime


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=250)
    unit_price = serializers.DecimalField(max_digits=7, decimal_places=2)
    time_in_expiry = serializers.SerializerMethodField(method_name='calculate_time_in_expiry')

    def calculate_time_in_expiry(self, product: Product):
        rem = product.exp_date - datetime.datetime.now().replace(tzinfo=datetime.timezone.utc)
        years = int(rem.days/365)
        months = int((rem.days - 365*years) / 30)
        days = int(rem.days - 365*years - 30*months)
        return str(years) + ' years ' + str(months) + ' months ' + str(days) + ' days'
