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
