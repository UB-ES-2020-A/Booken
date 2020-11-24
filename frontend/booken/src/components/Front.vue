<template>

  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
        integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
  <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
  <link href='https://fonts.googleapis.com/css?family=Lato' rel='stylesheet' type='text/css'>
  <div class="front-container">
    <div class="container" style="max-width: 1400px">

      <div class="jumbotron" style="background-image: url('https://w.wallhaven.cc/full/x1/wallhaven-x1kd1d.jpg')">
        <h1 class="display-4" style="color: white">¡Todos los libros a un clic de ti!</h1>
        <p class="lead" style="color: white">¿Preparándote para otro confinamiento? En <span
            style="font-family: LogoFont; color: #2bc4ed; font-size: 1.3em">booken</span> te ayudamos, compra <b>2</b>
          libros y el envío
          te sale gratis.</p>
        <hr class="my-4">
        <p style="font-size: 0.6em; color: white">*Para compras de más de 49€. Se aplican otras restricciones.</p>
      </div>
      <h2>Los libros de los que todos hablan</h2>
      <!-- First row of recommended books -->
      <div class="row row-cols-1 row-cols-sm-5">
        <div class="col mb-4" v-for="(item, index) in this.booksRR" :key="index">
          <div class="card h-100">
            <img
                :src="item.cover_image_url"
                class="card-img-top" alt="...">
            <div class="card-body">
              <h6 class="card-subtitle">{{ item.author[0] }}</h6>
              <h4 class="card-title">
                <router-link :to="{name: 'BookInfo', params: {id: item.id}}">{{ item.name }}</router-link>
              </h4>
              <p class="card-text">{{ item.description }}</p>
            </div>
            <div class="card-footer">
              <h4>
                <span class="badge badge-info">{{ item.price }}€</span>&nbsp;
                <span class="badge badge-secondary" v-if="item.genre == 'HUMANIDADES'">Humanidades</span>
                <span class="badge badge-secondary" v-if="item.genre == 'LITERATURA'">Literatura</span>
                <span class="badge badge-secondary"
                      v-if="item.genre == 'TECNICO Y FORMACION'">Técnico y formación</span>
                <span class="badge badge-secondary" v-if="item.genre == 'METODOS DE IDIOMAS'">Métodos de idiomas</span>
                <span class="badge badge-secondary" v-if="item.genre == 'COMICS Y MANGA'">Cómics y manga</span>
                <span class="badge badge-secondary" v-if="item.genre == 'OTRAS CATEGORIAS'">Otras categorías</span>
                <span class="badge badge-secondary" v-if="item.genre == 'INFANTIL'">Infantil</span>
                <span class="badge badge-dark" v-if="item.cover_type == 0">Tapa dura</span>
                <span class="badge badge-dark" v-else-if="item.cover_type == 1">Tapa blanda</span>
              </h4>
            </div>
          </div>
        </div>
      </div>
      <h2>Las novelas más populares</h2>
      <!-- Second row of recommended books -->
      <div class="row row-cols-1 row-cols-sm-5">
        <div class="col mb-4" v-for="(item, index) in this.booksRM" :key="index">
          <div class="card h-100">
            <img
                :src="item.cover_image_url"
                class="card-img-top" alt="...">
            <div class="card-body">
              <h6 class="card-subtitle">{{ item.author[0] }}</h6>
              <h4 class="card-title">
                <router-link :to="{name: 'BookInfo', params: {id: item.id}}">{{ item.name }}</router-link>
              </h4>
              <p class="card-text">{{ item.description }}</p>
            </div>
            <div class="card-footer">
              <h4>
                <span class="badge badge-info">{{ item.price }}€</span>&nbsp;
                <span class="badge badge-secondary" v-if="item.genre == 'HUMANIDADES'">Humanidades</span>
                <span class="badge badge-secondary" v-if="item.genre == 'LITERATURA'">Literatura</span>
                <span class="badge badge-secondary"
                      v-if="item.genre == 'TECNICO Y FORMACION'">Técnico y formación</span>
                <span class="badge badge-secondary" v-if="item.genre == 'METODOS DE IDIOMAS'">Métodos de idiomas</span>
                <span class="badge badge-secondary" v-if="item.genre == 'COMICS Y MANGA'">Cómics y manga</span>
                <span class="badge badge-secondary" v-if="item.genre == 'OTRAS CATEGORIAS'">Otras categorías</span>
                <span class="badge badge-secondary" v-if="item.genre == 'INFANTIL'">Infantil</span>
                <span class="badge badge-dark" v-if="item.cover_type == 0">Tapa dura</span>
                <span class="badge badge-dark" v-else-if="item.cover_type == 1">Tapa blanda</span>
              </h4>
            </div>
          </div>
        </div>
      </div>
      <!-- Customizable jumbotron -->
      <div class="jumbotron jumbotron-fluid" style="background-color: #2bc4ed; text-align: left !important;">
        <div class="container">
          <h1 class="display-4">¿No encuentras lo que buscas?</h1>
          <p class="lead">No dudes en
            <router-link to="/contact">contactarnos</router-link>
            , ¡y te ayudaremos!
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import {api} from "@/main";
import axios from "axios";

