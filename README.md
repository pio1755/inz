# Aplikacja do tworzenia planu zajęć

## ✅ Wymagania

- Python **3.8**
- pip

## 🚀 Instrukcja uruchomienia aplikacji

Aby uruchomić aplikację lokalnie, wykonaj poniższe kroki:

### 1️⃣ Pobranie zależności:

```bash
pip install -r requirements.txt
```

### 2️⃣ Przygotowanie migracji bazy danych:

```bash

python manage.py migrate
```

### 3️⃣ Utworzenie konta administratora:

```bash
python manage.py createsuperuser
```

Postępuj zgodnie z instrukcjami, podając nazwę użytkownika, email oraz hasło.

### 4️⃣ Uruchomienie aplikacji:

```bash
python manage.py runserver
```

Twoja aplikacja będzie dostępna pod adresem:

```
http://127.0.0.1:8000/
```

Zaloguj się za pomocą danych administratora utworzonych wcześniej.

---
