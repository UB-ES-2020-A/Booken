<style>

@import url("../assets/animate.min.css");
@import url("../assets/toastr.css");
</style>
<template>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
        integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
  <div>
    <div class="container" style="max-width: 1400px">
      <!-- Login form -->
      <div class="logincontainer" id="loginform">
        <div class="loginform">
          <div class="card animate__animated animate__slideInRight" style="background-color: #3b494d">
            <h2 style="margin-top: 2rem; color: white">Iniciar sesión</h2>
            <form style=" margin-left: 10%; margin-right: 10%">
              <div class="form-group" style="margin-top: 2rem;">
                <div class="input-group">
                <span class="input-group-text" style="background-color: #2bc4ed; border-color: #2bc4ed; "><i
                    class="fas fa-envelope" style="color: white; width: 20px"></i> </span>
                  <input name="" class="form-control" placeholder="Correo electrónico" type="text" id="emailL"
                         v-model="email">
                </div>
              </div>
              <div class="form-group" style="margin-top: 1rem; ">
                <div class="input-group">
                <span class="input-group-text" style="background-color: #2bc4ed; border-color: #2bc4ed">
                  <i class="fa fa-lock fa-lg" style="color: white; width: 20px"></i></span>
                  <input class="form-control" placeholder="Contraseña" type="password" id="passwordL"
                         v-model="password">
                </div>
              </div>
            </form>
            <button class="btn my-2 my-sm-0"
                    style="background-color: #2bc4ed; color: white; border-radius: 0 !important; margin: 0 !important;margin-top: 2rem !important"
                    type="submit" @click="doLogin" id="btLogin"
            ><b>Acceder</b>
            </button>
            <button class="btn my-2 my-sm-0"
                    style="background-color: #328399; color: white; border-radius: 0 !important; margin: 0 !important"
                    type="submit" @click="back2Main" id="btBackL"
            ><b>Volver a página principal</b>
            </button>
            <button class="btn my-2 my-sm-0"
                    style="background-color: #7caca4; color: white; border-radius: 0 !important; margin: 0 !important"
                    type="submit" @click="toggleRegister" id="bt2Reg"
            ><b>¿No tienes cuenta? ¡Créate una!</b>
            </button>
          </div>
        </div>
      </div>
      <!-- Register form -->
      <div class="logincontainer" id="registerform" style="display: none">
        <div class="loginform">
          <div class="card  animate__animated animate__slideInRight" style="background-color: #3b494d">
            <h2 style="margin-top: 2rem; color: white">Registro</h2>
            <form style=" margin-left: 10%; margin-right: 10%">
              <div class="form-group" style="margin-top: 2rem;">
                <div class="input-group">
                <span class="input-group-text" style="background-color: #2bc4ed; border-color: #2bc4ed"
                ><i class="fas fa-user" style="color: white; width: 20px"></i> </span>
                  <input name="" class="form-control" placeholder="Nombre" type="text" id="nameR"
                         v-model="name">
                </div>
              </div>
              <div class="form-group" style="margin-top: 1rem;">
                <div class="input-group">
                <span class="input-group-text" style="background-color: #2bc4ed; border-color: #2bc4ed"
                ><i class="fas fa-signature" style="color: white; width: 20px"></i> </span>
                  <input name="" class="form-control" placeholder="Apellidos" type="text" id="lastnameR"
                         v-model="lastname">
                </div>
              </div>
              <div class="form-group" style="margin-top: 1rem; ">
                <div class="input-group">
                <span class="input-group-text" style="background-color: #2bc4ed; border-color: #2bc4ed">
                  <i class="fas fa-envelope" style="color: white; width: 20px"></i> </span>
                  <input name="" class="form-control" placeholder="Correo electrónico" type="text" id="emailR"
                         v-model="email">
                </div>
              </div>
              <div class="form-group" style="margin-top: 1rem; ">
                <div class="input-group">
                <span class="input-group-text" style="background-color: #2bc4ed; border-color: #2bc4ed">
                  <i class="fa fa-lock fa-lg" style="color: white; width: 20px"></i></span>
                  <input class="form-control" placeholder="Contraseña" type="password" id="passwordR1"
                         v-model="password" @change="scorePassword" >
                </div>
              </div>
              <div class="myshow" v-if="editPassword">
                <div class="progress" style="width:100%; margin-top:1rem">
                  <div class="progress-bar" role="progressbar" aria-valuenow="0"
                       aria-valuemin="0" aria-valuemax="100" id="myprobar"
                       style="color: black">{{ checkPasswordStrength() }}
                  </div>
                </div>
                <div class="rounded" style="background: white; text-align: left; margin-top:1rem">
                  <ul class="list-group">
                    <li class="list-group-item d-flex justify-content-between">
                      <span style="font-size: 0.9em">Contiene carácter símbolo</span>
                      <i class="fa fa-check fa-lg my-auto" style="color: green; width: 20px"
                         v-if="this.checkPasswordSymbol(this.password)"></i>
                      <i class="fa fa-times fa-lg my-auto" style="color: red; width: 20px"
                         v-else></i>
                    </li>
                    <li class="list-group-item d-flex justify-content-between">
                      <span style="font-size: 0.9em">Contiene carácter mayúscula</span>
                      <i class="fa fa-check fa-lg my-auto" style="color: green; width: 20px"
                         v-if="this.checkPasswordUpper(this.password)"></i>
                      <i class="fa fa-times fa-lg my-auto" style="color: red; width: 20px"
                         v-else></i>
                    </li>
                    <li class="list-group-item d-flex justify-content-between">
                      <span style="font-size: 0.9em">Contiene carácter minúscula</span>
                      <i class="fa fa-check fa-lg my-auto" style="color: green; width: 20px"
                         v-if="this.checkPasswordLower(this.password)"></i>
                      <i class="fa fa-times fa-lg my-auto" style="color: red; width: 20px"
                         v-else></i>
                    </li>
                    <li class="list-group-item d-flex justify-content-between">
                      <span style="font-size: 0.9em">Contiene carácter numérico</span>
                      <i class="fa fa-check fa-lg my-auto" style="color: green; width: 20px"
                         v-if="this.checkPasswordNumber(this.password)"></i>
                      <i class="fa fa-times fa-lg my-auto" style="color: red; width: 20px"
                         v-else></i>
                    </li>
                    <li class="list-group-item d-flex justify-content-between">
                      <span style="font-size: 0.9em">Mínimo 8 carácteres</span>
                      <i class="fa fa-check fa-lg my-auto" style="color: green; width: 20px"
                         v-if="this.checkPasswordLength(this.password)"></i>
                      <i class="fa fa-times fa-lg my-auto" style="color: red; width: 20px"
                         v-else></i>
                    </li>

                  </ul>
                </div>
              </div>
              <div class="form-group" style="margin-top: 1rem;">
                <div class="input-group">
                <span class="input-group-text" style="background-color: #2bc4ed; border-color: #2bc4ed">
                  <i class="fa fa-lock fa-lg" style="color: white; width: 20px"></i> </span>
                  <input class="form-control" placeholder="Repite tu contraseña" type="password"
                         id="passwordR2" >
                </div>
              </div>
            </form>
            <button class="btn my-2 my-sm-0"
                    style="background-color: #2bc4ed; color: white; border-radius: 0 !important; margin: 0 !important;margin-top: 2rem !important"
                    type="submit" @click="doRegister" id="btReg"
            ><b>Crear cuenta</b>
            </button>
            <button class="btn my-2 my-sm-0"
                    style="background-color: #328399; color: white; border-radius: 0 !important; margin: 0 !important"
                    type="submit" @click="back2Main" id="btBack"
            ><b>Volver a página principal</b>
            </button>
            <button class="btn my-2 my-sm-0"
                    style="background-color: #7caca4; color: white; border-radius: 0 !important; margin: 0 !important"
                    type="submit" @click="toggleRegister" id="btBack2L"
            ><b>Volver a login</b>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import * as toastr from '../assets/toastr.js'
