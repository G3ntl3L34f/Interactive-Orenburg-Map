from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

def seed_data():
    db: Session = SessionLocal()

    # 🗑️ Очищаем старые данные перед добавлением новых
    db.query(models.Place).delete()
    db.commit()
    print("🗑️ Старые данные удалены")

    places = [
        {
            "name": "Бузулукский бор",
            "type": "природа",
            "description": "Уникальный сосновый лес",
            "latitude": 52.78,
            "longitude": 52.26,
            "photo": "/static/photos/buzulukskiy-bor.jpg"
        },
        {
            "name": "Оренбургский заповедник",
            "type": "природа",
            "description": "Степной заповедник",
            "latitude": 51.2,
            "longitude": 56.5,
            "photo": "/static/photos/orenburgskiy-zapovednik.jpg"
        },
        {
            "name": "Музей истории Оренбурга",
            "type": "культура",
            "description": "Исторический музей",
            "latitude": 51.77,
            "longitude": 55.10,
            "photo": "/static/photos/muzey-istorii.jpg"
        },
        {
            "name": "Караван-Сарай",
            "type": "история",
            "description": "Архитектурный комплекс XIX века",
            "latitude": 51.78,
            "longitude": 55.11,
            "photo": "/static/photos/karavan-saray.jpg"
        },
        {
            "name": "Соль-Илецк",
            "type": "природа",
            "description": "Соленые озёра",
            "latitude": 51.16,
            "longitude": 54.99,
            "photo": "/static/photos/sol-ileck.jpg"
        },
        {
            "name": "Гайский карьер",
            "type": "природа",
            "description": "Крупный промышленный карьер",
            "latitude": 51.47,
            "longitude": 58.45,
            "photo": "/static/photos/gayskiy-career.jpg"
        },
        {
            "name": "Орская крепость",
            "type": "история",
            "description": "Историческое укрепление",
            "latitude": 51.23,
            "longitude": 58.47,
            "photo": "/static/photos/orskaya-krepost.jpg"
        },
        {
            "name": "Оренбургский драмтеатр",
            "type": "культура",
            "description": "Главный театр области",
            "latitude": 51.77,
            "longitude": 55.12,
            "photo": "/static/photos/dramteatr.jpg"
        },
        {
            "name": "Ириклинское водохранилище",
            "type": "природа",
            "description": "Крупное водохранилище",
            "latitude": 51.85,
            "longitude": 57.75,
            "photo": "/static/photos/iriklin-reservoir.jpg"
        },
        {
            "name": "Сарматское золото (экспозиция)",
            "type": "культура",
            "description": "Археологические находки",
            "latitude": 51.77,
            "longitude": 55.09,
            "photo": "/static/photos/sarmatskoe-zoloto.jpg"
        }
    ]

    for place in places:
        db_place = models.Place(**place)
        db.add(db_place)

    db.commit()
    db.close()

    print("✅ Данные успешно добавлены!")
    print("📁 Добавьте фото в папку: /static/photos/")
    print("   Например: /static/photos/buzulukskiy-bor.jpg")

if __name__ == "__main__":
    seed_data()