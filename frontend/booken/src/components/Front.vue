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
              <button class="btn btn-success my-2 my-sm-0 mr-1" type="submit" v-if="item.id > 1" @click="moveUp(id)"
                      style=""><i class="fas fa-arrow-up"
                                  style="color: #FFF; font-size: 1.5em"/><a
                  class="navbartextbt"></a></button>
              <button class="btn btn-success my-2 my-sm-0 mr-1" type="submit" v-if="item.id < this.frontElements.length"
                      style="" @click="moveDown(id)"><i class="fas fa-arrow-down"
                                  style="color: #FFF; font-size: 1.5em"/><a
                  class="navbartextbt"></a></button>
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
                <hr class="my-4" v-if="item.t1Separator">
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
        <div class="card" style="margin-bottom: 1em">
          <div class="card-body" style="text-align: left">
            <div class="row">
              <div class="col">
                <h1 class="card-title">Añadir una sección</h1>
              </div>
              <div class="col" style="text-align: right">
                <button class="btn btn-danger my-2 my-sm-0 mr-2" type="submit"
                        v-if="edit" @click="discardChanges"><i class="fas fa-times"
                                                               style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
                    class="navbartextbt">Descartar</a></button>
                <button class="btn btn-warning my-2 my-sm-0 mr-2" type="submit"
                        v-if="edit" @click="saveSection" :disabled="canSectionBeSaved()"><i class="fas fa-save"
                                                                                            style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
                    class="navbartextbt">Guardar</a></button>
              </div>
            </div>
            <select class="form-control" v-model="this.addSectionValues.frontType">
              <option value=-1 disabled>Seleccionar</option>
              <option value=1>Banner</option>
              <option value=2>Fila de libros</option>
            </select>
            <div v-if="this.addSectionValues.frontType == 1" style="margin-top: 2em">
              <h3 class="card-subtitle">Configuración del banner</h3>
              <h5 style="margin-top: 1em">Tipo de fondo del banner*</h5>
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
              <div v-if="this.addBackgroundType==1" style="margin-top: 0.5em">
                <h5>URL imagen*</h5>
                <input class="form-control" type="text" v-model="this.addSectionValues.t1BackgndURL">
              </div>
              <div v-if="this.addBackgroundType==2" style="margin-top: 0.5em">
                <h5>Color*</h5>
                <input type="color" v-model="this.addSectionValues.t1BackgnCOL">
              </div>
              <div style="margin-top: 0.5em" v-if="this.addBackgroundType != -1">
                <h5>Título</h5>
                <input class="form-control" type="text" v-model="this.addSectionValues.t1Tit">
              </div>
              <div style="margin-top: 0.5em" v-if="this.addBackgroundType != -1">
                <h5>Subtítulo</h5>
                <input class="form-control" type="text" v-model="this.addSectionValues.t1Sub">
              </div>
              <div style="margin-top: 0.5em" v-if="this.addBackgroundType != -1">
                <h5>Tercera línea</h5>
                <input class="form-control" type="text" v-model="this.addSectionValues.t1Smalll">
              </div>
              <div style="margin-top: 0.5em" v-if="this.addBackgroundType != -1">
                <h5>Enlace del banner</h5>
                <input class="form-control" type="text" v-model="this.addSectionValues.t1LinkTo">
              </div>
            </div>
            <div v-if="this.addSectionValues.frontType == 2" style="margin-top: 2em">
              <h3 class="card-subtitle">Configuración de la fila</h3>
              <div style="margin-top: 0.5em">
                <h5>Título*</h5>
                <input class="form-control" type="text" v-model="this.addSectionValues.t2RowTitle">
                <h5 style="margin-top: 1em">Número de filas*</h5>
                <div>
                  <div class="form-check form-check-inline">
                    <input class="form-check-input" type="radio" value=3 v-model="this.addSectionValues.t2RowNumber"
                           @input="purgeSelectedBooks()">
                    <label class="form-check-label">3</label>
                  </div>
                  <div class="form-check form-check-inline">
                    <input class="form-check-input" type="radio" value=4 v-model="this.addSectionValues.t2RowNumber"
                           @input="purgeSelectedBooks()">
                    <label class="form-check-label">4</label>
                  </div>
                  <div class="form-check form-check-inline">
                    <input class="form-check-input" type="radio" value=5 v-model="this.addSectionValues.t2RowNumber"
                           @input="purgeSelectedBooks()">
                    <label class="form-check-label">5</label>
                  </div>
                </div>
                <div v-if="this.addSectionValues.t2RowNumber">
                  <h5 style="margin-top: 1em">Libros a mostrar*</h5>
                  <select class="form-control" v-model="this.addSectionValues.t2BookMode">
                    <option value=1>Más vendidos</option>
                    <option value=2>Precio ascendente</option>
                    <option value=3>Precio descendente</option>
                    <option value=0>Selección manual</option>
                  </select>
                  <div v-if="this.addSectionValues.t2BookMode == 0">
                    <div class="row" style="margin-bottom: 1em">
                      <div class="col">
                        <h5 style="margin-top: 1.2em">Selecciona {{ addSectionValues.t2RowNumber }} libros* <span
                            v-if="addSectionValues.t2RowNumber - this.countSelBooks > 0">({{
                            parseInt(addSectionValues.t2RowNumber) - this.countSelBooks
                          }} restante<span
                              v-if="parseInt(addSectionValues.t2RowNumber) - this.countSelBooks != 1">s</span>)</span>
                        </h5>
                      </div>
                      <div class="col">
                        <select class="form-control pull-right"
                                @change="this.getBooksFromDBSelector($event.target.value)"
                                style="margin-top: 1em; width: auto">
                          <option value="TODO">Todo</option>
                          <option value="HUMANIDADES">Humanidades</option>
                          <option value="TECNICO Y FORMACION">Técnico y formación</option>
                          <option value="METODOS DE IDIOMAS">Métodos de idiomas</option>
                          <option value="LITERATURA">Literatura</option>
                          <option value="INFANTIL">Infantil</option>
                          <option value="COMICS Y MANGA">Cómics y manga</option>
                          <option value="JUVENIL">Juvenil</option>
                          <option value="OTRAS CATEGORIAS">Otras categorías</option>
                        </select>
                      </div>
                    </div>
                    <div class="card" style="height: 30em; overflow-y: auto">
                      <div class="row row-cols-1 row-cols-md-5" style="margin-left: 0.1em; margin-right: 0.1em">
                        <div :class="this.getSelBookClassName(item.id)" style="width: 20em; margin: 0.5em"
                             v-for="item in this.booksSelector"
                             :key="item.id" :id="item.id" @click="selectBook(item.id)">
                          <div class="card-body">
                            <h5 class="card-title">{{ item.name }}</h5>
                            <h6 class="card-subtitle mb-2 text-muted">{{ item.author[0] }}</h6>
                            <span class="badge badge-secondary" v-if="item.genre=='LITERATURA'">Literatura</span>
                            <span class="badge badge-secondary" v-if="item.genre=='TECNICO Y FORMACION'">Técnico y formación</span>
                            <span class="badge badge-secondary" v-if="item.genre=='METODOS DE IDIOMAS'">Métodos de idiomas</span>
                            <span class="badge badge-secondary" v-if="item.genre=='HUMANIDADES'">Humanidades</span>
                            <span class="badge badge-secondary" v-if="item.genre=='INFANTIL'">Infantil</span>
                            <span class="badge badge-secondary"
                                  v-if="item.genre=='COMICS Y MANGA'">Cómics y manga</span>
                            <span class="badge badge-secondary" v-if="item.genre=='JUVENIL'">Juvenil</span>
                            <span class="badge badge-secondary"
                                  v-if="item.genre=='OTRAS CATEGORIAS'">Otras categorías</span>
                            &nbsp;
                            <span class="badge badge-info">Stock: {{ item.total_available }}</span>&nbsp;
                            <span class="badge badge-success">Ventas: {{ item.num_sales }}</span>&nbsp;
                            <span class="badge badge-dark">{{ item.price }}€</span>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {api} from "@/main";
