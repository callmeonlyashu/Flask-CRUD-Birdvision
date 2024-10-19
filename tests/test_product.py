import unittest
from main import app
import json
from flask_jwt_extended import create_access_token


class ProductsApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        with self.app.app.app_context():
            self.jwt_token = create_access_token(identity='admin')

    def test_get_products(self):
        response = self.client.get('/products', headers={'Authorization': f'Bearer {self.jwt_token}'})
        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.text)
        self.assertIsInstance(response_json, list)

    def test_create_product(self):
        new_product = {
            "title": "New Product",
            "description": "Description of new product",
            "price": 29.99
        }
        response = self.client.post('/products', json=new_product, headers={'Authorization': f'Bearer {self.jwt_token}'})
        self.assertEqual(response.status_code, 201)
        response_json = json.loads(response.text)
        self.assertEqual(response_json['title'], new_product['title'])

    def test_get_product_by_id(self):
        product = {
            "title": "Product to Get",
            "description": "Description",
            "price": 15.00
        }
        create_response = self.client.post('/products', json=product, headers={'Authorization': f'Bearer {self.jwt_token}'})
        create_response_json = json.loads(create_response.text)
        product_id = create_response_json['id']

        response = self.client.get(f'/products/{product_id}', headers={'Authorization': f'Bearer {self.jwt_token}'})
        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.text)
        self.assertEqual(response_json['id'], product_id)

    def test_get_product_not_found(self):
        response = self.client.get('/products/999999', headers={'Authorization': f'Bearer {self.jwt_token}'})  # Assuming this ID does not exist
        self.assertEqual(response.status_code, 404)

    def test_update_product(self):
        product = {
            "title": "Product to Update",
            "description": "Description",
            "price": 19.99
        }
        create_response = self.client.post('/products', json=product, headers={'Authorization': f'Bearer {self.jwt_token}'})
        create_response_json = json.loads(create_response.text)

        product_id = create_response_json['id']

        updated_product = {
            "title": "Updated Product",
            "description": "Updated Description",
            "price": 24.99
        }
        response = self.client.put(f'/products/{product_id}', json=updated_product, headers={'Authorization': f'Bearer {self.jwt_token}'})
        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.text)
        self.assertEqual(response_json['title'], updated_product['title'])

    def test_update_product_not_found(self):
        response = self.client.put('/products/999999', json={"title": "New Title", "price": 150}, headers={'Authorization': f'Bearer {self.jwt_token}'})
        self.assertEqual(response.status_code, 404)

    def test_delete_product(self):
        product = {
            "title": "Product to Delete",
            "description": "Description",
            "price": 12.99
        }
        create_response = self.client.post('/products', json=product, headers={'Authorization': f'Bearer {self.jwt_token}'})
        create_response_json = json.loads(create_response.text)
        product_id = create_response_json['id']

        response = self.client.delete(f'/products/{product_id}', headers={'Authorization': f'Bearer {self.jwt_token}'})
        self.assertEqual(response.status_code, 204)

    def test_delete_product_not_found(self):
        response = self.client.delete('/products/999999', headers={'Authorization': f'Bearer {self.jwt_token}'})  # Assuming this ID does not exist
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()