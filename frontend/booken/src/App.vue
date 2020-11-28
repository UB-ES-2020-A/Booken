<style scoped>
@import url("./assets/animate.min.css");
@import url("./assets/wish_list.css");
@import url("./assets/shopping-cart.css");
</style>
<template>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
        integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
  <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
  <link href='https://fonts.googleapis.com/css?family=Lato' rel='stylesheet' type='text/css'>
  <wrapper class="d-flex flex-column">
    <!-- First navbar-->
    <div style="background: #2bc4ed;">

      <div class="container" style="max-width: 1400px">

        <nav class="navbar navbar-expand-lg navbar-dark ">
          <!-- Brand -->
          <a class="navbar-brand mainlogo ml-3 animate__animated animate__flipInX" href="/">booken<span
              class="badge badge-light" style="font-size: 0.3em; letter-spacing: normal">alpha</span></a>

          <form class="form-inline mx-auto searchBarOutside" style="min-width: 30%">
            <input class="form-control" style="min-width: 80%" type="search"
                   placeholder="Busca por autor, título, ISBN"
                   aria-label="Search">
            <button class="btn ml-2" style="min-width: 50px; background-color: #3b494d;" type="submit"><i
                class="fas fa-search"
                style="color: #FFF"/>
            </button>
          </form>

          <!-- Links Button -->
          <button class="navbar-toggler ml-auto lapse" type="button" data-toggle="collapse"
                  data-target="#mynavbar, #mynavbar2"
                  aria-controls="mynavbar, mynavbar2" aria-expanded="false">
            <span class="navbar-toggler-icon"></span>
          </button>

          <!-- Links -->
          <div class="collapse navbar-collapse my-3" id="mynavbar">
            <ul class="navbar-nav ml-xl-auto buttonList ml-lg-auto">
              <li class="nav-item my-xl-auto my-3 mx-2 mx-md-0 ">
                <div class="searchBarInside mx-auto mb-md-3 my-xl-auto ">
                  <form class="form-inline ">
                    <input class="form-control" type="search"
                           placeholder="Busca por autor, título, ISBN"
                           aria-label="Search">
                    <button class="btn ml-auto " style="background-color: #3b494d;" type="submit"><i
                        class="fas fa-search"
                        style="color: #FFF"/>
                    </button>
                  </form>
                </div>
              </li>
              <li class="nav-item  my-3 ml-2 mr-2 ml-md-0 mr-md-auto ">
                <button class="btn mt-md-3 my-xl-auto my-lg-auto" data-toggle="collapse"
                        data-target="#mynavbar, #mynavbar2"
                        style="background-color: #3b494d" type="submit"
                        v-if="!loggedIn"
                        @click="goToAccess">
                  <i class="fas fa-user" style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/>
                  <a class="navbartextbt">Identíficate</a>
                </button>
                <button class="btn mt-md-3 my-xl-auto my-lg-auto" data-toggle="collapse"
                        data-target="#mynavbar, #mynavbar2"
                        style="background-color: #3b494d;" type="submit"
                        v-if="loggedIn" @click="goToCP">
                  <i class="fas fa-user-circle" style="color: white; font-size: 1.5em; margin-right: 0.5em"/>
                  <a class="navbartextbt">Tu cuenta</a>
                </button>
              </li>
              <li class="nav-item  my-3 mx-2 mx-md-3 ">
                <button class="btn mt-md-3 my-xl-auto my-lg-auto" data-toggle="collapse"
                        data-target="#mynavbar, #mynavbar2"
                        style="background-color: #3b494d;" type="submit">
                  <i class="fas fa-question-circle" style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
                    class="navbartextbt" @click="getHelp">Ayuda</a>
                </button>
              </li>
              <li class="nav-item  my-3 ml-2 mr-2 ml-md-auto mr-md-0  ">
                <button class="btn mt-md-3 my-xl-auto my-lg-auto" data-toggle="collapse"
                        data-target="#mynavbar, #mynavbar2"
                        style="background-color: #3b494d;" type="submit" @click="toggleCart" v-if="!viewCart">
                  <i class="fas fa-shopping-basket " style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
                    class="navbartextbt">Cesta</a>
                </button>
                <button class="btn mt-md-3 my-xl-auto my-lg-auto" data-toggle="collapse"
                        data-target="#mynavbar, #mynavbar2"
                        style="background-color: #3b494d;" type="submit" @click="toggleCart" v-if="viewCart">
                  <i class="fas fa-arrow-left " style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
                    class="navbartextbt">Volver</a>
                </button>
              </li>
            </ul>
          </div>
        </nav>
      </div>
    </div>
    <!-- Second navbar -->
    <div class="bg-dark">
      <nav class="navbar navbar-expand-lg navbar-light">
        <div class="collapse navbar-collapse" id="mynavbar2">
          <div class="nav navbar-nav mx-auto" @click="hideCart">

            <router-link :to="{name: 'books', params: {category: 'HUMANIDADES'}}"
                         class="nav-item nav-link categoriestxt" active-class="active"
            >
              <div data-toggle="collapse" data-target="#mynavbar, #mynavbar2">Humanidades</div>
            </router-link>
            <router-link :to="{name: 'books', params: {category: 'TECNICO Y FORMACION'}}"
                         class="nav-item nav-link categoriestxt" active-class="active"
            >
              <div data-toggle="collapse" data-target="#mynavbar, #mynavbar2">Técnico y formación</div>
            </router-link>
            <router-link :to="{name: 'books', params: {category: 'METODOS DE IDIOMAS'}}"
                         class="nav-item nav-link categoriestxt" active-class="active"
            >
              <div data-toggle="collapse" data-target="#mynavbar, #mynavbar2">Métodos de idiomas</div>
            </router-link>
            <router-link class="nav-item nav-link categoriestxt" active-class="active"
                         :to="{name: 'books', params: {category: 'LITERATURA'}}">
              <div data-toggle="collapse" data-target="#mynavbar, #mynavbar2">Literatura</div>
            </router-link>
            <router-link class="nav-item nav-link categoriestxt" active-class="active"
                         :to="{name: 'books', params: {category: 'INFANTIL'}}">
              <div data-toggle="collapse" data-target="#mynavbar, #mynavbar2">Infantil</div>
            </router-link>
            <router-link class="nav-item nav-link categoriestxt" active-class="active"
                         :to="{name: 'books', params: {category: 'COMICS Y MANGA'}}">
              <div data-toggle="collapse" data-target="#mynavbar, #mynavbar2">Cómics y manga</div>
            </router-link>
            <router-link class="nav-item nav-link categoriestxt" active-class="active"
                         :to="{name: 'books', params: {category: 'JUVENIL'}}">
              <div data-toggle="collapse" data-target="#mynavbar, #mynavbar2">Juvenil</div>
            </router-link>
            <router-link class="nav-item nav-link categoriestxt" active-class="active"
                         :to="{name: 'books', params: {category: 'OTRAS CATEGORIAS'}}">
              <div data-toggle="collapse" data-target="#mynavbar, #mynavbar2">Otras categorías</div>
            </router-link>
            <router-link class="nav-link categoriestxt" active-class="active"
                         :to="{name: 'books', params: {category: 'TODO'}}">
              <div data-toggle="collapse" data-target="#mynavbar, #mynavbar2" style="color: yellow">Ver todo</div>
            </router-link>
          </div>
        </div>
      </nav>
    </div>

    <main class="flex-fill">
      <router-view :key="$route.fullPath" v-if="!viewCart" :logged="this.loggedIn" :token="this.tokenIn"
                   :id="this.idIn" :type="this.typeIn" :total="this.total" :taxes="this.taxes" :subtotal="this.subtotal"
                   :cart="this.cart"/>
      <!-- Cart -->
      <div id="shopping_cart" v-if="viewCart">
        <h1 style="margin-top: 1em">Tu cesta</h1>
        <section class="shopping-cart" v-if="this.cart.length >= 1">
          <ol class="ui-list shopping-cart--list" id="shopping-cart--list">


            <li class="_grid shopping-cart--list-item" v-for="(item,i) in this.cart" :key="i">
              <div class="_column product-image" id="#image">
                <img class="product-image--img" :src="item.cover" alt="Item image" style="max-width: 110px"/>
              </div>
              <div class="_column product-info">
                <h4 class="product-name">{{ item.title }}</h4>
                <p class="product-desc">{{ item.desc }}</p>
                <div class="price product-single-price">{{ item.price }}€</div>
              </div>
              <div class="_column product-modifiers">
                <div class="_grid">
                  <button class="_btn _column product-subtract" @click="decreaseQuant(item.id)">&minus;</button>
                  <div class="_column product-qty">{{ item.quant }}</div>
                  <button class="_btn _column product-plus" @click="increaseQuant(item.id)" :disabled="item.quant>=item.quant_t">&plus;</button>
                </div>
                <button class="_btn entypo-trash product-remove" @click="removeBook(item.id)">Quitar</button>
                <div class="price product-total-price">{{ item.quant * item.price }}€</div>
              </div>
            </li>
          </ol>
          <footer class="_grid cart-totals">
            <div class="_column subtotal" id="subtotalCtr">
              <div class="cart-totals-key">Subtotal</div>
              <div class="cart-totals-value">{{ subtotal }}€</div>
            </div>
            <div class="_column taxes" id="taxesCtr">
              <div class="cart-totals-key">IVA (21%)</div>
              <div class="cart-totals-value">{{ taxes }}€</div>
            </div>
            <div class="_column total" id="totalCtr">
              <div class="cart-totals-key">Total</div>
              <div class="cart-totals-value">{{ total }}€</div>
            </div>
            <div class="col mb-2">
              <div class="row">
                <div class="col-sm-12  col-md-6">
                  <button class="btn btn-lg btn-block"
                          style="background-color:#3b494d; color: white; margin-top: 0.5rem"
                          @click="toggleCart">
                    Continuar comprando
                  </button>
                </div>
                <div class="col-sm-12 col-md-6 text-right">
                  <button class="btn btn-lg btn-block"
                          style="background-color: #2bc4ed; color: white; margin-top: 0.5rem"
                          @click="checkout">
                    Tramitar pedido
                  </button>
                </div>
              </div>
            </div>
          </footer>

        </section>
        <div style="margin-top: 1rem" v-if="this.cart.length == 0">
          <div class="row">
            <div class="col">
              <h3 style="margin-top: 1.5rem;">Tu cesta está vacía.</h3>
              <button class="btn btn-lg animate__animated animate__bounce animate__infinite" @click="toggleCart"
                      style="background-color:#3b494d; color: white; margin-top: 5rem; margin-bottom: 10rem">¿Compras
                algo?
              </button>
            </div>
          </div>
        </div>

        <!-- Wish_list -->
        <h1 style="margin-top: 1em" v-if="this.loggedIn">Deseados</h1>
        <div v-if="this.wish_list.length > 0 && this.loggedIn">
          <div class="container wish_container" v-for="(wish_item) in this.wish_list" :key="wish_item">

            <div class="row">

              <div class="col-md-3" style="margin:auto">
                <img style="max-height:10em;" :src="wish_item.cover_image_url" :alt="wish_item.name">
              </div>


              <div class="col-md" style="margin:auto">
                <div style="text-align:left;">
                  <h5 class="card-title" @click="this.viewCart=0">
                    <router-link :to="{name: 'BookInfo', params: {id: wish_item.id}}" style="color:#424242;">
                      {{ wish_item.title }}
                    </router-link>
                  </h5>
                </div>


                <div class="row">
                  <div class="col-md-8">
                    <p class="card-text" style="text-align:left;">{{ wish_item.description }}</p>
                  </div>
                  <div class="col-md" style="margin:auto; margin-right:0; max-width:9.8em">
                    <div style="display:flex; flex-direction: horizontal; background-color: #6E6E6E; margin-bottom:auto;
                            border-color:#6E6E6E; border-style:solid; border-radius:0.2em; max-height:3em;">
                      <span style="margin:0.5em; color:#FFFFFF">{{ wish_item.price }}€</span>
                      <button class="btn btn-success" @click="addToCart(wish_item)">Añadir</button>
                    </div>
                  </div>
                </div>


                <div class="wish_footer" style="margin-top:1em !important;">
                  <div style="display:flex;">
                    <p class="wish_property" style="margin-right:1em"><small
                        class="text-muted">{{ wish_item.genre }}</small></p>
                    <p v-if="wish_item.cover_type == 0" class="wish_property"><small class="text-muted">TAPA
                      DURA</small>
                    </p>
                    <p v-if="wish_item.cover_type == 1" class="wish_property"><small class="text-muted">TAPA
                      BLANDA</small></p>
                  </div>
                  <p class="wish_delete" @click="deleteFromWishList(wish_item)"><small
                      class="text-muted">eliminar</small>
                  </p>
                </div>
              </div>

            </div>
          </div>
        </div>
        <div v-if="this.wish_list.length == 0 && this.loggedIn">
          <h3 style="margin-bottom: 5em; margin-top: 1.5em">¡Vaya! No hay nada por aquí 👀.</h3>
        </div>
      </div>
    </main>
    <!-- Footer -->
    <footer class="site-footer">
      <div class="container">
        <div class="row">
          <div class="col-sm-12 col-md-6">
            <h6>Sobre booken</h6>
            <p class="text-justify">Librería virtual de habla hispana que brinda información y hace envíos a los cinco
              continentes, garantizando un gran
              fondo bibliográfico apoyado por la experiencia de expertos libreros y expertos en internet desde hace
              más
              de una década.</p>

            <p>booken permite registrase y acceder tanto a empresas como usuarios a infinidad de posibilidades,
              con el fin de conseguir el libro que se necesita. Se ha creado así una gran comunidad lectora, alrededor
              nuestro. Somos tu librero en Internet.
            </p>
          </div>

          <div class="col-xs-6 col-md-3">
            <h6>AYUDA</h6>
            <ul class="footer-links">
              <li @click="hideCart">
                <router-link to="/contact">Contacto</router-link>
              </li>
              <li @click="hideCart"><a href="">Preguntas frecuentes</a></li>

            </ul>
          </div>

          <div class="col-xs-6 col-md-3">
            <h6>Información legal</h6>
            <ul class="footer-links">
              <li><a href="https://pdfhost.io/v/eKtsS3QVL_Privacy_Policy.pdf">Condiciones de uso</a></li>
              <li><a href="https://pastebin.com/7Xfv3tkY">Política de devoluciones</a></li>
              <li><a href="https://pdfhost.io/v/ElKYUhMFl_privacidadpdf.pdf">Política de protección de datos</a></li>
            </ul>
          </div>
        </div>
        <hr>
      </div>
      <div class="container">
        <div class="row">
          <div class="col-md-8 mx-auto">
            <p class="copyright-text" style="color: white">Copyright &copy; {{ this.getYear() }}
              <a href="#" style="font-family: LogoFont; font-size: 1.45em; color: #2bc4ed">booken</a>.
            </p>
          </div>
        </div>
      </div>
    </footer>
  </wrapper>
