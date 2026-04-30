# 🗺️ Интерактивная карта Оренбургской области

## ⚙️ Установка и запуск

### 1️⃣ Установить зависимости
```bash
pip install -r requirements.txt
```

### 2️⃣ Загрузить данные в БД
```bash
python seed_data.py
```

### 3️⃣ Запустить сервер
```bash
python -m uvicorn main:app --reload
```

### 4️⃣ Открыть в браузере
```
http://localhost:8000
```

---

## 📸 Как добавить фотографии

### Структура папок
```
project/
├── static/
│   └── photos/          ← Папка для фото
│       ├── buzulukskiy-bor.jpg
│       ├── orenburgskiy-zapovednik.jpg
│       ├── muzey-istorii.jpg
│       └── ... (остальные 7 фото)
```

### Требования к фото
- **Размер:** 400x300 пиксель (оптимально)
- **Формат:** JPG, PNG
- **Названия файлов:** Должны совпадать с именами в `seed_data.py`

### Названия файлов для каждого места
1. `buzulukskiy-bor.jpg` - Бузулукский бор
2. `orenburgskiy-zapovednik.jpg` - Оренбургский заповедник
3. `muzey-istorii.jpg` - Музей истории Оренбурга
4. `karavan-saray.jpg` - Караван-Сарай
5. `sol-ileck.jpg` - Соль-Илецк
6. `gayskiy-career.jpg` - Гайский карьер
7. `orskaya-krepost.jpg` - Орская крепость
8. `dramteatr.jpg` - Оренбургский драмтеатр
9. `iriklin-reservoir.jpg` - Ириклинское водохранилище
10. `sarmatskoe-zoloto.jpg` - Сарматское золото

### Как добавить фото
1. Скачайте/найдите фото каждого места
2. Переименуйте согласно таблице выше
3. Поместите в папку `/static/photos/`
4. Перезагрузите браузер

---

## 🎯 Структура проекта

```
├── main.py              # FastAPI приложение
├── database.py          # Конфигурация БД
├── models.py            # SQLAlchemy модели
├── schemas.py           # Pydantic схемы
├── seed_data.py         # Загрузка данных
├── index.html           # Фронтенд (карта)
├── orenburg.geojson     # Границы области
├── requirements.txt     # Зависимости
└── static/
    └── photos/          # Папка для фото
```

---

## 📊 API Endpoints

- `GET /api/places` - Получить все места
- `POST /api/places` - Добавить новое место
- `GET /api/info` - Информация о проекте

---

## 🗑️ Очистить данные

Если нужно пересоздать БД:

```bash
# Удалить БД
rm places.db

# Пересоздать
python seed_data.py
```

---

## ✅ Готово!

Теперь карта полностью готова к использованию. 
Просто добавьте фото в папку `/static/photos/` и всё будет работать! 🚀
