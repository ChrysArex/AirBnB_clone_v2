#!/usr/bin/python3
"""Define the DBStorage engine"""
from sqlalchemy import create_engine, MetaData, text
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State
from models.user import User
import os

class DBStorage():
    """Manage the database for the HBNB project"""
    __engine = None
    __session = None

    def __init__(self):
        """create the engine"""
        self.__engine = create_engine(
            f"mysql+mysqldb://{os.getenv('HBNB_MYSQL_USER')}:{os.getenv('HBNB_MYSQL_PWD')}@{os.getenv('HBNB_MYSQL_HOST')}/{os.getenv('HBNB_MYSQL_DB')}",
            pool_pre_ping=True
        )
        self.__session = sessionmaker(bind=self.__engine)()

        metadata = MetaData()
        if os.getenv("HBNB_ENV") == "test":
            metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """query all objects depending on the class name"""
        data = {}
        if cls:
            query_class = globals().get(cls)
            if query_class:
                for element in self.__session.query(query_class).all():
                    data[f"{cls}.{element.id}"] = element
        else:
            model_classes = [User, State, City, Amenity, Place, Review]
            for model_class in model_classes:
                for element in self.__session.query(model_class).all():
                    data[f"{model_class.__name__}.{element.id}"] = element
        return data

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database and the current session"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()
 