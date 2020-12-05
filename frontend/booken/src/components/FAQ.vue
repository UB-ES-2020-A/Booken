<template>
  <div class="front-container">
    <div class="container" style="max-width: 1400px">
      <div class="row justify-content-md-between justify-content-sm-start">

        <div class="d-flex justify-content-between" v-if="type==1">
          <h2>Preguntas más frecuentes</h2>

          <button class="btn btn-warning my-2 my-sm-0 mr-2" type="submit"
                  data-toggle="modal" data-target="#addFAQ" v-if="type == 1">
            <i class="fas fa-edit" style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/>
            <a class="navbartextbt">Nueva FAQ</a>
            <span aria-hidden="true"></span>
          </button>

          <div class="modal fade" id="addFAQ" tabindex="-1" role="dialog"
               aria-labelledby="modalAddFAQ"
               aria-hidden="true">
            <div class="modal-dialog" role="document"
                 style="min-height: calc(100vh - 60px); display: flex;flex-direction: column;justify-content: center;overflow: auto;">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title" id="modalFAQLabel">Añadir FAQ</h5>
                  <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                  </button>
                </div>
                <div class="modal-body">
                  <form>
                    <div class="form-group" style="text-align: left">
                      <label for="categoryLabel" class="col-form-label">Categoria de la pregunta</label>
                      <input type="test" class="form-control" v-model="newCategory">
                    </div>

                    <div class="form-group" style="text-align: left">
                      <label for="questionLabel" class="col-form-label">Pregunta</label>
                      <input type="test" class="form-control" v-model="newQuestion">
                    </div>

                    <div class="form-group" style="text-align: left">
                      <label for="answerLabel" class="col-form-label">Respuesta</label>
                      <textarea type="text" class="form-control cln" col=30 rows=10 v-model="newAnswer"/>
                    </div>
                  </form>
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-secondary" data-dismiss="modal">
                    Cancelar
                  </button>
                  <button type="button" class="btn" style="background: #2bc4ed; color: white"
                          data-dismiss="modal" @click="addFAQ_DB">
                    Registrar FAQ
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-12 col-md-6 mr-md-auto my-auto " v-else>
          <h2>Preguntas más frecuentes</h2>
        </div>
      </div>

      <hr>

      <div class="row mb-4" v-if="this.consultsCat" :key="this.consultsCat.length">
        <div class="col-3">
          <div class="nav flex-column nav-pills" role="tablist" aria-orientation="vertical">

            <a v-for="(category, index) in this.consultsCat" :key="index"
               :class="['nav-link', (index === 0 ? 'active' : '')]"
               :href="'#h'+index"
               :id="'t'+index"
               data-toggle="pill" role="tab">{{ category }}</a>

          </div>
        </div>

        <div class="col-9">
          <div class=" tab-content" id="v-pills-tabContent">

            <div v-for="(category, index) in this.consultsCat" :key="index"
                 :class="['tab-pane fade', (index === 0 ? 'show active' : '')]"
                 :id="'h'+index"
                 aria-labelledby="'t'+index" role="tabpanel">

              <div class="accordion">
                <div v-for="(consult) in this.consults" :key="consult.category[0].type">
                  <div v-if="category === consult.category[0].type">

                    <div style="display:flex;">
                      <button class="card-header text-decoration-none btn btn-link btn-block text-left" type="button"
                              data-toggle="collapse" :data-target="'#'+this.suppressSpace(consult.question)"
                              aria-expanded="true">
                        ¿{{ consult.question }}?
                      </button>

                      <button type="submit" class="close" aria-label="Close" style="font-size:2em; color:red;"
                              data-toggle="modal" data-target="#deleteFAQ" v-if="type===1"
                              @click="this.FAQ_to_delete = consult.id">
                        <span aria-hidden="true">&times;</span>
                      </button>

                      <div class="modal fade" id="deleteFAQ" tabindex="-1" role="dialog"
                           aria-labelledby="deleteFAQTitle" aria-hidden="true">
                        <div class="modal-dialog modal-dialog-centered" role="document">
                          <div class="modal-content">
                            <div class="modal-header" style="border-bottom: 0 none;">
                              <h5 class="modal-title" id="exampleModalLongTitle">¿Quieres eliminar la FAQ?</h5>
                              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                              </button>
                            </div>
                            <div class="modal-footer" style="border-top: 0 none;">
                              <button type="button" class="btn btn-secondary" style="width:50px"
                                      @click="deleteFAQ_DB()"
                                      data-dismiss="modal">Sí
                              </button>
                              <button type="button" class="btn btn-primary" style="width:50px" data-dismiss="modal">No
                              </button>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>

                    <div :id="this.suppressSpace(consult.question)" class="collapse">
                      <div class="card-body">
                        {{ consult.answer }}
                      </div>
                    </div>
                  </div>

                </div>
              </div>
            </div>


          </div>
        </div>
      </div>
      <div class="jumbotron rounded "
           style="background-color: whitesmoke; margin-top:1em; margin-bottom: 2em; text-align: left !important;">
        <div class="container ">
          <h1 class="display-5" style="font-weight: bold">¿Sigues con la duda?</h1>
          <hr>
          <br>
          <p class="lead">No dudes en
            <router-link to="/contact" style="font-weight: bold">contactarnos</router-link>
            , ¡y te ayudaremos!
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {api} from "../main";
import axios from "axios";
import * as toastr from "@/assets/toastr";

