<style>

@import url("../assets/toastr.css");
@import url("../assets/animate.min.css");
@import url("../assets/book_info.css");

</style>
<template>
  <div class="container front-container">
    <div style="max-width: 1400px; ">
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
            integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
      <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
      <link rel="stylesheet" href="https://unpkg.com/@fracto/vue-credit-card/dist/VueCreditCard.css">
      <div class="card">
        <div class="card-header">
          <h3>Panel de control</h3>
        </div>
        <ul class="nav nav-pills flex-column flex-sm-row" id="pills-tab" role="tablist">
          <li class="flex-sm-fill text-sm-center nav-item active myPillItems" role="presentation">
            <a class="nav-link active" id="pills-orders-tab" data-toggle="pill" href="#pills-orders" role="tab"
               aria-controls="pills-orders" aria-selected="false">Tus pedidos</a>
          </li>
          <li class="flex-sm-fill text-sm-center nav-item myPillItems" role="presentation">
            <a class="nav-link" id="pills-home-tab" data-toggle="pill" href="#pills-home" role="tab"
               aria-controls="pills-home" aria-selected="false">Perfil</a>
          </li>
          <li class="flex-sm-fill text-sm-center nav-item myPillItems" role="presentation">
            <a class="nav-link" id="pills-directions-tab" data-toggle="pill" href="#pills-directions" role="tab"
               aria-controls="pills-directions" aria-selected="false">Direcciones</a>
          </li>
          <li class="flex-sm-fill text-sm-center nav-item myPillItems" role="presentation">
            <a class="nav-link" id="pills-pay-tab" data-toggle="pill" href="#pills-pay" role="tab"
               aria-controls="pills-pay" aria-selected="false">Métodos de pago</a>
          </li>
          <li class="flex-sm-fill text-sm-center nav-item myPillItems" role="presentation" v-if="type == 2">
            <a class="nav-link" id="pills-economy-tab" data-toggle="pill" href="#pills-economy" role="tab"
               aria-controls="pills-economy" aria-selected="false">Rendimiento</a>
          </li>
        </ul>
        <div class="tab-content mt-3" id="pills-tabContent">
          <!-- ORDERS: view order history -->
          <div class="tab-pane fade show active" id="pills-orders" role="tabpanel" aria-labelledby="pills-orders-tab">
            <div class="container-fluid">
              <ul class="nav nav-pills flex-column flex-sm-row" role="tablist">
                <li class="flex-sm-fill text-sm-center nav-item active myPillItems" role="presentation">
                  <a class="nav-link active" data-toggle="pill" href="#pills-all" role="tab"
                     aria-controls="pills-all" aria-selected="false">Todas</a>
                </li>
                <li class="flex-sm-fill text-sm-center nav-item active myPillItems" role="presentation">
                  <a class="nav-link" data-toggle="pill" href="#pills-0" role="tab"
                     aria-controls="pills-0" aria-selected="false">En progreso</a>
                </li>
                <li class="flex-sm-fill text-sm-center nav-item myPillItems" role="presentation">
                  <a class="nav-link" data-toggle="pill" href="#pills-1" role="tab"
                     aria-controls="pills-1" aria-selected="false">Enviado</a>
                </li>
                <li class="flex-sm-fill text-sm-center nav-item myPillItems" role="presentation">
                  <a class="nav-link" data-toggle="pill" href="#pills-2" role="tab"
                     aria-controls="pills-2" aria-selected="false">Recibido</a>
                </li>
              </ul>

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
              <div class="row">
                <div class="col-12 col-lg-4 mb-4 myAddressCard" v-for="item in this.addresses" :key="item.id">
                  <div class="card" style="text-align: left">
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
                          <p style="cursor: pointer; margin-bottom: 0em; text-align: right; color: red" @click="deleteAddress(item.id)">
                             <i class="fas fa-trash-alt"></i></p>
                        </div>
                    </div>
                  </div>
                </div>
                <div class="col-12 col-lg-4 mb-4 myAddressCard" v-if="this.addressNumber < 3">
                  <div class="card h-100" style="text-align: center">
                    <button style="color: #3b494d; height: 100%" type="submit"
                            data-toggle="modal" data-target="#modalAddress" data-whatever="@getbootstrap"
                            @click="updateAddressModal(-1)">
                      <i class="fas fa-plus" style="font-size: 6em; top: 50%"></i>
                    </button>
                  </div>
                </div>
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
          <!-- PAYMENT: edit or change payment methods -->
          <div class="tab-pane fade" id="pills-pay" role="tabpanel" aria-labelledby="pills-pay-tab">
            <div class="container-fluid">
              <div class="row">
                <div class="col" style="text-align: left">
                  <h5>Tus tarjetas</h5>
                </div>
              </div>
              <div class="row">
                <div class="col-12 col-lg-6 mb-4 myPaymentCard" v-for="item in this.cards" :key="item.id">
                  <div class="card" style=" text-align: left">
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
                      <p style="cursor: pointer; text-align: right; margin-bottom: 0em; color: red" @click="deleteCard(item.id)"><i class="fas fa-trash-alt"></i></p>
                    </div>
                  </div>
                </div>
                <div class="col-12 col-lg-6 mb-4 myPaymentCard" v-if="this.cardNumber < 2">
                  <div class="card h-100">
                    <button style="color: #3b494d; height: 100%" type="submit" data-toggle="modal"
                            data-target="#modalPayment" data-whatever="@getbootstrap">
                      <i class="fas fa-plus" style="font-size: 6em; top: 50%"></i>
                    </button>
                    <div class="modal fade" id="modalPayment" tabindex="-1" role="dialog"
                         aria-labelledby="modalAddressLabel"
                         aria-hidden="true">
                      <div class="modal-dialog" role="document"
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
                                <label for="paymentTitular" class="col-form-label">Nombre de titular</label>
                                <input type="text" class="form-control" id="paymentTitular">
                              </div>
                              <div class="form-group" style="text-align: left">
                                <label for="paymentNumber" class="col-form-label">Número de tarjeta</label>
                                <input type="number" class="form-control" id="paymentNumber">
                              </div>
                              <div class="form-group" style="text-align: left">
                                <label for="paymentEndDate" class="col-form-label">Fecha de vencimiento</label>
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


                    asd

                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">
                      Cancelar
                    </button>
                    <button type="button" class="btn" style="background: #2bc4ed; color: white" data-dismiss="modal">
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
            <!-- ORDERS : view order history -->
            <div class="tab-pane fade show active" id="pills-all" role="tabpanel" aria-labelledby="pills-orders-tab">
              <div class="container-fluid">
                <ul class="nav nav-pills flex-column flex-sm-row" role="tablist">
                  <li class="flex-sm-fill text-sm-center nav-item active myPillItems" role="presentation">
                    <a class="nav-link active" data-toggle="pill" href="#pills-all" role="tab"
                       aria-controls="pills-all" aria-selected="false">Todas</a>
                  </li>
                  <li class="flex-sm-fill text-sm-center nav-item active myPillItems" role="presentation">
                    <a class="nav-link active" data-toggle="pill" href="#pills-0" role="tab"
                       aria-controls="pills-0" aria-selected="false">En progreso</a>
                  </li>
                  <li class="flex-sm-fill text-sm-center nav-item myPillItems" role="presentation">
                    <a class="nav-link" data-toggle="pill" href="#pills-1" role="tab"
                       aria-controls="pills-1" aria-selected="false">Enviado</a>
                  </li>
                  <li class="flex-sm-fill text-sm-center nav-item myPillItems" role="presentation">
                    <a class="nav-link" data-toggle="pill" href="#pills-2" role="tab"
                       aria-controls="pills-2" aria-selected="false">Recibido</a>
                  </li>
                </ul>
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
                    <tr v-for="(item) in this.orders" :key="item.id">
                      <td><b>#{{ item.id }}</b></td>
                      <td>{{ item.date }}</td>
                      <td>{{ item.total }}€</td>
                      <td class="text-right" v-if="item.state==0"><span class="badge badge-primary">Recibido</span></td>
                      <td class="text-right" v-if="item.state==1"><span class="badge badge-light">Preparado</span></td>
                      <td class="text-right" v-if="item.state==2"><span class="badge badge-info">Enviado</span></td>
                      <td class="text-right" v-if="item.state==3"><span class="badge badge-success">Entregado</span>
                      </td>
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
            <!-- ORDERS IN PROGRESS: view order in progress history -->
            <div class="tab-pane fade show active" id="pills-0" role="tabpanel" aria-labelledby="pills-orders-tab">
              <div class="container-fluid">
                <ul class="nav nav-pills flex-column flex-sm-row" role="tablist">
                  <li class="flex-sm-fill text-sm-center nav-item active myPillItems" role="presentation">
                    <a class="nav-link active" data-toggle="pill" href="#pills-all" role="tab"
                       aria-controls="pills-all" aria-selected="false">Todas</a>
                  </li>
                  <li class="flex-sm-fill text-sm-center nav-item active myPillItems" role="presentation">
                    <a class="nav-link active" data-toggle="pill" href="#pills-0" role="tab"
                       aria-controls="pills-0" aria-selected="false">En progreso</a>
                  </li>
                  <li class="flex-sm-fill text-sm-center nav-item myPillItems" role="presentation">
                    <a class="nav-link" data-toggle="pill" href="#pills-1" role="tab"
                       aria-controls="pills-1" aria-selected="false">Enviado</a>
                  </li>
                  <li class="flex-sm-fill text-sm-center nav-item myPillItems" role="presentation">
                    <a class="nav-link" data-toggle="pill" href="#pills-2" role="tab"
                       aria-controls="pills-2" aria-selected="false">Recibido</a>
                  </li>
                </ul>
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
                    <tr v-for="(item) in this.stateOrdersInProgress" :key="item.id">
                      <td><b>#{{ item.id }}</b></td>
                      <td>{{ item.date }}</td>
                      <td>{{ item.total }}€</td>
                      <td class="text-right" v-if="item.state==0"><span class="badge badge-primary">Recibido</span></td>
                      <td class="text-right" v-if="item.state==1"><span class="badge badge-light">Preparado</span></td>
                      <td class="text-right" v-if="item.state==2"><span class="badge badge-info">Enviado</span></td>
                      <td class="text-right" v-if="item.state==3"><span class="badge badge-success">Entregado</span>
                      </td>
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
            <!-- ORDERS SEND: view order send history -->
            <div class="tab-pane fade show active" id="pills-1" role="tabpanel" aria-labelledby="pills-orders-tab">
              <div class="container-fluid">
                <ul class="nav nav-pills flex-column flex-sm-row" role="tablist">
                  <li class="flex-sm-fill text-sm-center nav-item active myPillItems" role="presentation">
                    <a class="nav-link active" data-toggle="pill" href="#pills-all" role="tab"
                       aria-controls="pills-all" aria-selected="false">Todas</a>
                  </li>
                  <li class="flex-sm-fill text-sm-center nav-item active myPillItems" role="presentation">
                    <a class="nav-link active" data-toggle="pill" href="#pills-0" role="tab"
                       aria-controls="pills-0" aria-selected="false">En progreso</a>
                  </li>
                  <li class="flex-sm-fill text-sm-center nav-item myPillItems" role="presentation">
                    <a class="nav-link" data-toggle="pill" href="#pills-1" role="tab"
                       aria-controls="pills-1" aria-selected="false">Enviado</a>
                  </li>
                  <li class="flex-sm-fill text-sm-center nav-item myPillItems" role="presentation">
                    <a class="nav-link" data-toggle="pill" href="#pills-2" role="tab"
                       aria-controls="pills-2" aria-selected="false">Recibido</a>
                  </li>
                </ul>
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
                    <tr v-for="(item) in this.stateOrdersSend" :key="item.id">
                      <td><b>#{{ item.id }}</b></td>
                      <td>{{ item.date }}</td>
                      <td>{{ item.total }}€</td>
                      <td class="text-right" v-if="item.state==0"><span class="badge badge-primary">Recibido</span></td>
                      <td class="text-right" v-if="item.state==1"><span class="badge badge-light">Preparado</span></td>
                      <td class="text-right" v-if="item.state==2"><span class="badge badge-info">Enviado</span></td>
                      <td class="text-right" v-if="item.state==3"><span class="badge badge-success">Entregado</span>
                      </td>
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
            <!-- ORDERS RECEIVED: view order received history -->
            <div class="tab-pane fade show active" id="pills-2" role="tabpanel" aria-labelledby="pills-orders-tab">
              <div class="container-fluid">
                <ul class="nav nav-pills flex-column flex-sm-row" role="tablist">
                  <li class="flex-sm-fill text-sm-center nav-item active myPillItems" role="presentation">
                    <a class="nav-link active" data-toggle="pill" href="#pills-all" role="tab"
                       aria-controls="pills-all" aria-selected="false">Todas</a>
                  </li>
                  <li class="flex-sm-fill text-sm-center nav-item active myPillItems" role="presentation">
                    <a class="nav-link active" data-toggle="pill" href="#pills-0" role="tab"
                       aria-controls="pills-0" aria-selected="false">En progreso</a>
                  </li>
                  <li class="flex-sm-fill text-sm-center nav-item myPillItems" role="presentation">
                    <a class="nav-link" data-toggle="pill" href="#pills-1" role="tab"
                       aria-controls="pills-1" aria-selected="false">Enviado</a>
                  </li>
                  <li class="flex-sm-fill text-sm-center nav-item myPillItems" role="presentation">
                    <a class="nav-link" data-toggle="pill" href="#pills-2" role="tab"
                       aria-controls="pills-2" aria-selected="false">Recibido</a>
                  </li>
                </ul>
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
                    <tr v-for="(item) in this.stateOrdersReceived" :key="item.id">
                      <td><b>#{{ item.id }}</b></td>
                      <td>{{ item.date }}</td>
                      <td>{{ item.total }}€</td>
                      <td class="text-right" v-if="item.state==0"><span class="badge badge-primary">Recibido</span></td>
                      <td class="text-right" v-if="item.state==1"><span class="badge badge-light">Preparado</span></td>
                      <td class="text-right" v-if="item.state==2"><span class="badge badge-info">Enviado</span></td>
                      <td class="text-right" v-if="item.state==3"><span class="badge badge-success">Entregado</span>
                      </td>
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
let api = 'https://booken-dev.herokuapp.com/'
import axios from 'axios'
import * as toastr from "@/assets/toastr";

