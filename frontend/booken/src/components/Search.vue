<template>
    <div class="front-container">
        <div class="container" style="max-width: 1400px">
            <div class="row justify-content-md-between justify-content-sm-start">
                <div class="col-12 col-md-6 mr-md-auto my-auto ">
                    <h2>Resultados de la busqueda:</h2>
                </div>
            </div>
        </div>
        <hr>
        <div class="row row-cols-1 row-cols-sm-5" v-if="this.books" :key="this.books.length">
            <div class="col mb-4" v-for="(book) in this.books" :key="book.id">
                <div class="card h-100">
                    <img
                            :src="book.cover_image_url"
                            class="card-img-top" alt="...">
                    <div class="card-body">
                        <h6 class="card-subtitle">{{book.author[0]}}</h6>
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
                            <span class="badge badge-secondary"
                                  v-if="book.genre == 'METODOS DE IDIOMAS'">Métodos de idiomas</span>
                            <span class="badge badge-secondary"
                                  v-if="book.genre == 'COMICS Y MANGA'">Cómics y manga</span>
                            <span class="badge badge-secondary"
                                  v-if="book.genre == 'OTRAS CATEGORIAS'">Otras categorías</span>
                            <span class="badge badge-secondary" v-if="book.genre == 'INFANTIL'">Infantil</span>
                            <span class="badge badge-dark" v-if="book.cover_type == 0"
                            >Tapa dura</span>
                            <span class="badge badge-dark" v-else-if="book.cover_type == 1">Tapa blanda</span>
                        </h4>
                    </div>
                </div>
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
            this.searchBook(this.$route.query.name)
        },
        data() {
            return {
                books: []
            }
        },
        methods: {
            searchBook(name) {
                var path = api + 'search'
                axios.get(path, {params: {name: name}})
                    .then((res) => {
                        this.books = res.data.books[0]
                    })
                    .catch((error) => {
                        console.log(error)
                    })
            }
        }
    }
</script>

<style scoped>
    .front-container {
        margin-right: 5%;
        margin-left: 15%;
        margin-top: 50px;
        text-align: left;
    }
</style>