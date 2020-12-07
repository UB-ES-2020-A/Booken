<style>

@import url("../assets/toastr.css");
@import url("../assets/animate.min.css");
@import url("../assets/book_info.css");

</style>
<template>
  <div>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
          integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">

    <div class="container">
      <div class="card" style="margin-top: 1em">
        <div class="card-body" style="text-align: left">
          <!-- Book title and author -->
          <div class="row row-cols-1 row-cols-md-2">
            <div class="col" v-if="book_found">
              <h1 class="card-title" v-if="book_found && !edit"><p class="bookTitle">{{ bookInfo.name }}</p></h1>
              <h1 class="card-title" v-if="edit"><input class="form-control" type="text" v-model="bookInfo.name"
                                                        style="font-size: 52px" placeholder="Título del libro"></h1>
              <h3 class="card-subtitle" style="margin-bottom: 1em" v-if="book_found && !edit">{{
                  bookInfo.author
                }}</h3>
              <select class="form-control" v-model="bookInfo.author" v-if="edit" style="margin-bottom: 1em">
                <option value=-1>Selecciona autor</option>
                <option v-for="(a) in this.authors" :key="a.id" :selected="bookInfo.author == a.name" :value=a.name>
                  {{ a.name }}
                </option>
                <option value=0>Otro autor/a</option>
              </select>
              <div v-if="bookInfo.author == 0" style="margin-bottom: 1em">
                <input class="form-control" type="text" v-model="nAutor.name" placeholder="Nombre del autor"
                       style="margin-top: 0.5em">
                <input class="form-control" type="date" v-model="nAutor.birth_date" placeholder="Fecha nacimiento"
                       style="margin-top: 0.5em" title="Fecha de nacimiento">
                <input class="form-control" type="text" v-model="nAutor.country" placeholder="País"
                       style="margin-top: 0.5em">
                <input class="form-control" type="text" v-model="nAutor.city" placeholder="Ciudad del autor"
                       style="margin-top: 0.5em">
              </div>
            </div>
            <div class="col" style="text-align: right; margin-bottom: 1em" v-if="book_found">
              <h1 class="card-title" v-if="book_found && !edit"><p class="bookTitle"
                                                                   style="text-align: right !important">
                {{ this.replaceDecimal(bookInfo.price) }}€</p></h1>
              <h1 class="card-title" v-if="book_found && edit"><p class="bookTitle"
                                                                  style="text-align: right !important">
                <input class="form-control" type="text" v-model="bookInfo.price"
                       style="font-size: 28px; max-width: 140px; text-align: right !important"
                       placeholder="Precio (sin el €)"></p></h1>
              <button class="btn btn-warning my-2 my-sm-0 mr-2" type="submit"
                      v-if="type == 2 && !edit" @click="editInfo"><i class="fas fa-edit"
                                                                     style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
                  class="navbartextbt">Editar</a></button>
              <button class="btn btn-warning my-2 my-sm-0 mr-2" type="submit"
                      v-if="edit"><i class="fas fa-save" style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
                  class="navbartextbt" @click="saveChanges">Guardar</a></button>
            </div>
          </div>
          <!-- Book images/found -->
          <div class="col" v-if="book_found">
            <div class="row">
              <div ref="images" class="col" style="margin-bottom: 2rem">
                <div style="display:flex; flex-direction: row">
                  <div style="display:flex; flex-direction: column">
                    <img ref="pic1" class="sel-picture" :src="bookInfo.cover_image_url" @click="changeImage(1)"
                         v-if="bookInfo.cover_image_url != ''">
                    <img ref="pic1" class="sel-picture" src="https://i.ibb.co/jkbth7h/Portada-no-disponible.png"
                         v-if="bookInfo.cover_image_url == ''">
                    <img ref="pic2" class="sel-picture" :src="bookInfo.back_cover_image_url" @click="changeImage(2)"
                         v-if="bookInfo.back_cover_image_url != ''">
                  </div>
                  <div style="margin-left:auto; margin-right:auto">
                    <img ref="bigPic" class="animate__animated animate__zoomIn" id="displayPic" style="max-height: 20em"
                         :src="bookInfo.cover_image_url" v-if="bookInfo.cover_image_url != ''">
                    <img ref="bigPic" class="animate__animated animate__zoomIn" style="max-height: 20em"
                         src="https://i.ibb.co/jkbth7h/Portada-no-disponible.png" v-if="bookInfo.cover_image_url == ''"
                         id="displayPic3">
                    <img ref="bigPic" class="animate__animated animate__zoomIn" id="displayPic2"
                         style="max-height: 20em; display: none" :src="bookInfo.back_cover_image_url"
                         v-if="bookInfo.back_cover_image_url != ''">
                  </div>
                </div>
              </div>
              <div class="col-sm">
                <div class="row">
                  <div class="col-6">
                    <p ref="label_summary" class="label-info-selected" @click="change_info('summary')">Sinopsis</p>
                  </div>
                  <div class="col-6">
                    <p ref="label_details" class="label-info-not-selected" @click="change_info('details')">Detalles</p>
                  </div>
                </div>
                <div style="text-align:left" v-if="showSummary" class="animate__animated animate__fadeIn">
                  <p v-if="!edit">{{ bookInfo.synopsis }}</p>
                  <textarea class="form-control" rows="8" v-if="edit" v-model="bookInfo.synopsis"></textarea>
                </div>
                <div style="text-align:left" class="animate__animated animate__fadeIn" v-else>
                  <table class="table table-striped">
                    <tbody>
                    <tr>
                      <th scope="row">Editorial</th>
                      <td v-if="!edit">{{ bookInfo.editorial }}</td>
                      <td v-if="edit"><input class="form-control" v-model="bookInfo.editorial"></td>
                    </tr>
                    <tr>
                      <th scope="row">Año de publicación</th>
                      <td v-if="!edit">{{ bookInfo.year }}</td>
                      <td v-if="edit"><input class="form-control" type="number" maxlength=4 v-model="bookInfo.year">
                      </td>
                    </tr>
                    <tr>
                      <th scope="row">Género</th>
                      <td v-if="!edit && bookInfo.genre =='TECNICO Y FORMACION'">Técnico y formación</td>
                      <td v-else-if="!edit && bookInfo.genre =='METODOS DE IDIOMAS'">Métodos de idiomas</td>
                      <td v-else-if="!edit && bookInfo.genre == 'OTRAS CATEGORIAS'">Otras categorías</td>
                      <td v-else-if="!edit && bookInfo.genre == 'COMICS Y MANGA'">Cómics y manga</td>
                      <td v-else-if="!edit">{{ this.toLowercase(bookInfo.genre) }}</td>
                      <td v-if="edit">
                        <select class="form-control" v-model="bookInfo.genre">
                          <option value="">Seleccione género</option>
                          <option :selected="bookInfo.genre == 'HUMANIDADES'" value="HUMANIDADES">Humanidades</option>
                          <option :selected="bookInfo.genre == 'TECNICO Y FORMACION'" value="TECNICO Y FORMACION">
                            Técnico
                            y formación
                          </option>
                          <option :selected="bookInfo.genre == 'METODOS DE IDIOMAS'" value="METODOS DE IDIOMAS">Métodos
                            de
                            idiomas
                          </option>
                          <option :selected="bookInfo.genre == 'LITERATURA'" value="LITERATURA">Literatura</option>
                          <option :selected="bookInfo.genre == 'INFANTIL'" value="INFANTIL">Infantil</option>
                          <option :selected="bookInfo.genre == 'COMICS Y MANGA'" value="COMICS Y MANGA">Cómics y manga
                          </option>
                          <option :selected="bookInfo.genre == 'JUVENIL'" value="JUVENIL">Juvenil</option>
                          <option :selected="bookInfo.genre == 'OTRAS CATEGORIAS'" value="OTRAS CATEGORIAS">Otras
                            categorías
                          </option>
                        </select>
                      </td>
                    </tr>
                    <tr>
                      <th scope="row">Número de páginas</th>
                      <td v-if="!edit">{{ bookInfo.num_pages }}</td>
                      <td v-if="edit"><input class="form-control" v-model="bookInfo.num_pages" type="number"></td>
                    </tr>
                    <tr>
                      <th scope="row">Formato</th>
                      <td v-if="bookInfo.cover_type == 0 && !edit">Tapa dura</td>
                      <td v-if="bookInfo.cover_type == 1 && !edit">Tapa blanda</td>
                      <td v-if="edit">
                        <select class="form-control">
                          <option :selected="bookInfo.cover_type == -1">Seleccione formato</option>
                          <option :selected="bookInfo.cover_type == 0" value=0>Tapa dura</option>
                          <option :selected="bookInfo.cover_type == 1" value=1>Tapa blanda</option>
                        </select>
                      </td>
                    </tr>
                    <tr>
                      <th scope="row">ISBN</th>
                      <td v-if="!edit">{{ bookInfo.isbn }}</td>
                      <td v-if="edit"><input class="form-control" v-model="bookInfo.isbn" type="number" maxlength="13">
                      </td>
                    </tr>

                    <tr v-if="edit">
                      <th scope="row">Descripción corta</th>
                      <td><textarea class="form-control" rows="3" v-model="bookInfo.desc"></textarea></td>
                    </tr>
                    <tr v-if="edit">
                      <th scope="row">Unidades stock</th>
                      <td><input class="form-control" v-model="bookInfo.available" type="number"></td>
                    </tr>
                    <tr v-if="edit">
                      <th scope="row">Unidades vendidas</th>
                      <td><input class="form-control" v-model="bookInfo.num_sales" type="number"></td>
                    </tr>
                    <tr v-if="edit">
                      <th scope="row">URL portada</th>
                      <td><input class="form-control" v-model="bookInfo.cover_image_url"></td>
                    </tr>
                    <tr v-if="edit">
                      <th scope="row">URL contraportada</th>
                      <td><input class="form-control" v-model="bookInfo.back_cover_image_url"
                                 :disabled="bookInfo.cover_image_url == ''"
                                 title="Pon la portada antes de la contraportada."></td>
                    </tr>
                    </tbody>
                  </table>
                </div>
              </div>
              <div style="text-align: right" v-if="!edit">
                <button class="btn my-2 my-sm-0 mr-2" style="background-color: #3b494d" type="submit"
                        v-if="bookInfo.available > 0"><a
                    class="navbartextbt" @click="addToCart(bookInfo)">Añadir a la cesta</a></button>
                <button class="btn my-2 my-sm-0 mr-2" style="background-color: #3b494d" type="submit"
                        v-if="bookInfo.available <= 0" disabled><a
                    class="navbartextbt" v-if="!edit">Agotado</a></button>
                <button class="btn my-2 my-sm-0 mr-2" style="background-color: #3b494d" type="submit"><a
                    class="navbartextbt" v-if="!edit" @click="addToWishList(bookInfo)">Añadir a lista de deseos</a>
                </button>
              </div>
            </div>
          </div>
          <!-- Book images/not found -->
          <div class="col" v-else style="text-align: center">
            <h1>No se ha encontrado el libro</h1>
            <img style="width: 50%; margin-top: 2rem" class="animate__animated animate__tada  animate__infinite"
                 src="https://www.pinclipart.com/picdir/big/160-1604750_sad-cloud-icon-clipart.png">
          </div>
        </div>
      </div>
      <div class="card" style="text-align: left; margin-top: 1rem; margin-bottom: 1rem"
           v-if="book_found && book_id != 0">
        <div class="card-body">
          <div class="row row-cols-1 row-cols-md-2">
            <div class="col">
              <h2 class="card-title">Reseñas de los usuarios</h2>
            </div>
            <div class="col" style="text-align: right">
              <button class="btn my-2 my-sm-0 mr-2" style="background-color: #3b494d" type="submit"
                      data-toggle="modal" data-target="#exampleModal" data-whatever="@getbootstrap" v-if="logged">
                <i class="fa fa-pencil" style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
                  class="navbartextbt">Escribir reseña</a>
              </button>

              <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
                   aria-hidden="true">
                <div class="modal-dialog" role="document"
                     style="min-height: calc(100vh - 60px); display: flex;flex-direction: column;justify-content: center;overflow: auto;">
                  <div class="modal-content">
                    <div class="modal-header">
                      <h5 class="modal-title" id="exampleModalLabel">Escribir reseña</h5>
                      <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                      </button>
                    </div>
                    <div class="modal-body">
                      <form>
                        <div class="form-group" style="text-align: left">
                          <label for="reviewTitle" class="col-form-label">Título</label>
                          <input type="text" class="form-control" id="reviewTitle"
                                 v-model="valuationTitle">

                        </div>
                        <div class="form-group" style="text-align: left">
                          <label class="col-form-label">Tu valoración:</label>
                          <div class="valuation" style="margin-left: 0.1em">
                            <span class="fa fa-star" style="color: gray; font-size: 2em" @click="updateStars(1)"
                                  v-if="addvaluationNumber <= 0"></span>
                            <span class="fa fa-star" style="color: orange; font-size: 2em"
                                  @click="updateStars(1)" v-if="addvaluationNumber >= 1"></span>

                            <span class="fa fa-star" style="color: gray; font-size: 2em" @click="updateStars(2)"
                                  v-if="addvaluationNumber <= 1"></span>
                            <span class="fa fa-star" style="color: orange; font-size: 2em"
                                  @click="updateStars(2)" v-if="addvaluationNumber >= 2"></span>

                            <span class="fa fa-star" style="color: gray; font-size: 2em" @click="updateStars(3)"
                                  v-if="addvaluationNumber <= 2"></span>
                            <span class="fa fa-star" style="color: orange; font-size: 2em"
                                  @click="updateStars(3)" v-if="addvaluationNumber >= 3"></span>

                            <span class="fa fa-star" style="color: gray; font-size: 2em" @click="updateStars(4)"
                                  v-if="addvaluationNumber <= 3"></span>
                            <span class="fa fa-star" style="color: orange; font-size: 2em"
                                  @click="updateStars(4)" v-if="addvaluationNumber >= 4"></span>

                            <span class="fa fa-star" style="color: gray; font-size: 2em" @click="updateStars(5)"
                                  v-if="addvaluationNumber <= 4"></span>
                            <span class="fa fa-star" style="color: orange; font-size: 2em"
                                  @click="updateStars(5)" v-if="addvaluationNumber >= 5"></span>
                          </div>
                        </div>
                        <div class="form-group" style="text-align: left">
                          <label for="reviewText" class="col-form-label">Explayate (si quieres 😉):</label>
                          <textarea class="form-control" id="reviewText" rows="5" maxlength="250"
                                    placeholder="¿Qué te ha parecido el libro? ¿A quién se lo recomendarias?"
                                    v-model="valuationText"></textarea>
                          <div id="charNum"></div>
                        </div>
                        <div class="form-group" style="text-align: center">
                          <span class="badge badge-danger animate__animated animate__rubberBand"
                                style="font-size: 1.5em" v-if="valuationText != ''">¡NO NOS HAGAS SPOILER!</span>
                        </div>
                      </form>
                    </div>
                    <div class="modal-footer">
                      <button type="button" class="btn btn-secondary" data-dismiss="modal"
                              @click="addvaluationNumber = 0">
                        Cancelar
                      </button>
                      <button type="button" class="btn" style="background: #2bc4ed; color: white" data-dismiss="modal"
                              @click="postReview"
                              :disabled="valuationTitle == '' || valuationText == '' || addvaluationNumber == 0">
                        Enviar
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="row" v-if="reviews.length > 0">
            <div class="col-12" v-for="(item) in this.viewingReviews" :key="item.user">
              <div class="card" style="width: auto; margin-top: 1em">
                <div class="card-header">
                  <div class="row">
                    <div class="col">
                      {{ item.name }} - {{ item.date }}
                    </div>
                    <div class="col" style="text-align: right">
                      <button v-if="type == 2" class="btn btn-sm btn-danger" style="margin-left: 0.5em"
                              @click="deleteReview(item.id)"><i class="fas fa-trash"></i>
                      </button>
                    </div>
                  </div>
                </div>
                <div class="card-body">
                  <h5 class="card-title"><b>{{ item.title }}</b></h5>
                  <h6 class="card-subtitle" style="margin-top: 1em">Valoración</h6>
                  <div class="Reviewsvaluation" style="margin-left: 0.1em; margin-top: 0.5em">
                  <span class="fa fa-star" style="color: gray; font-size: 2em"
                        v-if="item.valuation <= 0"></span>
                    <span class="fa fa-star" style="color: orange; font-size: 2em"
                          v-if="item.valuation >= 1"></span>
                    <span class="fa fa-star" style="color: gray; font-size: 2em"
                          v-if="item.valuation <= 1"></span>
                    <span class="fa fa-star" style="color: orange; font-size: 2em"
                          v-if="item.valuation >= 2"></span>
                    <span class="fa fa-star" style="color: gray; font-size: 2em"
                          v-if="item.valuation <= 2"></span>
                    <span class="fa fa-star" style="color: orange; font-size: 2em"
                          v-if="item.valuation >= 3"></span>
                    <span class="fa fa-star" style="color: gray; font-size: 2em"
                          v-if="item.valuation <= 3"></span>
                    <span class="fa fa-star" style="color: orange; font-size: 2em"
                          v-if="item.valuation >= 4"></span>
                    <span class="fa fa-star" style="color: gray; font-size: 2em"
                          v-if="item.valuation <= 4"></span>
                    <span class="fa fa-star" style="color: orange; font-size: 2em"
                          v-if="item.valuation >= 5"></span>
                  </div>
                  <h6 class="card-subtitle" style="margin-top: 1em">Comentario</h6>
                  <p class="card-text" style="margin-top: 0.5em">{{ item.comment }}</p>
                </div>
              </div>
            </div>
          </div>
          <div class="row" v-if="reviews.length == 0">
            <div class="col-12 text-center my-5">
              <img src="https://i.ibb.co/kDmqZRz/asd.png" style="object-fit:cover;
  max-width: 100%; ">
            </div>
          </div>
        </div>
        <button class="btn"
                style="background-color: #3b494d; width: 100%; border-top-left-radius: 0px; border-top-right-radius: 0px"
                type="submit"
                @click="changeViewingReviews"
                v-if="this.showing != (this.nPages - 1) && this.reviews.length > 2">
          <a class="navbartextbt">Cargar más</a>
        </button>
        <button class="btn"
                style="background-color: #3b494d; width: 100%; border-top-left-radius: 0px; border-top-right-radius: 0px"
                type="submit"
                @click="changeViewingReviews"
                v-if="this.showing == (this.nPages - 1) && this.reviews.length > 2">
          <a class="navbartextbt">Ver menos</a>
        </button>
      </div>
      <div class="card" style="text-align: left; margin-top: 1rem; margin-bottom: 2rem">
        <div class="card-body">
          <h2 class="card-title">Te recomendamos</h2>
          <div class="row row-cols-1 row-cols-md-4">
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
import axios from 'axios'
import * as toastr from '../assets/toastr.js'
import {bus, api} from '../main.js'

