from app.model.category_product import CategoryProduct
from app.model.product import Product
from app import response
from flask import request, jsonify
from app import db

def index():
    try:
        products = Product.query.all()
        data = transform(products)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.bad_request(message="An error occurred while fetching products.")

def store():
    try:
        name = request.json['name']
        description = request.json['description']
        price = request.json['price']
        
        product = Product(name=name, description=description, price=price)
        
        db.session.add(product)
        db.session.commit()

        return jsonify({"message": "Successfully created product!"}), 200

    except Exception as e:
        print(e)
        return jsonify({"message": "An error occurred while creating product!"}), 500

def transform(products):
    array = []
    for i in products:
        array.append({
            'id': i.id,
            'name': i.name,
            'description': i.description,
            'price': i.price
        })
    return array

def update(id):
    try:
        name = request.json['name']
        description = request.json['description']
        price = request.json['price']

        product = Product.query.filter_by(id=id).first()

        if product:
            product.name = name
            product.description = description
            product.price = price

            db.session.commit()

            return response.ok('', 'Successfully updated product!')
        else:
            return response.error('Product not found', 404)
    
    except Exception as e:
        print(e)
        return response.error('An error occurred while updating product', 500)

def singleTransform(product):
    data = {
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price
    }
    return data

def show(id):
    try:
        product = Product.query.filter_by(id=id).first()
        
        if not product:
            return response.badRequest([], "Product not found.")
        
        data = singleTransform(product)
        return response.ok(data, "Product retrieved successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return response.badRequest([], "An error occurred while retrieving the product.")
def add_category_to_product(product_id, category_id):
    try:
        product = Product.query.filter_by(id=product_id).first()
        category = CategoryProduct.query.filter_by(id=category_id).first()

        if not product or not category:
            return response.bad_request([], "Product or Category not found.")

        if category not in product.categories:
            product.categories.append(category)
            db.session.commit()
            return response.ok('', 'Successfully added category to product!')
        else:
            return response.error('Category already associated with this product', 400)

    except Exception as e:
        print(e)
        return response.error('An error occurred while adding category to product', 500)

def delete(id):
    try:
        product = Product.query.filter_by(id=id).first()
        if product:
            db.session.delete(product)
            db.session.commit()
            return response.ok('', 'Produk berhasil dihapus!')
        else:
            return response.error('Produk tidak ditemukan', 404)
    except Exception as e:
        print(e)
        return response.error('Terjadi kesalahan saat menghapus produk', 500)

