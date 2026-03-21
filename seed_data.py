from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

# создаём таблицы (если ещё не созданы)
models.Base.metadata.create_all(bind=engine)

def seed_data():
    db: Session = SessionLocal()

    places = [
        {
            "name": "Бузулукский бор",
            "type": "природа",
            "description": "Уникальный сосновый лес",
            "latitude": 52.78,
            "longitude": 52.26
        },
        {
            "name": "Оренбургский заповедник",
            "type": "природа",
            "description": "Степной заповедник",
            "latitude": 51.2,
            "longitude": 56.5
        },
        {
            "name": "Музей истории Оренбурга",
            "type": "культура",
            "description": "Исторический музей",
            "latitude": 51.77,
            "longitude": 55.10
        },
        {
            "name": "Караван-Сарай",
            "type": "история",
            "description": "Архитектурный комплекс XIX века",
            "latitude": 51.78,
            "longitude": 55.11
        },
        {
            "name": "Соль-Илецк",
            "type": "природа",
            "description": "Соленые озёра",
            "latitude": 51.16,
            "longitude": 54.99
        },
        {
            "name": "Гайский карьер",
            "type": "природа",
            "description": "Крупный промышленный карьер",
            "latitude": 51.47,
            "longitude": 58.45
        },
        {
            "name": "Орская крепость",
            "type": "история",
            "description": "Историческое укрепление",
            "latitude": 51.23,
            "longitude": 58.47
        },
        {
            "name": "Оренбургский драмтеатр",
            "type": "культура",
            "description": "Главный театр области",
            "latitude": 51.77,
            "longitude": 55.12
        },
        {
            "name": "Ириклинское водохранилище",
            "type": "природа",
            "description": "Крупное водохранилище",
            "latitude": 51.85,
            "longitude": 57.75
        },
        {
            "name": "Сарматское золото (экспозиция)",
            "type": "культура",
            "description": "Археологические находки",
            "latitude": 51.77,
            "longitude": 55.09
        }
    ]

    for place in places:
        db_place = models.Place(**place)
        db.add(db_place)

    db.commit()
    db.close()

    print("✅ Данные успешно добавлены!")

if __name__ == "__main__":
    seed_data()