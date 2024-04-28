

from base import app
from fastapi.testclient import TestClient

from src.api.schemas.product import ProductInfo

client = TestClient(app)

product_data = {"name": "Test Product", "measure": "kg",
                "code": "TP001", "image_url": "uploads/products/c37f562d-dfd3-44be-8feb-101839a62b47.jpg"}
updated_product_data = {"name": "Updated Product", "measure": "g",
                        "code": "UP002", "image_url": "uploads/products/c37f562d-dfd3-44be-8feb-101839a62b47.jpg"}


def test_create_product():
    response = client.post("/products/", json=product_data)
    assert response.status_code == 200


def test_get_product_by_id():
    response = client.get("/products/1/")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_update_product():
    response = client.put("/products/1/", json=updated_product_data)
    assert response.status_code == 200
    assert response.json() == ProductInfo(id=1, **updated_product_data).dict()


def test_delete_product():
    response = client.delete("/products/1/")
    assert response.status_code in [200, 404]
