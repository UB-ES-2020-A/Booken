import {createApp} from 'vue'
import {VueCookieNext} from 'vue-cookie-next'
import App from './App.vue'
import router from './router'
import mitt from 'mitt'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

export const bus = mitt()
export const api = process.env.VUE_APP_BACKEND_URL

const app = createApp(App)

app.use(VueCookieNext)
app.use(router)
app.mount('#app')