import axios from 'axios'
import {bus, api} from '../main.js'

export default {
  name: 'Access',
  props: {},
  data() {
    return {
      // eslint-disable-next-line vue/no-dupe-keys
      email: '',
      password: '',
      name: '',
      lastname: '',
      logged: false,
      type: -1,
      token: '',
      id: -1,
      editPassword: false
    }
  }, methods: {
    getYear() {
      return new Date().getFullYear()
    },
    toggleInputsSignIn() {
      document.getElementById('emailL').disabled = !document.getElementById('emailL').disabled
      document.getElementById('passwordL').disabled = !document.getElementById('passwordL').disabled

      document.getElementById('btLogin').disabled = !document.getElementById('btLogin').disabled;
      document.getElementById('btBackL').disabled = !document.getElementById('btBackL').disabled;
      document.getElementById('bt2Reg').disabled = !document.getElementById('bt2Reg').disabled;
    },
    toggleInputsRegister() {
      document.getElementById('nameR').disabled = !document.getElementById('nameR').disabled;
      document.getElementById('lastnameR').disabled = !document.getElementById('lastnameR').disabled;
      document.getElementById('emailR').disabled = !document.getElementById('emailR').disabled;
      document.getElementById('passwordR1').disabled = !document.getElementById('passwordR1').disabled;
      document.getElementById('passwordR2').disabled = !document.getElementById('passwordR2').disabled;

      document.getElementById('btReg').disabled = !document.getElementById('btReg').disabled;
      document.getElementById('btBack').disabled = !document.getElementById('btBack').disabled;
      document.getElementById('btBack2L').disabled = !document.getElementById('btBack2L').disabled;
    },
    login(register, params) {
      const path = api + 'login'
      axios.post(path, params)
          .then((res) => {
            this.logged = true
            this.token = res.data.token
            this.type = res.data.type
            this.id = res.data.id
            if (register) {
              toastr.success('', '¡Bienvenido a booken!',
                  {
                    timeOut: 2500,
                    progressBar: true,
                    newestOnTop: true,
                    positionClass: 'toast-bottom-right',
                    preventDuplicates: true
                  })
            } else {
              toastr.success('', '¡Hola otra vez!',
                  {
                    timeOut: 2500,
                    progressBar: true,
                    newestOnTop: true,
                    positionClass: 'toast-bottom-right',
                    preventDuplicates: true
                  })
            }
            bus.emit('has-logged-in', {
              'logged': this.logged,
              'token': String(this.token.toString()),
              'type': parseInt(this.type),
              'id': this.id
            })
            this.$router.push({path: '/'})
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error)
            this.user = ''
            this.toggleInputsSignIn()
            toastr.error('', 'Usuario o contraseña incorrectos.',
                {
                  timeOut: 1500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
          })
    },
    doLogin() {
      if (document.getElementById('emailL').value == '' || document.getElementById('passwordL').value == '') {
        toastr.info('', 'Rellena todos los campos para acceder.',
            {
              timeOut: 2500,
              progressBar: true,
              newestOnTop: true,
              positionClass: 'toast-bottom-right',
              preventDuplicates: true
            })
      } else if (!this.validateEmail(this.email)) {
        toastr.error('', 'Dirección de correo electrónico no válida.',
            {
              timeOut: 2500,
              progressBar: true,
              newestOnTop: true,
              positionClass: 'toast-bottom-right',
              preventDuplicates: true
            })
      } else {
        const param = {
          email: this.email,
          password: this.password
        }
        this.toggleInputsSignIn()
        this.login(false, param)
      }
    },
    register() {
      const path = api + 'account'
      axios.post(path, {
        'name': this.name, 'lastname': this.lastname, 'password': this.password,
        'email': this.email
      })
          // eslint-disable-next-line no-unused-vars
          .then((res) => {
            this.login(true, {
              email: this.email,
              password: this.password
            })
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.log(error)
            this.toggleInputsRegister()
            toastr.error('', 'No se puede crear la cuenta.',
                {
                  timeOut: 1500,
                  progressBar: true,
                  newestOnTop: true,
                  positionClass: 'toast-bottom-right',
                  preventDuplicates: true
                })
          })
    },
    validateEmail(email) {
      return /\S+@\S+\.\S+/.test(email);
    },
    editPasswordToTrue() {
      this.editPassword = true;
    },
    editPasswordToFalse() {
      this.editPassword = false;
    },
    scorePassword() {
      let score = 0;
      const pass = this.password;

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

      const elem = document.getElementById("myprobar");
      if (elem != null) elem.style.width = score + '%';

      return score
    },
    checkPasswordStrength() {
      const score = this.scorePassword();
      if (score >= 80) {
        document.getElementById("myprobar").style.background = "forestgreen";
        return "Muy seguro";
      }
      if (score >= 60) {
        document.getElementById("myprobar").style.background = "limegreen";
        return "Seguro";
      }
      if (score >= 30) {
        document.getElementById("myprobar").style.background = "orange";
        return "Regular";
      }
      if (score) {
        document.getElementById("myprobar").style.background = "red";
        return "Débil"
      }
      return ""
    },
    checkPasswordSymbol(pwd) {
      return /\W/.test(pwd);
    },
    checkPasswordLower(pwd) {
      return /[a-z]/.test(pwd);
    },
    checkPasswordUpper(pwd) {
      return /[A-Z]/.test(pwd);
    },
    checkPasswordNumber(pwd) {
      return /\d/.test(pwd);
    },
    checkPasswordLength(pwd) {
      return /^[a-zA-Z\d\W]{8,}$/.test(pwd);
    },
    validatePassword(pwd) {
      return this.checkPasswordSymbol(pwd) && this.checkPasswordLower(pwd) &&
          this.checkPasswordUpper(pwd) && this.checkPasswordNumber(pwd) && this.checkPasswordLength(pwd)
    },
    doRegister() {
      if (document.getElementById('nameR').value == '' || document.getElementById('lastnameR').value == '' ||
          document.getElementById('emailL').value == '' || document.getElementById('passwordR1').value == '' ||
          document.getElementById('passwordR2').value == '') {
        toastr.info('', 'Rellena todos los campos para acceder.',
            {
              timeOut: 2500,
              progressBar: true,
              newestOnTop: true,
              positionClass: 'toast-bottom-right',
              preventDuplicates: true
            })
      } else {
        if (!this.validatePassword(this.password)) {
          toastr.error('', 'La contraseña no cumple los requisitos de seguridad.',
              {
                timeOut: 2500,
                progressBar: true,
                newestOnTop: true,
                positionClass: 'toast-bottom-right',
                preventDuplicates: true
              })
        } else if (!this.validateEmail(this.email)) {
          toastr.error('', 'Dirección de correo electrónico no válida.',
              {
                timeOut: 2500,
                progressBar: true,
                newestOnTop: true,
                positionClass: 'toast-bottom-right',
                preventDuplicates: true
              })
        } else if (document.getElementById('passwordR1').value !== document.getElementById('passwordR2').value) {
          toastr.error('', 'Las contraseñas no coniciden.',
              {
                timeOut: 2500,
                progressBar: true,
                newestOnTop: true,
                positionClass: 'toast-bottom-right',
                preventDuplicates: true
              })
        } else {
          this.toggleInputsRegister()
          this.register()
        }
      }
    }
    ,


    back2Main() {
      this.$router.push({path: '/'})
    }
    ,
    toggleRegister() {
      if (document.getElementById('loginform').style.display == 'block') {
        document.getElementById('loginform').style.display = 'none'
        document.getElementById('registerform').style.display = 'block'
      } else {
        document.getElementById('loginform').style.display = 'block'
        document.getElementById('registerform').style.display = 'none'
      }
    }
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.loginform {
  margin: 5% auto;
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