from django.contrib.sites import requests
import pytest

pytestmark = pytest.mark.django_db

class TestCategoryEndpoints:

    endpoint = "/api/category/"

    def test_category_get(self,category_factory,api_client):
        category_factory()
        # category_factory.create_patch(4)
        response = api_client().get(self.endpoint)

        assert response.status_code == 200
        # assert len(json.loads(response.content)) == 4

class TestBrandEndpoints:

    endpoint = "/api/brand/"

    def test_brand_get(self,brand_factory,api_client):
        brand_factory()
        response = api_client().get(self.endpoint)
        assert response.status_code == 200


class TestProductEndpoints:

    endpoint = "/api/Product/"

    def test_product_get(self,product_factory,api_client):
        product_factory()
        response = api_client().get(self.endpoint)
        assert response.status_code == 200
