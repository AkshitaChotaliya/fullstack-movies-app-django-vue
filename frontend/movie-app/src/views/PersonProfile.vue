<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">{{ person.name }}</h1>
    <p class="mb-4">Role: {{ role }}</p>

    <h2 class="text-xl font-semibold mb-2">Movies:</h2>
    <ul>
      <li v-for="movie in person.movies" :key="movie.id">
        <router-link :to="`/movies/${movie.id}`" class="text-blue-500">
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

