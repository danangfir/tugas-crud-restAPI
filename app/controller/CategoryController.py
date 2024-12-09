from app.model.category_product import CategoryProduct
from app import response
from flask import request, jsonify
from app import db

def index():
    try:
        categories = CategoryProduct.query.all()
        data = transform(categories)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.bad_request(message="An error occurred while fetching categories.")

def store():
    try:
        name = request.json['name']
        
        category = CategoryProduct(name=name)
        
        db.session.add(category)
        db.session.commit()

        return jsonify({"message": "Successfully created category!"}), 200

    except Exception as e:
        print(e)
        return jsonify({"message": "An error occurred while creating category!"}), 500

def transform(categories):
    array = []
    for i in categories:
        array.append({
            'id': i.id,
            'name': i.name,
            'created_at': i.created_at,
            'updated_at': i.updated_at
        })
    return array

def update(id):
    try:
        name = request.json['name']

        category = CategoryProduct.query.filter_by(id=id).first()

        if category:
            category.name = name

            db.session.commit()

            return response.ok('', 'Successfully updated category!')
        else:
            return response.error('Category not found', 404)
    
    except Exception as e:
        print(e)
        return response.error('An error occurred while updating category', 500)

def singleTransform(category):
    data = {
        'id': category.id,
        'name': category.name,
        'created_at': category.created_at,
        'updated_at': category.updated_at
    }
    return data

def show(id):
    try:
        category = CategoryProduct.query.filter_by(id=id).first()
        
        if not category:
            return response.badRequest([], "Category not found.")
        
        data = singleTransform(category)
        return response.ok(data, "Category retrieved successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return response.badRequest([], "An error occurred while retrieving the category.")

def delete(id):
    try:
        category = CategoryProduct.query.filter_by(id=id).first()

        if category:
            db.session.delete(category)
            db.session.commit()
            return response.ok('', 'Successfully deleted category!')
        else:
            return response.error('Category not found', 404)
    
    except Exception as e:
        print(e)
        return response.error('An error occurred while deleting category', 500)
