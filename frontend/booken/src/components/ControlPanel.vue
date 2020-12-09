<style>
@import url("../assets/toastr.css");
@import url("../assets/animate.min.css");
@import url("../assets/book_info.css");
</style>
<style lang="scss" src="../assets/ticket.scss" scoped>
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
          <div class="row justify-content-md-center">
            <div class="col-2 btn mr-auto" type="submit" data-toggle="modal" data-target="#configAccount">
              <i class="fas fa-user-cog fa-lg" style="color: #3b494d; font-size: 1.5em"/>
              <!--<a class="navbartextbtdark">Cerrar sesión</a>-->
            </div>
            <div class="modal fade" id="configAccount" tabindex="-1" role="dialog"
                 aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
              <div class="modal-dialog modal-dialog-centered" role="document">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="configAccountTitle">Configuración de la cuenta</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                      <span aria-hidden="true">&times;</span>
                    </button>
                  </div>
                  <div class="modal-body">
                    <!--<div class="row align-items-center mt-1 md-3">
                      <div class="col-8 text-left">
                        <div>Deseas recibir notificaciones?</div>
                      </div>
                      <div class="col-4 text-right">
                        <div class="btn-group btn-group-toggle" data-toggle="buttons">
                          <label class="btn btn-secondary active" style="width: 50px">
                            <input type="radio" name="options" id="option1" checked> Sí
                          </label>
                          <label class="btn btn-secondary" style="width: 50px">
                            <input type="radio" name="options" id="option2"> No
                          </label>
                        </div>
                      </div>
                    </div>-->

                    <div class="row align-items-center mt-3 md-1">
                      <div class="col-8 text-left">
                        <div>¿Quieres eliminar tu cuenta?</div>
                      </div>
                      <div class="col-4 text-right">
                        <button class="btn btn-secondary" style="width: 50px" type="submit"
                                data-toggle="modal" data-target="#deleteAccount">Sí
                        </button>

                      </div>
                      <div class="modal-lg fade" id="deleteAccount" tabindex="-1" role="dialog"
                           aria-labelledby="logOutTitle" aria-hidden="true">
                        <div class="modal-dialog modal-dialog-centered" role="document">
                          <div class="modal-content">
                            <div class="modal-header" style="border-bottom: 0 none; text-align: left">
                              <h5 class="modal-title" id="deleteAccountTitle">¿Estás seguro? Este proceso no se puede
                                revertir.</h5>
                              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                              </button>
                            </div>
                            <div class="modal-footer" style="border-top: 0 none;">
                              <button type="button" class="btn btn-secondary" style="width:50px" data-dismiss="modal"
                                      @click="deleteAccount" href="/">Sí
                              </button>
                              <button type="button" class="btn btn-primary" style="width:50px" data-dismiss="modal">No
                              </button>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>

                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-primary" data-dismiss="modal">Cerrar</button>
                  </div>
                </div>
              </div>
            </div>
            <h3 class="col-8 align-middle my-auto">Panel de control</h3>
            <div class="col-2 btn ml-auto" type="submit" data-toggle="modal" data-target="#logOut">
              <i class="fas fa-sign-out-alt fa-lg" style="color: #3b494d; font-size: 1.5em"/>
              <!--<a class="navbartextbtdark">Cerrar sesión</a>-->
            </div>
            <div class="modal fade" id="logOut" tabindex="-1" role="dialog"
                 aria-labelledby="logOutTitle" aria-hidden="true">
              <div class="modal-dialog modal-dialog-centered" role="document">
                <div class="modal-content">
                  <div class="modal-header" style="border-bottom: 0 none;">
                    <h5 class="modal-title" id="exampleModalLongTitle">¿Quieres cerrar la sesión?</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                      <span aria-hidden="true">&times;</span>
                    </button>
                  </div>
                  <div class="modal-footer" style="border-top: 0 none;">
                    <button type="button" class="btn btn-secondary" style="width:50px" @click="logout"
                            data-dismiss="modal">Sí
                    </button>
                    <button type="button" class="btn btn-primary" style="width:50px" data-dismiss="modal">No</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <ul class="nav nav-pills flex-column flex-sm-row" id="pills-tab" role="tablist">
          <li class="flex-sm-fill text-sm-center nav-item myPillItems" role="presentation" v-if="this.type == 0">
            <a class="nav-link active" id="pills-orders-tab" data-toggle="pill" href="#pills-orders" role="tab"
               aria-controls="pills-orders" aria-selected="false">Tus pedidos</a>
          </li>
          <li class="flex-sm-fill text-sm-center nav-item myPillItems" role="presentation" v-if="this.type == 1">
            <a class="nav-link active" id="pills-contacts-tab" data-toggle="pill" href="#pills-contacts" role="tab"
               aria-controls="pills-contacts" aria-selected="false">Lista de consultas</a>
          </li>
          <li class="flex-sm-fill text-sm-center nav-item myPillItems" role="presentation" v-if="this.type == 2">
            <a class="nav-link active" id="pills-orders-list-tab" data-toggle="pill" href="#pills-orders-list"
               role="tab"
               aria-controls="pills-orders-list" aria-selected="false">Lista de pedidos</a>
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
          <div class="tab-pane fade show active" id="pills-orders" role="tabpanel" aria-labelledby="pills-orders-tab"
               v-if="type == 0">
            <div class="container-fluid">
              <div class="row">
                <div class="col col-md mr-auto" style="text-align: right">
                  <label>Filtrar: </label>
                  <select name="sortBy" id="sortBy" @change="sortBy(sortType)" v-model="sortType"
                          class="form-control-sm" style="width: 180px; margin-left:10px; margin-right: 0.5em">
                    <option v-for="item in sortOptions" :key="item" :selected="sortType == '-1'" :value="item.value">
                      {{ item.text }}
                    </option>
                  </select>
                </div>
              </div>
              <div class="table-responsive">
                <table class="table table-striped" style="text-align: left" :key="this.orders.length">
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
                    <td class="text-right" v-if="item.state==0"><span class="badge badge-primary">En progreso</span>
                    </td>
                    <td class="text-right" v-if="item.state==1"><span class="badge badge-light">Enviado</span></td>
                    <td class="text-right" v-if="item.state==2"><span class="badge badge-info">Recibido</span></td>
                    <td class="text-right" v-if="item.state==0">
                      <button class="btn btn-danger" @click="cancelOrder(item.id)">Cancelar</button>
                    </td>
                    <td class="text-right" v-if="item.state!=0">
                      <button class="btn btn-light" @click="viewOrder(item)" data-toggle="modal"
                              data-target="#view-ticket-c">Ver pedido
                      </button>
                      <div class="modal fade" id="view-ticket-c" tabindex="-1" role="dialog"
                           aria-labelledby="modalAddressLabel"
                           aria-hidden="true">
                        <div class="modal-dialog" role="document"
                             style="min-height: calc(100vh - 60px); display: flex;flex-direction: column;justify-content: center;overflow: auto;">
                          <div class="modal-content">
                            <div class="modal-header">
                              <h5 class="modal-title">Detalles del pedido</h5>
                              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                              </button>
                            </div>
                            <div class="modal-body">
                              <div class="container-ticket">
                                <div class="ticket">
                                  <div class="head-ticket">
                                    <p class="x-bold">booken & co</p>
                                    <p class="bold">08032 BARCELONA</p>
                                    <p class="bold">Tfno: 932 98 65 00</p>
                                    <p>{{ order.date }}</p>
                                    <p>Pedido {{ getYear() + "-" + order.id.toString() }} QRL 02154</p>
                                    <div class="code-barre">
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                    </div>
                                  </div>
                                  <div class="body-ticket">
                                    <div class="produits">
                                      <div class="col2" v-for="art in this.order.articles" :key="art.id">
                                        <p>{{ art.quant }} x {{ art.book_title }}</p>
                                        <p class="prix">{{ art.price }}€</p>
                                      </div>
                                      <div class="col2">
                                        <p v-if="order.send_type == 1">1 x Envío Estándard</p>
                                        <p v-if="order.send_type == 2">1 x Envío Estándard Plus</p>
                                        <p v-if="order.send_type == 3">1 x Envío Ultra Express</p>
                                        <p class="prix">{{ order.shipping }}€</p>
                                      </div>
                                      <div class="hr-sm"></div>
                                      <div class="col2">
                                        <p>IVA (21%)</p>
                                        <p class="prix">{{ order.taxes }}€</p>
                                      </div>
                                      <div class="col2">
                                        <p v-if="order.articles.length == 1">Total 1 artículo</p>
                                        <p v-else>Total {{ order.articles.length }} artículos</p>
                                        <p class="prix">{{ order.total }}€</p>
                                      </div>
                                      <p>En pesetas : {{ round2Dec(order.total * 166.386) }} ptas</p>
                                      <p>(1 euro = 166.386 pesetas)</p>
                                    </div>
                                    <div class="hr-lg"></div>
                                    <div class="carte">
                                      <p class="title-carte">Dirección de envío</p>
                                      <p class="lel">{{ order.add_name + " " + order.add_lname }}</p>
                                      <p class="lel">{{ order.street + ", " + order.add_number }}</p>
                                      <p class="lel">{{ order.add_cp + " " + order.add_prov }}</p>
                                      <p class="lel">Tfno: {{ order.telf }}</p>
                                    </div>
                                    <div class="hr-lg"></div>
                                    <div class="carte">
                                      <p class="title-carte">Método de pago</p>
                                      <p class="lel">{{ order.card_vendor }} **** **** **** {{ order.card_num }}</p>
                                    </div>
                                    <div class="hr-lg"></div>
                                  </div>
                                  <div class="footer-ticket">
                                    <p class="title-footer">¡Gracias por comprar en booken!</p>
                                  </div>
                                </div>
                              </div>
                            </div>
                            <div class="modal-footer">
                              <button type="button" class="btn btn-secondary" @click="printReceipt">
                                Imprimir
                              </button>

                              <button type="button" class="btn btn-primary" @click="send_ticket(order.id)">
                                  <div v-if="!sending_mail">
                                      Enviar al correo
                                  </div>
                                  <div v-else>
                                      <span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true">
                                      </span>
                                      Enviando ticket...
                                  </div>
                              </button>
                            </div>
                          </div>
                        </div>
                      </div>
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
                      <li class="page-item">
                        <a class="page-link" v-if="cIndex != (index-1)" @click="changeViewingOrders(index-1)">
                          {{ index }}</a></li>
                    </span>
                  </ul>
                </nav>
              </div>
            </div>
          </div>
          <!-- CONTACTS: view contacts for support-->
          <div class="tab-pane fade show active" id="pills-contacts" role="tabpanel"
               aria-labelledby="pills-orders-list-tab" v-if="type == 1">
            <div class="container-fluid">
              <div class=" list-group-flush">

                <div v-for="(contact, index) in this.contacts" :key="index"
                     :class="['list-group-item ', (index === 0 ? '' : '')]"
                     href="#">

                  <div class="row">
                    <div class="col-12 col-md-9 my-md-auto my-2">
                      <div class="row d-flex justify-content-between">
                        <h6 class="col-12 col-md-10 my-md-auto my-1 text-left">
                            <b>Consulta: </b>{{ contact.contact_query }}
                        </h6>
                        <small class="col-12 col-md-2 my-md-auto my-1">{{ contact.contact_date }}</small>
                      </div>
                    </div>
                    <div class="col-12 col-md-3 my-md-auto my-2 myButton">
                      <div style="display:flex; flex-direction: row; justify-content: center; align-items:center;">
                          <button type="button" class="btn btn-danger align-middle"
                                  style="margin-right:0.5em" @click="deleteContact(index)">
                                  Eliminar
                          </button>
                          <button type="button" class="btn btn-primary align-middle" data-toggle="modal"
                                  data-target="#answerContact" @click="assignContact(index)">Responder
                          </button>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="modal fade" id="answerContact" tabindex="-1" role="dialog" aria-hidden="true">
                  <div class="modal-dialog modal-dialog-centered" role="document">
                    <div class="modal-content">
                      <div class="modal-header" style="border-bottom: 0 none;">
                        <h5 class="modal-title">Responder la pregunta</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                          <span aria-hidden="true">&times;</span>
                        </button>
                      </div>
                      <div class="modal-body">
                        <div class="row">
                          <div class="col-12 text-left">
                            <strong> Datos vinculados: </strong><br>
                          </div>
                          <div class="col-12 mt-2">
                            <div class="border rounded" style="background: whitesmoke;">
                              <div class="col-12 text-left mt-2">
                                <strong> ID: </strong> {{ contactToAnswer['id'] }}
                              </div>
                              <div class="col-12 text-left">
                                <strong> Email: </strong> {{ contactToAnswer['email'] }}
                              </div>
                              <div class="col-12 text-left">
                                <strong> Nombre: </strong> {{ contactToAnswer['full_name'] }}
                              </div>
                              <div class="col-12 text-left">
                                <strong> Teléfono: </strong> {{ contactToAnswer['phone_number'] }}
                              </div>
                              <div class="col-12 text-left mb-2">
                                <strong> Fecha de creación: </strong> {{ contactToAnswer['contact_date'] }}
                              </div>
                            </div>
                          </div>
                          <div class="col-12 text-left mt-4">
                            <strong> Pregunta: </strong><br> {{ contactToAnswer['contact_query'] }}
                          </div>
                          <div class="col-12 text-left mt-4">
                            <div class="form-group">
                              <label class="col-form-label"><strong>Respuesta:</strong></label>
                              <textarea type="text" class="form-control" col=30 rows=10 v-model="newContactAnswer"/>
                            </div>
                          </div>
                        </div>

                      </div>
                      <div class="modal-footer" style="border-top: 0 none;">

                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Cerrar</button>
                        <button type="button" class="btn btn-primary" @click="validate_response" v-if="!sent">
                            <div v-if="!sending_mail">
                                Enviar la respuesta
                            </div>
                            <div v-else>
                                <span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true">
                                </span>
                                Enviando respuesta...
                            </div>
                        </button>
                      </div>
                    </div>
                  </div>
                </div>

              </div>
            </div>
          </div>
          <!-- ORDERS LIST: view order list history for shop manager-->
          <div class="tab-pane fade show active" id="pills-orders-list" role="tabpanel"
               aria-labelledby="pills-orders-list-tab" v-if="type == 2">
            <div class="container-fluid">
              <div class="row">
                <div class="col col-md mr-auto" style="text-align: right">
                  <label>Filtrar: </label>
                  <select id="sortByHist" @change="sortByHist(sortTypeHist)" v-model="sortTypeHist"
                          class="form-control-sm" style="width: 180px; margin-left:10px; margin-right: 0.5em">
                    <option v-for="item in sortOptions" :key="item" :value="item.value">{{ item.text }}</option>
                  </select>
                </div>
              </div>
              <div class="table-responsive">
                <table class="table table-striped" style="text-align: left" :key="this.ordersHist.length">
                  <thead>
                  <tr>
                    <th scope="col">Número pedido</th>
                    <th scope="col">Fecha</th>
                    <th scope="col">Total</th>
                    <th scope="col" class="text-right">Estado</th>
                    <th scope="col" class="text-right">Editar pedido</th>
                    <th scope="col" class="text-right">Acciones</th>
                  </tr>
                  </thead>
                  <tbody>
                  <tr v-for="(item) in this.viewOrdersList" :key="item.state">
                    <td><b>#{{ item.id }}</b></td>
                    <td>{{ item.date }}</td>
                    <td>{{ item.total }}€</td>
                    <td class="text-right" v-if="item.state==0"><span class="badge badge-primary">En progreso</span>
                    </td>
                    <td class="text-right" v-if="item.state==1"><span class="badge badge-light">Enviado</span></td>
                    <td class="text-right" v-if="item.state==2"><span class="badge badge-info">Recibido</span></td>
                    <td class="text-right" v-if="item.state==2">
                      <b>Pedido recibido</b>
                    </td>
                    <td class="text-right" v-if="item.state!=2">
                      <select id="sortByStateHist" @change="changeState(sortState[item.id],item.id)"
                              v-model="sortState[item.id]"
                              class="form-control-sm" style="width: 120px;text-align: center">
                        <option v-for="state in sortEditOptions" :key="state" :value="state.value">{{ state.text }}
                        </option>
                      </select>
                    </td>
                    <td class="text-right" v-if="item.state==0">
                      <button class="btn btn-danger" @click="cancelOrderList(item.id)">Cancelar</button>
                    </td>
                    <td class="text-right" v-if="item.state!=0">
                      <button class="btn btn-light" @click="viewOrder(item)" data-toggle="modal"
                              data-target="#view-ticket-a">Ver pedido
                      </button>
                      <div class="modal fade" id="view-ticket-a" tabindex="-1" role="dialog"
                           aria-labelledby="modalAddressLabel"
                           aria-hidden="true">
                        <div class="modal-dialog" role="document"
                             style="min-height: calc(100vh - 60px); display: flex;flex-direction: column;justify-content: center;overflow: auto;">
                          <div class="modal-content">
                            <div class="modal-header">
                              <h5 class="modal-title">Detalles del pedido</h5>
                              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                              </button>
                            </div>
                            <div class="modal-body">
                              <div class="container-ticket" id="ticket-pdf">
                                <div class="ticket">
                                  <div class="head-ticket">
                                    <p class="x-bold">booken & co</p>
                                    <p class="bold">08032 BARCELONA</p>
                                    <p class="bold">Tfno: 932 98 65 00</p>
                                    <p>{{ order.date }}</p>
                                    <p>Pedido {{ getYear() + "-" + order.id.toString() }} QRL 02154</p>
                                    <div class="code-barre">
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                      <span></span>
                                    </div>
                                  </div>
                                  <div class="body-ticket">
                                    <div class="produits">
                                      <div class="col2" v-for="art in this.order.articles" :key="art.id">
                                        <p class="xd">{{ art.quant }} x {{ art.book_title }}</p>
                                        <p class="prix">{{ art.price }}€</p>
                                      </div>
                                      <div class="col2">
                                        <p v-if="order.send_type == 1">1 x Envío Estándard</p>
                                        <p v-if="order.send_type == 2">1 x Envío Estándard Plus</p>
                                        <p v-if="order.send_type == 3">1 x Envío Ultra Express</p>
                                        <p class="prix">{{ order.shipping }}€</p>
                                      </div>
                                      <div class="hr-sm"></div>
                                      <div class="col2">
                                        <p>IVA (21%)</p>
                                        <p class="prix">{{ order.taxes }}€</p>
                                      </div>
                                      <div class="col2">
                                        <p v-if="order.articles.length == 1">Total 1 artículo</p>
                                        <p v-else>Total {{ order.articles.length }} artículos</p>
                                        <p class="prix">{{ order.total }}€</p>
                                      </div>
                                      <p>En pesetas : {{ round2Dec(order.total * 166.386) }} ptas</p>
                                      <p>(1 euro = 166.386 pesetas)</p>
                                    </div>
                                    <div class="hr-lg"></div>
                                    <div class="carte">
                                      <p class="title-carte">Dirección de envío</p>
                                      <p class="lel">{{ order.add_name + " " + order.add_lname }}</p>
                                      <p class="lel">{{ order.street + ", " + order.add_number }}</p>
                                      <p class="lel">{{ order.add_cp + " " + order.add_prov }}</p>
                                      <p class="lel">Tfno: {{ order.telf }}</p>
                                    </div>
                                    <div class="hr-lg"></div>
                                    <div class="carte">
                                      <p class="title-carte">Método de pago</p>
                                      <p class="lel">{{ order.card_vendor }} **** **** **** {{ order.card_num }}</p>
                                    </div>
                                    <div class="hr-lg"></div>
                                  </div>
                                  <div class="footer-ticket">
                                    <p class="title-footer">¡Gracias por comprar en booken!</p>
                                  </div>
                                </div>
                              </div>
                            </div>
                            <div class="modal-footer">
                              <button type="button" class="btn btn-secondary" @click="printReceipt">
                                Imprimir
                              </button>

                              <button type="button" class="btn btn-primary" @click="send_ticket(order.id)">
                                  <div v-if="!sending_mail">
                                      Enviar al correo
                                  </div>
                                  <div v-else>
                                      <span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true">
                                      </span>
                                      Enviando ticket...
                                  </div>
                              </button>
                            </div>
                          </div>
                        </div>
                      </div>
                    </td>
                  </tr>
                  </tbody>
                </table>
                <nav aria-label="...">
                  <ul class="pagination pagination-lg">
                    <span v-for="index in this.sOrdersList.length" :key="index">
                      <li class="page-item active" aria-current="page" v-if="cIndexList == (index-1)">
                    <span class="page-link">
                      {{ index }}</span>
                    </li>
                      <li class="page-item"><a class="page-link" v-if="cIndexList != (index-1)"
                                               @click="changeViewingOrdersList(index-1)">{{ index }}</a></li>
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
                <div class="col-6 my-auto" style="text-align: left">
                  <h5>Tus datos</h5>
                </div>
                <div class="col-6" style="text-align: right">
                  <button class="btn btn-warning  mr-2" type="submit" style="width: auto"
                          v-if="!editProfile"><i
                      class="fas fa-edit"
                      style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
                      class="navbartextbt" @click="modifyProfile">Modificar</a></button>
                  <button class="btn btn-success mr-2" type="submit" style="width: auto"
                          v-if="editProfile"><i
                      class="fas fa-save"
                      style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
                      class="navbartextbt" @click="saveProfile">Guardar</a></button>
                </div>
              </div>
              <div class="row" style="text-align: left">
                <div class="col-12 col-md-6 mt-3">
                  <label for="exampleFormControlInput1">Nombre</label>
                  <input type="text" class="form-control"
                         placeholder="Aitor" :disabled="!editProfile" v-model="fname">

                </div>
                <div class="col-12 col-md-6 mt-3">
                  <label for="exampleFormControlInput1">Apellidos</label>
                  <input type="text" class="form-control" id="exampleFormControlInput1"
                         placeholder="Tilla Seca" :disabled="!editProfile" v-model="lname">
                </div>
                <div class="col-12 mt-3">
                  <label for="exampleFormControlInput1">Correo electrónico</label>
                  <input type="email" class="form-control"
                         placeholder="aitortilla@usa.gov.us" :disabled="!editProfile" v-model="email">

                </div>
              </div>
              <div class="row mt-5">
                <div class="col-6 my-auto" style="text-align: left">
                  <h5>Cambiar contraseña</h5>
                </div>
                <div class="col-6" style="text-align: right">
                  <button class="btn btn-warning mr-2" type="submit" style="width: auto" v-if="!editPass">
                    <i
                        class="fas fa-edit"
                        style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
                      class="navbartextbt" @click="changePassword">Cambiar</a></button>
                  <button class="btn btn-success mr-2" type="submit" style="width: auto" v-if="editPass"><i
                      class="fas fa-save"
                      style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
                      class="navbartextbt" @click="savePassword">Guardar</a></button>
                </div>
              </div>
              <div class="row" style="text-align: left">
                <div class="col-12 col-md-4 mt-3">
                  <label for="exampleFormControlInput1">Contraseña actual</label>
                  <input type="password" class="form-control"
                         placeholder="" :disabled="!editPass" v-model="oldPassword">
                </div>
                <div class="col-12 col-md-4 mt-3">
                  <label for="exampleFormControlInput1">Contraseña nueva</label>
                  <input type="password" class="form-control"
                         placeholder="" :disabled="!editPass"
                         v-model="newPassword" @change="this.scoreNewPassword">
                  <div class="myVisibleStat" v-if="editPass">
                    <div class="progress" style="width:100%; margin-top:1rem">
                      <div class="progress-bar" role="progressbar" aria-valuenow="0"
                           aria-valuemin="0" aria-valuemax="100" id="mynewprobar" style="color: black">
                        {{ this.checkNewPasswordStrength() }}
                      </div>
                    </div>
                    <div class="rounded" style="background: white; text-align: left; margin-top: 1rem">
                      <ul class="list-group">
                        <li class="list-group-item d-flex justify-content-between">
                          <span style="font-size: 0.9em">Contiene carácter símbolo</span>
                          <i class="fa fa-check fa-lg my-auto" style="color: green; width: 20px"
                             v-if="this.checkNewPasswordSymbol(this.newPassword)"></i>
                          <i class="fa fa-times fa-lg my-auto" style="color: red; width: 20px"
                             v-else></i>
                        </li>
                        <li class="list-group-item d-flex justify-content-between">
                          <span style="font-size: 0.9em">Contiene carácter mayúscula</span>
                          <i class="fa fa-check fa-lg my-auto" style="color: green; width: 20px"
                             v-if="this.checkNewPasswordUpper(this.newPassword)"></i>
                          <i class="fa fa-times fa-lg my-auto" style="color: red; width: 20px"
                             v-else></i>
                        </li>
                        <li class="list-group-item d-flex justify-content-between">
                          <span style="font-size: 0.9em">Contiene carácter minúscula</span>
                          <i class="fa fa-check fa-lg my-auto" style="color: green; width: 20px"
                             v-if="this.checkNewPasswordLower(this.newPassword)"></i>
                          <i class="fa fa-times fa-lg my-auto" style="color: red; width: 20px"
                             v-else></i>
                        </li>
                        <li class="list-group-item d-flex justify-content-between">
                          <span style="font-size: 0.9em">Contiene carácter numérico</span>
                          <i class="fa fa-check fa-lg my-auto" style="color: green; width: 20px"
                             v-if="this.checkNewPasswordNumber(this.newPassword)"></i>
                          <i class="fa fa-times fa-lg my-auto" style="color: red; width: 20px"
                             v-else></i>
                        </li>
                        <li class="list-group-item d-flex justify-content-between">
                          <span style="font-size: 0.9em">Mínimo 8 carácteres</span>
                          <i class="fa fa-check fa-lg my-auto" style="color: green; width: 20px"
                             v-if="this.checkNewPasswordLength(this.newPassword)"></i>
                          <i class="fa fa-times fa-lg my-auto" style="color: red; width: 20px"
                             v-else></i>
                        </li>

                      </ul>
                    </div>
                  </div>
                </div>
                <div class="col-12 col-md-4 my-3">
                  <label for="exampleFormControlInput1">Repite contraseña nueva</label>
                  <input type="password" class="form-control" placeholder="" :disabled="!editPass"
                         v-model="newPassword2">
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
                        <p style="cursor: pointer; margin-bottom: 0em; text-align: right; color: red"
                           @click="deleteAddress(item.id)">
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
                            <label class="col-form-label">Identificador</label>
                            <input type="test" class="form-control" v-model="newAddressLabel">
                          </div>
                          <div class="form-group" style="text-align: left">
                            <label class="col-form-label">Nombre y apellidos</label>
                            <div style="display:flex;">
                              <input type="text" class="form-control"
                                     v-model="newAddressName" placeHolder="Nombre">
                              <input type="text" class="form-control"
                                     v-model="newAddressSurname" placeHolder="Apellidos">
                            </div>
                          </div>
                          <div class="form-group" style="text-align: left">
                            <label class="col-form-label">Dirección</label>
                            <div style="display:flex">
                              <input type="text" class="form-control" style="width:80%;"
                                     v-model="newAddressRoad" placeHolder="Calle">
                              <input type="number" class="form-control" style="width:20%;"
                                     v-model="newAddressNumber" placeHolder="Nº">
                            </div>
                          </div>
                          <div class="form-group" style="text-align: left">
                            <label class="col-form-label">Código postal</label>
                            <input type="number" class="form-control" v-model="newAddressCode">
                          </div>
                          <div class="form-group" style="text-align: left">
                            <label class="col-form-label">Residencia</label>
                            <div style="display:flex">
                              <input type="text" class="form-control"
                                     v-model="newAddressCity" placeHolder="Ciudad">
                              <input type="text" class="form-control"
                                     v-model="newAddressProvince" placeHolder="Provincia">
                            </div>
                          </div>
                          <div class="form-group" style="text-align: left">
                            <label class="col-form-label">Teléfono</label>
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
                      <span v-if="item.vendor == 'MasterCard'"><i class="fab fa-cc-mastercard"
                                                                  style="font-size: 1.8em"></i></span>
                      <span v-if="item.vendor == 'Visa' || item.vendor == 'Visa electron'"><i class="fab fa-cc-visa"
                                                                                              style="font-size: 1.8em"></i></span>
                      <span v-if="item.vendor == 'JCB'"><i class="fab fa-cc-jcb" style="font-size: 1.8em"></i></span>
                      <span v-if="item.vendor == 'Discover'"><i class="fab fa-cc-discover"
                                                                style="font-size: 1.8em"></i></span>
                      <span v-if="item.vendor == 'AMEX'"><i class="fab fa-cc-amex"
                                                            style="font-size: 1.8em"></i></span>
                      <span v-if="item.vendor == 'Diners'"><i class="fab fa-cc-diners-club"
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
                                <label for="paymentNumber" class="col-form-label">Número de tarjeta</label>
                                <input class="form-control" id="paymentNumber" @input="chkInput">
                              </div>
                              <div class="form-group" style="text-align: left">
                                <label for="paymentTitular" class="col-form-label">Titular de la tarjeta</label>
                                <input type="text" class="form-control" id="paymentTitular">
                              </div>
                              <div class="form-group" style="text-align: left">
                                <label for="paymentEndDate" class="col-form-label">Fecha de vencimiento</label>
                                <input type="text" class="form-control" id="paymentEndDate" placeholder="mm/aaaa">
                              </div>
                              <div class="form-group" style="text-align: center; font-size: 3em">
                                <span v-if="ccvendor == 'MasterCard'"><i class="fab fa-cc-mastercard"
                                                                         style="font-size: 1.8em"></i></span>
                                <span v-if="ccvendor == 'Visa' || ccvendor == 'Visa electron'"><i class="fab fa-cc-visa"
                                                                                                  style="font-size: 1.8em"></i></span>
                                <span v-if="ccvendor == 'JCB'"><i class="fab fa-cc-jcb"
                                                                  style="font-size: 1.8em"></i></span>
                                <span v-if="ccvendor == 'Discover'"><i class="fab fa-cc-discover"
                                                                       style="font-size: 1.8em"></i></span>
                                <span v-if="ccvendor == 'AMEX'"><i class="fab fa-cc-amex"
                                                                   style="font-size: 1.8em"></i></span>
                                <span v-if="ccvendor == 'Diners'"><i class="fab fa-cc-diners-club"
                                                                     style="font-size: 1.8em"></i></span>
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
            <div style="margin-left: 0.5em; margin-right: 0.5em">
              <h4 style="text-align: left; margin-left: 0.5em">Rendimiento global</h4>
              <div class="row row-cols-1 row-cols-md-3">
                <div class="col">
                  <div class="card" style="text-align: left; margin: 0.5em">
                    <div class="card-header" style="background-color: #2F96B4; color: white">
                      <div class="row">
                        <div class="col">
                          <h5>Ventas</h5>
                        </div>
                        <div class="col" style="text-align: right">
                          <h5><b>{{ total_sales }}</b></h5>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="col">
                  <div class="card" style="text-align: left; margin: 0.5em">
                    <div class="card-header" style="background-color: #6D58FF; color: white">
                      <div class="row">
                        <div class="col">
                          <h5>Ganancias</h5>
                        </div>
                        <div class="col" style="text-align: right">
                          <h5><b>{{ total_gain }}€</b></h5>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="col">
                  <div class="card" style="text-align: left; margin: 0.5em">
                    <div class="card-header" style="background-color: #16BF78; color: white">
                      <div class="row">
                        <div class="col">
                          <h5>Usuarios</h5>
                        </div>
                        <div class="col" style="text-align: right">
                          <h5><b>{{ total_users }}</b></h5>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="row row-cols-1 row-cols-md-2" style="margin-top: 1em">
                <div class="col">
                  <h4 style="text-align: left; margin-left: 0.5em; margin-top: 0.5em">Rendimiento por año</h4>
                </div>
                <div class="col" style="text-align: right">
                  <select class="custom-select" id="validationTooltip04" style="width: auto; margin-right: 0.5em"
                          @change="changeData()" v-model="selYear">
                    <option v-for="year in this.years_data" :key="year" :value="year">{{ year }}</option>
                  </select>
                </div>
              </div>
              <div class="row row-cols-1 row-cols-md-2">
                <div class="col">
                  <div class="card" style="text-align: left; margin: 0.5em">
                    <div class="card-header" style="background-color: #2F96B4; color: white">
                      <div class="row">
                        <div class="col">
                          <h5>Ventas ({{ selYear }})</h5>
                        </div>
                        <div class="col" style="text-align: right">
                          <h5><b>{{ salesYear }}</b></h5>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="col">
                  <div class="card" style="text-align: left; margin: 0.5em">
                    <div class="card-header" style="background-color: #6D58FF; color: white">
                      <div class="row">
                        <div class="col">
                          <h5>Ganancias ({{ selYear }})</h5>
                        </div>
                        <div class="col" style="text-align: right">
                          <h5><b>{{ gainYear }}€</b></h5>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="row row-cols-1 row-cols-md-2" style="margin-top: 1em">
                <div class="col">
                  <apexchart
                      width="100%"
                      type="bar"
                      :options="salesMonthOptions"
                      :series="salesMonthSeries"
                  ></apexchart>
                </div>
                <div class="col">
                  <apexchart
                      width="100%"
                      type="bar"
                      :options="gainMonthOptions"
                      :series="gainMonthSeries"
                  ></apexchart>
                </div>
              </div>
              <div class="row row-cols-1 row-cols-md-2" style="margin-top: 1em">
                <div class="col">
                  <apexchart
                      width="100%"
                      type="pie"
                      :options="salesGenreOptions"
                  ></apexchart>
                </div>
                <div class="col">
                  <apexchart
                      width="100%"
                      type="pie"
                      :options="gainGenreOptions"
                  ></apexchart>
                </div>
              </div>
              <div class="row row-cols-1 row-cols-md-1" style="margin-top: 1em">
                <div class="col">
                  <apexchart
                      width="100%"
                      type="line"
                      :options="loginLogOptions"
                  ></apexchart>
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
import {jsPDF} from "jspdf"
import {bus, api} from '../main.js'
import axios from 'axios'
import * as toastr from "@/assets/toastr";
import VueApexCharts from "vue3-apexcharts"

