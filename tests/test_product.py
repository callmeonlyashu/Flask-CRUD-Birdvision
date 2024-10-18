import pytest
from main import app
import json

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_get_products(client):
    response = client.get('/products')
    assert response.status_code == 200
    response_json = json.loads(response.text)
    assert isinstance(response_json, list)


def test_create_product(client):
    new_product = {
        "title": "New Product",
        "description": "Description of new product",
        "price": 29.99
    }
    response = client.post('/products', json=new_product)
    assert response.status_code == 201
    response_json = json.loads(response.text)
    assert response_json['title'] == new_product['title']


def test_get_product_by_id(client):
    product = {
        "title": "Product to Get",
        "description": "Description",
        "price": 15.00
    }
    create_response = client.post('/products', json=product)
    create_response_json = json.loads(create_response.text)
    product_id = create_response_json['id']

    response = client.get(f'/products/{product_id}')
    assert response.status_code == 200
    response_json = json.loads(response.text)
    assert response_json['id'] == product_id


def test_get_product_not_found(client):
    response = client.get('/products/999999')  # Assuming this ID does not exist
    assert response.status_code == 404


def test_update_product(client):
    product = {
        "title": "Product to Update",
        "description": "Description",
        "price": 19.99
    }
    create_response = client.post('/products', json=product)
    create_response_json = json.loads(create_response.text)

    product_id = create_response_json['id']

    updated_product = {
        "title": "Updated Product",
        "description": "Updated Description",
        "price": 24.99
    }
    response = client.put(f'/products/{product_id}', json=updated_product)
    assert response.status_code == 200
    response_json = json.loads(response.text)
    assert response_json['title'] == updated_product['title']


def test_update_product_not_found(client):
    response = client.put('/products/999999', json={"title": "New Title", "price": 150})
    assert response.status_code == 404


def test_delete_product(client):
    product = {
        "title": "Product to Delete",
        "description": "Description",
        "price": 12.99
    }
    create_response = client.post('/products', json=product)
    create_response_json = json.loads(create_response.text)
    product_id = create_response_json['id']

    response = client.delete(f'/products/{product_id}')
    assert response.status_code == 204


def test_delete_product_not_found(client):
    response = client.delete('/products/999999')  # Assuming this ID does not exist
    assert response.status_code == 404