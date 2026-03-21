from pydantic import BaseModel

class PlaceBase(BaseModel):
    name: str
    type: str
    description: str
    latitude: float
    longitude: float

class PlaceCreate(PlaceBase):
    pass

class Place(PlaceBase):
    id: int

    class Config:
        from_attributes = True