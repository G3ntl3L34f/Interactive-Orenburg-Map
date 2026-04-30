from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas
import os

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

@app.get("/api/places", response_model=list[schemas.Place])
def get_places(db: Session = Depends(get_db)):
    return db.query(models.Place).all()

@app.get("/api/info")
def get_info():
    return {
        "project": "Интерактивная карта Оренбургской области",
        "endpoints": {
            "places": "/api/places",
            "docs": "/docs"
        }
    }

@app.post("/api/places", response_model=schemas.Place)
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


# Служение статических файлов (фото, CSS, JS)
# ВАЖНО: должно быть в КОНЦЕ после всех маршрутов API!
current_dir = os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory=os.path.join(current_dir, "static")), name="static")
app.mount("/", StaticFiles(directory=current_dir, html=True), name="root")

#uvicorn main:app --reload