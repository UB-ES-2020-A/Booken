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
        <div class = "row">
            <p class="bookTitle">{{bookInfo.name}}</p>
        </div>
        <div class="row">
            <div class = "col-sm-1">
                <div style="display:flex; flex-direction: row">
                    <div>
                        <img ref="pic1" class="sel-picture" src="https://i1.wp.com/www.eastcoastdesigns.ca/wp-content/uploads/2018/02/black-and-white-book.png?fit=1600%2C1600&ssl=1.jpg" @click="changeImage(1)">
                        <img ref="pic2" class="sel-picture" src="https://image.shutterstock.com/image-vector/black-realistic-blank-book-cover-260nw-300099890.jpg" @click="changeImage(2)">
                    </div>
                    <div>
                        <img ref="bigPic" id="displayPic" src="https://i1.wp.com/www.eastcoastdesigns.ca/wp-content/uploads/2018/02/black-and-white-book.png?fit=1600%2C1600&ssl=1.jpg">
                    </div>
                </div>
            </div>
            <div class="col-sm-4"></div>
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

    this.initBookInfo()
  },

  data() {
    return{

        bookInfo: {
            name: 'NameTest',
            author: 'AuthorTest',
            genre: 'GenreTest',
            year: 'YearTest',
            editorial: 'EditorialTest',
            language: 'LenguageTest',
            price: '',
            synopsis: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            cover: '',
            back_cover: '',
        },

        showSummary: 1

    }
  },

  methods: {
    toPrint (toPrint) {
      console.log(toPrint)
    },

    initBookInfo(){
        var path = 'http://loaclhost:8080/book/0'

        axios.get(path)
            .then((res) => {
                this.bookInfo.name = res.data.Book.book.name
            })
            .catch((error) => {
                this.toPrint(error)
                this.bookInfo.name = 'NotFound'
            })
    },

    changeImage(id_image){
        this.toPrint(id_image)
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