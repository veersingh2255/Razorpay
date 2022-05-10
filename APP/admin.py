from django.contrib import admin

from .models import coffee

from django.utils.html import format_html


class Admin(admin.ModelAdmin):
    # fields = ('amount',)
    # exclude = ('paid','name',)
    list_display = ('name','amount','payment_ID','paid',)
    # list_display_links = ('payment_id',)
    Order_id_URL = f'https://dashboard.razorpay.com/app/orders/{coffee.payment_id}'
    print(Order_id_URL)
    def payment_ID(self, obj):
        return format_html(
            f'<a href="{obj.payment_id}">{obj.payment_id}</a>',)



admin.site.register(coffee,Admin)
