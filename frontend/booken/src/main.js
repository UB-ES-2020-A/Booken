import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import mitt from 'mitt'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

// eslint-disable-next-line no-unused-vars
export const bus = mitt()
export const api = 'http://127.0.0.1:5000/'
//export const api = 'https://booken-dev.herokuapp.com/'

createApp(App).use(router).mount('#app')
