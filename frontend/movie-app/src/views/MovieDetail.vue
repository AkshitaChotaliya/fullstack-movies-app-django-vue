<template>
  <div class="p-6">
    <div v-if="!movie">Loading...</div>
    <div v-else>
      <h1 class="text-2xl font-bold mb-2">{{ movie.title }}</h1>
      <p class="text-gray-700">Released: {{ movie.release_year }}</p>
      <p>Genres: {{ movie.genres.map(g => g.name).join(', ') }}</p>
      <p>Director: <router-link :to="`/person/director/${movie.director.id}`">{{ movie.director.name }}</router-link></p>
      <p>Actors:
        <span v-for="actor in movie.actors" :key="actor.id">
          <router-link :to="`/person/actor/${actor.id}`">{{ actor.name }}</router-link>
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

  console.log("<---- movie.value:  ---->",movie.value);
  
}

onMounted(fetchMovie)
</script>