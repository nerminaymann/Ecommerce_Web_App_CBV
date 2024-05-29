import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient
from .factories import CategoryFactory,BrandFactory,ProductFactory
# from django.conf import settings
#
#
# DEFAULT_LEVEL_INDICATOR = getattr(settings, "MPTT_DEFAULT_LEVEL_INDICATOR", "---")


register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)

@pytest.fixture
def api_client(request):
    return APIClient()