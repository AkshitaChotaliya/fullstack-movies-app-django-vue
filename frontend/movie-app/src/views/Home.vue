<template>
  <div class="container">
    <h1 class="heading">Movies</h1>
    <div class="filter-bar">
      <input v-model="filters.genre" placeholder="Filter by genre" class="input" />
      <input v-model="filters.director" placeholder="Filter by director" class="input" />
      <input v-model="filters.actor" placeholder="Filter by actor" class="input" />
      <button @click="fetchMovies" class="btn">Search</button>
    </div>
    <div v-if="loading" class="loading">Loading...</div>
    <div v-else>
      <div v-for="movie in movies" :key="movie.id" class="movie-card">
        <router-link :to="`/movies/${movie.id}`" class="movie-title">{{ movie.title }}</router-link>
        <div class="movie-meta">Year: {{ movie.release_year }} | Director: {{ movie.director.name }}</div>
        <div class="movie-genres">Genres: {{ movie.genres.map(g => g.name).join(', ') }}</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const movies = ref([])
const filters = ref({ genre: '', director: '', actor: '' })
const loading = ref(true)

const fetchMovies = async () => {
  loading.value = true
  try {
    const hasAnyFilter = filters.value.genre || filters.value.director || filters.value.actor
    const params = {}

    if (filters.value.genre) params['genre'] = filters.value.genre
    if (filters.value.director) params['director'] = filters.value.director
    if (filters.value.actor) params['actor'] = filters.value.actor

    const res = await axios.get('http://localhost:8010/api/movies/', {
      params: hasAnyFilter ? params : {}
    })

    movies.value = res.data
  } catch (err) {
    console.error('Error fetching movies:', err)
  } finally {
    loading.value = false
  }
}


onMounted(fetchMovies)
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 24px;
  font-family: Arial, sans-serif;
}

.heading {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 16px;
}

.filter-bar {
  display: flex;
  gap: 10px;
  margin-bottom: 16px;
  flex-wrap: wrap;
}

.input {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  flex: 1;
  min-width: 160px;
}

.btn {
  background-color: #2563eb;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
}

.btn:hover {
  background-color: #1e40af;
}

.loading {
  text-align: center;
  padding: 16px;
  font-size: 16px;
  color: #555;
}

.movie-card {
  border: 1px solid #ddd;
  border-radius: 6px;
  padding: 16px;
  margin-bottom: 12px;
  transition: background-color 0.2s;
}

.movie-card:hover {
  background-color: #f9f9f9;
}

.movie-title {
  font-size: 18px;
  font-weight: 600;
  color: #2563eb;
  text-decoration: none;
}

.movie-title:hover {
  text-decoration: underline;
  color: #1e40af;
}

.movie-meta,
.movie-genres {
  font-size: 14px;
  color: #555;
  margin-top: 4px;
}
</style>
