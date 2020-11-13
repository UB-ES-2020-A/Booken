<style>
@import url("./assets/animate.min.css");
</style>
<template>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
        integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
  <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
  <link href='https://fonts.googleapis.com/css?family=Lato' rel='stylesheet' type='text/css'>

  <div>
    <div style="background: #2bc4ed;">

      <div class="container" style="max-width: 1400px">

        <nav class="navbar navbar-expand-lg navbar-dark ">
          <!-- Brand -->
          <a class="navbar-brand mainlogo ml-3 animate__animated animate__flipInX" href="/">booken<span
              class="badge badge-light" style="font-size: 0.3em; letter-spacing: normal">alpha</span></a>

          <!--<div class="navbar-nav navbar-expand-md ml-2">
            <div class="nav-item">
              <div class="searchBarOutside ">
                <form class="form">
                  <input class="form-control" type="search"
                         placeholder="Busca por autor, título, ISBN"
                         aria-label="Search">
                  <button class="btn" style="background-color: #3b494d;" type="submit"><i
                      class="fas fa-search"
                      style="color: #FFF"/>
                  </button>
                </form>
              </div>
            </div>
          </div>-->
          <form class="form-inline mx-auto searchBarOutside" style="min-width: 30%">
            <input class="form-control" style="min-width: 80%" type="search"
                   placeholder="Busca por autor, título, ISBN"
                   aria-label="Search">
            <button class="btn ml-2" style="min-width: 50px; background-color: #3b494d;" type="submit"><i
                class="fas fa-search"
                style="color: #FFF"/>
            </button>
          </form>

          <!--<ul class="navbar-nav navbar-expand-md ml-lg-2 ">
            <li class="nav-item ">
              <div class="searchBarOutside ">
                <form class="form-inline ">
                  <input class="form-control " type="search"
                         placeholder="Busca por autor, título, ISBN"
                         aria-label="Search">
                  <button class="btn " style="background-color: #3b494d" type="submit"><i
                      class="fas fa-search"
                      style="color: #FFF"/>
                  </button>
                </form>
              </div>
            </li>
          </ul>-->

          <!-- Links Button -->
          <button class="navbar-toggler ml-auto" type="button" data-toggle="collapse"
                  data-target="#mynavbar, #mynavbar2"
                  aria-controls="mynavbar, mynavbar2" aria-expanded="false">
            <span class="navbar-toggler-icon"></span>
          </button>


          <!-- Links -->
          <div class="collapse navbar-collapse my-3" id="mynavbar">
            <!--
                        <ul class="navbar-nav ">
                          <li class="nav-item my-xl-auto my-2">
                            <form class="form-inline">
                              <input class="form-control mr-sm-2" type="search"
                                     placeholder="Busca por autor, título, ISBN"
                                     aria-label="Search">
                              <button class="btn" style="background-color: #3b494d" type="submit"><i
                                  class="fas fa-search"
                                  style="color: #FFF"/>
                              </button>
                            </form>
                          </li>
                        </ul>
                        -->


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
                <button class="btn mt-md-3 my-xl-auto my-lg-auto" data-toggle="collapse" data-target=".mynavbar"
                        style="background-color: #3b494d" type="submit"
                        v-if="!loggedIn"
                        @click="goToAccess">
                  <i class="fas fa-user" style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/>
                  <a class="navbartextbt">Identíficate</a>
                </button>
                <button class="btn mt-md-3 my-xl-auto my-lg-auto" data-toggle="collapse" data-target=".mynavbar"
                        style="background-color: #3b494d;" type="submit"
                        v-if="loggedIn" @click="goToCP">
                  <i class="fas fa-user-circle" style="color: white; font-size: 1.5em; margin-right: 0.5em"/>
                  <a class="navbartextbt">Tu cuenta</a>
                </button>
              </li>

              <li class="nav-item  my-3 mx-2 mx-md-3 ">
                <button class="btn mt-md-3 my-xl-auto my-lg-auto" data-toggle="collapse" data-target=".mynavbar"
                        style="background-color: #3b494d;" type="submit">
                  <i class="fas fa-question-circle" style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
                    class="navbartextbt" @click="getHelp">Ayuda</a>
                </button>
              </li>

              <li class="nav-item  my-3 ml-2 mr-2 ml-md-auto mr-md-0  ">
                <button class="btn mt-md-3 my-xl-auto my-lg-auto" data-toggle="collapse" data-target=".mynavbar"
                        style="background-color: #3b494d;" type="submit" @click="toggleCart" v-if="!viewCart">
                  <i class="fas fa-shopping-basket " style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
                    class="navbartextbt">Cesta</a>
                </button>
                <button class="btn mt-md-3 my-xl-auto my-lg-auto" data-toggle="collapse" data-target=".mynavbar"
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

    <div class="bg-dark">
      <nav class="navbar navbar-expand-lg navbar-light">
        <div class="collapse navbar-collapse" id="mynavbar2">
          <div class="nav navbar-nav mx-auto" @click="hideCart">
            <router-link :to="{name: 'books', params: {category: 'HUMANIDADES'}}"
                         class="nav-item nav-link categoriestxt" active-class="active"

            >Humanidades
            </router-link>
            <router-link :to="{name: 'books', params: {category: 'TECNICO Y FORMACION'}}"
                         class="nav-item nav-link categoriestxt" active-class="active"
            >Técnico y formación
            </router-link>
            <router-link :to="{name: 'books', params: {category: 'METODOS DE IDIOMAS'}}"
                         class="nav-item nav-link categoriestxt" active-class="active"
            >Métodos de idiomas
            </router-link>
            <router-link class="nav-item nav-link categoriestxt" active-class="active"
                         :to="{name: 'books', params: {category: 'LITERATURA'}}">Literatura
            </router-link>
            <router-link class="nav-item nav-link categoriestxt" active-class="active"
                         :to="{name: 'books', params: {category: 'INFANTIL'}}">Infantil
            </router-link>
            <router-link class="nav-item nav-link categoriestxt" active-class="active"
                         :to="{name: 'books', params: {category: 'COMICS Y MANGA'}}">Cómics y manga
            </router-link>
            <router-link class="nav-item nav-link categoriestxt" active-class="active"
                         :to="{name: 'books', params: {category: 'JUVENIL'}}">Juvenil
            </router-link>
            <router-link class="nav-item nav-link categoriestxt" active-class="active"
                         :to="{name: 'books', params: {category: 'OTRAS CATEGORIAS'}}">Otras categorías
            </router-link>

            <router-link class="nav-link categoriestxt" active-class="active"

                         :to="{name: 'books', params: {category: 'TODO'}}"><b style="color: yellow">Ver todo</b>
            </router-link>
          </div>
        </div>
      </nav>
    </div>
    <router-view :key="$route.fullPath" v-if="!viewCart" :logged="this.loggedIn" :token="this.tokenIn" :id="this.idIn"/>
    <div id="shopping_cart" v-if="viewCart">
      <h1 style="margin-top: 1em">Tu cesta</h1>
      <div class="container mb-4" v-if="this.cart.length >= 1">
        <div class="row">
          <div class="col-12">
            <div class="table-responsive">
              <table class="table table-striped" style="text-align: left">
                <thead>
                <tr>
                  <th scope="col"></th>
                  <th scope="col">Artículo</th>
                  <th scope="col">Precio</th>
                  <th scope="col" class="text-center">Cantidad</th>
                  <th scope="col" class="text-right">Total</th>
                  <th></th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="(item,i) in this.cart" :key="i">
                  <td></td>
                  <!--<td><img :src="image" style="width: 10%"></td>-->
                  <td>{{ item.title }}</td>
                  <td>{{ item.price }} €</td>
                  <td class="text-center">
                    <button class="btn my-2 my-sm-0" style="background-color: #3b494d; margin-right: 0.5rem"
                            type="submit" @click="decreaseQuant(item.id)"
                    ><i
                        class="fas fa-minus" style="color: #FFF"/></button>
                    {{ item.quant }}
                    <button class="btn my-2 my-sm-0" style="background-color: #3b494d; margin-left: 0.5rem"
                            type="submit" @click="increaseQuant(item.id)"><i
                        class="fas fa-plus" style="color: #FFF"/></button>
                  </td>
                  <td class="text-right">{{ round2Dec(item.price * item.quant) }} €</td>
                  <td class="text-right">
                    <button class="btn btn-sm btn-danger" @click="removeBook(item.id)"><i class="fas fa-trash"></i>
                    </button>
                  </td>
                </tr>

                <tr>
                  <td></td>
                  <td></td>
                  <td></td>
                  <td></td>
                  <td>IVA (21%)</td>
                  <td class="text-right">{{ round2Dec(taxes) }} €</td>
                </tr>
                <tr>
                  <td></td>
                  <td></td>
                  <td></td>
                  <td></td>
                  <td>Envío</td>
                  <td class="text-right">{{ round2Dec(shipping) }} €</td>
                </tr>
                <tr>
                  <td></td>
                  <td></td>
                  <td></td>
                  <td></td>
                  <td><strong>TOTAL</strong></td>
                  <td class="text-right"><strong>{{ round2Dec(total) }} €</strong></td>
                </tr>
                </tbody>
              </table>
            </div>
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
                  Pagar
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
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
    </div>

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
  </div>
