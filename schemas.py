from pydantic import BaseModel

class PlaceBase(BaseModel):
    name: str
    type: str
    description: str
    latitude: float
    longitude: float
    photo: str = None

class PlaceCreate(PlaceBase):
    pass

class Place(PlaceBase):
    id: int

    class Config:
        from_attributes = True