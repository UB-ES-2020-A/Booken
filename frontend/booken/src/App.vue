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
          <button class="navbar-toggler ml-auto" type="button" data-toggle="collapse" data-target=".mynavbar">
            <span class="navbar-toggler-icon"></span>
          </button>


          <!-- Links -->
          <div class="collapse navbar-collapse my-3 mynavbar " id="collapse_target1">
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
                <button class="btn mt-md-3 my-xl-auto my-lg-auto" style="background-color: #3b494d" type="submit"
                        v-if="!loggedIn"
                        @click="goToAccess">
                  <i class="fas fa-user" style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/>
                  <a class="navbartextbt" data-toggle="collapse" data-target=".mynavbar">Identíficate</a>
                </button>
                <button class="btn mt-md-3 my-xl-auto my-lg-auto" style="background-color: #3b494d;" type="submit"
                        v-if="loggedIn">
                  <i class="fas fa-user" style="color: #000; font-size: 1.5em; margin-right: 0.5em"/><a
                    class="navbartextbt">Tu cuenta</a>
                </button>
              </li>

              <li class="nav-item  my-3 mx-2 mx-md-3 ">
                <button class="btn mt-md-3 my-xl-auto my-lg-auto" style="background-color: #3b494d;" type="submit">
                  <i class="fas fa-question-circle" style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
                    class="navbartextbt">Ayuda</a>
                </button>
              </li>

              <li class="nav-item  my-3 ml-2 mr-2 ml-md-auto mr-md-0  ">
                <button class="btn mt-md-3 my-xl-auto my-lg-auto" style="background-color: #3b494d;" type="submit">
                  <i class="fas fa-shopping-basket " style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
                    class="navbartextbt">Cesta</a>
                </button>
              </li>


            </ul>
          </div>
        </nav>
      </div>

      <div class="bg-dark">
        <nav class="navbar navbar-expand-lg navbar-light ">
          <div class="collapse navbar-collapse mynavbar" id="collapse_target2">
            <ul class="navbar-nav mx-auto">
              <li class="nav-item">
                <a class="nav-link categoriestxt" href="#">Humanidades</a>
              </li>
              <li class="nav-item">
                <a class="nav-link categoriestxt" href="#">Técnico y formación</a>
              </li>
              <li class="nav-item">
                <a class="nav-link categoriestxt" href="#">Métodos de idiomas</a>
              </li>
              <li class="nav-item">
                <a class="nav-link categoriestxt" href="#">Literatura</a>
              </li>
              <li class="nav-item">
                <a class="nav-link categoriestxt" href="#">Infantil</a>
              </li>
              <li class="nav-item">
                <a class="nav-link categoriestxt" href="#">Cómics</a> <!-- manga-->
              </li>
              <li class="nav-item">
                <a class="nav-link categoriestxt" href="#">Juvenil</a>
              </li>
              <li class="nav-item">
                <a class="nav-link categoriestxt" href="#">Otras categorías</a>
              </li>
            </ul>
          </div>

        </nav>
      </div>
    </div>


    <router-view/>


    <footer class="site-footer">
      <div class="container">
        <div class="row">
          <div class="col-sm-12 col-md-6">
            <h6>Sobre booken</h6>
            <p class="text-justify">Librería virtual de habla hispana que brinda información y hace envíos a los cinco
              continentes, garantizando un gran
              fondo bibliográfico apoyado por la experiencia de expertos libreros y expertos en internet desde hace más
              de una década.</p>

            <p>booken permite registrase y acceder tanto a empresas como usuarios a infinidad de posibilidades,
              con el fin de conseguir el libro que se necesita. Se ha creado así una gran comunidad lectora, alrededor
              nuestro. Somos tu librero en Internet.
            </p>
          </div>

          <div class="col-xs-6 col-md-3">
            <h6>AYUDA</h6>
            <ul class="footer-links">
              <li>
                <router-link to="/contact">Contacto</router-link>
              </li>
              <li><a href="">Preguntas frecuentes</a></li>

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
import Front from './components/Front.vue'

export default {
  name: 'App',
  components: {
    // eslint-disable-next-line vue/no-unused-components
    Front
  },
  props: {
    msg: String
  },
  data() {
    return {
      loggedIn: false
    }
  }, methods: {
    getYear() {
      return new Date().getFullYear()
    },
    goToAccess() {
      this.$router.push({path: '/access', query: {logged: this.loggedIn}})
    },
    goShoppingCart() {
      this.$router.push({path: '/cart'})
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

@media (max-width: 1rem !important) {
  .customnav {
    width: 100%;
  }
}

.categoriestxt {
  color: #2bc4ed !important;
  font-size: 1.1em;
}

.navbartextbt {
  color: white;
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
