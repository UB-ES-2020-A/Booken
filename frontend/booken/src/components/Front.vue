<template>

  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
        integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
  <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
  <link href='https://fonts.googleapis.com/css?family=Lato' rel='stylesheet' type='text/css'>
  <div class="front-container">
    <div class="container" style="max-width: 1400px">
      <!-- Iterables here -->
      <div v-if="!this.edit">
        <div v-if="this.type == 2">
          <button class="btn btn-success my-2 my-sm-0 mr-2" type="submit" @click="addSection"
                  style="margin-left: 1em"><i class="fas fa-plus"
                                              style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
              class="navbartextbt">Añadir sección</a></button>
        </div>
        <div v-for="item in this.frontElements" :key="item.id">
          <!-- in case it is a jumbotron -->
          <div>
            <div role="group" style="text-align: right; margin-bottom: 0.1em" v-if="this.type == 2">
              <button class="btn btn-warning my-2 my-sm-0 mr-1" type="submit" @click="editSection(item.id)"
                      style=""><i class="fas fa-edit"
                                  style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
                  class="navbartextbt">Editar sección</a></button>
              <button class="btn btn-danger my-2 my-sm-0" type="submit" @click="deleteSection(item.id)"
                      style=""><i class="fas fa-trash"
                                  style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
                  class="navbartextbt">Eliminar sección</a></button>
            </div>
            <a :href="item.t1LinkTo" style="text-decoration: none">
              <div class="jumbotron"
                   :style="{'background-color': item.t1BackgnCOL, 'background-image': 'url(' + item.t1BackgndURL + ')'}"
                   v-if="item.frontType==1">
                <h1 class="display-4" style="color: white">{{ item.t1Tit }}</h1>
                <p class="lead" style="color: white">
                  {{ item.t1Sub }}
                </p>
                <hr class="my-4">
                <p style="font-size: 0.6em; color: white">{{ item.t1Smalll }}</p>
              </div>
            </a>
          </div>
          <!-- in case it is a custom row -->
          <div v-if="item.frontType==2">
            <h2>{{ item.t2RowTitle }}</h2>
            <div :class="this.getRowClassName(item.t2RowNumber)">
              <div class="col mb-4" v-for="(inner_item, index) in item.books" :key="index">

                <div class="card h-100">
                  <router-link :to="{name: 'BookInfo', params: {id: inner_item.id}}">
                    <img
                        :src="inner_item.cover_image_url"
                        class="card-img-top" alt="...">
                  </router-link>
                  <div class="card-body">
                    <h6 class="card-subtitle">{{ inner_item.author[0] }}</h6>
                    <h4 class="card-title">
                      <router-link :to="{name: 'BookInfo', params: {id: inner_item.id}}">{{
                          inner_item.name
                        }}
                      </router-link>
                    </h4>
                    <p class="card-text">{{ inner_item.description }}</p>
                  </div>
                  <div class="card-footer">
                    <h4>
                      <span class="badge badge-info">{{ inner_item.price }}€</span>&nbsp;
                      <span class="badge badge-secondary" v-if="inner_item.genre == 'HUMANIDADES'">Humanidades</span>
                      <span class="badge badge-secondary" v-if="inner_item.genre == 'LITERATURA'">Literatura</span>
                      <span class="badge badge-secondary"
                            v-if="inner_item.genre == 'TECNICO Y FORMACION'">Técnico y formación</span>
                      <span class="badge badge-secondary"
                            v-if="inner_item.genre == 'METODOS DE IDIOMAS'">Métodos de idiomas</span>
                      <span class="badge badge-secondary"
                            v-if="inner_item.genre == 'COMICS Y MANGA'">Cómics y manga</span>
                      <span class="badge badge-secondary"
                            v-if="inner_item.genre == 'OTRAS CATEGORIAS'">Otras categorías</span>
                      <span class="badge badge-secondary" v-if="inner_item.genre == 'INFANTIL'">Infantil</span>
                      <span class="badge badge-dark" v-if="inner_item.cover_type == 0">Tapa dura</span>
                      <span class="badge badge-dark" v-else-if="inner_item.cover_type == 1">Tapa blanda</span>
                    </h4>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-if="this.edit">
        <div class="card">
          <div class="card-body" style="text-align: left">
            <h1 class="card-title">Añadir una sección</h1>
            <select class="form-control" v-model="this.addSectionValues.frontType">
              <option value=-1>Seleccionar</option>
              <option value=1>Banner</option>
              <option value=2>Fila de libros</option>
            </select>
            <div v-if="this.addSectionValues.frontType == 1" style="margin-top: 2em">
              <h3 class="card-subtitle">Configuración del banner</h3>
              <h5 style="margin-top: 1em">Tipo de fondo del banner</h5>
              <div>
                <div class="form-check form-check-inline">
                  <input class="form-check-input" type="radio" value=1 v-model="this.addBackgroundType">
                  <label class="form-check-label">Imagen</label>
                </div>
                <div class="form-check form-check-inline">
                  <input class="form-check-input" type="radio" value=2 v-model="this.addBackgroundType">
                  <label class="form-check-label">Color</label>
                </div>
              </div>
              <div v-if="addBackgroundType==1" style="margin-top: 0.5em">
                <h5>URL imagen</h5>
                <input class="form-control" type="text" v-model="this.addSectionValues.t1BackgndURL">
              </div>
              <div v-if="addBackgroundType==2" style="margin-top: 0.5em">
                <h5>Color</h5>
                <vue-color-picker-board :width="800"
                                        :height="100"
                                        :defaultColor="'#00AAFF'"
                                        @onSelection="this.addSectionValues.t1BackgnCOL">
                </vue-color-picker-board>
              </div>
              <div v-if="this.addSectionValues.frontType == 2" style="margin-top: 2em">
                <h3 class="card-subtitle">Configuración de la fila</h3>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {VueColorPickerBoard} from 'vue-color-picker-board'
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
  components: {
    VueColorPickerBoard
  },
  created() {
    this.getBooksFromDBL('LITERATURA')
  },
  data() {
    return {
      addBackgroundType: -1,
      edit: false,
      loggedIn: false,
      addSectionValues: {
        frontType: -1,
        t1BackgndURL: '',
        t1BackgnCOL: '#2bc4ed',
        t1LinkTo: '',
        t1Tit: '',
        t1Sub: '',
        t1Smalll: '',
        t2RowTitle: '',
        t2RowNumber: '',
        books: []
      },
      frontElements: [
        {
          id: 1,
          frontType: 1,
          t1BackgndURL: '',
          t1BackgnCOL: '#2bc4ed',
          t1LinkTo: 'https://stackoverflow.com/questions/35242272/vue-js-data-bind-style-backgroundimage-not-working',
          t1Tit: 'Rebajas!',
          t1Sub: 'Esto es un sub',
          t1Smalll: 'Letra peq',
          t2RowTitle: '',
          t2RowNumber: '-1',
          books: []
        },
        {
          id: 2,
          frontType: 1,
          t1BackgndURL: 'https://w.wallhaven.cc/full/x1/wallhaven-x1kd1d.jpg',
          t1BackgnCOL: '#2bc4ed',
          t1LinkTo: '',
          t1Tit: 'Rebajas!',
          t1Sub: 'Esto es un sub',
          t1Smalll: 'Letra peq',
          t2RowTitle: '',
          t2RowNumber: '-1',
          books: []
        },
        {
          id: 3,
          frontType: 2,
          t1BackgndURL: '',
          t1BackgnCOL: '',
          t1LinkTo: '',
          t1Tit: '',
          t1Sub: '',
          t1Smalll: '',
          t2RowTitle: 'Prueba',
          t2RowNumber: '6',
          books: [{
            "id": 1,
            "ISBN": 9788431690656,
            "name": "Mitos griegos",
            "author": [
              "Maria Angelidou"
            ],
            "genre": "HUMANIDADES",
            "year": 2013,
            "editorial": "Vicens Vives",
            "language": "Castellano",
            "price": 7.5,
            "num_pages": 128,
            "cover_type": 0,
            "synopsis": "El presente volumen constituye una inmejorable introducción al universo de la mitología. Recoge catorce mitos griegos, seleccionados entre los más famosos y atractivos, que han sido narrados con amenidad y sencillez, pero también con una evidente ambición literaria. El libro cuenta con magníficas ilustraciones realizadas por el artista búlgaro Svetlín.",
            "description": "Una inmejorable introducción al universo de la mitología",
            "num_sales": 0,
            "total_available": 28,
            "cover_image_url": "https://pictures.abebooks.com/isbn/9788431690656-es.jpg",
            "back_cover_image_url": "https://images-na.ssl-images-amazon.com/images/I/81MQygGNrCL.jpg"
          }]
        }
      ],
      books: [],
      booksR: [],
      booksRR: [],
      booksRM: []
    }
  }, methods: {
    editSection(id) {
      console.log(id)
      this.edit = true
    },
    addSection() {
      this.edit = true
      this.addSectionValues = {
        frontType: -1,
        t1BackgndURL: '',
        t1BackgnCOL: '#2bc4ed',
        t1LinkTo: '',
        t1Tit: '',
        t1Sub: '',
        t1Smalll: '',
        t2RowTitle: '',
        t2RowNumber: '',
        books: []
      }
      this.addBackgroundType = -1
    },
    saveSection(id) {
      console.log(id)
      this.edit = false
    },
    deleteSection(id) {
      console.log(id)
    },
    getRowClassName(rows) {
      return "row row-cols-1 row-cols-sm-" + String(rows)
    },
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
            console.log(error) //
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
            console.log(error) //
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
.article-column1 {
  -moz-box-shadow: -5px 5px 29px #777777;
  -webkit-box-shadow: -5px 5px 29px #777777;
  box-shadow: -5px 5px 29px #777777;
  border-radius: 3px;
  -moz-border-radius: 3px;
  -webkit-border-radius: 3px;
  display: block;
}

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
