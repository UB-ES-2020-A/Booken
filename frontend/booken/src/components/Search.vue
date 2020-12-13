<template>
  <div class="front-container">
    <div class="container" v-if="this.nbooks >0" style="max-width: 1400px">
      <div class="row justify-content-md-between justify-content-sm-start">
        <div class="col-12 col-md-6 mr-md-auto my-auto" v-if="!this.searching">
          <h2>Resultados de la búsqueda: {{ search }}</h2>
          <hr>
        </div>
      </div>
      <div class="row row-cols-1 row-cols-sm-5" v-if="this.nbooks > 0 && !this.searching" :key="this.nbooks">
        <div class="col mb-4" v-for="book in this.books" :key="book.id">
          <div class="card h-100">
            <img
                :src="book.book.cover_image_url"
                class="card-img-top" alt="...">
            <div class="card-body">
              <h6 class="card-subtitle">{{ book.book.author[0] }}</h6>
              <h4 class="card-title">
                <router-link :to="{name: 'BookInfo', params: {id: book.book.id}}">{{ book.book.name }}</router-link>
              </h4>
              <p class="card-text">{{ book.book.description }}</p>
            </div>
            <div class="card-footer">
              <h4>
                <span class="badge badge-info">{{ book.book.price }}€</span>&nbsp;
                <span class="badge badge-secondary" v-if="book.book.genre == 'HUMANIDADES'">Humanidades</span>
                <span class="badge badge-secondary" v-if="book.book.genre == 'LITERATURA'">Literatura</span>
                <span class="badge badge-secondary"
                      v-if="book.book.genre == 'TECNICO Y FORMACION'">Técnico y formación</span>
                <span class="badge badge-secondary"
                      v-if="book.book.genre == 'METODOS DE IDIOMAS'">Métodos de idiomas</span>
                <span class="badge badge-secondary"
                      v-if="book.book.genre == 'COMICS Y MANGA'">Cómics y manga</span>
                <span class="badge badge-secondary"
                      v-if="book.book.genre == 'OTRAS CATEGORIAS'">Otras categorías</span>
                <span class="badge badge-secondary" v-if="book.book.genre == 'INFANTIL'">Infantil</span>
                <span class="badge badge-dark" v-if="book.book.cover_type == 0">Tapa dura</span>
                <span class="badge badge-dark" v-else-if="book.book.cover_type == 1">Tapa blanda</span>
              </h4>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="col" v-if="this.nbooks <= 0 && this.searching == false" style="text-align: center">
      <h1>No se han encontrado libros para: {{ search }}</h1>
      <img style="width: 25%; margin-top: 2rem" class="animate__animated animate__tada  animate__infinite"
           src="https://www.pinclipart.com/picdir/big/160-1604750_sad-cloud-icon-clipart.png">
    </div>
    <div class="col" v-if="this.searching == true" style="text-align: center">
      <h3>Cargando</h3>
      <div class="spinner-border text-info" role="status" style="width: 5em; height: 5em; margin-top: 0.5em">
      </div>
    </div>
  </div>
</template>

<script>
import {api} from "../main";
import axios from "axios";

export default {
  name: "Search",
  created() {
    this.search = this.$route.query.name
    this.searchBook(this.$route.query.name)
  },
  data() {
    return {
      books: [],
      nbooks: 0,
      search: '',
      searching: true
    }
  },
  methods: {
    searchBook(name) {
      var path = api + 'search'
      this.searching = true
      axios.get(path, {params: {name: name}})
          .then((res) => {
            this.books = res.data.books
            this.nbooks = this.books.length
            this.search = name
            this.searching = false
          })
          .catch((error) => {
            console.log(error)
            this.searching = false
          })
    }
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
</style>