#!/usr/bin/env python3
'''Create a SQLAlchemy model named User'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    A SQLAlchemy model representing a user in the database.

    Attributes:
        id (int): The primary key of the user.
        email (str): The email address of the user. Non-nullable.
        hashed_password (str): The hashed password of the user. Non-nullable.
        session_id (str): The session ID of the user. Nullable.
        reset_token (str): The reset token of the user. Nullable.
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)
