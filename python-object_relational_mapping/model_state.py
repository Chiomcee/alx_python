#!/usr/bin/python3
"""
The script defines a class called State that inherits 
from the declarative_base() class in SQLAlchemy.
It also imports the necessary modules to define the class.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    """  """
    __tablename__ = 'state'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


