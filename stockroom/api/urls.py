from django.conf.urls.defaults import *
from piston.resource import Resource

from handlers import CategoryHandler, ProductHandler, ItemHandler

category_handler = Resource(CategoryHandler)
product_handler = Resource(ProductHandler)
item_handler = Resource(ItemHandler)

urlpatterns = patterns('',
    url(r'^category/(?P<category_pk>\d+)/$', category_handler),
    url(r'^product/(?P<product_pk>\d+)/$', product_handler),
    url(r'^item/(?P<item_pk>\d+)/$', item_handler),
)
