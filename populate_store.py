import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'ecommerce_project.settings')

import django
django.setup()
from store.models import Product, Order, OrderItem,ShippingAddress

def populate():
    pros={}

    for pro, pro_data in pros.item():
        p = add_pro(pro)
        for i in pro_data["shipping address"]:
            add_shipping_address(p,i["customer"],i["order"],address=i["address"]
                                 ,city=i["state"],zipcode=i["zipcode"]
                                 ,data_added=i["data_added"])

    for p in Product.objects.all():
        for i in ShippingAddress.objects.filter(product = p):
            print(f' - {p} : {i}')

    for p in Product.objects.all():
        for i in Product.objects.filter(product=p):
            print(f' - {p} : {i}')


def add_pro(name):
    p = Product.objects.get_or_create(name=name)[0]
    p.save
    return p

def add_shipping_address(pro,customer,order,address,city,state,zipcode,data_added):
    s = ShippingAddress.objects.get_or_create(product = pro)[0]
    s.customer = customer
    s.order = order
    s.address = address
    s.city = city
    s.state = state
    s.zipcode = zipcode
    s.data_added = data_added
    s.save()
    return s

def add_order_item(name):
    o = OrderItem.objects.get_or_create(name=name)[0]
    o.save()
    return o

if __name__ == '__main__':
    print('Starting WAD population script...')
    populate()