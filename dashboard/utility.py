import pandas as pd
import plotly.express as px

from datetime import datetime
from pyairtable.formulas import match

def order_in_progress(table) -> int:
    formula = match({"order_status": "in_progress"})
    return len(table.all(formula=formula))

def total_order_this_month(table) -> int:
    count = 0
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    orders = table.all(fields=['order_placed'],sort=['-order_placed']) #sorts desc

    for record in orders:
        m = str(record['fields']['order_placed'].split('-')[1])
        y = str(record['fields']['order_placed'].split('-')[0])
        if y == currentYear and m == currentMonth:
            count+=1
    return count

def recent_orders(table) -> list:
    recent_orders = table.all(
        fields=['order_id','order_placed','product_name','price',
                'first_name','last_name','order_status'],
        sort=['-order_placed'])
    li = []
    for records in recent_orders[:4]:
        li.append(records['fields'])
    return li

def total_revenue(table) -> float:
    price_list = table.all(fields=['price'])
    revenue = 0
    for record in price_list:
        revenue+=record['fields']['price']
    return round(revenue,2)
    
def gen_charts(table) -> None:
    '''
        This function is used to generate the bar graph and pie chart.
    '''
    status_list = table.all(fields=['product_name','order_status'])
    pn = []
    ost = []
    for record in status_list:
        pn.append(record['fields']['product_name'])
        ost.append(record['fields']['order_status'])
    
    pn_occur = {item: pn.count(item) for item in pn}
    ost_occur = {item: ost.count(item) for item in ost}
    
    df_pn = pd.DataFrame({'Product':list(pn_occur.keys()), 'Quantity':list(pn_occur.values())})
    df_ost = pd.DataFrame({'OrderStatus':list(ost_occur.keys()), 'Freq':list(ost_occur.values())})

    fig = px.bar(df_pn, x='Product', y='Quantity',text_auto=True)
    fig2 = px.pie(df_ost, values='Freq', names='OrderStatus',color='OrderStatus',
                 color_discrete_map={'placed':'lightcyan',
                                 'in_progress':'cyan',
                                 'cancelled':'royalblue',
                                 'shipped':'darkblue'})

    fig.write_image('static/barchart.png')
    fig2.write_image('static/piechart.png')
    return
