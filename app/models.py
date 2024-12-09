from app import db

class Users(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(230), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return '<User %r>' % self.name

class Todo(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    title = db.Column(db.String(230), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('Users', foreign_keys=user_id, backref=db.backref('todos', lazy=True))

    def __repr__(self):
        return '<Todo %r>' % self.title

class Product(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(230), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return '<Product %r>' % self.name

class CategoryProduct(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(230), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return '<CategoryProduct %r>' % self.name

product_category = db.Table('product_category',
    db.Column('product_id', db.BigInteger, db.ForeignKey('product.id'), primary_key=True),
    db.Column('category_id', db.BigInteger, db.ForeignKey('category_product.id'), primary_key=True)
)

