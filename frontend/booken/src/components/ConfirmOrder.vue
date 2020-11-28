<style scoped>
@import url("../assets/toastr.css");
@import url("../assets/animate.min.css");
@import url("../assets/book_info.css");
</style>
<style lang="scss" src="../assets/order-button.scss" scoped>
</style>
<template>
  <div class="container" style="margin-top: 2em; margin-bottom: 2em">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
          integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
    <div class="card">
      <div style="margin: 1em" v-if="processing==0">
        <div class="row">
          <div class="col">
            <h2 class="card-title" style="text-align: left">Confirmar pedido</h2>
          </div>
          <div class="col" style="text-align: right; display: inline">
            <h1 v-if="selected!=0">Total: {{ total + prices[selected] }}€</h1>
            <h1 v-if="selected==0">Total: {{ total }}€ + envío</h1>
          </div>
        </div>
        <div style="margin: 0.5em">
          <h3 class="card-title" style="text-align: left; margin-top: 1em">¿Cómo te lo mandamos?</h3>
          <div class="row row-cols-1 row-cols-md-4">
            <div class="col mb-2">
              <div class="card h-100 text-white bg-info" style="max-width: 18rem; text-align: left"
                   @click="changeSend(1)"
                   v-if="selected!=1">
                <div class="card-header"><b>Envío estándar - 5€</b></div>
                <div class="card-body">
                  <h5 class="card-title">5 a 7 días laborables</h5>
                  <p class="card-text">Recibirás tu pedido el <b>{{ this.getDatePlus(5) }}</b>, probablemente cuando no
                    estés en casa así que
                    tendrás
                    que ir a buscarla a algún sitio.</p>
                </div>
              </div>
              <div class="card h-100 text-white bg-info"
                   style="max-width: 18rem; text-align: left; border-color: black; border-width: 2px"
                   v-if="selected==1">
                <div class="card-header"><b>Envío estándar - 5€</b></div>
                <div class="card-body">
                  <h5 class="card-title">5 a 7 días laborables</h5>
                  <p class="card-text">Recibirás tu pedido el <b>{{ this.getDatePlus(5) }}</b>, probablemente cuando no
                    estés en casa así que
                    tendrás
                    que ir a buscarla a algún sitio.</p>
                </div>
              </div>
            </div>
            <div class="col mb-2">
              <div class="card h-100 text-white bg-warning" style="max-width: 18rem; text-align: left"
                   @click="changeSend(2)" v-if="selected!=2">
                <div class="card-header"><b>Envío estándar Plus - 7€</b></div>
                <div class="card-body">
                  <h5 class="card-title">2 a 3 días laborables</h5>
                  <p class="card-text">Recibirás tu pedido el <b>{{ this.getDatePlus(2) }}</b>, más rápido y si no estás
                    en casa te lo
                    intentamos hacer llegar otra vez.</p>
                </div>
              </div>
              <div class="card h-100 text-white bg-warning"
                   style="max-width: 18rem; text-align: left; border-color: black; border-width: 2px"
                   v-if="selected==2">
                <div class="card-header"><b>Envío estándar Plus - 7€</b></div>
                <div class="card-body">
                  <h5 class="card-title">2 a 3 días laborables</h5>
                  <p class="card-text">Recibirás tu pedido el <b>{{ this.getDatePlus(2) }}</b>, más rápido y si no estás
                    en casa te lo
                    intentamos hacer llegar otra vez.</p>
                </div>
              </div>
            </div>
            <div class="col mb-2">
              <div class="card h-100 text-white bg-success"
                   style="max-width: 18rem; text-align: left" @click="changeSend(3)" v-if="selected!=3">
                <div class="card-header"><b>Envío Ultra Express - 50€</b></div>
                <div class="card-body">
                  <h5 class="card-title">¡Ahora mismo!</h5>
                  <p class="card-text">Gracias a nuestro increíble sistema logístico recibirás tu paquete en unos
                    minutos después del pago. Eso o el siguiente día hábil a partir de la confirmación.</p>
                </div>
              </div>
              <div class="card h-100 text-white bg-success"
                   style="max-width: 18rem; text-align: left; border-color: black; border-width: 2px"
                   v-if="selected==3">
                <div class="card-header"><b>Envío Ultra Express - 50€</b></div>
                <div class="card-body">
                  <h5 class="card-title">¡Ahora mismo!</h5>
                  <p class="card-text">Gracias a nuestro increíble sistema logístico recibirás tu paquete en unos
                    minutos después del pago. Eso o el siguiente día hábil a partir de la confirmación.</p>
                </div>
              </div>
            </div>
          </div>
          <h3 class="card-title" style="text-align: left; margin-top: 1em">¿Y a dónde?</h3>
          <div class="row row-cols-1 row-cols-md-4">
            <div class="col mb-2" v-for="(item, index) in this.addresses" :key="item.id">
              <div class="card" style="text-align: left" v-if="selectedAdd!=index" @click="changeAdd(index)">
                <div class="card-header">
                  {{ item.label_name }}
                </div>
                <ul class="list-group list-group-flush">
                  <li class="list-group-item">
                    {{ item.name }} {{ item.surnames }}<br>
                    {{ item.street }}, {{ item.number }}<br>
                    {{ item.cp }} {{ item.city }}, {{ item.province }}<br>
                    {{ item.telf }}
                  </li>
                </ul>
                <div class="card-header">
                  <div style="display: flex; float:right;">
                    <p style="cursor: pointer; margin-bottom: 0em; text-align: right; margin-right: 1em; color: #3b494d;"
                       data-toggle="modal" data-target="#modalAddress" @click="updateAddressModal(item.id)"><i
                        class="fas fa-pen"></i></p>
                    <p style="cursor: pointer; margin-bottom: 0em; text-align: right; color: red"
                       @click="deleteAddress(item.id)">
                      <i class="fas fa-trash-alt"></i></p>
                  </div>
                </div>
              </div>
              <div class="card" style="text-align: left;  border-color: black; border-width: 2px"
                   v-if="selectedAdd==index">
                <div class="card-header">
                  {{ item.label_name }}
                </div>
                <ul class="list-group list-group-flush">
                  <li class="list-group-item">
                    {{ item.name }} {{ item.surnames }}<br>
                    {{ item.street }}, {{ item.number }}<br>
                    {{ item.cp }} {{ item.city }}, {{ item.province }}<br>
                    {{ item.telf }}
                  </li>
                </ul>
                <div class="card-header">
                  <div style="display: flex; float:right;">
                    <p style="cursor: pointer; margin-bottom: 0em; text-align: right; margin-right: 1em; color: #3b494d;"
                       data-toggle="modal" data-target="#modalAddress" @click="updateAddressModal(item.id)"><i
                        class="fas fa-pen"></i></p>
                    <p style="cursor: pointer; margin-bottom: 0em; text-align: right; color: red"
                       @click="deleteAddress(item.id)">
                      <i class="fas fa-trash-alt"></i></p>
                  </div>
                </div>
              </div>
            </div>
            <div class="col mb-2" v-if="this.addressNumber < 3">
              <div class="card h-100" style="text-align: center">
                <button style="color: #3b494d; height: 100%" type="submit"
                        data-toggle="modal" data-target="#modalAddress" data-whatever="@getbootstrap"
                        @click="updateAddressModal(-1)">
                  <i class="fas fa-plus" style="font-size: 6em; top: 50%"></i>
                </button>
                <div class="modal fade" id="modalAddress" tabindex="-1" role="dialog"
                     aria-labelledby="modalAddressLabel"
                     aria-hidden="true">
                  <div class="modal-dialog" role="document"
                       style="min-height: calc(100vh - 60px); display: flex;flex-direction: column;justify-content: center;overflow: auto;">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title" id="modalAddressLabel">Añadir dirección</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                          <span aria-hidden="true">&times;</span>
                        </button>
                      </div>
                      <div class="modal-body">
                        <form>
                          <div class="form-group" style="text-align: left">
                            <label for="addressLabel" class="col-form-label">Identificador</label>
                            <input type="test" class="form-control" v-model="newAddressLabel">
                          </div>
                          <div class="form-group" style="text-align: left">
                            <label for="addressName" class="col-form-label">Nombre y apellidos</label>
                            <div style="display:flex;">
                              <input type="text" class="form-control"
                                     v-model="newAddressName" placeHolder="Nombre">
                              <input type="text" class="form-control"
                                     v-model="newAddressSurname" placeHolder="Apellidos">
                            </div>
                          </div>
                          <div class="form-group" style="text-align: left">
                            <label for="addressRoad" class="col-form-label">Dirección</label>
                            <div style="display:flex">
                              <input type="text" class="form-control" style="width:80%;"
                                     v-model="newAddressRoad" placeHolder="Calle">
                              <input type="number" class="form-control" style="width:20%;"
                                     v-model="newAddressNumber" placeHolder="Nº">
                            </div>
                          </div>
                          <div class="form-group" style="text-align: left">
                            <label for="addressCode" class="col-form-label">Código postal</label>
                            <input type="number" class="form-control" v-model="newAddressCode">
                          </div>
                          <div class="form-group" style="text-align: left">
                            <label for="addressProvince" class="col-form-label">Residencia</label>
                            <div style="display:flex">
                              <input type="text" class="form-control"
                                     v-model="newAddressCity" placeHolder="Ciudad">
                              <input type="text" class="form-control"
                                     v-model="newAddressProvince" placeHolder="Provincia">
                            </div>
                          </div>
                          <div class="form-group" style="text-align: left">
                            <label for="addressPhone" class="col-form-label">Telefono</label>
                            <input type="number" class="form-control" v-model="newAddressPhone">
                          </div>
                        </form>
                      </div>
                      <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">
                          Cancelar
                        </button>
                        <button type="button" class="btn" style="background: #2bc4ed; color: white"
                                data-dismiss="modal" @click="addAddress">
                          Enviar
                        </button>
                      </div>
                    </div>
                  </div>
                </div>

              </div>
            </div>
          </div>
          <h3 class="card-title" style="text-align: left; margin-top: 1em">Por último, ¿con que pagarás?</h3>
          <div class="row row-cols-1 row-cols-md-4">
            <div class="col mb-2" v-for="(item, index) in this.cards" :key="item.id">
              <div class="card" style=" text-align: left" @click="changeCard(index)" v-if="selectedCard!=index">
                <div class="card-header">
                      <span v-if="item.vendor == 'MASTERCARD'"><i class="fab fa-cc-mastercard"
                                                                  style="font-size: 1.8em"></i></span>
                  <span v-if="item.vendor == 'VISA'"><i class="fab fa-cc-visa"
                                                        style="font-size: 1.8em"></i></span>
                  <span v-if="item.vendor == 'JCB'"><i class="fab fa-cc-jcb" style="font-size: 1.8em"></i></span>
                  <span v-if="item.vendor == 'DISCOVER'"><i class="fab fa-cc-discover"
                                                            style="font-size: 1.8em"></i></span><br>
                </div>
                <ul class="list-group list-group-flush">
                  <li class="list-group-item">
                    <b>Titular:</b> {{ item.holder }}<br>
                    <b>Termina en:</b> {{ item.end_number }}<br>
                    <b>Caduca:</b> {{ item.expires }}
                  </li>
                </ul>
                <div class="card-header" style="text-align: right !important">
                  <p style="cursor: pointer; text-align: right; margin-bottom: 0em; color: red"
                     @click="deleteCard(item.id)"><i class="fas fa-trash-alt"></i></p>
                </div>
              </div>
              <div class="card" style=" text-align: left;  border-color: black; border-width: 2px"
                   v-if="selectedCard==index">
                <div class="card-header">
                      <span v-if="item.vendor == 'MASTERCARD'"><i class="fab fa-cc-mastercard"
                                                                  style="font-size: 1.8em"></i></span>
                  <span v-if="item.vendor == 'VISA'"><i class="fab fa-cc-visa"
                                                        style="font-size: 1.8em"></i></span>
                  <span v-if="item.vendor == 'JCB'"><i class="fab fa-cc-jcb" style="font-size: 1.8em"></i></span>
                  <span v-if="item.vendor == 'DISCOVER'"><i class="fab fa-cc-discover"
                                                            style="font-size: 1.8em"></i></span><br>
                </div>
                <ul class="list-group list-group-flush">
                  <li class="list-group-item">
                    <b>Titular:</b> {{ item.holder }}<br>
                    <b>Termina en:</b> {{ item.end_number }}<br>
                    <b>Caduca:</b> {{ item.expires }}
                  </li>
                </ul>
                <div class="card-header" style="text-align: right !important">
                  <p style="cursor: pointer; text-align: right; margin-bottom: 0em; color: red"
                     @click="deleteCard(item.id)"><i class="fas fa-trash-alt"></i></p>
                </div>
              </div>
            </div>
            <div class="col mb-2" v-if="this.cardNumber < 2">
              <div class="card h-100">
                <button style="color: #3b494d; height: 100%" type="submit" data-toggle="modal"
                        data-target="#modalPayment" data-whatever="@getbootstrap">
                  <i class="fas fa-plus" style="font-size: 6em"></i>
                </button>
                <div class="modal fade" id="modalPayment" tabindex="-1" role="dialog"
                     aria-labelledby="modalAddressLabel"
                     aria-hidden="true">
                  <div class="modal-dialog " role="document"
                       style="min-height: calc(100vh - 60px); display: flex;flex-direction: column;justify-content: center;overflow: auto;">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title" id="modalPaymentLabel">Añadir tarjeta</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                          <span aria-hidden="true">&times;</span>
                        </button>
                      </div>
                      <div class="modal-body">
                        <form>
                          <div class="form-group" style="text-align: left">
                            <label for="paymentNumber" class="col-form-label">Número de tarjeta</label>
                            <input type="number" class="form-control" id="paymentNumber">
                          </div>
                          <div class="form-group" style="text-align: left">
                            <label for="paymentTitular" class="col-form-label">Titular de la tarjeta</label>
                            <input type="text" class="form-control" id="paymentTitular">
                          </div>

                          <div class="form-group" style="text-align: left">
                            <label for="paymentEndDate" class="col-form-label">Fecha de caducidad</label>
                            <input type="text" class="form-control" id="paymentEndDate" placeholder="mm/yyyy">
                          </div>
                          <div class="form-group" style="text-align: left">
                            <label for="paymentMethod" class="col-form-label">Metodo de pago</label>
                            <select class="form-group"
                                    style="text-align: left; width:100%; height: 2.5em" id="paymentMethod">
                              <option>VISA</option>
                              <option>JCB</option>
                              <option>DISCOVER</option>
                            </select>
                          </div>
                        </form>
                      </div>
                      <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">
                          Cancelar
                        </button>
                        <button type="button" class="btn" style="background: #2bc4ed; color: white"
                                data-dismiss="modal" @click="addCard">
                          Enviar
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div style="margin: 1em" v-if="processing >= 1">
        <div class="row">
          <div class="col" id="processing">
            <h1>Procesando pago</h1>
            <div class="spinner-border text-info" role="status"
                 style="margin-top: 2rem; height: 3.5rem; width: 3.5rem; margin-bottom: 2rem">
              <span class="sr-only">Loading...</span>
            </div>
          </div>
          <div class="col" id="completed" style="display: none">
            <h1>Pago completado</h1>
            <h3 style="margin-top: 2em">Tu pedido será entregado el día {{ dateAprox }} por Correos. Recibirás un correo
              electrónico cuando sea enviado.</h3>
            <h4 style="margin-top: 1em">Gracias por comprar en <span style="font-family: LogoFont; font-size: 1.3em">booken</span>.
            </h4>
          </div>
        </div>
      </div>
      <button class="truck-button a" style="width: 100%; text-align: center" id="nocanpay" disabled>
        <span class="default">Completa todos los campos para continuar</span>
      </button>
      <button class="truck-button" style="width: 100%; text-align: center; display: none" id="canpay">
        <span class="default">Pagar pedido</span>
        <span class="success">
        Pedido completado
        <svg viewbox="0 0 12 10">
            <polyline points="1.5 6 4.5 9 10.5 1"></polyline>
        </svg>
    </span>
        <div class="truck" style="margin-left: 0.5em">
          <div class="wheel"></div>
          <div class="back"></div>
          <div class="front"></div>
          <div class="box"></div>
        </div>
      </button>
    </div>
  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import axios from 'axios'
