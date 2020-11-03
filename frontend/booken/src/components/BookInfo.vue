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
    <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">

    <div class="container">
      <div class="card" style="margin-top: 1em">
        <div class="card-body" style="text-align: left">
          <div class="row row-cols-1 row-cols-md-2">
            <div class="col">
              <h1 class="card-title" v-if="book_found"><p class="bookTitle">{{ bookInfo.name }}</p></h1>
              <h3 class="card-subtitle" style="margin-bottom: 1em" v-if="book_found">{{ bookInfo.author }}</h3>
            </div>
            <div class="col" style="text-align: right">
              <h1 class="card-title" v-if="book_found"><p class="bookTitle" style="text-align: right !important">
                {{ this.replaceDecimal(bookInfo.price) }}€</p></h1>
              <button class="btn btn-warning my-2 my-sm-0 mr-2" type="submit"
                      v-if="admin"><i class="fas fa-edit" style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
                  class="navbartextbt">Editar</a></button>
            </div>
          </div>
          <div class="col" v-if="book_found">
            <div class="row">
              <div ref="images" class="col" style="margin-bottom: 2rem">
                <div style="display:flex; flex-direction: row">
                  <div style="display:flex; flex-direction: column">
                    <img ref="pic1" class="sel-picture" :src="bookInfo.cover_image_url" @click="changeImage(1)">
                    <img ref="pic2" class="sel-picture" :src="bookInfo.back_cover_image_url" @click="changeImage(2)">
                  </div>
                  <div style="margin-left:auto; margin-right:auto">
                    <img ref="bigPic" class="animate__animated animate__zoomIn" id="displayPic" style="max-height: 20em"
                         :src="bookInfo.cover_image_url">
                    <img ref="bigPic" class="animate__animated animate__zoomIn" id="displayPic2"
                         style="max-height: 20em; display: none" :src="bookInfo.back_cover_image_url">
                  </div>
                </div>
              </div>
              <div class="col-sm">
                <div class="row">
                  <div class="col-sm">
                    <p ref="label_summary" class="label-info-selected" @click="change_info('summary')">Sinopsis</p>
                  </div>
                  <div class="col-sm">
                    <p ref="label_details" class="label-info-not-selected" @click="change_info('details')">Detalles</p>
                  </div>
                </div>
                <div style="text-align:left" v-if="showSummary" class="animate__animated animate__fadeIn">
                  <p>{{ bookInfo.synopsis }}</p>
                </div>
                <div style="text-align:left" class="animate__animated animate__fadeIn" v-else>
                  <table class="table table-striped">
                    <tbody>
                    <tr>
                      <th scope="row">Editorial</th>
                      <td>{{ bookInfo.editorial }}</td>
                    </tr>
                    <tr>
                      <th scope="row">Año de publicación</th>
                      <td>{{ bookInfo.year }}</td>
                    </tr>
                    <tr>
                      <th scope="row">Género</th>
                      <td>{{ this.toLowercase(bookInfo.genre )}}</td>
                    </tr>
                    <tr>
                      <th scope="row">Número de páginas</th>
                      <td>{{bookInfo.num_pages}}</td>
                    </tr>
                    <tr>
                      <th scope="row">Formato</th>
                      <td v-if="bookInfo.cover_type == 0">Tapa dura</td>
                      <td v-if="bookInfo.cover_type == 1">Tapa blanda</td>
                    </tr>
                    <tr>
                      <th scope="row">ISBN</th>
                      <td>{{bookInfo.isbn}}</td>
                    </tr>
                    </tbody>
                  </table>
                </div>
              </div>
              <div style="text-align: right">
                <button class="btn my-2 my-sm-0 mr-2" style="background-color: #3b494d" type="submit"
                        v-if="bookInfo.available > 0"><a
                    class="navbartextbt">Añadir a la cesta</a></button>
                <button class="btn my-2 my-sm-0 mr-2" style="background-color: #3b494d" type="submit"
                        v-if="bookInfo.available <= 0" disabled><a
                    class="navbartextbt">Agotado</a></button>
                <button class="btn my-2 my-sm-0 mr-2" style="background-color: #3b494d" type="submit"><a
                    class="navbartextbt">Añadir a lista de deseos</a></button>
              </div>
            </div>

          </div>

          <div class="col" v-else style="text-align: center">
            <h1>No se ha encontrado el libro</h1>
            <img style="width: 50%; margin-top: 2rem" class="animate__animated animate__tada  animate__infinite"
                 src="https://www.pinclipart.com/picdir/big/160-1604750_sad-cloud-icon-clipart.png">
          </div>
        </div>
      </div>
      <div class="card" style="text-align: left; margin-top: 1rem; margin-bottom: 1rem" v-if="book_found">
        <div class="card-body">
          <div class="row row-cols-1 row-cols-md-2">
            <div class="col">
              <h2 class="card-title">Reseñas de los usuarios</h2>
            </div>
            <div class="col" style="text-align: right">
              <button class="btn my-2 my-sm-0 mr-2" style="background-color: #3b494d" type="submit">
                <i class="fa fa-pencil" style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
                  class="navbartextbt">Escribir reseña</a>
              </button>
            </div>
          </div>
          <div class="card" style="width: auto; margin-top: 0.5em">
            <div class="card-header">
              Miguel C. — 11 de marzo de 2020
            </div>
            <div class="card-body">
              <h5 class="card-title"><b>¡Me ha encantado!</b></h5>
              <h6 class="card-subtitle" style="margin-top: 1em">Valoración</h6>
              <div style="margin-left: 0.1em">
                <span class="fa fa-star" style="color: orange"></span>
                <span class="fa fa-star" style="color: orange"></span>
                <span class="fa fa-star" style="color: orange"></span>
                <span class="fa fa-star" style="color: orange"></span>
                <span class="fa fa-star" style="color: orange"></span>
              </div>
              <h6 class="card-subtitle" style="margin-top: 10px">Comentario</h6>
              <p class="card-text">
                Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the
                industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and
                scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap
                into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the
                release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing
                software like Aldus PageMaker including versions of Lorem Ipsum.
              </p>
            </div>
          </div>
          <div class="card" style="width: auto; margin-top: 0.5em">
            <div class="card-header">
              Miguel C. — 11 de marzo de 2020
            </div>
            <div class="card-body">
              <h5 class="card-title"><b>¡Me ha encantado!</b></h5>
              <h6 class="card-subtitle" style="margin-top: 1em">Valoración</h6>
              <div style="margin-left: 0.1em">
                <span class="fa fa-star" style="color: orange"></span>
                <span class="fa fa-star" style="color: orange"></span>
                <span class="fa fa-star" style="color: orange"></span>
                <span class="fa fa-star" style="color: orange"></span>
                <span class="fa fa-star" style="color: orange"></span>
              </div>
              <h6 class="card-subtitle" style="margin-top: 10px">Comentario</h6>
              <p class="card-text">
                Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the
                industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and
                scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap
                into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the
                release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing
                software like Aldus PageMaker including versions of Lorem Ipsum.
              </p>
            </div>
          </div>
        </div>
        <button class="btn my-2 my-sm-0 mr-2"
                style="background-color: #3b494d; width: 100%; border-top-left-radius: 0px; border-top-right-radius: 0px"
                type="submit">
          <a class="navbartextbt">Cargar más</a>
        </button>
      </div>
      <div class="card" style="text-align: left; margin-top: 1rem; margin-bottom: 2rem">
        <div class="card-body">
          <h2 class="card-title">Te recomendamos</h2>
          <div class="row row-cols-1 row-cols-md-4">
            <div class="col mb-4">
              <div class="card h-100">
                <img
                    src="https://www.planetadelibros.com/usuaris/libros/fotos/270/m_libros/portada_el-cuarto-mono_julio-hermoso-oliveras_201803221718.jpg"
                    class="card-img-top" alt="...">
                <div class="card-body">
                  <h6 class="card-subtitle">J. D. Barker</h6>
                  <h4 class="card-title"><a href="">El Cuarto Mono</a></h4>
                </div>
              </div>
            </div>
            <div class="col mb-4">
              <div class="card h-100">
                <img
                    src="https://www.planetadelibros.com/usuaris/libros/fotos/270/m_libros/portada_el-cuarto-mono_julio-hermoso-oliveras_201803221718.jpg"
                    class="card-img-top" alt="...">
                <div class="card-body">
                  <h6 class="card-subtitle">J. D. Barker</h6>
                  <h4 class="card-title"><a href="">El Cuarto Mono</a></h4>
                </div>
              </div>
            </div>
            <div class="col mb-4">
              <div class="card h-100">
                <img
                    src="https://www.planetadelibros.com/usuaris/libros/fotos/270/m_libros/portada_el-cuarto-mono_julio-hermoso-oliveras_201803221718.jpg"
                    class="card-img-top" alt="...">
                <div class="card-body">
                  <h6 class="card-subtitle">J. D. Barker</h6>
                  <h4 class="card-title"><a href="">El Cuarto Mono</a></h4>
                </div>
              </div>
            </div>
            <div class="col mb-4">
              <div class="card h-100">
                <img
                    src="https://www.planetadelibros.com/usuaris/libros/fotos/270/m_libros/portada_el-cuarto-mono_julio-hermoso-oliveras_201803221718.jpg"
                    class="card-img-top" alt="...">
                <div class="card-body">
                  <h6 class="card-subtitle">J. D. Barker</h6>
                  <h4 class="card-title"><a href="">El Cuarto Mono</a></h4>
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

