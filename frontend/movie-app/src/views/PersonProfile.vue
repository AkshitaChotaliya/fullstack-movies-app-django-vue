<template>
  <div class="container">
    <h1 class="name">{{ person.name }}</h1>
    <p class="role">Role: {{ role }}</p>

    <h2 class="section-title">Movies:</h2>
    <ul class="movie-list">
      <li v-for="movie in person.movies" :key="movie.id" class="movie-item">
        <router-link :to="`/movies/${movie.id}`" class="movie-link">
          {{ movie.title }} ({{ movie.release_year }})
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const id = route.params.id
const role = route.params.role
const person = ref({ name: '', movies: [] })

const fetchPersonData = async () => {
  try {
    const response = await axios.get(`/api/person/${role}/${id}`)
    person.value = response.data
  } catch (error) {
    console.error('Failed to fetch person data:', error)
  }
}

onMounted(fetchPersonData)
</script>

<style scoped>
.container {
  max-width: 700px;
  margin: 40px auto;
  padding: 32px;
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #2c3e50;
  transition: box-shadow 0.3s ease;
}

.container:hover {
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.12);
}

.name {
  font-size: 28px;
  font-weight: 700;
  margin-bottom: 8px;
  color: #1f2937;
}

.role {
  font-size: 18px;
  font-weight: 400;
  margin-bottom: 24px;
  color: #6b7280;
}

.section-title {
  font-size: 22px;
  font-weight: 600;
  margin-bottom: 16px;
  border-bottom: 2px solid #e5e7eb;
  padding-bottom: 4px;
}

.movie-list {
  list-style: none;
  padding-left: 0;
}

.movie-item {
  margin-bottom: 12px;
  padding: 8px 12px;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  transition: background-color 0.2s, border-color 0.2s;
}

.movie-item:hover {
  background-color: #f9fafb;
  border-color: #d1d5db;
}

.movie-link {
  text-decoration: none;
  font-size: 16px;
  color: #2563eb;
  transition: color 0.2s;
}

.movie-link:hover {
  color: #1e40af;
  text-decoration: underline;
}
</style>
