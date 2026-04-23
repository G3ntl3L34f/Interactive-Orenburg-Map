from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/places", response_model=list[schemas.Place])
def get_places(db: Session = Depends(get_db)):
    return db.query(models.Place).all()

@app.get("/")
def root():
    return {
        "project": "Интерактивная карта Оренбургской области",
        "endpoints": {
            "places": "/places",
            "docs": "/docs"
        }
    }


@app.post("/places", response_model=schemas.Place)
def create_place(place: schemas.PlaceCreate, db: Session = Depends(get_db)):
    db_place = models.Place(**place.dict())
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return db_place


@app.delete("/places/{place_id}")
def delete_place(place_id: int, db: Session = Depends(get_db)):
    place = db.query(models.Place).get(place_id)
    if place:
        db.delete(place)
        db.commit()
    return {"message": "deleted"}


#uvicorn main:app --reload