#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    # For DBStorage
    if storage_type == 'db':
        cities = relationship("City", backref="state")

    # For FileStorage
    else:
        @property
        def cities(self):
            from models import storage
            return [city for city in storage.all(City).values()
                    if city.state_id == self.id]
