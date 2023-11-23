#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities_relationship = relationship("City", cascade="all, delete", backref="state")

    @property
    def cities(self):
        """Getter for the cities attribute."""
        return self.cities_relationship