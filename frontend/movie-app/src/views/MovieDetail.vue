<template>
  <div class="container">
    <div v-if="!movie" class="loading">Loading...</div>
    <div v-else>
      <h1 class="title">{{ movie.title }}</h1>
      <p class="info"><strong>Released:</strong> {{ movie.release_year }}</p>
      <p class="info"><strong>Genres:</strong> {{ movie.genres.map(g => g.name).join(', ') }}</p>
      <p class="info">
        <strong>Director:</strong>
        <router-link :to="`/person/director/${movie.director.id}`" class="link">
          {{ movie.director.name }}
        </router-link>
      </p>
      <p class="info">
        <strong>Actors:</strong>
        <span v-for="(actor, index) in movie.actors" :key="actor.id">
          <router-link :to="`/person/actor/${actor.id}`" class="link">
            {{ actor.name }}
          </router-link>
          <span v-if="index < movie.actors.length - 1">, </span>
        </span>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const movie = ref(null)

const fetchMovie = async () => {
  const res = await axios.get(`http://localhost:8010/api/movies/${route.params.id}/`)
  movie.value = res.data
  console.log('<---- movie.value: ---->', movie.value)
}

onMounted(fetchMovie)
</script>

<style scoped>
.container {
  max-width: 720px;
  margin: 40px auto;
  padding: 32px;
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.1);
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  transition: all 0.3s ease;
}

.container:hover {
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
}

.loading {
  font-size: 18px;
  text-align: center;
  padding: 24px;
  color: #555;
}

.title {
  font-size: 32px;
  font-weight: 700;
  margin-bottom: 16px;
  color: #1f2937;
  border-bottom: 2px solid #e5e7eb;
  padding-bottom: 8px;
}

.info {
  font-size: 17px;
  color: #374151;
  margin: 12px 0;
  line-height: 1.6;
}

.link {
  color: #2563eb;
  font-weight: 500;
  text-decoration: none;
  transition: color 0.3s ease;
}

.link:hover {
  color: #1e40af;
  text-decoration: underline;
}
</style>
