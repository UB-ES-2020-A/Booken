<template>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
        integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
  <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
  <link href='https://fonts.googleapis.com/css?family=Lato' rel='stylesheet' type='text/css'>

  <div class="front-container">
    <div class="container" style="max-width: 1400px;">
      <div class="row justify-content-md-between justify-content-sm-start">

        <div class="col-12 col-md-6 mr-md-auto my-auto ">
          <h2>{{ this.toLowercase($route.params.category) }}</h2>

          <!--Viendo todos los resultados para-->
        </div>
        <div class="col-12 col-md-6 my-auto filterBox">
          <label>Ordenar por: </label>
          <select class="form-control-sm " style="width: 180px; margin-left:10px">
            <option>Recomendado</option>
            <option>Precio ascendente</option>
            <option>Precio descendente</option>
            <option>Más vendidos</option>
          </select>
        </div>
      </div>
      <hr>

      <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4 row-cols-xl-4" :key="$route.params.category">
        <div class="col my-3" v-for="(book) in this.books" :key="book.id">
          <div class="card h-100">
            <img :src="book.cover_image_url"
                 class="card-img-top imgBook" alt="..."
                 style="object-fit: fill; object-position: center; width: 100%">
            <div class="card-body">
              <h6 class="card-subtitle mb-2">{{ this.joinAuthours(book.author) }}</h6>
              <h4 class="card-title">
                <router-link :to="{name: 'BookInfo', params: {id: book.id}}">{{ book.name }}</router-link>
              </h4>

              <p class="card-text text-muted"
                 style="overflow: hidden; text-overflow: ellipsis; display: -webkit-box;  -webkit-line-clamp: 3;
                  -webkit-box-orient: vertical;">
                {{ book.description }}</p>
            </div>
            <ul class="list-group list-group-flush">

              <li class="list-group-item">{{ this.toLowercase(book.genre) }}</li>
              <li class="list-group-item" v-if="book.cover_type == 0">Tapa dura</li>
              <li class="list-group-item" v-if="book.cover_type == 1">Tapa blanda</li>

            </ul>
            <div class="card-footer">
              <div>Comprar por</div>
              <div class="q" style="text-align: right">
                <span class="badge badge-info" style="text-align: right;">{{ book.price }}€</span>
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
      return stg.replace(/\S*/g, function (word) {
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
          })
          .catch((error) => {
            this.toPrint(error)
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