from django.conf import settings
from django.db.models import Q, Min
from django.shortcuts import get_object_or_404

from piston.handler import BaseHandler
from piston.utils import validate, rc
from easy_thumbnails.files import get_thumbnailer

from stockroom.models import ProductCategory, Product, StockItem


ITEM_THUMBNAIL_MAX_HEIGHT = getattr(settings, "ITEM_THUMBNAIL_MAX_HEIGHT", 360)
ITEM_THUMBNAIL_MAX_WIDTH = getattr(settings, "ITEM_THUMBNAIL_MAX_WIDTH", 205)

class CsrfExemptBaseHandler(BaseHandler):
    """
        handles request that have had csrfmiddlewaretoken inserted 
        automatically by django's CsrfViewMiddleware
        see: http://andrew.io/weblog/2010/01/django-piston-and-handling-csrf-tokens/
      
        This piston issue is reported and may soon be fixed here:
        http://bitbucket.org/jespern/django-piston/issue/82
    """
    def flatten_dict(self, dct):
        if 'csrfmiddlewaretoken' in dct:
            dct = dct.copy()
            del dct['csrfmiddlewaretoken']
        return super(CsrfExemptBaseHandler, self).flatten_dict(dct)

class ProductHandler(BaseHandler):
    allowed_methods = ('GET',)
    
    def read(self, request, product_pk=None):
        product = get_object_or_404(Product, pk=product_pk)
        return product

class ItemHandler(BaseHandler):
    allowed_methods = ('GET',)
    
    def read(self, request, item_pk=None):
        p = get_object_or_404(Product.objects.select_related(), pk=item_pk)
        stockitems = StockItem.objects.filter(product=p).order_by('sale_price', 'price')

        product = {
            'title': p.title,
            'description': p.description,
            'sizes': [],
            'category': p.category.name,
        }
        if p.images.count() > 0:
            if p.thumbnail.image_file:
                thumbnail_file = p.thumbnail.image_file
                thumbnail_options = dict(size=(ITEM_THUMBNAIL_MAX_WIDTH, ITEM_THUMBNAIL_MAX_HEIGHT))
                thumbnail = get_thumbnailer(thumbnail_file).get_thumbnail(thumbnail_options)
                product['image'] = thumbnail.url
            else:
                product['image'] = None
        else:
            product['image'] = None
                
        items = list(stockitems)
        for item in items:
            if item.on_sale:
                price = item.sale_price
            else:
                price = item.price
            product['sizes'].append((item.id, "%s, $%s" % (item.package_title, price)))
        return product

class CategoryHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = ProductCategory
    
    def read(self, request, category_pk=None):
        # First, fetch the category and it's children
        categories = ProductCategory.objects.filter(Q(pk=category_pk) | Q(parent=category_pk)).values_list('id', flat=True)
        # Then, fetch StockItems whose product is in any of the categories
        products = StockItem.objects.select_related().filter(product__category__in=categories)
        return products

