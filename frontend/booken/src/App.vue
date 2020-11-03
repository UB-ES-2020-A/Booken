<style>
@import url("./assets/animate.min.css");
</style>
<template>
  <div>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
          integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
    <link href='https://fonts.googleapis.com/css?family=Lato' rel='stylesheet' type='text/css'>
    <nav class="navbar navbar-expand-sm navbar-dark bg-dark" style="background-color:#2bc4ed !important;">
      <a class="navbar-brand mainlogo ml-5 animate__animated animate__flipInX" href="/">booken<span class="badge badge-light"
                                                                 style="font-size: 0.3em; letter-spacing: normal">alpha</span></a>

      <button class="navbar-toggler ml-auto" data-toggle="collapse" data-target=".navbars">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse navbars" id="collapse_target1">
        <ul class="navbar-nav mx-auto">
          <form class="form-inline my-2 my-lg-0">
            <input class="form-control mr-sm-2" type="search" placeholder="Busca por autor, título, ISBN"
                   aria-label="Search" style="width: 80%; margin-right: 1em">
            <button class="btn my-2 my-sm-0" style="background-color: #3b494d" type="submit"><i class="fas fa-search"
                                                                                                style="color: #FFF"/>
            </button>
          </form>
        </ul>
        <ul class="navbar-nav ml-auto">
          <div class="btn-toolbar">
            <li class="nav-item">
              <button class="btn my-2 my-sm-0 mr-2" data-toggle="collapse" data-target=".navbars" style="background-color: #3b494d" type="submit" v-if="!loggedIn" @click="goToAccess">
                <i class="fas fa-user" style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
                  class="navbartextbt">Identíficate</a>
              </button>
              <button class="btn my-2 my-sm-0 mr-2" style="background-color: #3b494d" type="submit" v-if="loggedIn">
                <i class="fas fa-user" style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
                  class="navbartextbt">Tu cuenta</a>
              </button>
            </li>
            <li class="nav-item">
              <button class="btn my-2 my-sm-0 mr-2" style="background-color: #3b494d" type="submit">
                <i class="fas fa-question-circle" style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
                  class="navbartextbt">Ayuda</a>
              </button>
            </li>
            <li class="nav-item">
              <button class="btn my-2 my-sm-0 mr-5" @click="goShoppingCart" style="background-color: #3b494d" type="submit">
                <i class="fas fa-shopping-basket" style="color: #FFF; font-size: 1.5em; margin-right: 0.5em"/><a
                  class="navbartextbt">Cesta</a>
              </button>
            </li>
          </div>

        </ul>
      </div>
    </nav>
    <nav class="navbar navbar-expand-sm navbar-light bg-dark">
      <div class="collapse navbar-collapse navbars" id="collapse_target2">
        <ul class="navbar-nav mx-auto">
          <li class="nav-item">
            <router-link class="nav-link categoriestxt" :to="{name: 'books', params: {category: 'HUMANIDADES'}}">Humanidades</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link categoriestxt" :to="{name: 'books', params: {category: 'TECNICO Y FORMACION'}}">Técnico y formación</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link categoriestxt" :to="{name: 'books', params: {category: 'METODOS DE IDIOMAS'}}">Métodos de idiomas</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link categoriestxt" :to="{name: 'books', params: {category: 'LITERATURA'}}">Literatura</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link categoriestxt" :to="{name: 'books', params: {category: 'INFANTIL'}}">Infantil</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link categoriestxt" :to="{name: 'books', params: {category: 'COMICS Y MANGA'}}">Cómics y manga</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link categoriestxt" :to="{name: 'books', params: {category: 'JUVENIL'}}">Juvenil</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link categoriestxt" :to="{name: 'books', params: {category: 'OTRAS CATEGORIAS'}}">Otras categorías</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link categoriestxt" :to="{name: 'books', params: {category: 'TODO'}}"><b style="color: yellow">Ver todo</b></router-link>
          </li>
        </ul>
      </div>
    </nav>
    <router-view :key="$route.fullPath"/>
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
              <li><router-link to="/contact">Contacto</router-link></li>
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
    },
    goToLocation() {
      this.$router.push({path: '/location'})
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