let api = 'https://booken-dev.herokuapp.com/'
export default {
  name: 'BookInfo',

  props: {
    msg: String
  },

  created() {
    this.logged = this.$route.query.logged
    this.is_admin = this.$route.query.is_admin
    this.token = this.$route.query.token
    this.book_id = this.$route.query.id

    this.initBookInfo()
  },

  data() {
    return {

      book_found: 0,
      book_id: 0,
      admin: 0,

      bookInfo: {
        name: 'NameTest',
        author: 'AuthorTest',
        genre: 'GenreTest',
        year: 0,
        editorial: 'EditorialTest',
        language: 'LenguageTest',
        available: 10,
        price: 0,
        isbn: 0,
        num_pages: 0,
        cover_type: 0,
        cover_image_url: '',
        back_cover_image_url: '',
        synopsis: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        cover: 'https://static.fnac-static.com/multimedia/Images/ES/NR/22/0f/18/1576738/1507-1.jpg',
        back_cover: 'https://images-na.ssl-images-amazon.com/images/I/71XhS2XgMxL.jpg',
      },

      showSummary: 1

    }
  },
  methods: {
    toPrint(toPrint) {
      console.log(toPrint)
    },

    initBookInfo() {
      var path = api + 'book/' + this.$route.params.id

      axios.get(path)
          .then((res) => {
            console.log('lel')
            this.book_found = 1
            this.bookInfo.name = res.data.book.name
            this.bookInfo.author = res.data.book.author[0]
            this.bookInfo.genre = res.data.book.genre
            this.bookInfo.year = res.data.book.year
            this.bookInfo.editorial = res.data.book.editorial
            this.bookInfo.language = res.data.book.language
            this.bookInfo.price = res.data.book.price
            this.bookInfo.isbn = res.data.book.ISBN
            this.bookInfo.cover_image_url = res.data.book.cover_image_url
            this.bookInfo.num_pages = res.data.book.num_pages
            this.bookInfo.back_cover_image_url = res.data.book.back_cover_image_url
            this.bookInfo.synopsis = res.data.book.synopsis
          })
          .catch((error) => {
            this.toPrint(error)
          })
    },
    replaceDecimal(stg) {
      return stg.replace(',', '.')
    },
    toLowercase(stg) {
      return stg.replace(/\S*/g, function (word) {
        return word.charAt(0) + word.slice(1).toLowerCase();
      });
    },
    getBooksFromDB(req) {
      var path = api + 'books/' + req
      if (req === 'TODO') {
        path = api + 'books'
      }
      axios.get(path)
          .then((res) => {
            this.books = res.data.books
          })
          .catch((error) => {
            this.toPrint(error)
          })
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
    },

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