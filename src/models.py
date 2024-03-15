import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    favorites = relationship('Favorite', back_populates='user')


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    gender = Column(String(50))
    eye_color = Column(String(50), nullable=False)
    hair_color = Column(String(50), nullable=False)
    skin_color = Column(String(50), nullable=False)
    birth_year = Column(Integer, nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False)
    vehicles = relationship('Vehicle', backref='character', uselist=False)
    favorites = relationship('Favorite', backref='character', lazy=True)
    

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    climate = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water = Column(Integer, nullable=True)
    characters = relationship('Character', backref='planet', lazy=True)
    favorites = relationship('Favorite', backref='planet', lazy=True)



class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    crew = Column(Integer, nullable=False)
    length = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=False, unique=True)
    favourites = relationship('Favorite', backref='vehicle', lazy=True)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
