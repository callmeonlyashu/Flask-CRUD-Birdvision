from sqlalchemy import Column, Integer, String, Float
from src.database.db import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)