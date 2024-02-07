import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

"""class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {} """


class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    subscripcion = Column(DateTime)
    name = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    planetasfavoritos = relationship('Favoriteplanets', backref="usuarios")
    personajesfavoritos = relationship('Favoritecharacters', backref="usuarios")

class Planets(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    planetasfavoritos = relationship('Favoriteplanets', backref="planetas")


class Characters(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    personajesfavoritos = relationship('Favoritecharacters', backref="personajes")


class Favoriteplanets(Base):
    __tablename__ = 'planetasfavoritos'
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), primary_key=True)
    planetas_id = Column(Integer, ForeignKey('planetas.id'), primary_key=True)


class Favoritecharacters(Base):
    __tablename__ = 'personajesfavoritos'
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), primary_key=True)
    personajes_id = Column(Integer, ForeignKey('personajes.id'), primary_key=True)
    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