export default {
  name: "ControlPanel",
  props: {
    logged: Boolean,
    token: String,
    id: Number,
    type: Number
  },
  data() {
    return {
      editProfile: false,
      editPass: false,
      orders: [],
      sOrders: [],
      viewOrders: [],
      OrdersInProgress: [],
      OrdersSend: [],
      OrdersReceived: [],
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

      addCardForm: {
        "card_owner": '',
        "number": '',
        "date": '',
        "payment_method": ''
      },

      address_edit: -1,
      
      newAddressLabel: '',
      newAddressName: '',
      newAddressSurname: '',
      newAddressRoad: '',
      newAddressNumber: '',
      newAddressCode: '',
      newAddressCity: '',
      newAddressProvince: '',
      newAddressPhone: '',

      addresses: [{}]
    }
  },
  created() {
    this.getOrders()
    this.splitOrders()
    this.getAddresses()
    this.getCards()
    this.stateOrdersInProgress()
    this.stateOrdersReceived()
    this.stateOrdersSend()
  },
  methods: {
    getOrders() {
      var path = api + 'order/' + this.id

      axios.get(path)
          .then((res) => {
            this.orders = res.data.orders
          })
          .catch((error) => {
            this.toPrint(error)
            toastr.error('', 'No se ha podido recuperar los pedidos.',
                {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
          })
    },
    getCards() {
      var path = api + 'account/' + this.id + '/cards'
      axios.get(path)
          .then((res) => {
            this.cards = []
            var data = res.data.accounts_cards
            for(var i = 0; i < data.length; i++){
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
            this.toPrint(error)
            toastr.error('', 'No se ha podido recuperar las tarjetas.',
                {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
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
            this.toPrint(error)
            toastr.error('', 'No se ha podido recuperar las direcciones.',
                {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
          })
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
      var path = api + 'order/' + id
      axios.delete(path)
          // eslint-disable-next-line no-unused-vars
          .then((res) => {
            this.getBooksFromDB(this.$route.params.category)
            toastr.success('', '¡Pedido cancelado!',
                {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
          })
          .catch((error) => {
            toastr.error('', 'No se ha podido cancelar el pedido.',
                {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
            this.toPrint(error)
          })
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
    },
    stateOrdersInProgress() {
      var path = api + 'orders-state-0'

      axios.get(path)
          .then((res) => {
            this.OrdersInProgress = res.data.orders
          })
          .catch((error) => {
            this.toPrint(error)
            toastr.error('', 'No se ha podido recuperar los pedidos.',
                {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
          })

    },
    stateOrdersSend() {
      var path = api + 'orders-state-1'

      axios.get(path)
          .then((res) => {
            this.OrdersSend = res.data.orders
          })
          .catch((error) => {
            this.toPrint(error)
            toastr.error('', 'No se ha podido recuperar los pedidos.',
                {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
          })

    },
    stateOrdersReceived() {
      var path = api + 'orders-state-2'

      axios.get(path)
          .then((res) => {
            this.OrdersReceived = res.data.orders
          })
          .catch((error) => {
            this.toPrint(error)
            toastr.error('', 'No se ha podido recuperar los pedidos.',
                {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
          })

    },
    addCard(){
        this.addCardForm.card_owner = document.getElementById('paymentTitular').value
        this.addCardForm.number = document.getElementById('paymentNumber').value
        this.addCardForm.date = document.getElementById('paymentEndDate').value
        this.addCardForm.payment_method = document.getElementById('paymentMethod').value

        if (this.addCardForm.card_owner == '' || this.addCardForm.number == '' || this.addCardForm.date == ''
            || this.addCardForm.payment_method == ''){
                toastr.info('', 'Rellena los campos obligatorios para generar la consulta.',
                    {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
        } else if(this.addCardForm.number.length != 24){
                toastr.info('', 'El numero de cuenta debe contener 24 digitos.',
                    {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})

        } else if (!this.validateEndDate(this.addCardForm.date)) {
            toastr.error('', 'Fecha de caducidad no valida.',
                {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
        } else{
            this.cardToDB()
        }

        document.getElementById('paymentTitular').value = ''
        document.getElementById('paymentNumber').value = ''
        document.getElementById('paymentEndDate').value = ''
        document.getElementById('paymentMethod').value = ''
    },
    cardToDB(){
        const path = api + 'account/' + this.id + '/card'
      axios.post(path, this.addCardForm)
          // eslint-disable-next-line no-unused-vars
          .then((res) => {
                toastr.success('', '¡Tarjeta guardada con éxito!',
                  {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
                this.getCards()
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.log(error)
            toastr.error('', 'Algo no salió como se esperaba... pruebe de nuevo mas tarde',
                {timeOut: 1500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
            this.getCards()
          })
    },
    deleteCard(card_id){
        const path = api + 'account/' + this.id + '/card/' + card_id
      axios.delete(path)
          // eslint-disable-next-line no-unused-vars
          .then((res) => {
                toastr.success('', '¡Tarjeta eliminada con éxito!',
                  {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
                this.getCards()
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.log(error)
            toastr.error('', 'Algo no salió como se esperaba... pruebe de nuevo mas tarde',
                {timeOut: 1500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
            this.getCards()
          })
    },
    validateEndDate(date) {
        if(date.length == 7){
            var count = 0
            for(var i = 0; i<date.length; i++){
                try{
                    if(count == 2){
                        if(date[i] != '/')
                            return false
                        count += 1
                    }
                    else{
                        parseInt(date[i])
                        count += 1
                    }
                }catch(error){
                    return false
                }
            }
            return true
        }else
            return false
    },
    updateAddressModal(address_id){
        this.address_edit = address_id
        
        if(this.address_edit == -1){
            this.newAddressLabel = ''
            this.newAddressName = ''  
            this.newAddressSurname = ''  
            this.newAddressRoad = ''
            this.newAddressNumber= ''
            this.newAddressCode= ''  
            this.newAddressCity= ''
            this.newAddressProvince= ''
            this.newAddressPhone = ''
        }
        else{
            for( var i = 0; i<this.addresses.length; i++){
                var address = this.addresses[i]

                if(address.id == this.address_edit){
                    this.newAddressLabel = address.label_name
                    this.newAddressName = address.name
                    this.newAddressSurname = address.surnames
                    this.newAddressRoad = address.street
                    this.newAddressNumber= address.number
                    this.newAddressCode= address.cp
                    this.newAddressCity= address.city
                    this.newAddressProvince= address.province
                    this.newAddressPhone = address.telf
                }
            }
        }
    },
    addAddress(){
        if (this.newAddressName == '' || this.newAddressSurname == '' || this.newAddressRoad == ''
            || this.newAddressNumber== '' || this.newAddressCode== '' || this.newAddressCity== ''
            || this.newAddressProvince== '' || this.newAddressPhone == ''){
                toastr.info('', 'Rellena los campos obligatorios para generar la consulta.',
                    {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
        }
        else if(this.newAddressCode.length!=5){
            toastr.info('', 'El codigo postal debe contener 4 digitos.',
                {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
        }else if(this.newAddressPhone.length!=9){
            toastr.info('', 'El numero de telefono debe contener 9 digitos.',
                {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
        }else{
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
            if(this.address_edit!=-1)
                this.addressUpdateToDB(tmp)
            else
                this.addressToDB(tmp)
        }
    },
    addressToDB(parameters){
        const path = api + 'account/' + this.id + '/address'

      axios.post(path, parameters)
          // eslint-disable-next-line no-unused-vars
          .then((res) => {
                toastr.success('', '¡Dirección guardada con éxito!',
                  {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
                this.getAddresses()
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.log(error)
            toastr.error('', 'Algo no salió como se esperaba... pruebe de nuevo mas tarde',
                {timeOut: 1500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
            this.getAddresses()
          })
    },
    addressUpdateToDB(parameters){
        const path = api + 'account/' + this.id + '/address/' + this.address_edit

      axios.put(path, parameters)
          // eslint-disable-next-line no-unused-vars
          .then((res) => {
                toastr.success('', '¡Dirección guardada con éxito!',
                  {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
                this.getAddresses()
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.log(error)
            toastr.error('', 'Algo no salió como se esperaba... pruebe de nuevo mas tarde',
                {timeOut: 1500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
            this.getAddresses()
          })
    },
    deleteAddress(address_id){
        const path = api + 'account/' + this.id + '/address/' + address_id
      axios.delete(path)
          // eslint-disable-next-line no-unused-vars
          .then((res) => {
                toastr.success('', '¡Dirección eliminada con éxito!',
                  {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
                this.getAddresses()
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.log(error)
            toastr.error('', 'Algo no salió como se esperaba... pruebe de nuevo mas tarde',
                {timeOut: 1500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
            this.getAddresses()
          })
    }
  }
}
</script>

<style scoped>
.front-container {
  width: 100%;
  margin: 2em auto;
}

@media (min-width: 0px) {
  .myPillItems {
    width: 100%
  }

  .myAddressCard {
    min-height: 220px;
  }

  .myPaymentCard {
    min-height: 200px;
  }
}

@media (min-width: 992px) {
  .myPillItems {
    width: 20%
  }

  .myAddressCard {
    height: auto;
  }


  .myPaymentCard {
    height: auto;
  }
}
</style>