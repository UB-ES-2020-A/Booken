<template>
  <div class="front-container">
    <div class="container" style="max-width: 1400px">
      <div class="row justify-content-md-between justify-content-sm-start">
        <div class="col-12 col-md-6 mr-md-auto my-auto ">
          <h2>Preguntas más frecuentes</h2>
        </div>
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

                  <button class="card-header text-decoration-none btn btn-link btn-block text-left" type="button"
                          data-toggle="collapse" :data-target="'#'+this.suppressSpace(consult.question)"
                          aria-expanded="true" aria-controls="collapseOne">
                    {{ consult.question }}?
                  </button>

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
                    {{ consult.question }}?
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

  </div>
</template>

<script>
import {api} from "../main";
import axios from "axios";

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
      consults: [
        {
          category: [{'type':'Usuarios extras'}],
          question: 'Usuarios Question 1',
          answer: 'Usuarios Answer'
        },
        {
          category: [{'type':'General'}],
          question: 'Gastos de envío Question',
          answer: 'Gastos de envío Answer'
        },
        {
          category: [{'type':'Gastos de envío'}],
          question: 'Gastos de envío Question 2',
          answer: ' Gastos de envío Answer 2'
        },
        {
          category: [{'type':'Devolución'}],
          question: 'Devolución Question',
          answer: 'Devolución Answer'
        },

        {
          category: [{'type':'Seguimiento de pedido'}],
          question: 'Seguimiento de pedido Question',
          answer: 'Seguimiento de pedido Answer'
        },
        {
          category: [{'type':'Pago con tarjeta'}],
          question: 'Pago con tarjeta Question',
          answer: 'Pago con tarjeta Answer'
        },
        {
          category: [{'type':'Usuarios extras'}],
          question: 'Usuarios Question',
          answer: 'Usuarios Answer'
        },
        {
          category: [{'type':'Pago con tarjeta'}],
          question: 'Pago con tarjeta Question23',
          answer: 'Pago con tarjeta Answer'
        },
        {
          category: [{'type':'Pago con tarjeta'}],
          question: 'Pago con tarjeta Question123',
          answer: 'Pago con tarjeta Answer'
        },
        {
          category: [{'type':'Pago con tarjeta'}],
          question: 'Se puede devolcer un artículo que está dañadao cuando lo he recibido',
          answer: 'Pago con tarjeta Answer'
        },

      ],
      consultsCat: new Map(),
      consultsCatHead: new Map(),
      firstQuestion: ''
    }
  }
  ,
  methods: {
    suppressSpace(word) {
      return word.replace(/ /g, '')
    },
    getConsults(){
      var path = api + 'faqs'
      axios.get(path)
          .then((res) => {
            this.consults = res.data.FAQ
            console.log(this.consults[0].answer)
            this.getCategories()
          })
          .catch((error) => {
            console.log(error)
          })
    },
    getCategories() {
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