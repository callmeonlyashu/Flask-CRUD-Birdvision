from apisvc.models.product import Product
from src.database.db import SessionLocal
from flask import jsonify
from flask import request, jsonify
from flask_jwt_extended import create_access_token
from src.auth_handlers.token_manager import decode_auth_header


users = {
    "admin": "password",
}


def auth_login():
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith("Basic "):
        try:
            username, password = decode_auth_header(auth_header)
        except Exception:
            return jsonify({"msg": "Invalid authentication header"}), 401

        # Verify credentials
        if username in users and users[username] == password:
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200
        return jsonify({"msg": "Unauthorized"}), 401
    return jsonify({"msg": "Missing Authorization Header"}), 401


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def getProducts():
    try:
        db = next(get_db())
        products = db.query(Product).all()
        return jsonify([{"id": p.id, "title": p.title, "description": p.description, "price": p.price} for p in products]), 200
    except Exception as e:
        return jsonify(error="Failed to get the products from DB"), 500


def getProductById(id):
    try:
        db = next(get_db())
        product = db.query(Product).filter(Product.id == id).first()
        if product:
            return jsonify({"id": product.id, "title": product.title, "description": product.description, "price": product.price}), 200
        return jsonify(error="Product not found"), 404
    except Exception as e:
        return jsonify(error="Failed to get the products from DB"), 500


def createProduct(body):
    try:
        db = next(get_db())
        new_product = Product(title=body['title'], description=body.get('description'), price=body['price'])
        db.add(new_product)
        db.commit()
        return jsonify({"id": new_product.id, "title": new_product.title, "description": new_product.description, "price": new_product.price}), 201
    except Exception as e:
        return jsonify(error="Failed to post the products to DB"), 500


def updateProduct(id, body):
    try:
        db = next(get_db())
        product = db.query(Product).filter(Product.id == id).first()
        if product:
            product.title = body['title']
            product.description = body.get('description')
            product.price = body['price']
            db.commit()
            return jsonify({"id": product.id, "title": product.title, "description": product.description, "price": product.price}), 200
        return jsonify(error="Product not found"), 404
    except Exception as e:
        return jsonify(error="Failed to post the products to DB"), 500


def deleteProduct(id):
    try:
        db = next(get_db())
        product = db.query(Product).filter(Product.id == id).first()
        if product:
            db.delete(product)
            db.commit()
            return jsonify(info="Product deleted successfully"), 204
        return jsonify(error="Product not found"), 404
    except Exception as e:
        return jsonify(error="Failed to post the products to DB"), 500