// eslint-disable-next-line no-unused-vars
import IMask from 'imask'
// eslint-disable-next-line no-unused-vars
import * as toastr from '../assets/toastr.js'
import gsap from 'gsap'
import {bus, api} from '../main.js'
export default {
  name: "ConfirmOrder",
  props: {
    logged: Boolean,
    token: String,
    id: Number,
    type: Number,
    shipping: Number,
    total: Number,
    subtotal: Number,
    taxes: Number,
    cart: Array
  },
  mounted() {
    document.querySelectorAll('.truck-button').forEach(button => {
      button.addEventListener('click', e => {

        e.preventDefault();

        let box = button.querySelector('.box'),
            truck = button.querySelector('.truck');

        if (!button.classList.contains('done')) {
          this.processing = 1
          this.checkout()
          if (!button.classList.contains('animation')) {

            button.classList.add('animation');

            gsap.to(button, {
              '--box-s': 1,
              '--box-o': 1,
              duration: .3,
              delay: .5
            });

            gsap.to(box, {
              x: 0,
              duration: .4,
              delay: .7
            });

            gsap.to(button, {
              '--hx': -5,
              '--bx': 50,
              duration: .18,
              delay: .92
            });

            gsap.to(box, {
              y: 0,
              duration: .1,
              delay: 1.15
            });

            gsap.set(button, {
              '--truck-y': 0,
              '--truck-y-n': -26
            });

            gsap.to(button, {
              '--truck-y': 1,
              '--truck-y-n': -25,
              duration: .2,
              delay: 1.25,
              onComplete() {
                gsap.timeline({
                  onComplete() {
                    toastr.success('', '¡Order done!',
                        {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
                    button.classList.add('done');
                    document.getElementById('processing').style.display = 'none'
                    document.getElementById('completed').style.display = 'block'
                    button.disabled = true
                  }
                }).to(truck, {
                  x: 0,
                  duration: .4
                }).to(truck, {
                  x: 40,
                  duration: 1
                }).to(truck, {
                  x: 20,
                  duration: .6
                }).to(truck, {
                  x: 1000,
                  duration: .4
                });
                gsap.to(button, {
                  '--progress': 1,
                  duration: 2.4,
                  ease: "power2.in"
                });
              }
            });
          }

        } else {
          button.classList.remove('animation', 'done');
          gsap.set(truck, {
            x: 4
          });
          gsap.set(button, {
            '--progress': 0,
            '--hx': 0,
            '--bx': 0,
            '--box-s': .5,
            '--box-o': 0,
            '--truck-y': 0,
            '--truck-y-n': -26
          });
          gsap.set(box, {
            x: -24,
            y: -6
          });
        }
        setTimeout(() => {
          this.$router.push({path: '/cp'})
        }, 8000)
      });
    });

  },
  created() {
    this.getAddresses()
    this.getCards()
  },
  data() {
    return {
      formData: {
        cardName: '',
        cardNumber: '',
        cardMonth: '',
        cardYear: '',
        cardCvv: ''
      },
      selected: 0,
      selectedCard: -1,
      selectedAdd: -1,
      addresses: [],
      processing: 0,
      cardNumber: 0,
      addressNumber: 0,
      cards: [],
      prices: [0, 5, 7, 50],
      days: [0, 5, 2, 1],
      dateAprox: '',
      send: 0,
      addCardForm: {
        "card_owner": '',
        "number": '',
        "date": '',
        "payment_method": ''
      }
    }
  },
  methods: {
    checkout() {
      this.dateAprox = this.getDatePlus(this.days[this.selected])
      const path = api + 'order/' + this.id
      const parameters = {
        date: this.dateAprox,
        total: this.total,
        shipping: this.prices[this.selected],
        taxes: this.taxes,
        state: 0,
        send_type: this.send,
        card_id: this.selectedCard
      }
      console.log(path)
      console.log(parameters)
      axios.post(path, parameters)
              .then((res) => {
                console.log(res)
                var order_id = res.data
                console.log(order_id)
                this.finalizePurchase(order_id)
              })
              .catch((error) => {
                // eslint-disable-next-line
                toastr.error('', 'Order error.',
                        {timeOut: 1500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
                console.log(error)
              })
    },
    finalizePurchase(order_id) {
      console.log(this.cart)
      for (let i = 0; i < this.cart.length; i += 1) {
        var item = this.cart[i]
        console.log(item)
        var price = item.price * item.quant
        const path = api + 'article-order/' + order_id
        const parameters = {
          price: price,
          id_book: item.id,
          quant: item.quant
        }
        axios.post(path, parameters)
                .then(() => {
                  console.log('Order done')
                  console.log('Article added')
                  bus.emit('empty_cart')
                })
                .catch((error) => {
                  // eslint-disable-next-line
                  console.log(error)
                  const path_del = api + 'order/' + order_id
                  axios.delete(path_del)
                          .then(() => {
                            console.log('Bad Order deleted')
                            return
                          })
                          .catch((error) => {
                            console.log(error)
                            return
                          })
                })
      }
    },
    changeSend(w) {
      this.selected = w
      this.showPayButtonChk()
    },
    changeCard(w) {
      this.selectedCard = w
      this.showPayButtonChk()
    },
    changeAdd(w) {
      this.selectedAdd = w
      this.showPayButtonChk()
    },
    showPayButtonChk(){
      if(this.selectedCard!=-1 && this.selectedAdd!=-1 && this.selected!=0){
        document.getElementById('canpay').style.display = 'block'
        document.getElementById('nocanpay').style.display = 'none'
      }else{
        document.getElementById('nocanpay').style.display = 'block'
        document.getElementById('canpay').style.display = 'none'
      }
    },
    cardToDB() {
      const path = api + 'account/' + this.id + '/card'
      axios.post(path, this.addCardForm)
          // eslint-disable-next-line no-unused-vars
          .then((res) => {
            toastr.success('', '¡Tarjeta guardada con éxito!',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
            this.getCards()
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.log(error)
            toastr.error('', 'Algo no salió como se esperaba... pruebe de nuevo mas tarde',
                {
                  timeOut: 1500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
            this.getCards()
          })
    },
    addCard() {
      this.addCardForm.card_owner = document.getElementById('paymentTitular').value
      this.addCardForm.number = document.getElementById('paymentNumber').value
      this.addCardForm.date = document.getElementById('paymentEndDate').value
      this.addCardForm.payment_method = document.getElementById('paymentMethod').value

      if (this.addCardForm.card_owner == '' || this.addCardForm.number == '' || this.addCardForm.date == ''
          || this.addCardForm.payment_method == '') {
        toastr.info('', 'Rellena los campos obligatorios para generar la consulta.',
            {
              timeOut: 2500,
              progressBar: true,
              newestOnTop: true,
              positionClass: 'toast-bottom-right',
              preventDuplicates: true
            })
      } else if (this.addCardForm.number.length != 16) {
        toastr.info('', 'El numero de cuenta debe contener 16 digitos.',
            {
              timeOut: 2500,
              progressBar: true,
              newestOnTop: true,
              positionClass: 'toast-bottom-right',
              preventDuplicates: true
            })

      } else if (!this.validateEndDate(this.addCardForm.date)) {
        toastr.error('', 'Fecha de caducidad no válida.',
            {
              timeOut: 2500,
              progressBar: true,
              newestOnTop: true,
              positionClass: 'toast-bottom-right',
              preventDuplicates: true
            })
      } else {
        this.cardToDB()
      }
      document.getElementById('paymentTitular').value = ''
      document.getElementById('paymentNumber').value = ''
      document.getElementById('paymentEndDate').value = ''
      document.getElementById('paymentMethod').value = ''
    },
    deleteCard(card_id) {
      const path = api + 'account/' + this.id + '/card/' + card_id
      axios.delete(path)
          // eslint-disable-next-line no-unused-vars
          .then((res) => {
            toastr.success('', '¡Tarjeta eliminada con éxito!',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
            this.getCards()
            this.changeCard(-1)
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.log(error)
            toastr.error('', 'Algo no salió como se esperaba... pruebe de nuevo mas tarde',
                {
                  timeOut: 1500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
            this.getCards()
          })
    },
    validateEndDate(date) {
      if (date.length == 7) {
        var count = 0
        for (var i = 0; i < date.length; i++) {
          try {
            if (count == 2) {
              if (date[i] != '/')
                return false
              count += 1
            } else {
              parseInt(date[i])
              count += 1
            }
          } catch (error) {
            return false
          }
        }
        return true
      } else
        return false
    },
    updateAddressModal(address_id) {
      this.address_edit = address_id

      if (this.address_edit == -1) {
        this.newAddressLabel = ''
        this.newAddressName = ''
        this.newAddressSurname = ''
        this.newAddressRoad = ''
        this.newAddressNumber = ''
        this.newAddressCode = ''
        this.newAddressCity = ''
        this.newAddressProvince = ''
        this.newAddressPhone = ''
      } else {
        for (var i = 0; i < this.addresses.length; i++) {
          var address = this.addresses[i]

          if (address.id == this.address_edit) {
            this.newAddressLabel = address.label_name
            this.newAddressName = address.name
            this.newAddressSurname = address.surnames
            this.newAddressRoad = address.street
            this.newAddressNumber = address.number
            this.newAddressCode = address.cp
            this.newAddressCity = address.city
            this.newAddressProvince = address.province
            this.newAddressPhone = address.telf
          }
        }
      }
    },
    addAddress() {
      if (this.newAddressName == '' || this.newAddressSurname == '' || this.newAddressRoad == ''
          || this.newAddressNumber == '' || this.newAddressCode == '' || this.newAddressCity == ''
          || this.newAddressProvince == '' || this.newAddressPhone == '') {
        toastr.info('', 'Rellena los campos obligatorios para generar la consulta.',
            {
              timeOut: 2500,
              progressBar: true,
              newestOnTop: true,
              positionClass: 'toast-bottom-right',
              preventDuplicates: true
            })
      } else if (this.newAddressCode.length != 5) {
        toastr.info('', 'El codigo postal debe contener 4 digitos.',
            {
              timeOut: 2500,
              progressBar: true,
              newestOnTop: true,
              positionClass: 'toast-bottom-right',
              preventDuplicates: true
            })
      } else if (this.newAddressPhone.length != 9) {
        toastr.info('', 'El numero de telefono debe contener 9 digitos.',
            {
              timeOut: 2500,
              progressBar: true,
              newestOnTop: true,
              positionClass: 'toast-bottom-right',
              preventDuplicates: true
            })
      } else {
        var tmp = {
          "label_name": this.newAddressLabel,
          "name": this.newAddressName,
          "surnames": this.newAddressSurname,
          "street": this.newAddressRoad,
          "number": this.newAddressNumber,
          "cp": this.newAddressCode,
          "city": this.newAddressCity,
          "province": this.newAddressProvince,
          "telf": this.newAddressPhone
        }
        if (this.address_edit != -1)
          this.addressUpdateToDB(tmp)
        else
          this.addressToDB(tmp)
      }
    },
    addressToDB(parameters) {
      const path = api + 'account/' + this.id + '/address'

      axios.post(path, parameters)
          // eslint-disable-next-line no-unused-vars
          .then((res) => {
            toastr.success('', '¡Dirección guardada con éxito!',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
            this.getAddresses()
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.log(error)
            toastr.error('', 'Algo no salió como se esperaba... pruebe de nuevo mas tarde',
                {
                  timeOut: 1500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
            this.getAddresses()
          })
    },
    addressUpdateToDB(parameters) {
      const path = api + 'account/' + this.id + '/address/' + this.address_edit

      axios.put(path, parameters)
          // eslint-disable-next-line no-unused-vars
          .then((res) => {
            toastr.success('', '¡Dirección guardada con éxito!',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
            this.getAddresses()
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.log(error)
            toastr.error('', 'Algo no salió como se esperaba... pruebe de nuevo mas tarde',
                {
                  timeOut: 1500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
            this.getAddresses()
          })
    },
    deleteAddress(address_id) {
      const path = api + 'account/' + this.id + '/address/' + address_id
      axios.delete(path)
          // eslint-disable-next-line no-unused-vars
          .then((res) => {
            toastr.success('', '¡Dirección eliminada con éxito!',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
            this.getAddresses()
            this.changeAdd(-1)
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.log(error)
            toastr.error('', 'Algo no salió como se esperaba... pruebe de nuevo mas tarde',
                {
                  timeOut: 1500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
            this.getAddresses()
          })

    },
    getCards() {
      var path = api + 'account/' + this.id + '/cards'
      axios.get(path)
          .then((res) => {
            this.cards = []
            var data = res.data.accounts_cards
            for (var i = 0; i < data.length; i++) {
              var tmp = {
                "id": data[i].id,
                "vendor": data[i].method,
                "expires": data[i].date,
                "number": data[i].number,
                "end_number": data[i].number,
                "cvc": "",
                "holder": data[i].card_owner
              }
              this.cards.push(tmp)
            }
            this.cardNumber = this.cards.length
          })
          .catch((error) => {
            console.log(error)
            toastr.error('', 'No se ha podido recuperar las tarjetas.',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
          })
    },
    getAddresses() {
      var path = api + 'account/' + this.id + '/addresses'

      axios.get(path)
          .then((res) => {
            this.addresses = res.data.accounts_addresses
            this.addressNumber = this.addresses.length
          })
          .catch((error) => {
            console.log(error)
            toastr.error('', 'No se ha podido recuperar las direcciones.',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
          })
    },
    getDatePlus(days) {
      var today = new Date();
      today.setDate(today.getDate() + days);
      var dd = String(today.getDate()).padStart(2, '0');
      var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
      var yyyy = today.getFullYear();
      return dd + "/" + mm + "/" + yyyy;
    }
  }
}
</script>

<style scoped>

</style>