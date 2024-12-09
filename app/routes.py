from app import app
from app.controller import UserController, ProductController, CategoryController
from flask import request

# User Routes
@app.route('/users', methods=['POST', 'GET'])
def users():
    if request.method == 'GET':
        return UserController.index()  # Fetch all users
    else:
        return UserController.store()  # Create a new user

@app.route('/users/<id>', methods=['GET', 'PUT', 'DELETE'])
def usersDetail(id):
    if request.method == 'GET':
        return UserController.show(id)  # Fetch a specific user by ID
    elif request.method == 'PUT':
        return UserController.update(id)  # Update a specific user by ID
    elif request.method == 'DELETE':
        return UserController.delete(id)  # Delete a specific user by ID

# Product Routes
# Product Routes
@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'GET':
        return ProductController.index()  # Fetch all products
    elif request.method == 'POST':
        return ProductController.store()  # Create a new product

@app.route('/products/<int:product_id>', methods=['GET', 'PUT', 'DELETE'])
def product_detail(product_id):
    if request.method == 'GET':
        return ProductController.show(product_id)  # Mengambil produk tertentu berdasarkan ID
    elif request.method == 'PUT':
        return ProductController.update(product_id)  # Memperbarui produk tertentu berdasarkan ID
    elif request.method == 'DELETE':
        return ProductController.delete(product_id)  # Menghapus produk tertentu berdasarkan ID
 # Delete a specific product by ID  # Delete a specific product by ID

@app.route('/products/<int:product_id>/categories/<int:category_id>', methods=['POST'])
def add_category_to_product(product_id, category_id):
    return ProductController.add_category_to_product(product_id, category_id)  # Add category to a product  # Add category to a product

# Category Routes
# Category Routes
@app.route('/categories', methods=['POST', 'GET'])
def categories():
    if request.method == 'GET':
        return CategoryController.index()  # Fetch all categories
    else:
        return CategoryController.store()  # Create a new category

@app.route('/categories/<id>', methods=['GET', 'PUT', 'DELETE'])
def categoryDetail(id):
    if request.method == 'GET':
        return CategoryController.show(id)  # Fetch a specific category by ID
    elif request.method == 'PUT':
        return CategoryController.update(id)  # Update a specific category by ID
    elif request.method == 'DELETE':
        return CategoryController.delete(id)  # Delete a specific category by ID
