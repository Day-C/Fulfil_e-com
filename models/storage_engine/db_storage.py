#!/usr/bin/python3
"""database manger"""
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.user import User
from models.product import Product
from models.review import Review
from models.category import Category
from models.subcategory import Subcategory
from models.order import Order
from models.delivery import Delivery
from models.brand import Brand
from os import getenv


classes = {"user": User, "product": Product, "review": Review, "order": Order, "category": Category, "subcategory": Subcategory, "delivery": Delivery}


class DbStorage():
    """manage all connections to database"""
    
    __session = None;
    __engine = None;

    def __init__(self):
        """Create a connection to the database."""

        #get database credentials from envirunment
        user = getenv("FUFIL_USER")
        password = getenv("FUFIL_USER_PWD")
        database = getenv("FUFIL_DB")
        host = getenv("FUFIL_HOST")
        #print("{} {} {} {}".format(user, password, database, host))
        #create connection to mysql db with 'mysqldb' driver
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            user, password, host, database), pool_pre_ping=True)

    def save(self):
        """add data to storage."""
        self.__session.commit()

    def all(self, cls=None):
        """retrive all instances of a class from storage"""

        if cls:
            objs = self.__session.query(classes[cls]).all()
        else:
            objs = []
            for clss in classes:
                result = self.__session.query(classes[clss]).all()
                for l in range(len(result)):
                    objs.append(result[l])
        new_dict = {}
        for i in range(len(objs)):
            key = objs[i].__class__.__name__ + '.' + objs[i].id
            new_dict[key] = objs[i]
        return new_dict


    def new(self, obj):
        """add objects to the current session"""

        self.__session.add(obj)

    def delete(self, obj=None):
        """remove an object from the current session."""

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables and session"""

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def get(self, cls, id):
        """rerives a specific object from ccurrent session."""

        if cls in classes:
            objs = self.__session.query(classes[cls]).all()
            if objs:
                for j in range(len(objs)):
                    if objs[j].id == id:
                        return objs[j]
    
        return None

    def count(self, cls):
        """count the number of instances of a specific clss in session"""

        if cls in classes:
            i = 0
            objs = self.__session.query(classes[cls]).all()
            for obj in range(len(objs)):
                i += 1;
            return i
        else:
            return 0
