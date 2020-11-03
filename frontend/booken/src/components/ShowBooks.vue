<template>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
        integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
  <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
  <link href='https://fonts.googleapis.com/css?family=Lato' rel='stylesheet' type='text/css'>
  <div style="margin-top: 2rem; margin-left: 5%; margin-right: 5%">
    <div class="row row-cols-1 row-cols-sm-2">
      <div class="col mb-4" style="text-align: left">
        <h2>Viendo todos los resultados para: {{ $route.params.category }}</h2>
      </div>
      <div class="col mb-4">

        <h2>Ordenar por:</h2>
        <select class="form-control" style="width: 180px">
          <option>Recomendado</option>
          <option>Precio ascendente</option>
          <option>Precio descendente</option>
          <option>Más vendidos</option>
        </select>


      </div>
    </div>
    <div class="row row-cols-1 row-cols-sm-6">
      <div class="col mb-4" v-for="(book) in this.books" :key="book.author">
        <div class="card h-100">
          <img
              src="https://www.planetadelibros.com/usuaris/libros/fotos/270/m_libros/portada_el-cuarto-mono_julio-hermoso-oliveras_201803221718.jpg"
              class="card-img-top" alt="...">
          <div class="card-body">
            <h6 class="card-subtitle">{{ this.joinAuthours(book.author) }}</h6>
            <h4 class="card-title">
              <router-link to="/book">{{ book.name }}</router-link>
            </h4>

            <p class="card-text">FALTA DESC</p>
          </div>
          <div class="card-footer">
            <h4>
              <span class="badge badge-info">{{ this.replaceDecimal(book.price) }}</span>&nbsp;
              <span class="badge badge-secondary">{{ this.toLowercase(book.genre) }}</span>&nbsp;
              <span class="badge badge-dark" v-if="book.cover_type == 0">Tapa dura</span>
              <span class="badge badge-dark" v-else-if="book.cover_type == 1">Tapa blanda</span>
            </h4>
          </div>
        </div>
      </div>

    </div>
  </div>

</template>

<script>
import axios from 'axios'

let api = 'https://booken-app.herokuapp.com/'
export default {
  name: "ShowBooks",
  created() {
    this.getBooksFromDB(this.$route.params.category)
  },
  data() {
    return {
      books: []
    }
  },
  methods: {
    joinAuthours(aut) {
      if (aut.length == 1) {
        console.log(aut[0])
        return aut[0]
      } else {
        var ret = ''
        for (const a in aut) {
          ret += aut[a] + ','
        }
        return ret.slice(0, -1)
      }

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
            this.books = res.data.Books
          })
          .catch((error) => {
            this.toPrint(error)
          })
    }
  }
}
</script>

<style scoped>

</style>