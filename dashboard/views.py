from django.shortcuts import render
from pyairtable import Table
from decouple import config

from .utility import total_order_this_month,order_in_progress,recent_orders,total_revenue,gen_charts

def home(request):
    response = {}
    table = Table(config("API_KEY"), config("BASE_ID"), config("TABLE_NAME"))
    gen_charts(table)
    response['total_order'] = len(table.all())
    response['total_order_this_month'] = total_order_this_month(table)
    response['order_in_progress'] = order_in_progress(table)
    response['recent_orders'] = recent_orders(table)
    response['total_revenue'] = total_revenue(table)
    return render(request,'home.html',{'response':response})