export default {
  name: "FAQ",
  props: {
    logged: Boolean,
    token: String,
    id: Number,
    type: Number
  },
  created() {
    this.getConsults()
    //this.getCategories()
  },
  data() {
    return {
      selectedIndex: 0,
      FAQ_to_delete: 0,
      consults: [],
      consultsCat: new Set(), // List of categories

      //New FAQ
      newCategory: '',
      newQuestion: '',
      newAnswer: '',
    }
  }
  ,
  methods: {
    suppressSpace(word) {
      return word.replace(/ /g, '')
    },
    getConsults() {
      var path = api + 'faqs'
      axios.get(path)
          .then((res) => {
            this.consults = res.data.FAQ
            console.log(this.consults)
            this.getCategories()
          })
          .catch((error) => {
            console.log(error)
          })
    },
    getCategories() {
      this.consultsCat.clear()
      if (this.consults.length === 0) return

      for (let i in this.consults) {
        let cat = this.consults[i].category[0].type
        this.consultsCat.add(cat)
      }
    },


    deleteFAQ_DB() {
      var path = api + 'faq/' + this.FAQ_to_delete
      axios.delete(path)
          .then((res) => {
            console.log(res)
            this.getConsults()
          })
          .catch((error) => {
            console.log(error)
          })
    },
    addFAQ_DB() {
      if (this.newCategory == '' || this.newQuestion == '' || this.newAnswer == '') {
        toastr.info('', 'Rellena los campos obligatorios para añadir la FAQ.',
            {
              timeOut: 2500,
              progressBar: true,
              newestOnTop: true,
              positionClass: 'toast-bottom-right',
              preventDuplicates: true
            })
      } else {
        if (this.newQuestion[this.newQuestion.length - 1] == '?') {
          this.newQuestion = this.newQuestion.slice(0, -1)
        }
        if (this.newQuestion[0] == '¿') {
          this.newQuestion = this.newQuestion.slice(1, this.newQuestion.length)
        }
        var tmp = {
          "category": this.newCategory,
          "question": this.newQuestion,
          "answer": this.newAnswer
        }

        var path = api + 'faq'
        axios.post(path, tmp)
            .then((res) => {
              console.log(res)
              this.getConsults()

              toastr.success('', '¡FAQ registrada con éxito!',
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
              toastr.error('', 'Rellena los campos obligatorios para añadir la FAQ.',
                  {
                    timeOut: 2500,
                    progressBar: true,
                    newestOnTop: true,
                    positionClass: 'toast-bottom-right',
                    preventDuplicates: true
                  })
            })

        this.newCategory = ''
        this.newQuestion = ''
        this.newAnswer = ''
      }
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