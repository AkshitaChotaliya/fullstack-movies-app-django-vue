# 🎬 Movies API Backend (Django + Docker)

This is a full-featured Django REST API to manage **Movies**, **Actors**, **Directors**, and **Genres**, including filtering, relationships, and Swagger documentation. It uses **Docker**, **PostgreSQL**, and **drf-yasg** for API docs.

---

## 🧱 Features

- 📽️ CRUD operations for Movies, Actors, Directors, Genres
- 🔗 Relationships:
  - A movie belongs to one director
  - A movie can have multiple actors and genres
- 🔍 Filter movies by genre, director, actor, release year
- 🔍 Filter actors by movie or genre
- 🔐 RESTful API with Django REST Framework
- 📄 Swagger docs via drf-yasg
- 🐳 Dockerized setup with PostgreSQL

---

## ⚙️ Tech Stack

- Backend: **Django 5+, DRF**
- API Docs: **Swagger/OpenAPI** via `drf-yasg`
- Database: **PostgreSQL**
- DevOps: **Docker & docker-compose**

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Docker & Docker Compose installed
- (Optional) Python 3.11+ and pipenv/venv for local dev

---

### 🐳 Run Project with Docker

```bash
# 1. Build and start services
docker-compose up --build

# 2. Run migrations
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate

# 3. (Optional) Create superuser
docker-compose exec web python manage.py createsuperuser
```

---

### 🔗 API Endpoints

| Resource     | Endpoint           | Methods          |
|--------------|--------------------|------------------|
| Movies       | `/api/movies/`     | GET, POST, PUT, DELETE |
| Actors       | `/api/actors/`     | GET, POST, PUT, DELETE |
| Directors    | `/api/directors/`  | GET, POST, PUT, DELETE |
| Genres       | `/api/genres/`     | GET, POST, PUT, DELETE |

---

### 🔍 Filtering Support

- **Movies**
  - `?genre=Action`
  - `?director=Quentin Tarantino`
  - `?release_year=1999`
  - `?actor=Leonardo DiCaprio`

- **Actors**
  - `?movie=Inception`
  - `?genre=Drama`

---

### 📄 API Documentation

Swagger UI is available at:

```
http://localhost:8010/swagger/
```

ReDoc (alternative docs) at:

```
http://localhost:8010/redoc/
```

---

## 🧪 Running Tests

```bash
docker-compose exec web python manage.py test
```

---

## 🗃️ Folder Structure (Backend)

```
backend/
├── myapp/
│   ├── models.py        # Movie, Actor, Director, Genre models
│   ├── serializers.py   # DRF serializers
│   ├── views.py         # ViewSets with filters
│   └── urls.py          # API routes
├── backend/
│   └── settings.py      # Config (DB, CORS, Swagger, etc.)
├── manage.py
├── Dockerfile
└── docker-compose.yml
```

---

## 🐳 Docker Services

| Service | Port | Description       |
|---------|------|-------------------|
| web     | 8010 | Django backend    |
| db      | 5432 | PostgreSQL DB     |

---


