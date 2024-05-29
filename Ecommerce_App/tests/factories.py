import factory

from Ecommerce_App import settings
from product.models import Product,Category,Brand
# from django.conf import settings
#
#
# DEFAULT_LEVEL_INDICATOR = getattr(settings, "MPTT_DEFAULT_LEVEL_INDICATOR", "---")
class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = 'test_category'

    #WHEN (UNIQUE OF NAME IS TRUE):
    # name = factory.sequence(lambda n: f'test_category_{n}')
    # name = factory.Sequence(lambda n : 'test_category_%d' % n)

class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = 'test_brand'

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = 'test_product'
    description = 'test_description'
    is_digital = True
    category = factory.SubFactory(CategoryFactory)
    brand = factory.SubFactory(BrandFactory)




