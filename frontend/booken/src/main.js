import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import mitt from 'mitt'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

// eslint-disable-next-line no-unused-vars
export const bus = mitt()

export const api = process.env.VUE_APP_BACKEND_URL

createApp(App).use(router).mount('#app')
