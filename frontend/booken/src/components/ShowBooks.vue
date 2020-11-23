<template>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
        integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
  <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
  <link href='https://fonts.googleapis.com/css?family=Lato' rel='stylesheet' type='text/css'>

  <div class="front-container">
    <div class="container" style="max-width: 1400px">
      <div class="row justify-content-md-between justify-content-sm-start">
        <!-- Set title correctly -->
        <div class="col-12 col-md-6 mr-md-auto my-auto ">
          <h2 v-if="$route.params.category == 'HUMANIDADES'">Humanidades</h2>
          <h2 v-if="$route.params.category == 'TECNICO Y FORMACION'">Técnico y formación</h2>
          <h2 v-if="$route.params.category == 'METODOS DE IDIOMAS'">Métodos de idiomas</h2>
          <h2 v-if="$route.params.category == 'COMICS Y MANGA'">Cómics y manga</h2>
          <h2 v-if="$route.params.category == 'LITERATURA'">Literatura</h2>
          <h2 v-if="$route.params.category == 'JUVENIL'">Juvenil</h2>
          <h2 v-if="$route.params.category == 'INFANTIL'">Infantil</h2>
          <h2 v-if="$route.params.category == 'OTRAS CATEGORIAS'">Otras categorías</h2>
          <h2 v-if="$route.params.category == 'TODO'">Todos los libros</h2>
        </div>
        <!-- Sort by div -->
        <div class="col-12 col-md-6 my-auto filterBox">
          <label>Ordenar por: </label>
          <select name="sortBy" id="sortBy" @change="sortBy(sortType)" v-model="sortType"
                  class="form-control-sm" style="width: 180px; margin-left:10px; margin-right: 0.5em">
            <option v-for="item in sortOptions" :key="item" :selected="sortType == '-1'" :value="item.value">{{ item.text }}</option>
          </select>
          <router-link :to="{name: 'BookInfo', params: {id: 0}}">
            <button class="btn btn-success my-2 my-sm-0 mr-2" type="submit"
                    v-if="this.type == 2" style="margin-left: 1em"><i class="fas fa-plus"
                                                                      style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
                class="navbartextbt">Añadir</a></button>
          </router-link>
        </div>
      </div>
      <hr>
      <div class="row row-cols-1 row-cols-md-5" :key="nbooks">
        <!-- Book card -->
        <div class="col mb-4" v-for="(book) in this.books" :key="book.id">
          <div class="card h-100">
            <img
                :src="book.cover_image_url"
                class="card-img-top" alt="...">
            <div class="card-body">
              <h6 class="card-subtitle">{{ this.joinAuthours(book.author) }}</h6>
              <h4 class="card-title">
                <router-link :to="{name: 'BookInfo', params: {id: book.id}}">{{ book.name }}</router-link>
              </h4>

              <p class="card-text">{{ book.description }}</p>
            </div>
            <div class="card-footer">
              <h4>
                <span class="badge badge-info">{{ book.price }}€</span>&nbsp;
                <span class="badge badge-secondary" v-if="book.genre == 'HUMANIDADES'">Humanidades</span>
                <span class="badge badge-secondary" v-if="book.genre == 'LITERATURA'">Literatura</span>
                <span class="badge badge-secondary"
                      v-if="book.genre == 'TECNICO Y FORMACION'">Técnico y formación</span>
                <span class="badge badge-secondary" v-if="book.genre == 'METODOS DE IDIOMAS'">Métodos de idiomas</span>
                <span class="badge badge-secondary" v-if="book.genre == 'COMICS Y MANGA'">Cómics y manga</span>
                <span class="badge badge-secondary" v-if="book.genre == 'OTRAS CATEGORIAS'">Otras categorías</span>
                <span class="badge badge-secondary" v-if="book.genre == 'INFANTIL'">Infantil</span>
                <span class="badge badge-dark" v-if="book.cover_type == 0">Tapa dura</span>
                <span class="badge badge-dark" v-else-if="book.cover_type == 1">Tapa blanda</span>
                <button v-if="type == 2" class="btn btn-sm btn-danger" style="margin-left: 0.5em"
                        @click="deleteBook(book.id)"><i class="fas fa-times"></i>
                </button>
              </h4>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import * as toastr from "@/assets/toastr";
