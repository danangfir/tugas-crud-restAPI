from app import db

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