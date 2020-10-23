<template>
  <div>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
          integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
    <link href='https://fonts.googleapis.com/css?family=Lato' rel='stylesheet' type='text/css'>
    <div class="logincontainer" id="loginform">
      <div class="loginform">
        <div class="card" style="background-color: #3b494d">
          <h2 style="margin-top: 2rem; color: white">Iniciar sesión</h2>
          <form>
            <div class="form-group" style="margin-top: 2rem; margin-right: 20%">
              <div class="input-group" style="margin-left: 10%;">
                <span class="input-group-text" style="background-color: #2bc4ed; border-color: #2bc4ed"
                ><i class="fas fa-envelope" style="color: white"></i> </span>
                <input name="" class="form-control" placeholder="Correo electrónico" type="text" id="email"
                       v-model="email">
              </div>
            </div>
            <div class="form-group" style="margin-top: 1rem; margin-right: 20%">
              <div class="input-group" style="margin-left: 10%;">
                <span class="input-group-text" style="background-color: #2bc4ed; border-color: #2bc4ed">
                  <i class="fa fa-lock" style="color: white"></i> </span>
                <input class="form-control" placeholder="Contraseña" type="password" id="password" v-model="password">
              </div>
            </div>
          </form>
          <button class="btn my-2 my-sm-0" style="background-color: #2bc4ed; color: white; border-radius: 0 !important; margin: 0 !important;margin-top: 2rem !important" type="submit"
          ><b>Acceder</b>
          </button>
          <button class="btn my-2 my-sm-0" style="background-color: #328399; color: white; border-radius: 0 !important; margin: 0 !important" type="submit"
          ><b>Volver a página principal</b>
          </button>
          <button class="btn my-2 my-sm-0" style="background-color: #7caca4; color: white; border-radius: 0 !important; margin: 0 !important" type="submit"
          ><b>¿No tienes cuenta? ¡Créate una!</b>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Access',
  props: {
    msg: String
  },
  data() {
    return {
      loggedIn: false,
      email: '',
      password: ''
    }
  }, methods: {
    getYear() {
      return new Date().getFullYear()
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.loginform {
  margin: 0 auto;
  margin-top: 5%;
  margin-bottom: 5%;
}

.logincontainer {
  margin-left: 5%;
  margin-right: 5%;
}

@font-face {
  font-family: 'LogoFont';
  src: url('../assets/logo_font.woff')
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
  background-color: #3b494d;
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
