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
                        <label class="col-form-label">Categoria de la pregunta</label>
                        <input type="test" class="form-control" v-model="newCategory">
                      </div>

                      <div class="form-group" style="text-align: left">
                        <label class="col-form-label">Pregunta</label>
                        <input type="test" class="form-control" v-model="newQuestion">
                      </div>

                      <div class="form-group" style="text-align: left">
                        <label class="col-form-label">Respuesta</label>
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
          <div class="nav flex-column nav-pills" id="v-pills-tab" role="tablist" aria-orientation="vertical">
            <a class="nav-link active" data-toggle="pill" role="tab"
               aria-selected="false"
               v-for="[iter, consultCat] in this.consultsCatHead" :key="iter"
               :href="'#'+iter">{{ consultCat }}</a>
            <a class="nav-link" data-toggle="pill" role="tab"
               aria-selected="false"
               v-for="[iter, consultCat] in this.consultsCat" :key="iter"
               :href="'#'+iter">{{ consultCat }}</a>
          </div>
        </div>

          <div class="col-9">
            <div class=" tab-content" id="v-pills-tabContent">

              <div class="tab-pane fade show active" role="tabpanel"
                   v-for="[iter, consultCat] in this.consultsCatHead" :key="iter"
                   :id="iter">
                <div class="accordion">
                  <div class="" v-for="(consult) in this.consults" :key="consult.category[0].type">
                    <div v-if="consultCat === consult.category[0].type">

                      <div style="display:flex;">
                          <button class="card-header text-decoration-none btn btn-link btn-block text-left" type="button"
                                  data-toggle="collapse" :data-target="'#'+this.suppressSpace(consult.question)"
                                  aria-expanded="true" aria-controls="collapseOne">
                            ¿{{ consult.question }}?
                          </button>

                          <button type="submit" class="close" aria-label="Close" style="font-size:2em; color:red;"
                            data-toggle="modal" data-target="#deleteFAQ" v-if="type==1"
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
                                  <button type="button" class="btn btn-primary" style="width:50px" data-dismiss="modal">No</button>
                                </div>
                              </div>
                            </div>
                          </div>
                      </div>

                      <div :id="this.suppressSpace(consult.question)"
                           v-if="this.suppressSpace(consult.question) === this.firstQuestion" class="collapse show">
                        <div class="card-body">
                          {{ consult.answer }}
                        </div>
                      </div>

                      <div :id="this.suppressSpace(consult.question)" v-else class="collapse">
                        <div class="card-body">
                          {{ consult.answer }}
                        </div>
                      </div>
                    </div>

                  </div>
                </div>
              </div>

              <div class="tab-pane fade" role="tabpanel"
                   v-for="[iter, consultCat] in this.consultsCat" :key="iter"
                   :id="iter">
                <div class="accordion">
                  <div class="" v-for="(consult) in this.consults" :key="consult.category[0].type">
                    <div v-if="consultCat === consult.category[0].type">
                      <button class="card-header text-decoration-none btn btn-link btn-block text-left" type="button"
                              data-toggle="collapse" :data-target="'#'+this.suppressSpace(consult.question)"
                              aria-expanded="true" aria-controls="collapseOne">
                        ¿{{ consult.question }}?
                      </button>

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
      <div class="jumbotron rounded"
           style="background-color: whitesmoke; margin-top: 8rem; text-align: left !important;">
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
  },
  data() {
    return {
      FAQ_to_delete: 0,
      consults: [
        {
          category: [{'type': 'Usuarios extras'}],
          question: 'Usuarios Question 1',
          answer: 'Usuarios Answer'
        },
        {
          category: [{'type': 'General'}],
          question: 'Gastos de envío Question',
          answer: 'Gastos de envío Answer'
        },
        {
          category: [{'type': 'Gastos de envío'}],
          question: 'Gastos de envío Question 2',
          answer: ' Gastos de envío Answer 2'
        },
        {
          category: [{'type': 'Devolución'}],
          question: 'Devolución Question',
          answer: 'Devolución Answer'
        },

        {
          category: [{'type': 'Seguimiento de pedido'}],
          question: 'Seguimiento de pedido Question',
          answer: 'Seguimiento de pedido Answer'
        },
        {
          category: [{'type': 'Pago con tarjeta'}],
          question: 'Pago con tarjeta Question',
          answer: 'Pago con tarjeta Answer'
        },
        {
          category: [{'type': 'Usuarios extras'}],
          question: 'Usuarios Question',
          answer: 'Usuarios Answer'
        },
        {
          category: [{'type': 'Pago con tarjeta'}],
          question: 'Pago con tarjeta Question23',
          answer: 'Pago con tarjeta Answer'
        },
        {
          category: [{'type': 'Pago con tarjeta'}],
          question: 'Pago con tarjeta Question123',
          answer: 'Pago con tarjeta Answer'
        },
        {
          category: [{'type': 'Pago con tarjeta'}],
          question: 'Se puede devolcer un artículo que está dañadao cuando lo he recibido',
          answer: 'Pago con tarjeta Answer'
        },
      ],
      consultsCat: new Map(),
      consultsCatHead: new Map(),
      firstQuestion: '',

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
      this.consultsCatHead.clear()

      if(this.consults.length == 0)
        return

      let first, firstValue
      for (let i in this.consults) {
        let cat = this.consults[i].category[0].type
        let iter = this.suppressSpace(cat)
        if (i === '0') {
          first = iter
          firstValue = cat
        }
        if (!this.consultsCat.has(iter)) {
          this.consultsCat.set(iter, cat)
        }
      }
      this.consultsCatHead.set(first, firstValue)
      this.consultsCat.delete(first)
      //this.firstQuestion = this.suppressSpace(this.consults[0].question)
    },
    
    deleteFAQ_DB(){
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
    addFAQ_DB(){
      if (this.newCategory == '' || this.newQuestion == '' || this.newAnswer == ''){
        toastr.info('', 'Rellena los campos obligatorios para añadir la FAQ.',
            {
              timeOut: 2500,
              progressBar: true,
              newestOnTop: true,
              positionClass: 'toast-bottom-right',
              preventDuplicates: true
            })
      }
      else {
        if (this.newQuestion[this.newQuestion.length-1] == '?'){
         this.newQuestion = this.newQuestion.slice(0,-1)
        }
        if (this.newQuestion[0] == '¿'){
         this.newQuestion = this.newQuestion.slice(1,this.newQuestion.length)
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