</template>
<script>
import * as toastr from './assets/toastr.js'
import Front from './components/Front.vue'
import Access from "@/components/Access"
import {bus, api} from './main.js'
import axios from 'axios'
import BookInfo from "@/components/BookInfo";
import Contact from "@/components/Contact";
import ControlPanel from "@/components/ControlPanel";
import ShowBooks from "@/components/ShowBooks";

export default {
  name: 'App',
  components: {
    // eslint-disable-next-line vue/no-unused-components
    Front,
    // eslint-disable-next-line no-undef,vue/no-unused-components
    Access,
    // eslint-disable-next-line vue/no-unused-components
    BookInfo,
    // eslint-disable-next-line vue/no-unused-components
    Contact,
    // eslint-disable-next-line vue/no-unused-components
    ControlPanel,
    // eslint-disable-next-line vue/no-unused-components
    ShowBooks
  },
  created() {
    bus.on('has-logged-in', (asd) => {
      this.loggedIn = Boolean(asd.logged)
      this.tokenIn = String(asd.token)
      this.typeIn = parseInt(asd.type)
      this.idIn = parseInt(asd.id)
    })
    bus.on('added-to-cart', (book) => {
      this.checkAddToCart(book)
      bus.emit('cart-updated')
    })
    bus.on('cart-updated', () => {
      this.computeTotals()
    })
    bus.on('has-logged-out', () => {
      this.loggedIn = false
      this.tokenIn = ''
      this.typeIn = -1
      this.idIn = -1
    })
    bus.on('empty_cart', () => {
      this.cart = []
      bus.emit('cart-updated')
    })
  },
  data() {
    return {
      loggedIn: false,
      tokenIn: '',
      taxes: 0,
      subtotal: 0,
      shipping: 7.00,
      total: 5.00,
      idIn: -1,
      cart: [],
      wish_list: [
        {
          ISBN: 9788431690656,
          author: ["Maria Angelidou"],
          back_cover_image_url: "https://images-na.ssl-images-amazon.com/images/I/81MQygGNrCL.jpg",
          cover_image_url: "https://pictures.abebooks.com/isbn/9788431690656-es.jpg",
          cover_type: 0,
          description: "Regresa Megan Maxwell con una novela romántico-erótica tan ardiente que se derretirá en tus manos. Vuelve a soñar con la nueva novela de la autora nacional más vendida.",
          editorial: "Vicens Vives",
          genre: "HUMANIDADES",
          id: 1,
          language: "Castellano",
          name: "Mitos griegos",
          num_pages: 128,
          num_sales: 0,
          price: 7.5,
          synopsis: "El presente volumen constituye una inmejorable introducción al universo de la mitología. Recoge catorce mitos griegos, seleccionados entre los más famosos y atractivos, que han sido narrados con amenidad y sencillez, pero también con una evidente ambición literaria. El libro cuenta con magníficas ilustraciones realizadas por el artista búlgaro Svetlín.",
          total_available: 28,
          year: 2013
        },
        {
          ISBN: 9788466668545,
          author: ["Arturo Pérez-Reverte"],
          back_cover_image_url: "",
          cover_image_url: "https://imagessl5.casadellibro.com/a/l/t5/45/9788466668545.jpg",
          cover_type: 0,
          description: "Vive el fenómeno que ha enganchado a más de 1.000.000 de lectores",
          editorial: "S.A. Ediciones B",
          genre: "LITERATURA",
          id: 6,
          language: "Castellano",
          name: "Rey Blanco",
          num_pages: 528,
          num_sales: 10,
          price: 20,
          synopsis: "Cuando Antonia Scott recibe este mensaje, sabe muy bien quien se lo envía. Tambien sabe que ese juego es casi imposible de ganar. Pero a Antonia no le gusta perder.  Despues de todo este tiempo huyendo, la realidad ha acabado alcanzándola. Antonia es cinturón negro en mentirse a sí misma, pero ahora tiene claro que si pierde esta batalla, las habrá perdido todas.  -La reina es la figura más poderosa del tablero -dice el Rey Blanco-. Pero por poderosa que sea una pieza de ajedrez, nunca debe olvidar que hay una mano que la mueve.  -Eso ya lo veremos-, responde Antonia.  EL FINAL ES SOLO EL PRINCIPIO",
          total_available: 100,
          year: 2020,
        }
      ],
      typeIn: -1,
      email: "prueba@gmail.com",
      viewCart: false,
      //toggledNav: false
    }
  },
  methods: {
    round2Dec(trnd) {
      return Math.round(trnd * 100) / 100
    },
    computeTotals() {
      this.getSubTotal()
      this.taxes = Math.round((0.21 * this.subtotal) * 100) / 100
      this.total = Math.round((this.subtotal + this.taxes) * 100) / 100
    },
    increaseQuant(id) {
      var b = this.searchInCart(id)
      b.quant += 1
      bus.emit('cart-updated')
      toastr.success('', 'Carrito actualizado.',
          {timeOut: 2500, progressBar: true, newestOnTop: true, preventDuplicates: true, positionClass: 'toast-bottom-right'})
    },
    getSubTotal() {
      this.subtotal = 0
      var i, item
      for (i in this.cart) {
        item = this.cart[i]
        this.subtotal += (item.price * item.quant)
      }
      this.subtotal = Math.round((this.subtotal) * 100) / 100
    },
    getBookIndex(id) {
      var i, item
      if (this.cart.length == 0) {
        return null
      } else {
        for (i in this.cart) {
          item = this.cart[i]
          if (item.id == id) {
            return i
          }
        }
      }
    },
    decreaseQuant(id) {
      var b = this.searchInCart(id)
      if (b.quant == 1) {
        this.cart.splice(this.getBookIndex(id), 1)
      } else {
        b.quant -= 1
      }
      bus.emit('cart-updated')
      toastr.success('', 'Carrito actualizado.',
          {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right', preventDuplicates: true})
    },
    removeBook(id) {
      this.cart.splice(this.getBookIndex(id), 1)
      bus.emit('cart-updated')
      toastr.success('', 'Carrito actualizado.',
          {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right', preventDuplicates: true})
    },
    getHelp() {
      if (this.viewCart)
        this.viewCart = false
      this.$router.push({path: '/cfm'})
    },
    hideCart() {
      if (this.viewCart)
        this.viewCart = false
    },
    toggleCart() {
      this.viewCart = !this.viewCart
      if (this.viewCart)
        this.getWishList()
    },
    checkout() {
      this.viewCart = false
      if (this.loggedIn)
        this.$router.push({path: '/cfm'})
      else
        this.$router.push({path: '/access'})

    },
    searchInCart(id) {
      var i, item
      if (this.cart.length == 0) {
        return null
      } else {
        for (i in this.cart) {
          item = this.cart[i]
          if (item.id == id) {
            return item
          }
        }
      }
    },
    checkAddToCart(book) {
      var b = this.searchInCart(book.id)
      if (b == null) {
        this.cart.push(book)
      } else {
        b.quant += 1
      }
    },
    getYear() {
      return new Date().getFullYear()
    },
    goToAccess() {
      if (this.viewCart)
        this.viewCart = false
      this.$router.push({path: '/access'})
    },
    goToCP() {
      if (this.viewCart)
        this.viewCart = false
      this.$router.push({path: '/cp'})
    },
    getTodayDate() {
      var today = new Date()
      var dd = String(today.getDate()).padStart(2, '0')
      var mm = String(today.getMonth() + 1).padStart(2, '0')
      var yyyy = today.getFullYear()

      today = dd + '/' + mm + '/' + yyyy
      return today
    },
    addToCart(book) {
      toastr.success('', 'Libro añadido a tu cesta.',
          {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right', preventDuplicates: true})
      console.log(book)
      bus.emit('added-to-cart', {
        'id': book.id,
        'title': book.name,
        'price': book.price,
        'cover': book.cover_image_url,
        'quant': 1
      })
    },
    getWishList() {
      if (this.loggedIn) {
        this.wish_list = []
        var path = api + 'wishlist/' + this.idIn
        axios.get(path)
            .then((res) => {
              this.wish_list = res.data.List.Wishlist.books
            })
            .catch((error) => {
              console.log(error)
            })
      }
    },
    deleteFromWishList(book) {
      var path = api + 'wishlist/' + this.idIn + '/' + book.id
      axios.delete(path)
          .then((res) => {
            console.log(res)
            toastr.success('', 'Lista de deseados actualizada correctamente.',
                {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right', preventDuplicates: true})

            this.getWishList();
          })
          .catch((error) => {
            console.log(error)
            toastr.error('', 'Algo no salió como se esperaba, intentelo de nuevo mas tarde',
                {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right', preventDuplicates: true})

            this.getWishList();
          })
    }
  }
}

</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
<style scoped>
@font-face {
  font-family: 'LogoFont';
  src: url('/assets/logo_font.woff')
}

@media (min-width: 0px) {
  .nav-item .btn {
    width: 100%;
  }

  .navbar-nav .nav-item .form-inline .form-control {
    width: 80%;
  }

  .navbar-nav .nav-item .form-inline .btn {
    width: 15%;
  }

  .searchBarOutside {
    display: none;
    min-width: 50% !important;
  }

  .navbar-nav .nav-item .searchBarInside {
    display: inline;
  }


}

@media (min-width: 768px) {
  .nav-item .btn {
    width: 30%;
  }

  .buttonList {
    display: inline;
  }

  .buttonList .nav-item {
    display: inline;
  }

  .searchBarOutside {
    min-width: 55% !important;
    display: inline;
  }


  .searchBarOutside .btn {
    width: 50px;
    width: 50px;

  }

  .navbar-nav .nav-item .searchBarInside {
    display: none;
  }
}

@media (min-width: 992px) {
  .buttonList a {
    display: none;
  }

  .buttonList .nav-item .btn {
    width: 50px;
  }

  .searchBarOutside {
    min-width: 50% !important;
  }

  .categoriestxt {
    font-size: 0.9em !important;
  }

}

@media (min-width: 1400px) {

  .searchBarOutside {
    min-width: 35% !important;
  }

  .buttonList a {
    display: inline;
  }

  .buttonList .nav-item .btn {
    width: 180px;
  }
}

body, wrapper {
  min-height: 100vh;
}

.flex-fill {
  flex: 1 1 auto;
}

.categoriestxt {
  color: #2bc4ed !important;
  font-size: 1.1em;
}

.navbartextbt {
  color: white !important;
  font-size: 1.2em
}


.mainlogo {
  font-family: LogoFont;
  color: #3b494d !important;
  font-size: 3.3em;
  letter-spacing: 0.1em;
}

.site-footer {
  background-color: #292b2c;
  padding: 45px 0 20px;
  font-size: 15px;
  line-height: 24px;
  color: #737373;
}

.site-footer hr {
  border-top-color: #bbb;
  opacity: 0.5
}

.site-footer hr.small {
  margin: 20px 0
}

.site-footer h6 {
  color: #fff;
  font-size: 16px;
  text-transform: uppercase;
  margin-top: 5px;
  letter-spacing: 2px
}

.site-footer a {
  color: #737373;
}

.site-footer a:hover {
  color: #3366cc;
  text-decoration: none;
}

.footer-links {
  padding-left: 0;
  list-style: none
}

.footer-links li {
  display: block
}

.footer-links a {
  color: #737373
}

.footer-links a:active, .footer-links a:focus, .footer-links a:hover {
  color: #3366cc;
  text-decoration: none;
}

.footer-links.inline li {
  display: inline-block
}

.site-footer .social-icons {
  text-align: right
}

.site-footer .social-icons a {
  width: 40px;
  height: 40px;
  line-height: 40px;
  margin-left: 6px;
  margin-right: 0;
  border-radius: 100%;
  background-color: #33353d
}

.copyright-text {
  margin: 0
}

@media (max-width: 991px) {
  .site-footer [class^=col-] {
    margin-bottom: 30px
  }
}

@media (max-width: 767px) {
  .site-footer {
    padding-bottom: 0
  }

  .site-footer .copyright-text, .site-footer .social-icons {
    text-align: center
  }
}
</style>