import axios from "axios";
import 'verte/dist/verte.css'

export default {
  name: 'Front',
  props: {
    logged: Boolean,
    token: String,
    id: Number,
    type: Number
  },
  created() {
    scrollTo(0, 0)
    this.getBooksFromDBSelector('TODO')
  },
  data() {
    return {
      addBackgroundType: -1,
      edit: false,
      loggedIn: false,
      idEditingSection: -1,
      addSectionValues: {
        frontType: -1,
        t2BookMode: -1,
        t1BackgndURL: '',
        t1BackgnCOL: '',
        t1LinkTo: '',
        t1Tit: '',
        t1Separator: false,
        t1Sub: '',
        t1Smalll: '',
        t2RowTitle: '',
        t2RowNumber: -1,
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
          t1Separator: true,
          t1Sub: 'Esto es un sub',
          t1Smalll: 'Letra peq',
          t2RowTitle: '',
          t2RowNumber: '-1',
          t2BookMode: -1,
          books: []
        },
        {
          id: 2,
          frontType: 1,
          t1BackgndURL: 'https://w.wallhaven.cc/full/x1/wallhaven-x1kd1d.jpg',
          t1BackgnCOL: '#2bc4ed',
          t1LinkTo: '',
          t1Tit: 'Rebajas!',
          t1Separator: false,
          t1Sub: 'Esto es un sub',
          t1Smalll: 'Letra peq',
          t2RowTitle: '',
          t2RowNumber: '-1',
          t2BookMode: -1,
          books: []
        },
        {
          id: 3,
          frontType: 2,
          t1BackgndURL: '',
          t1BackgnCOL: '',
          t1LinkTo: '',
          t1Tit: '',
          t1Separator: false,
          t1Sub: '',
          t1Smalll: '',
          t2RowTitle: 'Prueba',
          t2RowNumber: '6',
          t2BookMode: 0,
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
      booksRM: [],
      booksSelector: [],
      countSelBooks: 0,
      selectedBooks: []
    }
  }, methods: {
    purgeSelectedBooks() {
      Array.from(document.getElementsByClassName('card selected-book')).forEach((el) => el.classList.remove('selected-book'))
      this.countSelBooks = 0
      this.selectedBooks = []
    },
    canSectionBeSaved() {
      if (this.addSectionValues.frontType == 1) {
        if (this.addBackgroundType == 1) {
          if (this.addSectionValues.t1BackgndURL == '') {
            return !false
          } else {
            return !true
          }
        } else if (this.addBackgroundType == 2) {
          if (this.addSectionValues.t1BackgnCOL == '') {
            return !false
          } else {
            return !true
          }
        }
      } else if (this.addSectionValues.frontType == 2) {
        if (parseInt(this.addSectionValues.t2RowNumber) >= 3 && parseInt(this.addSectionValues.t2RowNumber) <= 5 && this.addSectionValues.t2RowTitle != '') {
          if (this.addSectionValues.t2BookMode == 0 && this.selectedBooks.length == parseInt(this.addSectionValues.t2RowNumber)) {
            return !true
          } else if (this.addSectionValues.t2BookMode >= 1 && this.addSectionValues.t2BookMode <= 3) {
            return !true
          }
          return !false
        }
      }
      return !false
    },
    moveUp(id){
      console.log(id)
    },
    moveDown(id){
      console.log(id)
    },
    selectBook(id) {
      let div = document.getElementById(id)
      if (div.classList.contains("selected-book")) {
        div.classList.remove("selected-book")
        this.countSelBooks -= 1
        this.selectedBooks.splice(this.selectedBooks.indexOf(id), 1)
      } else {
        if (parseInt(this.addSectionValues.t2RowNumber) > this.countSelBooks) {
          this.countSelBooks += 1
          this.selectedBooks.push(id)
          div.classList.add("selected-book")
        }
      }
      console.log(this.selectedBooks)
    }
    ,
    getSelBookClassName(id) {
      if (this.selectedBooks.includes(id))
        return "card selected-book"
      else
        return "card"
    }
    ,
    discardChanges() {
      this.edit = false
      this.idEditingSection = -1
    }
    ,
    editSection(id) {
      this.idEditingSection = id
      this.edit = true
    }
    ,
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
    }
    ,
    saveSection() {
      this.edit = false
      this.idEditingSection = -1
    }
    ,
    deleteSection(id) {
      console.log(id)
    }
    ,
    getRowClassName(rows) {
      return "row row-cols-1 row-cols-sm-" + String(rows)
    }
    ,
    compare(a, b) {
      if (a.num_sales < b.num_sales)
        return 1;
      if (a.num_sales > b.num_sales)
        return -1;
      return 0;
    }
    ,
    getYear() {
      return new Date().getFullYear()
    }
    ,
    // eslint-disable-next-line no-unused-vars
    getBooksFromDBSelector(req) {
      var path = api + 'books/' + req
      if (req === 'TODO') {
        path = api + 'books'
      }
      axios.get(path)
          .then((res) => {
            this.booksSelector = res.data.books
          })
          .catch((error) => {
            console.log(error) //
          })
    }
    ,
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

.selected-book {
  border-color: black;
  border-width: 0.2em;
}

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