import {api} from '../main.js'

export default {
  name: "ShowBooks",
  created() {
    this.getBooksFromDB(this.$route.params.category)
  },
  data() {
    return {
      books: [],
      admin: 1,
      nbooks: 0,
      sortType: '-1',
      sortOptions: [
        {text: 'Más vendidos', value: '-1'},
        {text: 'Precio ascendente', value: '0'},
        {text: 'Precio descendente', value: '1'},
      ],
    }
  },
  props: {
    logged: Boolean,
    token: String,
    id: Number,
    type: Number
  },
  computed: {
    ascendArray: function() {
      function compare(a, b) {
        if (a.price < b.price)
          return -1;
        if (a.price > b.price)
          return 1;
        return 0;
      }

      // eslint-disable-next-line vue/no-side-effects-in-computed-properties
      return this.books.sort(compare);
    },
    descendArray: function() {
      function compare(a, b) {
        if (a.price < b.price)
          return 1;
        if (a.price > b.price)
          return -1;
        return 0;
      }

      // eslint-disable-next-line vue/no-side-effects-in-computed-properties
      return this.books.sort(compare);
    },
    freqArray: function() {
      function compare(a, b) {
        if (a.num_sales < b.num_sales)
          return 1;
        if (a.num_sales > b.num_sales)
          return -1;
        return 0;
      }

      // eslint-disable-next-line vue/no-side-effects-in-computed-properties
      return this.books.sort(compare);
    }
  },
  methods: {
    deleteBook(id) {
      var path = api + 'book/' + id
      axios.delete(path)
          // eslint-disable-next-line no-unused-vars
          .then((res) => {
            this.getBooksFromDB(this.$route.params.category)
            toastr.success('', '¡Libro borrado!',
                {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
          })
          .catch((error) => {
            this.toPrint(error)
          })
    },
    joinAuthours(aut) {
      if (aut.length == 1) {
        return aut[0]
      } else {
        var ret = ''
        for (const a in aut) {
          ret += aut[a] + ','
        }
        return ret.slice(0, -1)
      }

    },
    toLowercase(stg) {
      return stg.toString().replace(/\S*/g, function (word) {
        return word.charAt(0) + word.slice(1).toLowerCase()
      })
    },
    getBooksFromDB(req) {
      var path = api + 'books/' + req
      if (req === 'TODO') {
        path = api + 'books'
      }
      axios.get(path)
          .then((res) => {
            this.books = res.data.books
            this.books = this.freqArray
            this.nbooks = this.books.length
          })
          .catch((error) => {
            this.toPrint(error)
          })
    },
    sortBy(type) {
      if (type == "-1") {
        this.freqSort()
      }
      if (type == "0") {
        this.ascendSort()
      }
      if (type == "1") {
        this.descendSort()
      }
    },
    freqSort() {
      this.books = this.freqArray
      console.log(this.books)
    },
    ascendSort() {
      this.books = this.ascendArray
    },
    descendSort() {
      this.books = this.descendArray
    },
  }
}
</script>

<style scoped>

.front-container {
  margin-right: 5%;
  margin-left: 5%;
  margin-top: 50px;
  text-align: left;
}

@media (min-width: 0px) {
  .filterBox {
    margin-top: 15px !important;
  }

  .imgBook {
    height: 100vw;
  }
}

@media (min-width: 576px) {
  .imgBook {
    height: 60vw;
  }
}

@media (min-width: 768px) {
  .filterBox {
    text-align: right;
    margin-top: 0px !important;
  }

  .imgBook {
    height: 32vw;

  }
}

@media (min-width: 992px) {
  .imgBook {
    height: 24vw;
  }
}

@media (min-width: 1600px) {
  .imgBook {
    height: 20vw;
  }
}
</style>