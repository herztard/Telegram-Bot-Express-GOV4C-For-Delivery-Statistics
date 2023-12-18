import re
import requests
import json
import datetime

now = datetime.datetime.now()

region_codes = 'https://mykhat.kz/delivery/region/list'

url = 'http://express.gov4c.kz/ddocs/api/v1/report'

headers = {'Content-type': 'application/json'}

data = {
    'dateFrom': '2021-01-01',
    'dateTo': now.strftime('%Y-%m-%d')
}

response = requests.get(url, data=json.dumps(data), headers=headers)
data = response.json()
x = json.dumps(data)

def grouper(iterable, n):
    args = [iter(iterable)] * n
    return zip(*args)

def number_wt(): #'wt' means 'whole time'
    data = json.loads(x)
    sorted_orders = sorted(data, key=lambda number: number['order']['id']) #sort by id of the order
    last_order_number = sorted_orders[-1]['order']['id'] - 9 #get the last order, '-9' потому что id заказов от 1 до 4 и от 6 до 10 отсутствуют
    return last_order_number

def success_ended_wt(): #count orders, which were success ended
    count = 0
    for i in data:
        if i['order']['statuscode'] == 'SUCCESS_ENDED':
            count += 1
    return count

def processing_wt(): #count orders, which are in processing
    count = 0
    for i in data:
        if i['order']['statuscode'] == 'PROCESSING':
            count += 1
    return count

def customer_refused_wt(): #count orders, which were refused by the customer
    count = 0
    for i in data:
        if i['order']['statuscode'] == 'CUSTOMER_REFUSED':
            count += 1
    return count

def shipped_wt(): #count orders, which were shipped
    count = 0
    for i in data:
        if i['order']['statuscode'] == 'SHIPPED':
            count += 1
    return count

def number_t(): #t means today
    count = 0
    for i in data:
        date = i['orderStatuses'][-1]['updateDate']
        date = [''.join(i) for i in grouper(date, 10)]
        if date[0] == now.strftime('%Y-%m-%d'):
            count += 1
    return count

def success_ended_t():
    count = 0
    for i in data:
        if i['order']['statuscode'] == 'SUCCESS_ENDED':
            date = i['orderStatuses'][-1]['updateDate']
            date = [''.join(i) for i in grouper(date, 10)]
            if date[0] == now.strftime('%Y-%m-%d'):
                count += 1
    return count

def processing_t():
    count = 0
    for i in data:
        if i['order']['statuscode'] == 'PROCESSING':
            date = i['orderStatuses'][-1]['updateDate']
            date = [''.join(i) for i in grouper(date, 10)]
            if date[0] == now.strftime('%Y-%m-%d'):
                count += 1
    return count

def customer_refused_t():
    count = 0
    for i in data:
        if i['order']['statuscode'] == 'CUSTOMER_REFUSED':
            date = i['orderStatuses'][-1]['updateDate']
            date = [''.join(i) for i in grouper(date, 10)]
            if date[0] == now.strftime('%Y-%m-%d'):
                count += 1
    return count

def shipped_t():
    count = 0
    for i in data:
        if i['order']['statuscode'] == 'SHIPPED':
            date = i['orderStatuses'][-1]['updateDate']
            date = [''.join(i) for i in grouper(date, 10)]
            if date[0] == now.strftime('%Y-%m-%d'):
                count += 1
    return count

def region():
    for i in region_codes:
        if i['data']['code'] == '600':
            return 'Актау'
        elif i['data']['code'] == '618':
            return 'Актюбинск'
        elif i['data']['code'] == '675':
            return 'Алматы'
        elif i['data']['code'] == '744':
            return 'Нур-Султан'
        elif i['data']['code'] == '758':
            return 'Атырау'
        elif i['data']['code'] == '1602':
            return 'Караганда'
        elif i['data']['code'] == '1820':
            return 'Кокшетау'
        elif i['data']['code'] == '1894':
            return 'Костанай'
        elif i['data']['code'] == '2043':
            return 'Кызылорда'
        elif i['data']['code'] == '2436':
            return 'Павлодар'
        elif i['data']['code'] == '2472':
            return 'Петропавловск'
        elif i['data']['code'] == '2701':
            return 'Семей'
        elif i['data']['code'] == '2820':
            return 'Талдыкорган'
        elif i['data']['code'] == '2834':
            return 'Тараз'
        elif i['data']['code'] == '2884':
            return 'Темиртау'
        elif i['data']['code'] == '72533':
            return 'Туркестан'
        elif i['data']['code'] == '3021':
            return 'Уральск'
        elif i['data']['code'] == '3037':
            return 'Усть-Каменогорск'
        elif i['data']['code'] == '72834':
            return 'Уштобе'
        elif i['data']['code'] == '3247':
            return 'Шымкент'
        # elif i['data']['code'] == '3270':
        #     return 'Экибастуз'
        else:
            return 'Экибастуз'







print('number_wt', number_wt())
print('success_ended_wt', success_ended_wt())
print('processing_wt', processing_wt())
print('customer_refused_wt', customer_refused_wt())
print('shipped_wt', shipped_wt())
print('number_t', number_t())
print('success_ended_t', success_ended_t())
print('processing_t', processing_t())
print('customer_refused_t', customer_refused_t())
print('shipped_t', shipped_t())
