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

    <div class = "container">
        <div class = "col" v-if="book_found">
            <p class="bookTitle">{{bookInfo.name}}</p>

            <div class="row">
                <div ref="images" class = "col">
                    <div style="display:flex; flex-direction: row">
                        <div style="display:flex; flex-direction: column">
                            <img ref="pic1" class="sel-picture" :src="bookInfo.cover" @click="changeImage(1)">
                            <img ref="pic2" class="sel-picture" :src="bookInfo.back_cover" @click="changeImage(2)">
                        </div>
                        <div style ="margin-left:auto; margin-right:auto">
                            <img ref="bigPic" id="displayPic" style = "max-height:335px" :src="bookInfo.cover">
                        </div>
                    </div>
                </div>
                <div class = "col-sm">
                    <div class = "row">
                        <div class = "col-sm-2">
                            <p ref="label_summary" class="label-info-selected" @click="change_info('summary')">Sinopsis</p>
                        </div>
                        <div class = "col-sm-2">
                            <p ref="label_details" class="label-info-not-selected" @click="change_info('details')">Detalles</p>
                        </div>
                    </div>
                    <div style="text-align:left" v-if="showSummary">
                        <p>{{bookInfo.synopsis}}</p>
                    </div>
                    <div style="text-align:left" v-else>
                        <p><b>Autor: </b>{{ bookInfo.author }}</p>
                        <p><b>Editorial: </b>{{ bookInfo.editorial }}</p>
                        <p><b>Año de publicación: </b>{{ bookInfo.year }}</p>
                        <p><b>Genero: </b>{{ bookInfo.genre }}</p>
                        <p><b>Idioma: </b>{{ bookInfo.language }}</p>
                    </div>
                </div>
            </div>
        </div>

        <div class = "col" v-else>
            <p class="bookTitle">No se ha encontrado el libro</p>
            <img style="width: 50%; padding: 10px" src="https://www.pinclipart.com/picdir/big/160-1604750_sad-cloud-icon-clipart.png">
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'BookInfo',

  props: {
    msg: String
  },

  created(){
    this.logged = this.$route.query.logged
    this.is_admin = this.$route.query.is_admin
    this.token = this.$route.query.token
    this.book_id = this.$route.query.id

    this.initBookInfo()
  },

  data() {
    return{

        book_found: 0,
        book_id: 0,

        bookInfo: {
            name: 'NameTest',
            author: 'AuthorTest',
            genre: 'GenreTest',
            year: 0,
            editorial: 'EditorialTest',
            language: 'LenguageTest',
            price: 0,
            synopsis: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            cover: 'https://static.fnac-static.com/multimedia/Images/ES/NR/22/0f/18/1576738/1507-1.jpg',
            back_cover: 'https://images-na.ssl-images-amazon.com/images/I/71XhS2XgMxL.jpg',
        },

        showSummary: 1

    }
  },

  methods: {
    toPrint (toPrint) {
      console.log(toPrint)
    },

    initBookInfo(){
        this.toPrint(this.book_id)
        var path = `http://127.0.0.1:5000/book/${this.book_id}`

        axios.get(path)
            .then((res) => {
                this.book_found = 1
                this.bookInfo.name = res.data.Book.book.name
                this.bookInfo.author = res.data.Book.book.author[0]
                this.bookInfo.genre = res.data.Book.book.genre
                this.bookInfo.year = res.data.Book.book.year
                this.bookInfo.editorial = res.data.Book.book.editorial
                this.bookInfo.language = res.data.Book.book.language
                this.bookInfo.price = res.data.Book.book.price
                this.bookInfo.synopsis = res.data.Book.book.synopsis
            })
            .catch((error) => {
                this.toPrint(error)
            })
    },

    changeImage(id_image){
        if(id_image == 1){
            this.$refs.bigPic.src = this.$refs.pic1.src
        }else{
            this.$refs.bigPic.src = this.$refs.pic2.src
        }
    },

    change_info(info){
      if(info=="summary"){
        this.$refs.label_summary.classList = "label-info-selected"
        this.$refs.label_details.classList = "label-info-not-selected"
        this.showSummary = 1
      }
      else if(info=="details"){
        this.$refs.label_summary.classList = "label-info-not-selected"
        this.$refs.label_details.classList = "label-info-selected"
        this.showSummary = 0
      }
    }
  }
}
</script>