</template>
<script>
import * as toastr from './assets/toastr.js'
import Front from './components/Front.vue'
import Access from "@/components/Access"
import {bus} from './main.js'
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
      this.typeIn = asd.type
      this.idIn = parseInt(asd.id)
    })
    bus.on('added-to-cart', (book) => {
      this.checkAddToCart(book)
      bus.emit('cart-updated')
    })
    bus.on('cart-updated', () => {
      this.computeTotals()
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
      typeIn: -1,
      email: "prueba@gmail.com",
      viewCart: false
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
      this.total = Math.round((this.subtotal + this.taxes + this.shipping) * 100) / 100
    },
    increaseQuant(id) {
      var b = this.searchInCart(id)
      b.quant += 1
      bus.emit('cart-updated')
      toastr.success('', 'Carrito actualizado.',
          {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
    },
    getSubTotal() {
      this.subtotal = 0
      var i, item
      for (i in this.cart) {
        item = this.cart[i]
        this.subtotal += (item.price * item.quant)
      }
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
          {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
    },
    removeBook(id) {
      this.cart.splice(this.getBookIndex(id), 1)
      bus.emit('cart-updated')
      toastr.success('', 'Carrito actualizado.',
          {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
    },
    getHelp() {
      if(this.viewCart)
        this.viewCart = false
    },
    hideCart () {
      if(this.viewCart)
        this.viewCart = false
    },
    toggleCart() {
      this.viewCart = !this.viewCart
    },
    finalizePurchase(order_id) {
      for (let i = 0; i < this.cart.length; i += 1) {
        var item = this.cart[i]
        console.log(item)
        var price = item.price * item.quant
        var id = item.id
        const path = `https://booken-dev.herokuapp.com/article-order/${order_id}/${id}`
        const parameters = {
          price: price
        }
        axios.post(path, parameters)
          .then(() => {
            console.log('Article added')
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.log(error)
          })

      }
    },
    checkout() {
      const path = `https://booken-dev.herokuapp.com/order/${this.idIn}`
      const parameters = {
          date: this.date,
          total: this.total,
          shipping: this.shipping,
          taxes: this.taxes,
          state: 0
        }
      console.log(path)
      console.log(this.idIn)
      axios.post(path, parameters)
          .then((res) => {
            console.log(res)
            var order_id = res
            this.finalizePurchase(order_id)
            console.log('Order done')
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.log(error)
          })
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
      if(this.viewCart)
        this.viewCart = false
      this.$router.push({path: '/access'})
    },
    goToCP() {
      if(this.viewCart)
        this.viewCart = false
      this.$router.push({path: '/cp'})
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
