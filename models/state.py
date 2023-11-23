#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class inherits from BaseModel and Base"""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    
    cities = relationship("City", cascade="all, delete", backref="state")

    @property
    def cities(self):
        """Getter attribute to return related City instances"""
        from models import storage
        from models.city import City
        city_list = storage.all(City)
        return [city for city in city_list.values() if city.state_id == self.id]
