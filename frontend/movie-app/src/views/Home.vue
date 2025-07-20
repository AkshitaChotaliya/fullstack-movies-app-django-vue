<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">Movies</h1>
    <div class="mb-4 flex gap-2">
      <input v-model="filters.genre" placeholder="Filter by genre" class="input" />
      <input v-model="filters.director" placeholder="Filter by director" class="input" />
      <input v-model="filters.actor" placeholder="Filter by actor" class="input" />
      <button @click="fetchMovies" class="btn">Search</button>
    </div>
    <div v-if="loading" class="text-center py-4">Loading...</div>
    <div v-else>
      <div v-for="movie in movies" :key="movie.id" class="border rounded p-4 mb-2 hover:bg-gray-50">
        <router-link :to="`/movies/${movie.id}`" class="text-xl font-semibold text-blue-600 hover:text-blue-800">{{ movie.title }}</router-link>
        <div class="text-sm text-gray-600">Year: {{ movie.release_year }} | Director: {{ movie.director.name }}</div>
        <div class="text-sm">Genres: {{ movie.genres.map(g => g.name).join(', ') }}</div>
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
    const params = {}
    if (filters.value.genre) params['genres__name'] = filters.value.genre
    if (filters.value.director) params['director__name'] = filters.value.director
    if (filters.value.actor) params['actors__name'] = filters.value.actor
    const res = await axios.get('http://localhost:8010/api/movies/', { params })
    movies.value = res.data
  } catch (err) {
    console.error(err)
  } finally {
    loading.value = false
  }
}

onMounted(fetchMovies)
</script>

<style scoped>
.input {
  @apply border p-2 rounded;
}
.btn {
  @apply bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700;
}
</style>