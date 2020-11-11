<style>

@import url("../assets/toastr.css");
@import url("../assets/animate.min.css");
@import url("../assets/book_info.css");

</style>
<template>
  <div class="front-container">
    <div style="max-width: 1400px">
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
            integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
      <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
      <div class="card">
        <div class="card-header">
          <h3>Panel de control</h3>
        </div>
        <ul class="nav nav-pills mb-3" id="pills-tab" role="tablist">
          <li class="nav-item active" role="presentation">
            <a class="nav-link active" id="pills-orders-tab" data-toggle="pill" href="#pills-orders" role="tab"
               aria-controls="pills-orders" aria-selected="false">Tus pedidos</a>
          </li>
          <li class="nav-item" role="presentation">
            <a class="nav-link" id="pills-home-tab" data-toggle="pill" href="#pills-home" role="tab"
               aria-controls="pills-home" aria-selected="false">Perfil</a>
          </li>
          <li class="nav-item" role="presentation">
            <a class="nav-link" id="pills-directions-tab" data-toggle="pill" href="#pills-directions" role="tab"
               aria-controls="pills-directions" aria-selected="false">Direcciones</a>
          </li>
          <li class="nav-item" role="presentation">
            <a class="nav-link" id="pills-pay-tab" data-toggle="pill" href="#pills-pay" role="tab"
               aria-controls="pills-pay" aria-selected="false">Métodos de pago</a>
          </li>
          <li class="nav-item" role="presentation">
            <a class="nav-link" id="pills-economy-tab" data-toggle="pill" href="#pills-economy" role="tab"
               aria-controls="pills-economy" aria-selected="false">Rendimiento</a>
          </li>
        </ul>
        <div class="tab-content" id="pills-tabContent">
          <!-- ORDERS: view order history -->
          <div class="tab-pane fade show active" id="pills-orders" role="tabpanel" aria-labelledby="pills-orders-tab">
            <div class="container-fluid">
              <div class="table-responsive">
                <table class="table table-striped" style="text-align: left">
                  <thead>
                  <tr>
                    <th scope="col">Número pedido</th>
                    <th scope="col">Fecha</th>
                    <th scope="col">Total</th>
                    <th scope="col" class="text-right">Estado</th>
                    <th scope="col" class="text-right">Acciones</th>
                  </tr>
                  </thead>
                  <tbody>
                  <tr v-for="(item) in this.viewOrders" :key="item.id">
                    <td><b>#{{ item.id }}</b></td>
                    <td>{{ item.date }}</td>
                    <td>{{ item.total }}€</td>
                    <td class="text-right" v-if="item.state==0"><span class="badge badge-primary">Recibido</span></td>
                    <td class="text-right" v-if="item.state==1"><span class="badge badge-light">Preparado</span></td>
                    <td class="text-right" v-if="item.state==2"><span class="badge badge-info">Enviado</span></td>
                    <td class="text-right" v-if="item.state==3"><span class="badge badge-success">Entregado</span></td>
                    <td class="text-right" v-if="item.state==0">
                      <button class="btn btn-danger" @click="cancelOrder(item.id)">Cancelar</button>
                    </td>
                    <td class="text-right" v-if="item.state!=0">
                      <button class="btn btn-light" @click="viewOrder(item.id)">Ver pedido</button>
                    </td>
                  </tr>
                  </tbody>
                </table>
                <nav aria-label="...">
                  <ul class="pagination pagination-lg">
                    <span v-for="index in this.sOrders.length" :key="index">
                      <li class="page-item active" aria-current="page" v-if="cIndex == (index-1)">
                    <span class="page-link">
                      {{ index }}</span>
                    </li>
                      <li class="page-item"><a class="page-link" v-if="cIndex != (index-1)"
                                               @click="changeViewingOrders(index-1)">{{ index }}</a></li>
                    </span>
                  </ul>
                </nav>
              </div>
            </div>
          </div>
          <!-- PROFILE: edit data or change password -->
          <div class="tab-pane fade" id="pills-home" role="tabpanel" aria-labelledby="pills-home-tab">
            <div class="container-fluid">
              <div class="row">
                <div class="col" style="text-align: left">
                  <h5>Tus datos</h5>
                </div>
                <div class="col" style="text-align: right">
                  <button class="btn btn-warning my-2 my-sm-0 mr-2" type="submit" style="width: auto"
                          v-if="!editProfile"><i
                      class="fas fa-edit"
                      style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
                      class="navbartextbt" @click="modifyProfile">Modificar</a></button>
                  <button class="btn btn-success my-2 my-sm-0 mr-2" type="submit" style="width: auto"
                          v-if="editProfile"><i
                      class="fas fa-save"
                      style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
                      class="navbartextbt" @click="saveProfile">Guardar</a></button>
                </div>
              </div>
              <div class="row" style="text-align: left">
                <div class="col">
                  <div class="form-group">
                    <label for="exampleFormControlInput1">Nombre</label>
                    <input type="text" class="form-control"
                           placeholder="Aitor" :disabled="!editProfile">
                  </div>
                </div>
                <div class="col">
                  <label for="exampleFormControlInput1">Apellidos</label>
                  <input type="text" class="form-control" id="exampleFormControlInput1"
                         placeholder="Tilla Seca" :disabled="!editProfile">
                </div>
              </div>
              <div class="row" style="text-align: left">
                <div class="col">
                  <div class="form-group">
                    <label for="exampleFormControlInput1">Correo electrónico</label>
                    <input type="email" class="form-control"
                           placeholder="aitortilla@usa.gov.us" :disabled="!editProfile">
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col" style="text-align: left">
                  <h5>Cambiar contraseña</h5>
                </div>
                <div class="col" style="text-align: right">
                  <button class="btn btn-warning my-2 my-sm-0 mr-2" type="submit" style="width: auto" v-if="!editPass">
                    <i
                        class="fas fa-edit"
                        style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
                      class="navbartextbt" @click="changePassword">Cambiar</a></button>
                  <button class="btn btn-success my-2 my-sm-0 mr-2" type="submit" style="width: auto" v-if="editPass"><i
                      class="fas fa-save"
                      style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
                      class="navbartextbt" @click="savePassword">Guardar</a></button>
                </div>
              </div>
              <div class="row" style="text-align: left">
                <div class="col">
                  <div class="form-group">
                    <label for="exampleFormControlInput1">Contraseña actual</label>
                    <input type="password" class="form-control"
                           placeholder="" :disabled="!editPass">
                  </div>
                </div>
                <div class="col">
                  <div class="form-group">
                    <label for="exampleFormControlInput1">Contraseña nueva</label>
                    <input type="password" class="form-control"
                           placeholder="" :disabled="!editPass">
                    <div class="progress">
                      <div class="progress-bar bg-success" role="progressbar" style="width: 30%" aria-valuenow="25"
                           aria-valuemin="0" aria-valuemax="100"> Todavía no funciona xD
                      </div>
                    </div>
                  </div>
                </div>
                <div class="col">
                  <div class="form-group">
                    <label for="exampleFormControlInput1">Repite contraseña nueva</label>
                    <input type="password" class="form-control"
                           placeholder="" :disabled="!editPass">
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- ADDRESS: edit data or change addresses -->
          <div class="tab-pane fade" id="pills-directions" role="tabpanel" aria-labelledby="pills-directions-tab">
            <div class="container-fluid">
              <div class="row">
                <div class="col" style="text-align: left">
                  <h5>Tus direcciones</h5>
                </div>
              </div>
              <div class="row row-cols-1 row-cols-sm-6">
                <div class="col mb-4" style="margin-right: 1.5rem" v-for="item in this.addresses" :key="item.id">
                  <div class="card h-100" style="width: 15.5rem; max-width: 16rem; text-align: left">
                    <div class="card-header">
                      {{ item.add_name }}
                    </div>
                    <ul class="list-group list-group-flush">
                      <li class="list-group-item">
                        {{ item.name }} {{ item.surnames }}<br>
                        {{ item.street }}, {{ item.number }}<br>
                        {{ item.cp }} {{ item.city }}, {{ item.province }}<br>
                        {{ item.telf }}
                      </li>
                    </ul>
                    <div class="card-header" style="text-align: right !important">
                      <a href="" style="text-align: right; color: #3b494d; margin-right: 1.5em"><i
                          class="fas fa-pen"></i></a>
                      <a href="" style="text-align: right; color: red"><i class="fas fa-trash-alt"></i></a>
                    </div>
                  </div>
                </div>
                <div class="col mb-4" style="margin-right: 1.5rem" v-if="addressNumber < 4">
                  <div class="card h-100" style="width: 15.5rem; max-width: 16rem; text-align: center">
                    <button style="color: #3b494d; height: 100%" type="submit"
                            data-toggle="modal" data-target="#exampleModal"><i class="fas fa-plus"
                                                                               style="font-size: 6em; top: 50%"></i>
                    </button>
                  </div>

                </div>
              </div>
            </div>
          </div>
          <!-- PAYMENT: edit or change payment methods -->
          <div class="tab-pane fade" id="pills-pay" role="tabpanel" aria-labelledby="pills-pay-tab">
            <div class="container-fluid">
              <div class="row">
                <div class="col" style="text-align: left">
                  <h5>Tus tarjetas</h5>
                </div>
              </div>
              <div class="row row-cols-1 row-cols-sm-6">
                <div class="col mb-4" style="margin-right: 1.5rem" v-for="item in this.cards" :key="item.id">
                  <div class="card h-100" style="width: 15.5rem; max-width: 16rem; text-align: left">
                    <ul class="list-group list-group-flush">
                      <li class="list-group-item">
                        <span v-if="item.vendor == 'MASTERCARD'"><i class="fab fa-cc-mastercard"
                                                                    style="font-size: 1.8em"></i></span>
                        <span v-if="item.vendor == 'VISA'"><i class="fab fa-cc-visa"
                                                              style="font-size: 1.8em"></i></span>
                        <span v-if="item.vendor == 'JCB'"><i class="fab fa-cc-jcb" style="font-size: 1.8em"></i></span>
                        <span v-if="item.vendor == 'DISCOVER'"><i class="fab fa-cc-discover"
                                                                  style="font-size: 1.8em"></i></span><br>
                        <b>Titular:</b> {{ item.holder }}<br>
                        <b>Termina en:</b> {{ item.end_number }}<br>
                        <b>Caduca:</b> {{ item.expires }}
                      </li>
                    </ul>
                    <div class="card-header" style="text-align: right !important">
                      <a href="" style="text-align: right; color: red"><i class="fas fa-trash-alt"></i></a>
                    </div>
                  </div>
                </div>
                <div class="col mb-4" style="margin-right: 1.5rem" v-if="cardNumber < 3">
                  <div class="card h-100" style="width: 15.5rem; max-width: 16rem; text-align: center !important">
                    <button style="color: #3b494d; height: 100%" type="submit"
                            data-toggle="modal" data-target="#exampleModal"><i class="fas fa-plus"
                                                                               style="font-size: 6em; top: 50%"></i>
                    </button>
                  </div>
                </div>
              </div>
            </div>
            <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
                 aria-hidden="true">
              <div class="modal-dialog" role="document"
                   style="min-height: calc(100vh - 60px); display: flex;flex-direction: column;justify-content: center;overflow: auto;">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Añadir una tarjeta</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                      <span aria-hidden="true">&times;</span>
                    </button>
                  </div>
                  <div class="modal-body">
                    <form>
                      <div class="form-group" style="text-align: left">
                        <label for="reviewTitle" class="col-form-label">Título</label>
                        <input type="text" class="form-control" id="reviewTitle"
                               v-model="ratingTitle">
                      </div>
                      <div class="form-group" style="text-align: left">
                        <label class="col-form-label">Tu valoración:</label>

                      </div>
                      <div class="form-group" style="text-align: left">
                        <label for="reviewText" class="col-form-label">Explayate (si quieres 😉):</label>
                        <textarea class="form-control" id="reviewText" rows="5" maxlength="250"
                                  placeholder="¿Qué te ha parecido el libro? ¿A quién se lo recomendarias?"
                                  v-model="ratingText"></textarea>
                        <div id="charNum"></div>
                      </div>
                      <div class="form-group" style="text-align: center">
                          <span class="badge badge-danger animate__animated animate__rubberBand"
                                style="font-size: 1.5em" v-if="ratingText != ''">¡NO NOS HAGAS SPOILER!</span>
                      </div>
                    </form>
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal" @click="addRatingNumber = 0">
                      Cancelar
                    </button>
                    <button type="button" class="btn" style="background: #2bc4ed; color: white" data-dismiss="modal"
                            @click="postReview"
                            :disabled="ratingTitle == '' || ratingText == '' || addRatingNumber == 0">
                      Enviar
                    </button>
                  </div>
                </div>
              </div>
            </div>

          </div>
          <!-- ECONOMY: for admin only -->
          <div class="tab-pane fade" id="pills-economy" role="tabpanel" aria-labelledby="pills-pay-tab">
            <!--<div class="container-fluid">
              <div class="row">
                <div class="col-md-6 col-xl-4">
                  <div class="card mb-3 widget-content">
                    <div class="widget-content-outer">
                      <div class="widget-content-wrapper">
                        <div class="widget-content-left">
                          <div class="widget-heading">Total Orders</div>
                          <div class="widget-subheading">Last year expenses</div>
                        </div>
                        <div class="widget-content-right">
                          <div class="widget-numbers text-success">1896</div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="col-md-6 col-xl-4">
                  <div class="card mb-3 widget-content">
                    <div class="widget-content-outer">
                      <div class="widget-content-wrapper">
                        <div class="widget-content-left">
                          <div class="widget-heading">Products Sold</div>
                          <div class="widget-subheading">Revenue streams</div>
                        </div>
                        <div class="widget-content-right">
                          <div class="widget-numbers text-warning">$3M</div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="col-md-6 col-xl-4">
                  <div class="card mb-3 widget-content">
                    <div class="widget-content-outer">
                      <div class="widget-content-wrapper">
                        <div class="widget-content-left">
                          <div class="widget-heading">Followers</div>
                          <div class="widget-subheading">People Interested</div>
                        </div>
                        <div class="widget-content-right">
                          <div class="widget-numbers text-danger">45,9%</div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="d-xl-none d-lg-block col-md-6 col-xl-4">
                  <div class="card mb-3 widget-content">
                    <div class="widget-content-outer">
                      <div class="widget-content-wrapper">
                        <div class="widget-content-left">
                          <div class="widget-heading">Income</div>
                          <div class="widget-subheading">Expected totals</div>
                        </div>
                        <div class="widget-content-right">
                          <div class="widget-numbers text-focus">$147</div>
                        </div>
                      </div>
                      <div class="widget-progress-wrapper">
                        <div class="progress-bar-sm progress-bar-animated-alt progress">
                          <div class="progress-bar bg-info" role="progressbar" aria-valuenow="54" aria-valuemin="0"
                               aria-valuemax="100" style="width: 54%;"></div>
                        </div>
                        <div class="progress-sub-label">
                          <div class="sub-label-left">Expenses</div>
                          <div class="sub-label-right">100%</div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="tab-content">
              <div class="tab-pane tabs-animation fade show active" id="tab-content-0" role="tabpanel">
                <div class="row">
                  <div class="col-md-6">
                    <div class="main-card mb-3 card">
                      <div class="card-body">
                        <h5 class="card-title">Pie Chart</h5>
                        <canvas id="chart-area"></canvas>
                      </div>
                    </div>
                    <div class="main-card mb-3 card">
                      <div class="card-body">
                        <h5 class="card-title">Radar Chart</h5>
                        <canvas id="radar-chart"></canvas>
                      </div>
                    </div>
                  </div>
                  <div class="col-md-6">
                    <div class="main-card mb-3 card">
                      <div class="card-body">
                        <h5 class="card-title">Doughnut</h5>
                        <canvas id="doughnut-chart"></canvas>
                      </div>
                    </div>
                    <div class="main-card mb-3 card">
                      <div class="card-body">
                        <h5 class="card-title">Polar Chart</h5>
                        <canvas id="polar-chart"></canvas>
                      </div>
                    </div>
                  </div>
                </div>

              </div>
              <div class="tab-pane tabs-animation fade" id="tab-content-1" role="tabpanel">
                <div class="row">
                  <div class="col-md-6">
                    <div class="main-card mb-3 card">
                      <div class="card-body">
                        <h5 class="card-title">Vertical Bars</h5>
                        <canvas id="canvas"></canvas>
                      </div>
                    </div>
                    <div class="main-card mb-3 card">
                      <div class="card-body">
                        <h5 class="card-title">Horizontal Bars</h5>
                        <canvas id="chart-horiz-bar"></canvas>
                      </div>
                    </div>
                  </div>
                  <div class="col-md-6">
                    <div class="main-card mb-3 card">
                      <div class="card-body">
                        <h5 class="card-title">Line Chart</h5>
                        <div style="height: 400px">
                          <canvas id="line-chart"></canvas>
                        </div>
                      </div>
                    </div>
                    <div class="main-card mb-3 card">
                      <div class="card-body">
                        <h5 class="card-title">Stacked Bars</h5>
                        <canvas id="stacked-bars-chart"></canvas>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>-->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
