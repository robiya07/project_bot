import sqlalchemy
from sqlalchemy import delete as sqlalchemy_delete
from sqlalchemy import update as sqlalchemy_update
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.future import select
from sqlalchemy.orm import relationship

from db.database import Base, db

db.init()


# ----------------------------- ABSTRACTS ----------------------------------
class AbstractClass:
    @classmethod
    async def create(cls, **kwargs):
        object = cls(**kwargs)
        db.add(object)
        try:
            await db.commit()
        except Exception:
            await db.rollback()
            raise
        return object

    @classmethod
    async def update(cls, id, **kwargs):
        query = (
            sqlalchemy_update(cls)
                .where(cls.id == id)
                .values(**kwargs)
                .execution_options(synchronize_session="fetch")
        )
        await db.execute(query)
        try:
            await db.commit()
        except Exception:
            await db.rollback()
            raise

    @classmethod
    async def get(cls, **kwargs):
        query = select(cls).where(cls.id == id)
        objects = await db.execute(query)
        object = objects.first()[0]
        return object

    @classmethod
    async def get_all(cls, **kwargs):
        query = select(cls)
        users = await db.execute(query)
        users = users.scalars().all()
        return users

    @classmethod
    async def delete(cls, id):
        query = sqlalchemy_delete(cls).where(cls.id == id)
        await db.execute(query)
        try:
            await db.commit()
        except Exception:
            await db.rollback()
            raise
        return True

    @classmethod
    async def counts(cls):
        objects_count_query = select(cls)
        objects_count = await db.execute(objects_count_query)
        return len(objects_count.scalars().all())


class CreatedModel(Base, AbstractClass):
    __abstract__ = True


# ------------------------------ SHOPS --------------------------------------


class About(CreatedModel):
    __tablename__ = 'about'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    bio = sqlalchemy.Column(sqlalchemy.Text)
    langs = sqlalchemy.Column(ARRAY(sqlalchemy.String(15)))
    def_lang = sqlalchemy.Column(sqlalchemy.String(3))
    token = sqlalchemy.Column(sqlalchemy.String(50), unique=True)


# ------------------------------ USERS --------------------------------------


class Customer(CreatedModel):
    __tablename__ = "customers"
    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    first_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    last_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    username = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True)
    phone = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True)
    # shop_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('shops.id'))

    basket = relationship('Basket', back_populates='customer')
    order = relationship('Order', back_populates='customer')
    comment = relationship('Comment', back_populates='author')


class Comment(CreatedModel):
    __tablename__ = 'comment'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    comment = sqlalchemy.Column(sqlalchemy.String(255))
    author_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('customers.id'))
    author = relationship('Customer', back_populates='comment')


# ------------------------------ PRODUCTS --------------------------------------

class Category(CreatedModel):
    __tablename__ = 'categories'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(50), unique=True)
    description = sqlalchemy.Column(sqlalchemy.String)
    parent = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    image = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    product = relationship('Product', back_populates='category')

    # shop

    @classmethod
    async def get_name(cls, name):
        query = select(cls).where(cls.name == name)
        try:
            objects = await db.execute(query)
            obj = objects.first()[0]
            return obj
        except:
            return

    @classmethod
    async def get_by_parent(cls, name):
        query = select(cls).where(cls.parent == name)
        objects = await db.execute(query)
        return objects.scalars().all()


class Product(CreatedModel):
    __tablename__ = "products"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(255))
    description = sqlalchemy.Column(sqlalchemy.Text)
    category_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('categories.id'))
    image = sqlalchemy.Column(sqlalchemy.String)
    price = sqlalchemy.Column(sqlalchemy.Integer)

    category = relationship('Category', back_populates='product')
    basket = relationship('Basket', back_populates='product')
    order = relationship('Order', back_populates='product')

    @classmethod
    async def get_category(cls, category):
        query = select(Category).join(Product, Category.id == Product.category_id, isouter=True).filter(
            Category.name == category or Product.id is not None)
        objects = await db.execute(query)
        obj = objects.scalars().all()
        return obj


class Basket(CreatedModel):
    __tablename__ = "basket"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    amount = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    user_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('customers.id'))
    product_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('products.id'))

    customer = relationship('Customer', back_populates='basket', )
    product = relationship('Product', back_populates='basket')


class Order(CreatedModel):
    __tablename__ = 'orders'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    amount = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    customer_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('customers.id'))
    product_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('products.id'))

    customer = relationship('Customer', back_populates='order')
    product = relationship('Product', back_populates='order')
