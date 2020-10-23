<style>
@import url("../assets/toastr.css");
@import url("../assets/animate.min.css");

</style>
<template>
  <div>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
          integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">

    <div class="logincontainer" id="loginform">
      <div class="loginform">
        <div class="card animate__animated animate__slideInRight" style="background-color: #3b494d">
          <h2 style="margin-top: 2rem; color: white">Iniciar sesión</h2>
          <form>
            <div class="form-group" style="margin-top: 2rem; margin-right: 20%">
              <div class="input-group" style="margin-left: 10%;">
                <span class="input-group-text" style="background-color: #2bc4ed; border-color: #2bc4ed"
                ><i class="fas fa-envelope" style="color: white"></i> </span>
                <input name="" class="form-control" placeholder="Correo electrónico" type="text" id="emailL"
                       v-model="email">
              </div>
            </div>
            <div class="form-group" style="margin-top: 1rem; margin-right: 20%">
              <div class="input-group" style="margin-left: 10%;">
                <span class="input-group-text" style="background-color: #2bc4ed; border-color: #2bc4ed">
                  <i class="fa fa-lock" style="color: white"></i> </span>
                <input class="form-control" placeholder="Contraseña" type="password" id="passwordL" v-model="password">
              </div>
            </div>
          </form>
          <button class="btn my-2 my-sm-0"
                  style="background-color: #2bc4ed; color: white; border-radius: 0 !important; margin: 0 !important;margin-top: 2rem !important"
                  type="submit" @click="doLogin"
          ><b>Acceder</b>
          </button>
          <button class="btn my-2 my-sm-0"
                  style="background-color: #328399; color: white; border-radius: 0 !important; margin: 0 !important"
                  type="submit" @click="back2Main"
          ><b>Volver a página principal</b>
          </button>
          <button class="btn my-2 my-sm-0"
                  style="background-color: #7caca4; color: white; border-radius: 0 !important; margin: 0 !important"
                  type="submit" @click="toggleRegister"
          ><b>¿No tienes cuenta? ¡Créate una!</b>
          </button>
        </div>
      </div>
    </div>

    <div class="logincontainer" id="registerform" style="display: none">
      <div class="loginform">
        <div class="card  animate__animated animate__slideInRight" style="background-color: #3b494d">
          <h2 style="margin-top: 2rem; color: white">Registro</h2>
          <form>
            <div class="form-group" style="margin-top: 2rem; margin-right: 20%">
              <div class="input-group" style="margin-left: 10%;">
                <span class="input-group-text" style="background-color: #2bc4ed; border-color: #2bc4ed"
                ><i class="fas fa-user" style="color: white"></i> </span>
                <input name="" class="form-control" placeholder="Nombre" type="text" id="nameR"
                       v-model="name">
              </div>
            </div>
            <div class="form-group" style="margin-top: 1rem; margin-right: 20%">
              <div class="input-group" style="margin-left: 10%;">
                <span class="input-group-text" style="background-color: #2bc4ed; border-color: #2bc4ed"
                ><i class="fas fa-signature" style="color: white"></i> </span>
                <input name="" class="form-control" placeholder="Apellidos" type="text" id="lastnameR"
                       v-model="lastname">
              </div>
            </div>
            <div class="form-group" style="margin-top: 1rem; margin-right: 20%">
              <div class="input-group" style="margin-left: 10%;">
                <span class="input-group-text" style="background-color: #2bc4ed; border-color: #2bc4ed"
                ><i class="fas fa-envelope" style="color: white"></i> </span>
                <input name="" class="form-control" placeholder="Correo electrónico" type="text" id="emailR"
                       v-model="email">
              </div>
            </div>
            <div class="form-group" style="margin-top: 1rem; margin-right: 20%">
              <div class="input-group" style="margin-left: 10%;">
                <span class="input-group-text" style="background-color: #2bc4ed; border-color: #2bc4ed">
                  <i class="fa fa-lock" style="color: white"></i> </span>
                <input class="form-control" placeholder="Contraseña" type="password" id="passwordR1" v-model="password">
              </div>
            </div>
            <div class="form-group" style="margin-top: 1rem; margin-right: 20%">
              <div class="input-group" style="margin-left: 10%;">
                <span class="input-group-text" style="background-color: #2bc4ed; border-color: #2bc4ed">
                  <i class="fa fa-lock" style="color: white"></i> </span>
                <input class="form-control" placeholder="Repite tu contraseña" type="password" id="passwordR2">
              </div>
            </div>
          </form>
          <button class="btn my-2 my-sm-0"
                  style="background-color: #2bc4ed; color: white; border-radius: 0 !important; margin: 0 !important;margin-top: 2rem !important"
                  type="submit" @click="doRegister"
          ><b>Crear cuenta</b>
          </button>
          <button class="btn my-2 my-sm-0"
                  style="background-color: #328399; color: white; border-radius: 0 !important; margin: 0 !important"
                  type="submit" @click="back2Main"
          ><b>Volver a página principal</b>
          </button>
          <button class="btn my-2 my-sm-0"
                  style="background-color: #7caca4; color: white; border-radius: 0 !important; margin: 0 !important"
                  type="submit" @click="toggleRegister"
          ><b>Volver a login</b>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// eslint-disable-next-line no-unused-vars
import * as toastr from '../assets/toastr.js'
// eslint-disable-next-line no-unused-vars
import axios from 'axios'
// eslint-disable-next-line no-unused-vars
let api = 'URL DE LA API'
export default {
  name: 'Access',
  props: {
    msg: String
  },
  data() {
    return {
      loggedIn: false,
      email: '',
      password: '',
      name: '',
      lastname: ''
    }
  }, methods: {
    getYear() {
      return new Date().getFullYear()
    },
    doLogin() {
      if (document.getElementById('emailL').style.display == '' || document.getElementById('passwordL').style.display == '') {
        toastr.info('', 'Welcome back ! Redirecting to events',
              {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right'})
      }
    },
    doRegister() {
    },

    back2Main() {
      this.$router.push({path: '/'})
    },
    toggleRegister() {
      if (document.getElementById('loginform').style.display == 'block') {
        document.getElementById('loginform').style.display = 'none'
        document.getElementById('registerform').style.display = 'block'
        this.username = ''
        this.password = ''
      } else {
        document.getElementById('loginform').style.display = 'block'
        document.getElementById('registerform').style.display = 'none'
        this.username = ''
        this.password = ''
      }
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
</style>
