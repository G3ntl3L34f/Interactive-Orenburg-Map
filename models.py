from sqlalchemy import Column, Integer, String, Float, Text
from database import Base

class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    description = Column(Text)
    latitude = Column(Float)
    longitude = Column(Float)
    photo = Column(String, nullable=True)