// eslint-disable-next-line no-unused-vars
import {bus} from '../main.js'
// eslint-disable-next-line no-unused-vars
import axios from 'axios'

export default {
  name: "ControlPanel",
  data() {
    return {
      editProfile: false,
      editPass: false,
      orders: [
        {
          "id": 1,
          "date": "25/11/2019",
          "total": 36.99,
          "shipping": 5,
          "taxes": 7.76,
          "state": 0,
          "adress": "Calle Sants 235, 4º A",
          "articles": [
            {
              "id": 0,
              "price": 36.99,
            }
          ],
          "card": {}
        },
        {
          "id": 2,
          "date": "25/11/2019",
          "total": 36.99,
          "shipping": 5,
          "taxes": 7.76,
          "state": 2,
          "adress": "Calle Sants 235, 4º A",
          "articles": [
            {
              "id": 0,
              "price": 36.99,
            }
          ]
        },
        {
          "id": 3,
          "date": "25/11/2019",
          "total": 36.99,
          "shipping": 5,
          "taxes": 7.76,
          "state": 1,
          "adress": "Calle Sants 235, 4º A",
          "articles": [
            {
              "id": 0,
              "price": 36.99,
            }
          ]
        },
        {
          "id": 4,
          "date": "25/11/2019",
          "total": 36.99,
          "shipping": 5,
          "taxes": 7.76,
          "state": 1,
          "adress": "Calle Sants 235, 4º A",
          "articles": [
            {
              "id": 0,
              "price": 36.99,
            }
          ]
        },
        {
          "id": 1,
          "date": "25/11/2019",
          "total": 36.99,
          "shipping": 5,
          "taxes": 7.76,
          "state": 3,
          "adress": "Calle Sants 235, 4º A",
          "articles": [
            {
              "id": 0,
              "price": 36.99,
            }
          ]
        }, {
          "id": 1,
          "date": "25/11/2019",
          "total": 36.99,
          "shipping": 5,
          "taxes": 7.76,
          "state": 0,
          "adress": "Calle Sants 235, 4º A",
          "articles": [
            {
              "id": 0,
              "price": 36.99,
            }
          ]
        },
        {
          "id": 1,
          "date": "25/11/2019",
          "total": 36.99,
          "shipping": 5,
          "taxes": 7.76,
          "state": 0,
          "adress": "Calle Sants 235, 4º A",
          "articles": [
            {
              "id": 0,
              "price": 36.99,
            }
          ]
        }, {
          "id": 1,
          "date": "25/11/2019",
          "total": 36.99,
          "shipping": 5,
          "taxes": 7.76,
          "state": 0,
          "adress": "Calle Sants 235, 4º A",
          "articles": [
            {
              "id": 0,
              "price": 36.99,
            }
          ]
        }, {
          "id": 1,
          "date": "25/11/2019",
          "total": 36.99,
          "shipping": 5,
          "taxes": 7.76,
          "state": 0,
          "adress": "Calle Sants 235, 4º A",
          "articles": [
            {
              "id": 0,
              "price": 36.99,
            }
          ]
        }, {
          "id": 1,
          "date": "25/11/2019",
          "total": 36.99,
          "shipping": 5,
          "taxes": 7.76,
          "state": 0,
          "adress": "Calle Sants 235, 4º A",
          "articles": [
            {
              "id": 0,
              "price": 36.99,
            }
          ]
        }, {
          "id": 1,
          "date": "25/11/2019",
          "total": 36.99,
          "shipping": 5,
          "taxes": 7.76,
          "state": 0,
          "adress": "Calle Sants 235, 4º A",
          "articles": [
            {
              "id": 0,
              "price": 36.99,
            }
          ]
        }, {
          "id": 1,
          "date": "25/11/2019",
          "total": 36.99,
          "shipping": 5,
          "taxes": 7.76,
          "state": 0,
          "adress": "Calle Sants 235, 4º A",
          "articles": [
            {
              "id": 0,
              "price": 36.99,
            }
          ]
        }, {
          "id": 1,
          "date": "25/11/2019",
          "total": 36.99,
          "shipping": 5,
          "taxes": 7.76,
          "state": 0,
          "adress": "Calle Sants 235, 4º A",
          "articles": [
            {
              "id": 0,
              "price": 36.99,
            }
          ]
        }, {
          "id": 1,
          "date": "25/11/2019",
          "total": 36.99,
          "shipping": 5,
          "taxes": 7.76,
          "state": 0,
          "adress": "Calle Sants 235, 4º A",
          "articles": [
            {
              "id": 0,
              "price": 36.99,
            }
          ]
        }, {
          "id": 1,
          "date": "25/11/2019",
          "total": 36.99,
          "shipping": 5,
          "taxes": 7.76,
          "state": 0,
          "adress": "Calle Sants 235, 4º A",
          "articles": [
            {
              "id": 0,
              "price": 36.99,
            }
          ]
        }, {
          "id": 1,
          "date": "25/11/2019",
          "total": 36.99,
          "shipping": 5,
          "taxes": 7.76,
          "state": 0,
          "adress": "Calle Sants 235, 4º A",
          "articles": [
            {
              "id": 0,
              "price": 36.99,
            }
          ]
        }, {
          "id": 1,
          "date": "25/11/2019",
          "total": 36.99,
          "shipping": 5,
          "taxes": 7.76,
          "state": 0,
          "adress": "Calle Sants 235, 4º A",
          "articles": [
            {
              "id": 0,
              "price": 36.99,
            }
          ]
        }, {
          "id": 1,
          "date": "25/11/2019",
          "total": 36.99,
          "shipping": 5,
          "taxes": 7.76,
          "state": 0,
          "adress": "Calle Sants 235, 4º A",
          "articles": [
            {
              "id": 0,
              "price": 36.99,
            }
          ]
        }, {
          "id": 1,
          "date": "25/11/2019",
          "total": 36.99,
          "shipping": 5,
          "taxes": 7.76,
          "state": 0,
          "adress": "Calle Sants 235, 4º A",
          "articles": [
            {
              "id": 0,
              "price": 36.99,
            }
          ]
        }, {
          "id": 1,
          "date": "25/11/2019",
          "total": 36.99,
          "shipping": 5,
          "taxes": 7.76,
          "state": 0,
          "adress": "Calle Sants 235, 4º A",
          "articles": [
            {
              "id": 0,
              "price": 36.99,
            }
          ]
        }, {
          "id": 1,
          "date": "25/11/2019",
          "total": 36.99,
          "shipping": 5,
          "taxes": 7.76,
          "state": 0,
          "adress": "Calle Sants 235, 4º A",
          "articles": [
            {
              "id": 0,
              "price": 36.99,
            }
          ]
        }, {
          "id": 1,
          "date": "25/11/2019",
          "total": 36.99,
          "shipping": 5,
          "taxes": 7.76,
          "state": 0,
          "adress": "Calle Sants 235, 4º A",
          "articles": [
            {
              "id": 0,
              "price": 36.99,
            }
          ]
        }, {
          "id": 1,
          "date": "25/11/2019",
          "total": 36.99,
          "shipping": 5,
          "taxes": 7.76,
          "state": 0,
          "adress": "Calle Sants 235, 4º A",
          "articles": [
            {
              "id": 0,
              "price": 36.99,
            }
          ]
        }, {
          "id": 1,
          "date": "25/11/2019",
          "total": 36.99,
          "shipping": 5,
          "taxes": 7.76,
          "state": 0,
          "adress": "Calle Sants 235, 4º A",
          "articles": [
            {
              "id": 0,
              "price": 36.99,
            }
          ]
        }
      ],
      sOrders: [],
      viewOrders: [],
      numberOfOrders: 0,
      numberOfPages: 0,
      maxPerPage: 10,
      cIndex: 0,
      addressNumber: 0,
      cardNumber: 0,
      cards: [
        {
          "id": 0,
          "vendor": "VISA",
          "expires": "01/2025",
          "number": "1234",
          "end_number": "1234",
          "cvc": "115",
          "holder": "Borat Led"
        }
      ],
      addresses: [
        {
          "id": 0,
          "add_name": "casa",
          "name": "Pepito",
          "surnames": "Asd",
          "street": "Calle Sants",
          "number": 32,
          "cp": "08014",
          "city": "Barcelona",
          "province": "Barcelona",
          "telf": "645214587"
        },
        {
          "id": 0,
          "add_name": "casa",
          "name": "Pepito",
          "surnames": "Asd",
          "street": "Calle Sants",
          "number": 32,
          "cp": "08014",
          "city": "Barcelona",
          "province": "Barcelona",
          "telf": "645214587"
        }
      ]
    }
  },
  created() {
    this.splitOrders()
    this.getAddresses()
    this.getCards()
  },
  methods: {
    getCards() {
      this.cardNumber = this.cards.length
    },
    getAddresses() {
      this.addressNumber = this.addresses.length
    },
    changeViewingOrders(index) {
      this.viewOrders = this.sOrders[index]
      this.cIndex = index
    },
    splitOrders() {
      this.numberOfOrders = this.orders.length
      this.numberOfPages = Math.ceil(this.orders.length / this.maxPerPage)
      let i
      let arr = []
      for (i = 0; i < (this.numberOfPages - 1); i++) {
        arr = this.orders.slice(i * this.maxPerPage, this.maxPerPage * (i + 1))
        this.sOrders.push(arr)
      }
      this.sOrders.push(this.orders.slice(-(this.orders.length % this.maxPerPage)))
      this.viewOrders = this.sOrders[0]
    },
    cancelOrder(id) {
      console.log(id)
    },
    viewOrder(id) {
      console.log(id)
    },
    modifyProfile() {
      this.editProfile = true
    },
    saveProfile() {
      this.editProfile = false
    },
    changePassword() {
      this.editPass = true
    },
    savePassword() {
      this.editPass = false
    }
  }
}
</script>

<style scoped>
.front-container {
  width: 75%;
  margin: auto;
  margin-top: 2em;
  margin-bottom: 1em;
}
</style>