export default {
  name: 'Front',
  props: {
    logged: Boolean,
    token: String,
    id: Number,
    type: Number
  },
  created() {
    this.getBooksFromDBL('LITERATURA')
  },
  data() {
    return {
      loggedIn: false,
      books: [],
      booksR: [],
      booksRR: [],
      booksRM: []
    }
  }, methods: {
    compare(a, b) {
      if (a.num_sales < b.num_sales)
        return 1;
      if (a.num_sales > b.num_sales)
        return -1;
      return 0;
    },
    getYear() {
      return new Date().getFullYear()
    },
    getBooksFromDBL(req) {
      var path = api + 'books/' + req
      if (req === 'TODO') {
        path = api + 'books'
      }
      axios.get(path)
          .then((res) => {
            this.books = res.data.books
            this.recommendBooks()
            this.getBooksFromDBR('TODO')
          })
          .catch((error) => {
            this.toPrint(error)
          })
    }, getBooksFromDBR(req) {
      var path = api + 'books/' + req
      if (req === 'TODO') {
        path = api + 'books'
      }
      axios.get(path)
          .then((res) => {
            this.booksR = res.data.books
            this.booksRR = this.booksR.sort(this.compare).slice(0, 5)
          })
          .catch((error) => {
            this.toPrint(error)
          })
    },
    recommendBooks() {
      var min = 0, max = this.books.length - 1
      var r1 = 0, r2 = 0, r3 = 0, r4 = 0, r5 = 0
      while (r1 == r2 || r1 == r3 || r1 == r4 || r1 == r5 ||
      r2 == r1 || r2 == r3 || r2 == r4 || r2 == r5 ||
      r3 == r1 || r3 == r2 || r3 == r4 || r3 == r5 ||
      r4 == r1 || r4 == r2 || r4 == r3 || r4 == r5 ||
      r5 == r1 || r5 == r2 || r5 == r3 || r5 == r4) {
        r1 = Math.floor(Math.random() * (max - min + 1) + min)
        r2 = Math.floor(Math.random() * (max - min + 1) + min)
        r3 = Math.floor(Math.random() * (max - min + 1) + min)
        r4 = Math.floor(Math.random() * (max - min + 1) + min)
        r5 = Math.floor(Math.random() * (max - min + 1) + min)
      }
      this.booksRM.push(this.books[r1])
      this.booksRM.push(this.books[r2])
      this.booksRM.push(this.books[r3])
      this.booksRM.push(this.books[r4])
      this.booksRM.push(this.books[r5])
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.front-container {
  margin-right: 5%;
  margin-left: 5%;
  margin-top: 50px;
  text-align: left;
}

@font-face {
  font-family: 'LogoFont';
  src: url('../assets/logo_font.woff')
}

.categoriestxt {
  color: #2bc4ed !important;
  font-size: 1.1em;
}

.navbartextbt {
  color: white;
  font-size: 1.2em
}

.mainlogo {
  font-family: LogoFont;
  color: #3b494d !important;
  font-size: 3.3em;
  letter-spacing: 0.1em;
}

.site-footer {
  background-color: #3b494d;
  padding: 45px 0 20px;
  font-size: 15px;
  line-height: 24px;
  color: #737373;
}

.site-footer hr {
  border-top-color: #bbb;
  opacity: 0.5
}

.site-footer hr.small {
  margin: 20px 0
}

.site-footer h6 {
  color: #fff;
  font-size: 16px;
  text-transform: uppercase;
  margin-top: 5px;
  letter-spacing: 2px
}

.site-footer a {
  color: #737373;
}

.site-footer a:hover {
  color: #3366cc;
  text-decoration: none;
}

.footer-links {
  padding-left: 0;
  list-style: none
}

.footer-links li {
  display: block
}

.footer-links a {
  color: #737373
}

.footer-links a:active, .footer-links a:focus, .footer-links a:hover {
  color: #3366cc;
  text-decoration: none;
}

.footer-links.inline li {
  display: inline-block
}

.site-footer .social-icons {
  text-align: right
}

.site-footer .social-icons a {
  width: 40px;
  height: 40px;
  line-height: 40px;
  margin-left: 6px;
  margin-right: 0;
  border-radius: 100%;
  background-color: #33353d
}

.copyright-text {
  margin: 0
}

@media (max-width: 991px) {
  .site-footer [class^=col-] {
    margin-bottom: 30px
  }
}

@media (max-width: 767px) {
  .site-footer {
    padding-bottom: 0
  }

  .site-footer .copyright-text, .site-footer .social-icons {
    text-align: center
  }
}
</style>
