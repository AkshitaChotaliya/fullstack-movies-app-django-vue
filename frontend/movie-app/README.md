
# 🎬 Full Stack Movies App

A full-stack web application for browsing movies, actors, and directors, built with:

- **Backend**: Django + Django REST Framework (DRF)
- **Frontend**: Vue 3 + Vite
- **Docker**: Containerized backend, frontend, and PostgreSQL DB

---

## 🔧 Features

- List, view, and filter movies by genre, year, and director  
- View movie details, actors, and directors  
- Dedicated profile view for each actor/director showing associated movies  
- REST API with filtering support  
- Dockerized setup for easy deployment and development  

---

## 🚀 Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/AkshitaChotaliya/fullstack-movies-app-django-vue.git
cd fullstack-movies-app-django-vue.git

### 2. Run with Docker

```bash
docker-compose down --volumes

docker-compose up --build
```

### 3. Run Migrations

```bash
docker-compose exec backend python manage.py migrate
```

---

## 🌐 App URLs

| Service      | URL                         |
|--------------|-----------------------------|
| Frontend     | http://localhost:5173       |
| Backend API  | http://localhost:8010/api/  |
| Swagger Docs | http://localhost:8010/swagger/ |


http://localhost:8010/swagger/
---

## 🗂 Project Structure

```
.
├── backend/                # Django project
│   ├── manage.py
│   ├── myproject/
│   └── requirements.txt
├── frontend/               # Vue 3 + Vite frontend
│   ├── src/
│   ├── views/
│   └── package.json
├── docker-compose.yml
├── README.md
```

---

## 🛣️ Vue Router Setup

```js
// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import MovieDetail from '../views/MovieDetail.vue'
import PersonProfile from '../views/PersonProfile.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/movies/:id', component: MovieDetail, props: true },
  { path: '/person/:id', component: PersonProfile, props: true },
  { path: '/person/:role/:id', component: PersonProfile, props: true }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
```

### ➕ Explanation

- `/movies/:id` → Single movie detail  
- `/person/:id` → Generic fallback profile (optional)  
- `/person/:role/:id` → Actor or Director profile with role-based logic (preferred)  

---

## 🐳 Docker Commands

```bash
# Build & run all services
docker-compose up --build
docker-compose up --build -d


# Access Django shell
docker-compose exec backend python manage.py shell

# Create superuser
docker-compose exec backend python manage.py createsuperuser
```

---

## 🧪 Tech Stack

| Layer      | Tech                          |
|------------|-------------------------------|
| Frontend   | Vue 3, Vite, Axios            |
| Backend    | Django, DRF, drf-yasg         |
| Database   | PostgreSQL                    |
| DevOps     | Docker, docker-compose        |

---

## ✅ Todos

- [x] Actor & Director profile views  
- [x] Genre and Year filtering  


---

## 📄 License

MIT License. Feel free to use and modify.
