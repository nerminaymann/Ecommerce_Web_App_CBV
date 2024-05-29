# import export
import pytest

import Ecommerce_App
from Ecommerce_App.tests import factories
# export DJANGO_SETTINGS_MODULE=mysite.settings

# from django.conf import settings
#
#
# """Default level indicator. By default is `'---'`."""
# DEFAULT_LEVEL_INDICATOR = getattr(settings, "MPTT_DEFAULT_LEVEL_INDICATOR", "---")

pytestmark = pytest.mark.django_db

class TestCategoryModel:
    def test_str_method(self,category_factory):
        category = category_factory()
        assert category.__str__() == "test_category"
class TestBrandModel:
    def test_str_method(self, brand_factory):
        brand = brand_factory()
        assert brand.__str__() == "test_brand"
class TestProductModel:
    def test_str_method(self, product_factory):
        product = product_factory()
        assert product.__str__() == "test_product"
