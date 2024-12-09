from app import db

class Product(db.Model):
    __tablename__ = 'product'
    
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(230), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    categories = db.relationship('CategoryProduct', secondary='product_category', backref='products')

class CategoryProduct(db.Model):
    __tablename__ = 'category_product'
    
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(230), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