export default {
  name: "ControlPanel",
  components: {
    // eslint-disable-next-line vue/no-unused-components
    apexchart: VueApexCharts
  },
  props: {
    logged: Boolean,
    token: String,
    id: Number,
    type: Number
  },
  data() {
    return {
      fname: '',
      lname: '',
      email: '',
      oldPassword: '',
      newPassword: '',
      newPassword2: '',
      editProfile: false,
      editPass: false,
      orders: [],
      ordersHist: [],
      sOrders: [],
      sOrdersList: [],
      viewOrders: [],
      viewOrdersList: [],
      OrdersInProgress: [],
      OrdersSend: [],
      OrdersReceived: [],
      numberOfOrders: 0,
      numberOfPages: 0,
      maxPerPage: 10,
      cIndex: 0,
      cIndexList: 0,
      addressNumber: 0,
      cardNumber: 0,
      salesMonthSeries: [],
      salesMonthOptions: {},
      salesGenreSeries: [],
      salesGenreOptions: {},
      gainMonthOptions: {},
      gainMonthSeries: {},
      gainGenreOptions: {},
      loginLogOptions: {},
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
      order: {
        id: -1,
        date: "",
        total: -1,
        shipping: -1,
        send_type: -1,
        card_vendor: "",
        card_num: "",
        add_name: "",
        add_lname: "",
        add_number: -1,
        add_cp: "",
        add_city: "",
        add_prov: "",
        street: "",
        telf: -1,
        articles: {},
        taxes: -1
      },
      address_edit: -1,
      ccvendor: '',
      newAddressLabel: '',
      newAddressName: '',
      newAddressSurname: '',
      newAddressRoad: '',
      newAddressNumber: '',
      newAddressCode: '',
      newAddressCity: '',
      newAddressProvince: '',
      newAddressPhone: '',
      addresses: [{}],
      sortType: '-1',
      sortTypeHist: '-1',
      sortState: [],
      sortOptions: [
        {text: 'Todos', value: '-1'},
        {text: 'En progreso', value: '0'},
        {text: 'Enviados', value: '1'},
        {text: 'Recibidos', value: '2'}
      ],
      sortEditOptions: [
        {text: 'En progreso', value: '0'},
        {text: 'Enviados', value: '1'},
        {text: 'Recibidos', value: '2'}
      ],
      years_data: [],
      log_month: {},
      total_sales: 0,
      total_users: 0,
      sales_month: {},
      sales_year: {},
      sales_genre: {},
      total_gain: 0,
      gain_month: {},
      gain_year: {},
      gain_genre: {},
      selYear: -1,
      salesYear: 0,
      gainYear: 0,
      contacts: [],
      contactToAnswer: [],
      newContactAnswer: '',
      sending_mail: 0,
      sent: 0
    }
  },
  created() {
    this.getOrders()
    this.getOrdersList()
    this.getAddresses()
    this.getCards()
    this.getAccount()
    this.sortType = '-1'
    this.sortTypeHist = '-1'
    //this.stateOrdersInProgress()
    //this.stateOrdersReceived()
    //this.stateOrdersSend()
    this.getContacts()
  },
  mounted() {
    this.getData()
  },
  methods: {
    round2Dec(trnd) {
      return Math.round(trnd * 100) / 100
    },
    printReceipt() {
      print()
    },
    getCardType(number) {
      // visa
      var re = new RegExp("^4");
      if (number.match(re) != null)
        return "Visa";

      // Mastercard
      re = new RegExp("^5[1-5]");
      if (number.match(re) != null)
        return "MasterCard";

      // AMEX
      re = new RegExp("^3[47]");
      if (number.match(re) != null)
        return "AMEX";

      // Discover
      re = new RegExp("^(6011|622(12[6-9]|1[3-9][0-9]|[2-8][0-9]{2}|9[0-1][0-9]|92[0-5]|64[4-9])|65)");
      if (number.match(re) != null)
        return "Discover";

      // Diners
      re = new RegExp("^36");
      if (number.match(re) != null)
        return "Diners";

      // JCB
      re = new RegExp("^35(2[89]|[3-8][0-9])");
      if (number.match(re) != null)
        return "JCB";

      // Visa Electron
      re = new RegExp("^(4026|417500|4508|4844|491(3|7))");
      if (number.match(re) != null)
        return "Visa Electron";

      return "";
    },
    ccFormat(value) {
      var v = value.replace(/\s+/g, '').replace(/[^0-9]/gi, '')
      var matches = v.match(/\d{4,16}/g);
      var match = matches && matches[0] || ''
      var parts = []
      var i, len
      for (i = 0, len = match.length; i < len; i += 4) {
        parts.push(match.substring(i, i + 4))
      }

      if (parts.length) {
        return parts.join(' ')
      } else {
        return value
      }
    },
    checkDigit(val) {
      var allowedChars = "0123456789"
      var entryVal = val
      var flag
      for (var i = 0; i < entryVal.length; i++) {
        flag = false
        for (var j = 0; j < allowedChars.length; j++) {
          if (entryVal.charAt(i) == allowedChars.charAt(j)) {
            flag = true
          }
        }
        if (flag == false) {
          entryVal = entryVal.replace(entryVal.charAt(i), "")
          i--
        }
      }
      this.ccvendor = this.getCardType(entryVal)
      return this.ccFormat(entryVal)
    },
    chkInput() {
      var val = document.getElementById('paymentNumber').value
      document.getElementById('paymentNumber').value = this.checkDigit(val)

    },
    logout() {
      bus.emit('has-logged-out')
      this.$router.push({path: '/'})
    },
    getAccount() {
      var path = api + 'account/' + this.id
      axios.get(path)
          .then((res) => {
            this.email = res.data.account.email
            this.fname = res.data.account.name
            this.lname = res.data.account.lastname
          })
          .catch((error) => {
            console.log(error)
          })
    },
    toSimpleArray(arr) {
      var arrr = []
      for (var i in arr) {
        arrr.push(arr[i])
      }
      return arrr
    },
    toSimpleArrayKeys(arr) {
      var arrr = []
      for (var i in arr) {
        arrr.push(i)
      }
      return arrr
    },
    getOrders() {
      var path = api + 'order-user/' + this.id
      var currentUser = {username: this.id, password: this.token}
      axios.get(path,{auth: currentUser})
          .then((res) => {
            this.orders = res.data.orders
            this.splitOrders()
          })
          .catch((error) => {
            console.log(error)
            toastr.error('', 'No se ha podido recuperar los pedidos.',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
          })
    },
    changeData() {
      this.chartGeneration(this.selYear)
    },
    chartGeneration(y) {
      this.selYear = y
      this.salesYear = this.sales_year[this.selYear]
      this.gainYear = this.gain_year[this.selYear]
      this.salesMonthOptions = {
        chart: {
          id: "vuechart-example",
        },
        xaxis: {
          categories: ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
            "Noviembre", "Diciembre"],
        },
        title: {
          text: 'Ventas por mes (' + this.selYear + ')',
          align: 'center',
          margin: 10,
          floating: false,
          style: {
            fontSize: '14px',
            fontWeight: 'bold',
            color: '#263238'
          },
        }
      }
      this.salesMonthSeries = [
        {
          name: "Ventas (unidades)",
          data: this.toSimpleArray(this.sales_month[y])
        },
      ]
      this.gainMonthOptions = {
        chart: {
          id: "vuechart-example",
        },
        xaxis: {
          categories: ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
            "Noviembre", "Diciembre"],
        },
        title: {
          text: 'Ganancias por mes (' + this.selYear + ')',
          align: 'center',
          margin: 10,
          floating: false,
          style: {
            fontSize: '14px',
            fontWeight: 'bold',
            color: '#263238'
          },
        }
      }
      this.gainMonthSeries = [
        {
          name: "Ganancia (€)",
          data: this.toSimpleArray(this.gain_month[y])
        },
      ]
      this.gainGenreOptions = {
        chart: {
          type: 'donut'
        },
        series: this.toSimpleArray(this.gain_genre[this.selYear]),
        labels: ["Humanidades", "Técnico y formación", "Métodos de idiomas", "Literatura", "Infantil", "Cómics y manga", "Juvenil", "Otras categorías"],
        title: {
          text: 'Ganancias por género (' + this.selYear + ')',
          align: 'center',
          margin: 10,
          floating: false,
          style: {
            fontSize: '14px',
            fontWeight: 'bold',
            color: '#263238'
          },
        }
      }
      this.salesGenreOptions = {
        chart: {
          type: 'donut'
        },
        series: this.toSimpleArray(this.sales_genre[this.selYear]),
        labels: ["Humanidades", "Técnico y formación", "Métodos de idiomas", "Literatura", "Infantil", "Cómics y manga", "Juvenil", "Otras categorías"],
        title: {
          text: 'Ventas por género (' + this.selYear + ')',
          align: 'center',
          margin: 10,
          floating: false,
          style: {
            fontSize: '14px',
            fontWeight: 'bold',
            color: '#263238'
          },
        }
      }
      this.loginLogOptions = {
        series: [{
          name: "Accesos",
          data: this.toSimpleArray(this.log_month)
        }],
        labels: this.toSimpleArrayKeys(this.log_month),
        title: {
          text: 'Accesos por mes (' + this.getMonthString(new Date().getMonth()) + ')',
          align: 'center',
          margin: 10,
          floating: false,
          style: {
            fontSize: '14px',
            fontWeight: 'bold',
            color: '#263238'
          },
        }
      }
    },
    getMonthString(month) {
      switch (month) {
        case 1:
          return "enero"
        case 2:
          return "febrero"
        case 3:
          return "marzo"
        case 4:
          return "abril"
        case 5:
          return "mayo"
        case 6:
          return "junio"
        case 7:
          return "julio"
        case 8:
          return "agosto"
        case 9:
          return "septiembre"
        case 10:
          return "octubre"
        case 11:
          return "noviembre"
        case 12:
          return "diciembre"
      }
    },
    getData() {
      var path = api + 'data_retriever/all'
      axios.get(path)
          .then((res) => {
            this.years_data = res.data.all.years_data
            this.total_sales = res.data.all.total_sales
            this.total_users = res.data.all.total_users
            this.sales_month = res.data.all.sales_month
            this.sales_year = res.data.all.sales_year
            this.sales_genre = res.data.all.sales_genre
            this.total_gain = res.data.all.total_gain
            this.gain_month = res.data.all.gain_month
            this.gain_year = res.data.all.gain_year
            this.gain_genre = res.data.all.gain_genre
            this.log_month = res.data.all.log_month
            this.chartGeneration(this.years_data[0])
          })
          .catch((error) => {
            console.log(error)
            toastr.error('', 'No se ha podido recuperar los datos.',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
          })
    },
    getOrdersList() {
      var path = api + 'orders'
      var currentUser = {username: this.id, password: this.token}
      axios.get(path,{auth: currentUser})
          .then((res) => {
            this.ordersHist = res.data.orders
            this.splitOrdersList()
          })
          .catch((error) => {
            console.log(error)
            toastr.error('', 'No se ha podido recuperar los pedidos.',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
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
    changeViewingOrders(index) {
      this.viewOrders = this.sOrders[index]
      this.cIndex = index
    },
    changeViewingOrdersList(index) {
      this.viewOrdersList = this.sOrdersList[index]
      this.cIndexList = index
    },
    splitOrders() {
      this.sOrders = []
      this.viewOrders = []
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
    splitOrdersList() {
      this.sOrdersList = []
      this.viewOrdersList = []
      this.numberOfOrders = this.ordersHist.length
      this.numberOfPages = Math.ceil(this.ordersHist.length / this.maxPerPage)
      let i
      let arr = []
      for (i = 0; i < (this.numberOfPages - 1); i++) {
        arr = this.ordersHist.slice(i * this.maxPerPage, this.maxPerPage * (i + 1))
        this.sOrdersList.push(arr)
      }
      this.sOrdersList.push(this.ordersHist.slice(-(this.ordersHist.length % this.maxPerPage)))
      this.viewOrdersList = this.sOrdersList[0]
      for (i = 0; i < this.viewOrdersList.length; i++) {
        this.sortState[this.viewOrdersList[i].id] = this.viewOrdersList[i].state
      }
    },
    cancelOrder(id) {
      var path = api + 'order/' + id
      var currentUser = {username: this.id, password: this.token}
      axios.delete(path,{auth: currentUser})
          // eslint-disable-next-line no-unused-vars
          .then((res) => {
            toastr.success('', '¡Pedido cancelado!',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
            this.getOrders()
          })
          .catch((error) => {
            console.log(error)
            toastr.error('', 'No se ha podido cancelar el pedido.',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
          })
    },
    cancelOrderList(id) {
      var path = api + 'order/' + id
      var currentUser = {username: this.id, password: this.token}
      axios.delete(path,{auth: currentUser})
          // eslint-disable-next-line no-unused-vars
          .then((res) => {
            toastr.success('', '¡Pedido cancelado!',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
            this.getOrdersList()
          })
          .catch((error) => {
            console.log(error)
            toastr.error('', 'No se ha podido cancelar el pedido.',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
          })
    },
    viewOrder(i) {
      this.order.id = i.id
      this.order.date = i.date
      this.order.total = i.total
      this.order.taxes = i.taxes
      this.order.shipping = i.shipping
      this.order.send_type = i.send_type
      this.order.card_num = i.card.number
      this.order.card_vendor = i.card.method
      this.order.add_name = i.address.name
      this.order.add_lname = i.address.surnames
      this.order.street = i.address.street
      this.order.add_number = i.address.number
      this.order.add_cp = i.address.cp
      this.order.add_city = i.address.city
      this.order.add_prov = i.address.province
      this.order.telf = i.address.telf
      this.order.articles = i.articles
    },
    modifyProfile() {
      this.editProfile = true
    },
    saveProfile() {
      this.editProfile = false
      var path = api + 'account/' + this.id
      var currentUser = {username: this.id, password: this.token}

      axios.put(path, {'name': this.fname, 'lastname': this.lname, 'email': this.email}, {auth: currentUser})
          .then((res) => {
            path = res
            toastr.success('', 'Datos de usuario actualizados.',
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
            toastr.error('', 'No se ha podido guardar los cambios.',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
          })
    },
    changePassword() {
      this.editPass = true
    },

    savePassword() {
      this.editPass = false

      if (this.newPassword == '' || this.newPassword2 == '' || this.oldPassword == '') {
        toastr.info('', 'Por favor rellene todos los campos gracias.',
            {
              timeOut: 2500,
              progressBar: true,
              newestOnTop: true,
              positionClass: 'toast-bottom-right',
              preventDuplicates: true
            })
      } else if (this.newPassword != this.newPassword2) {
        toastr.info('', 'La nueva contraseña no coincide, intentelo de nuevo.',
            {
              timeOut: 2500,
              progressBar: true,
              newestOnTop: true,
              positionClass: 'toast-bottom-right',
              preventDuplicates: true
            })
      } else if (!this.validatePassword(this.newPassword)) {
        toastr.error('', 'La contraseña no cumple los requisitos de seguridad.',
            {
              timeOut: 2500,
              progressBar: true,
              newestOnTop: true,
              positionClass: 'toast-bottom-right',
              preventDuplicates: true
            })
      } else {
        var path = api + 'account/' + this.id + "/change_password"
        var currentUser = {username: this.id, password: this.token}
        axios.put(path, {'old_password': this.oldPassword, 'new_password': this.newPassword}, {auth: currentUser})
            .then((res) => {
              path = res
              toastr.success('', 'Datos de usuario actualizados.',
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
              if (error.response.status == 406) {
                toastr.info('', 'La contraseña actual no coincide con la de la cuenta.',
                    {
                      timeOut: 2500,
                      progressBar: true,
                      newestOnTop: true,
                      positionClass: 'toast-bottom-right',
                      preventDuplicates: true
                    })
              } else {
                toastr.error('', 'No se ha podido guardar los cambios.',
                    {
                      timeOut: 2500,
                      progressBar: true,
                      newestOnTop: true,
                      positionClass: 'toast-bottom-right',
                      preventDuplicates: true
                    })
              }
            })
      }

      this.oldPassword = ''
      this.newPassword = ''
      this.newPassword2 = ''
    },
    checkNewPasswordSymbol(pwd) {
      return /\W/.test(pwd);
    },
    checkNewPasswordLower(pwd) {
      return /[a-z]/.test(pwd);
    },
    checkNewPasswordUpper(pwd) {
      return /[A-Z]/.test(pwd);
    },
    checkNewPasswordNumber(pwd) {
      return /\d/.test(pwd);
    },
    checkNewPasswordLength(pwd) {
      return /^[a-zA-Z\d\W]{8,}$/.test(pwd);
    },
    validatePassword(pwd) {
      return this.checkNewPasswordSymbol(pwd) && this.checkNewPasswordLower(pwd) &&
          this.checkNewPasswordUpper(pwd) && this.checkNewPasswordNumber(pwd) && this.checkNewPasswordLength(pwd)
    },
    scoreNewPassword() {
      let score = 0;
      const pass = this.newPassword;

      const variations = {
        digits: /\d/.test(pass),
        lower: /[a-z]/.test(pass),
        upper: /[A-Z]/.test(pass),
        symbols: /\W/.test(pass),
      };
      const variations_2 = {
        digits: /(.*\d){2}/.test(pass),
        lower: /(.*[a-z]){2}/.test(pass),
        upper: /(.*[A-Z]){2}/.test(pass),
        symbols: /(.*\W){2}/.test(pass),
      };
      const variations_3 = {
        digits: /(.*\d){3}/.test(pass),
        lower: /(.*[a-z]){3}/.test(pass),
        upper: /(.*[A-Z]){3}/.test(pass),
        symbols: /(.*\W){3}/.test(pass),
      };

      let variationCount = 0;
      for (const check in variations) variationCount += (variations[check] === true) ? 2 : 0;
      for (const check in variations_2) variationCount += (variations_2[check] === true) ? 1 : 0;
      for (const check in variations_3) variationCount += (variations_3[check] === true) ? 1 : 0;

      score += (pass.length <= 12) ? variationCount * 5 + pass.length * 2 : variationCount * 5 + 25;

      const elem = document.getElementById("mynewprobar");
      if (elem != null) elem.style.width = score + '%';

      return score
    },
    getYear() {
      return new Date().getFullYear()
    },
    checkNewPasswordStrength() {
      const score = this.scoreNewPassword();
      if (score >= 80) {
        document.getElementById("mynewprobar").style.background = "forestgreen";
        return "Muy seguro";
      }
      if (score >= 60) {
        document.getElementById("mynewprobar").style.background = "limegreen";
        return "Seguro";
      }
      if (score >= 30) {
        document.getElementById("mynewprobar").style.background = "orange";
        return "Regular";
      }
      if (score) {
        document.getElementById("mynewprobar").style.background = "red";
        return "Débil"
      }
      return ""
    },
    stateOrdersInProgress() {
      var path = api + 'orders-state-0/' + this.id
      var currentUser = {username: this.id, password: this.token}
      axios.get(path,{auth: currentUser})
          .then((res) => {
            this.orders = res.data.orders
            this.splitOrders()
          })
          .catch((error) => {
            console.log(error)
            toastr.error('', 'No se ha podido recuperar los pedidos.',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
          })

    },
    stateOrdersSend() {
      var path = api + 'orders-state-1/' + this.id
      var currentUser = {username: this.id, password: this.token}
      axios.get(path,{auth: currentUser})
          .then((res) => {
            this.orders = res.data.orders
            this.splitOrders()
          })
          .catch((error) => {
            console.log(error)
            toastr.error('', 'No se ha podido recuperar los pedidos.',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
          })

    },
    stateOrdersReceived() {
      var path = api + 'orders-state-2/' + this.id
      var currentUser = {username: this.id, password: this.token}

      axios.get(path,{auth: currentUser})
          .then((res) => {
            this.orders = res.data.orders
            this.splitOrders()
          })
          .catch((error) => {
            console.log(error)
            toastr.error('', 'No se ha podido recuperar los pedidos.',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
          })

    },
    stateOrdersListInProgress() {
      var path = api + 'orders-list-state-0'
      var currentUser = {username: this.id, password: this.token}

      axios.get(path,{auth: currentUser})
          .then((res) => {
            this.ordersHist = res.data.orders
            this.splitOrdersList()
          })
          .catch((error) => {
            console.log(error)
            toastr.error('', 'No se ha podido recuperar los pedidos.',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
          })

    },
    stateOrdersListSend() {
      var path = api + 'orders-list-state-1'
      var currentUser = {username: this.id, password: this.token}

      axios.get(path,{auth: currentUser})
          .then((res) => {
            this.ordersHist = res.data.orders
            this.splitOrdersList()
          })
          .catch((error) => {
            console.log(error)
            toastr.error('', 'No se ha podido recuperar los pedidos.',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
          })

    },
    stateOrdersListReceived() {
      var path = api + 'orders-list-state-2'
      var currentUser = {username: this.id, password: this.token}

      axios.get(path,{auth: currentUser})
          .then((res) => {
            this.ordersHist = res.data.orders
            this.splitOrdersList()
          })
          .catch((error) => {
            console.log(error)
            toastr.error('', 'No se ha podido recuperar los pedidos.',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
          })

    },
    addCard() {
      this.addCardForm.card_owner = document.getElementById('paymentTitular').value
      this.addCardForm.number = document.getElementById('paymentNumber').value
      this.addCardForm.date = document.getElementById('paymentEndDate').value
      this.addCardForm.payment_method = this.getCardType(this.addCardForm.number)


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
      } else if (!this.validateEndDate(this.addCardForm.date)) {
        toastr.error('', 'Fecha de caducidad no valida.',
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
      var today, someday
      var exMonth = date.slice(0, 2)
      var exYear = date.slice(3)
      today = new Date()
      someday = new Date()
      someday.setFullYear(exYear, exMonth, 1)
      if (someday < today) {
        return false
      }
      return true
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
    sortBy(type) {
      this.cIndex = 0
      if (type == "-1") {
        this.getOrders()
      }
      if (type == "0") {
        this.stateOrdersInProgress()
      }
      if (type == "1") {
        this.stateOrdersSend()
      }
      if (type == "2") {
        this.stateOrdersReceived()
      }

    },
    sortByHist(type) {
      this.cIndexList = 0
      if (type == "-1") {
        this.getOrdersList()
      }
      if (type == "0") {
        this.stateOrdersListInProgress()
      }
      if (type == "1") {
        this.stateOrdersListSend()
      }
      if (type == "2") {
        this.stateOrdersListReceived()
      }

    },
    changeState(type, order_id) {
      const path = api + 'order/' + order_id
      const parameters = {
        state: type
      }
      var currentUser = {username: this.id, password: this.token}
      axios.put(path, parameters,{auth: currentUser})
          // eslint-disable-next-line no-unused-vars
          .then((res) => {
            if (this.sortTypeHist == "-1") {
              this.getOrdersList()
            }
            if (this.sortTypeHist == "0") {
              this.stateOrdersListInProgress()
            }
            if (this.sortTypeHist == "1") {
              this.stateOrdersListSend()
            }
            if (this.sortTypeHist == "2") {
              this.stateOrdersListReceived()
            }
          })
          .catch((error) => {
            console.log(error)
            toastr.error('', 'No se ha podido recuperar los pedidos.',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
          })

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
    deleteAccount() {
      var path = api + 'account/' + this.id
      axios.delete(path)
          // eslint-disable-next-line no-unused-vars
          .then((res) => {
            toastr.success('', '¡Tu cuenta ha sido eliminada! :(',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
            bus.emit('has-logged-out')
            this.$router.push({path: '/'})
          })
          .catch((error) => {
            console.log(error)
            toastr.error('', 'Algo no salió como se esperaba, inténtelo de nuevo mas tarde...',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
          })
    },
    // eslint-disable-next-line no-unused-vars
    searchOrder(order_id) {
    },
    getContacts() {
      var path = api + 'contact_list/'
      axios.get(path)
          .then((res) => {
            this.contacts = res.data.contacts
          })
          .catch((error) => {
            console.log(error)
            toastr.error('', 'No se ha podido recuperar los contactos.',
                {
                  timeOut: 2500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
          })
    },
    assignContact(index) {
      this.contactToAnswer = this.contacts[index]
      this.sent = 0
      this.sending_mail = 0
    },
    deleteContact(index){
      this.assignContact(index)
      var path = api + 'contact_info/' + this.contactToAnswer.id
      axios.delete(path)
        // eslint-disable-next-line no-unused-vars
        .then((res) => {
          toastr.success('', '¡Consulta eliminada con éxito!',
              {
                timeOut: 2500,
                progressBar: true,
                newestOnTop: true,
                positionClass: 'toast-bottom-right',
                preventDuplicates: true
              })
          this.getContacts()
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
          this.getContacts()
      })
    },
    validate_response(){
      if(this.sending_mail)
        return
      this.sending_mail = 1
      if( this.newContactAnswer == '' ){
        toastr.info('', 'Por favor, añada una respuesta.',
            {
              timeOut: 2500,
              progressBar: true,
              newestOnTop: true,
              positionClass: 'toast-bottom-right',
              preventDuplicates: true
            })
        this.sending_mail = 0
      }
      else{
        var parameters = {
          "contact_id":this.contactToAnswer.id,
          "contact_response": this.newContactAnswer
        }
        console.log(parameters)
        this.send_response(parameters)
      }
      this.newContactAnswer = ''
    },
    send_response(parameters){
      var path = api + 'send_contact_response'
      axios.post(path, parameters)
        // eslint-disable-next-line no-unused-vars
        .then((res) => {
          toastr.success('', '¡La respuesta fue enviada!',
              {
                timeOut: 2500,
                progressBar: true,
                newestOnTop: true,
                positionClass: 'toast-bottom-right',
                preventDuplicates: true
              })
          this.sent = 1
          this.sending_mail = 0
          this.getContacts()
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
          this.sent = 1
          this.sending_mail = 0
          this.getContacts()
        })
    },
    send_ticket(order_id){
      if(this.sending_mail)
        return

      this.sending_mail = 1

      var parameters = {"account_id": this.id, "order_id": order_id}

      var path = api + 'send_ticket'
      axios.post(path, parameters)
        // eslint-disable-next-line no-unused-vars
        .then((res) => {
          toastr.success('', '¡El ticket fue enviado!',
              {
                timeOut: 2500,
                progressBar: true,
                newestOnTop: true,
                positionClass: 'toast-bottom-right',
                preventDuplicates: true
              })
          this.sending_mail = 0
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
          this.sending_mail = 0
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

.navbartextbtdark {
  color: #3b494d !important;
  font-size: 1.2em
}
</style>