export default {
  name: 'BookInfo',

  props: {
    logged: Boolean,
    token: String,
    id: Number,
    type: Number
  },

  created() {
    scrollTo(0, 0)
    this.is_edit = this.$route.query.is_edit
    this.book_id = this.$route.params.id
    this.initAuthors()
    if (this.book_id == 0) {
      if (this.admin) {
        this.book_found = 1
        this.edit = 1
      }
    } else {
      this.initBookInfo()
      this.getBooksFromDB('TODO')
      this.getReviewsFromDB()
    }
  },

  data() {
    return {
      admin: 1,
      loggedIn: false,
      book_found: 0,
      newAutor: 0,
      addvaluationNumber: 0,
      valuationTitle: '',
      valuationText: '',
      nAutor: {
        id: 0,
        c: '',
        name: '',
        birth_date: '',
        country: '',
        city: ''
      },
      book_id: '0',
      edit: 0,
      authors: [],
      books: [],
      booksRM: [],
      bookInfo: {
        id: 0,
        name: '',
        author_id: -2,
        author: -1,
        genre: '',
        year: '',
        editorial: '',
        language: '',
        available: '',
        price: '',
        num_sales: 0,
        isbn: '',
        desc: '',
        num_pages: '',
        cover_type: -1,
        cover_image_url: '',
        back_cover_image_url: '',
        synopsis: '',
        cover: 'https://static.fnac-static.com/multimedia/Images/ES/NR/22/0f/18/1576738/1507-1.jpg',
        back_cover: 'https://images-na.ssl-images-amazon.com/images/I/71XhS2XgMxL.jpg',
      },
      showSummary: 1,
      showing: 0,
      maxPerPage: 2,
      viewingReviews: [],
      nReviews: 0,
      nPages: 0,
      sReviews: [],
      reviews: []
    }
  },
  methods: {
    deleteReview(id) {
      var path = api + 'review/' + id
      axios.delete(path)
          // eslint-disable-next-line no-unused-vars
          .then((res) => {
            toastr.success('', 'Reseña eliminada',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
            this.getReviewsFromDB()
          })
          .catch((error) => {
            console.log(error)
            toastr.error('', 'No se ha podido borrar la reseña',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
          })
    },
    getReviewsFromDB() {
      var path = api + 'reviewsBook/' + this.$route.params.id
      axios.get(path)
          .then((res) => {
            this.reviews = res.data.reviews
            this.splitReviews()
          })
          .catch((error) => {
            console.log(error)
          })
    },
    changeViewingReviews() {
      if (this.showing == (this.nPages - 1)) {
        this.showing = 0
        this.viewingReviews = this.sReviews[0].slice()
      } else {
        this.showing -= -1
        let item
        for (item in this.sReviews[this.showing]) {
          this.viewingReviews.push(this.sReviews[this.showing][item])
        }
      }
    },
    splitReviews() {
      if (this.reviews.length <= 2) {
        this.viewingReviews = this.reviews
      } else {
        this.nReviews = this.reviews.length
        this.nPages = Math.ceil(this.nReviews / this.maxPerPage)
        let i
        let arr = []
        for (i = 0; i < this.nPages; i++) {
          arr = this.reviews.slice(i * this.maxPerPage, this.maxPerPage * (i + 1))
          this.sReviews.push(arr)
        }
        this.viewingReviews = this.sReviews[0].slice()
      }
    },
    getTodayDate() {
      var today = new Date()
      var dd = String(today.getDate()).padStart(2, '0')
      var mm = String(today.getMonth() + 1).padStart(2, '0')
      var yyyy = today.getFullYear()

      today = dd + '/' + mm + '/' + yyyy
      return today
    },
    postReview() {

      var path = api + 'review'

      axios.post(path, {
        "user_id": this.id,
        "book_id": this.bookInfo.id,
        "title": this.valuationTitle,
        "valuation": this.addvaluationNumber,
        "comment": this.valuationText,
        "date": this.getTodayDate()
      })
          // eslint-disable-next-line no-unused-vars
          .then((res) => {
            toastr.success('', '¡Reseña añadida!',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
            this.getReviewsFromDB()
          })
          .catch((error) => {
            console.log(error)
            toastr.error('', 'No se ha guardar la reseña.',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
          })
    },
    getAuthorId(name) {
      let item
      for (item in this.authors) {
        if (this.authors[item].name == name) {
          return this.authors[item].id
        }
      }
      return -1
    },
    updateStars(index) {
      this.addvaluationNumber = index
    },
    editInfo() {
      if (this.admin) {
        this.edit = 1
      }
    },
    saveChanges() {
      if (this.admin) {
        if (this.bookInfo.isbn == '' || this.bookInfo.name == '' || this.bookInfo.author == '' || this.bookInfo.genre == ''
            || this.bookInfo.year == '' || this.bookInfo.editorial == '' || this.bookInfo.language == '' ||
            this.bookInfo.price == '' || this.bookInfo.synopsis == '' || this.bookInfo.desc == '' || this.bookInfo.num_pages == ''
            || this.bookInfo.cover_type == -1 || this.bookInfo.num_sales.toString() == '' || this.bookInfo.available == '') {
          toastr.info('', 'Por favor, rellena todos los campos.',
              {
                timeOut: 2500,
                progressBar: true,
                newestOnTop: true,
                positionClass: 'toast-bottom-right',
                preventDuplicates: true
              })
          return 0
        }
        if (this.bookInfo.year < 0 || this.bookInfo.price < 0 || this.bookInfo.available < 0 || this.bookInfo.num_sales < 0
            || this.bookInfo.num_pages < 0) {
          toastr.warning('', 'No se admiten valores negativos',
              {
                timeOut: 2500,
                progressBar: true,
                newestOnTop: true,
                positionClass: 'toast-bottom-right',
                preventDuplicates: true
              })
          return 0
        }
        if (this.bookInfo.author == 0) {
          if (this.nAutor.name == '' || this.nAutor.birth_date == '' || this.nAutor.country == '' || this.nAutor.city == '') {
            toastr.info('', 'Por favor, rellena todos los campos.',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
            return 0
          }
        }
        if (!this.isValidIsbn(this.bookInfo.isbn)) {
          toastr.warning('', 'El ISBN introducido no tiene el formato correcto.',
              {
                timeOut: 2500,
                progressBar: true,
                newestOnTop: true,
                positionClass: 'toast-bottom-right',
                preventDuplicates: true
              })
          return 0
        }
        this.edit = 0
        let path
        if (this.bookInfo.cover_image_url == '') {
          this.bookInfo.cover_image_url = 'https://i.ibb.co/jkbth7h/Portada-no-disponible.png'
        }
        if (this.book_id != 0) {
          path = api + 'book/' + this.book_id
          axios.put(path, {
            'author_id': this.getAuthorId(this.bookInfo.author),
            'author_name': this.nAutor.name,
            'author_bd': this.nAutor.birth_date,
            'author_city': this.nAutor.city,
            'author_country': this.nAutor.country,
            'isbn': this.bookInfo.isbn,
            'name': this.bookInfo.name,
            'genre': this.bookInfo.genre,
            'year': this.bookInfo.year,
            'editorial': this.bookInfo.editorial,
            'language': this.bookInfo.language,
            'price': this.bookInfo.price,
            'synopsis': this.bookInfo.synopsis,
            'description': this.bookInfo.desc,
            'num_pages': this.bookInfo.num_pages,
            'cover_type': this.bookInfo.cover_type,
            'num_sales': this.bookInfo.num_sales,
            'total_available': this.bookInfo.available,
            'cover_image_url': this.bookInfo.cover_image_url,
            'back_cover_image_url': this.bookInfo.back_cover_image_url
          })
              // eslint-disable-next-line no-unused-vars
              .then((res) => {
                toastr.success('', '¡Libro actualizado correctamente!',
                    {
                      timeOut: 2500,
                      progressBar: true,
                      newestOnTop: true,
                      positionClass: 'toast-bottom-right',
                      preventDuplicates: true
                    })
              })
              .catch((error) => {
                console.log(error)
                toastr.error('', 'No se ha podido guardar los cambios en el libro.',
                    {
                      timeOut: 2500,
                      progressBar: true,
                      newestOnTop: true,
                      positionClass: 'toast-bottom-right',
                      preventDuplicates: true
                    })
              })
        } else {
          path = api + 'book'
          axios.post(path, {
            'author_id': this.getAuthorId(this.bookInfo.author),
            'author_name': this.nAutor.name,
            'author_bd': this.nAutor.birth_date,
            'author_city': this.nAutor.city,
            'author_country': this.nAutor.country,
            'isbn': this.bookInfo.isbn,
            'name': this.bookInfo.name,
            'genre': this.bookInfo.genre,
            'year': this.bookInfo.year,
            'editorial': this.bookInfo.editorial,
            'language': this.bookInfo.language,
            'price': this.bookInfo.price,
            'synopsis': this.bookInfo.synopsis,
            'description': this.bookInfo.desc,
            'num_pages': this.bookInfo.num_pages,
            'cover_type': this.bookInfo.cover_type,
            'num_sales': this.bookInfo.num_sales,
            'total_available': this.bookInfo.available,
            'cover_image_url': this.bookInfo.cover_image_url,
            'back_cover_image_url': this.bookInfo.back_cover_image_url
          })
              // eslint-disable-next-line no-unused-vars
              .then((res) => {
                toastr.success('', '¡Libro añadido correctamente!',
                    {
                      timeOut: 2500,
                      progressBar: true,
                      newestOnTop: true,
                      positionClass: 'toast-bottom-right',
                      preventDuplicates: true
                    })
              })
              .catch((error) => {
                console.log(error)
                toastr.error('', 'No se ha podido añadir el libro.',
                    {
                      timeOut: 2500,
                      progressBar: true,
                      newestOnTop: true,
                      positionClass: 'toast-bottom-right',
                      preventDuplicates: true
                    })
              })
        }
      }
    },
    isValidIsbn(str) {

      var sum,
          weight,
          digit,
          check,
          i;

      str = str.toString().replace(/[^0-9X]/gi, '');

      if (str.length != 10 && str.length != 13) {
        return false;
      }

      if (str.length == 13) {
        sum = 0;
        for (i = 0; i < 12; i++) {
          digit = parseInt(str[i]);
          if (i % 2 == 1) {
            sum += 3 * digit;
          } else {
            sum += digit;
          }
        }
        check = (10 - (sum % 10)) % 10;
        return (check == str[str.length - 1]);
      }

      if (str.length == 10) {
        weight = 10;
        sum = 0;
        for (i = 0; i < 9; i++) {
          digit = parseInt(str[i]);
          sum += weight * digit;
          weight--;
        }
        check = (11 - (sum % 11)) % 11
        if (check == 10) {
          check = 'X';
        }
        return (check == str[str.length - 1].toUpperCase());
      }
    },
    addToWishList(book) {
      if (this.logged) {
        this.wish_list = []
        var path = api + 'wishlist/' + this.id + '/' + book.id
        axios.post(path)
            // eslint-disable-next-line no-unused-vars
            .then((res) => {
              toastr.success('', 'Añadido a tu lista de deseos.',
                  {
                    timeOut: 2500,
                    progressBar: true,
                    newestOnTop: true,
                    positionClass: 'toast-bottom-right',
                    preventDuplicates: true
                  })
            })
            .catch((error) => {
              console.log(error)
              if (error.response) {
                if (error.response.status == 400) {
                  toastr.info('', 'Este libro ya está a tu lista de deseados.',
                      {
                        timeOut: 2500,
                        progressBar: true,
                        newestOnTop: true,
                        positionClass: 'toast-bottom-right',
                        preventDuplicates: true
                      })
                }
              } else {
                toastr.error('', 'No se ha podido añadir el libro a deseados, intentálo de nuevo más tarde.',
                    {
                      timeOut: 2500,
                      progressBar: true,
                      newestOnTop: true,
                      positionClass: 'toast-bottom-right',
                      preventDuplicates: true
                    })
              }
            })
      } else {
        toastr.info('', 'Debes estar registrado para añadir un libro a deseados.',
            {
              timeOut: 2500,
              progressBar: true,
              newestOnTop: true,
              positionClass: 'toast-bottom-right',
              preventDuplicates: true
            })
      }
    },
    addToCart(book) {
      toastr.success('', 'Libro añadido a tu cesta.',
          {
            timeOut: 2500,
            progressBar: true,
            newestOnTop: true,
            positionClass: 'toast-bottom-right',
            preventDuplicates: true
          })
      bus.emit('added-to-cart', {
        'id': book.id,
        'title': book.name,
        'price': book.price,
        'desc': book.desc,
        'cover': book.cover_image_url,
        'quant': 1,
        'quant_t': book.available
      })
    },
    initAuthors() {
      var path = api + 'authors'

      axios.get(path)
          .then((res) => {
            this.authors = res.data.authors
          })
          .catch((error) => {
            console.log(error)
          })
    }
    ,
    initBookInfo() {
      var path = api + 'book/' + this.$route.params.id

      axios.get(path)
          .then((res) => {
            this.book_found = 1
            this.bookInfo.id = res.data.book.id
            this.bookInfo.name = res.data.book.name
            this.bookInfo.author = res.data.book.author[0]
            this.bookInfo.genre = res.data.book.genre
            this.bookInfo.year = res.data.book.year
            this.bookInfo.editorial = res.data.book.editorial
            this.bookInfo.language = res.data.book.language
            this.bookInfo.price = res.data.book.price
            this.bookInfo.num_sales = res.data.book.num_sales
            this.bookInfo.isbn = res.data.book.ISBN
            this.bookInfo.cover_type = res.data.book.cover_type
            this.bookInfo.desc = res.data.book.description
            this.bookInfo.cover_image_url = res.data.book.cover_image_url
            this.bookInfo.available = res.data.book.total_available
            this.bookInfo.num_pages = res.data.book.num_pages
            this.bookInfo.back_cover_image_url = res.data.book.back_cover_image_url
            this.bookInfo.synopsis = res.data.book.synopsis
          })
          .catch((error) => {
            console.log(error)
          })
    }
    ,
    replaceDecimal(stg) {
      return stg
    }
    ,
    toLowercase(stg) {
      return stg.toString().replace(/\S*/g, function (word) {
        return word.charAt(0) + word.slice(1).toLowerCase();
      })
    }
    ,
    getBooksFromDB(req) {
      var path = api + 'books/' + req
      if (req === 'TODO') {
        path = api + 'books'
      }
      axios.get(path)
          .then((res) => {
            this.books = res.data.books
            this.recommendBooks()
          })
          .catch((error) => {
            console.log(error)
          })
    },
    recommendBooks() {
      var min = 0, max = this.books.length - 1
      var r1 = 0, r2 = 0, r3 = 0, r4 = 0
      while (r1 == r2 || r1 == r3 || r1 == r4 ||
      r2 == r1 || r2 == r3 || r2 == r4 ||
      r3 == r1 || r3 == r2 || r3 == r4 ||
      r4 == r1 || r4 == r2 || r4 == r3) {
        r1 = Math.floor(Math.random() * (max - min + 1) + min)
        r2 = Math.floor(Math.random() * (max - min + 1) + min)
        r3 = Math.floor(Math.random() * (max - min + 1) + min)
        r4 = Math.floor(Math.random() * (max - min + 1) + min)
      }
      this.booksRM.push(this.books[r1])
      this.booksRM.push(this.books[r2])
      this.booksRM.push(this.books[r3])
      this.booksRM.push(this.books[r4])
    },
    changeImage(id_image) {
      if (id_image == 1) {
        document.getElementById('displayPic').style.display = 'block'
        document.getElementById('displayPic2').style.display = 'none'
        /*this.$refs.bigPic.src = this.$refs.pic1.src*/
      } else {
        document.getElementById('displayPic2').style.display = 'block'
        document.getElementById('displayPic').style.display = 'none'
        /*this.$refs.bigPic.src = this.$refs.pic2.src*/
      }
    }
    ,

    change_info(info) {
      if (info == "summary") {
        this.$refs.label_summary.classList = "label-info-selected"
        this.$refs.label_details.classList = "label-info-not-selected"
        this.showSummary = 1
      } else if (info == "details") {
        this.$refs.label_summary.classList = "label-info-not-selected"
        this.$refs.label_details.classList = "label-info-selected"
        this.showSummary = 0
      }
    }
  }
}
</script>