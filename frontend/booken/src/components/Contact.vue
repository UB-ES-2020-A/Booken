<style>
@import url("../assets/toastr.css");
@import url("../assets/animate.min.css");

</style>
<template>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
          integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
    <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
    <link href='https://fonts.googleapis.com/css?family=Lato' rel='stylesheet' type='text/css'>

  <div class="container">

    <h1>Formulario de contacto</h1>
    <form>
      <div class="form-group">
        <label for="exampleFormControlInput1">Nombre y apellidos</label>
        <input type="text" class="form-control" id="full_name" placeholder="Nombre Apellidos">
      </div>
      <div class="form-group">
        <label for="exampleFormControlInput2">Correo electrónico</label>
        <input type="email" class="form-control" id="email" placeholder="hola@quetal.com">
      </div>
      <div class="form-group">
        <label>Teléfono de contacto</label>
        <input type="number" class="form-control" id="phone_number" placeholder="">
      </div>

      <div class="form-group">
        <label>Consulta</label>
        <textarea class="form-control" id="contact_query" rows="10"></textarea>
      </div>
      <div class="form-group">
          <div class="form-check" style="margin-top: 2em">
            <input class="form-check-input" type="checkbox" id="check_box">
            <label class="form-check-label" for="gridCheck1">
              He leído y acepto <a href="https://pdfhost.io/v/ElKYUhMFl_privacidadpdf.pdf">la política de privacidad</a>.
            </label>
          </div>
        </div>

      <div class="form-group row justify-content-center align-items-center">
          <button type="button" class="btn btn-primary" style="max-width: 300px; margin: 30px 0" @click="doContactQuery">Enviar</button>
        </div>

    </form>

  </div>
</template>

<script>
import * as toastr from '../assets/toastr.js'
import axios from 'axios'
import {api} from '../main.js'

export default {
  name: 'Location',
  props: {
    logged: Boolean,
    token: String,
    id: Number,
    type: Number
  },
  created() {
    scrollTo(0,0)
  },
  data() {
    return {
        addContactForm:{
            full_name: '',
            email: '',
            phone_number: '',
            contact_query: ''
        }
    }
  },
  methods: {
    getYear() {
      return new Date().getFullYear()
    },
    doContactQuery(){
        this.addContactForm.full_name = document.getElementById('full_name').value
        this.addContactForm.email = document.getElementById('email').value
        this.addContactForm.phone_number = parseInt(document.getElementById('phone_number').value)
        this.addContactForm.contact_query = document.getElementById('contact_query').value
        var check_box = document.getElementById('check_box').checked
        if (this.addContactForm.full_name == '' || this.addContactForm.email == '' || this.addContactForm.contact_query == ''){
            toastr.info('', 'Rellena los campos obligatorios para generar la consulta.',
                {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right',preventDuplicates: true})
        } else if (!this.validateEmail(this.addContactForm.email)) {
            toastr.error('', 'Dirección de correo electrónico no válida.',
                {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right',preventDuplicates: true})
        } else if (!check_box){
            toastr.info('', 'Debe aceptar la politica de privacidad',
                {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right',preventDuplicates: true})
        } else{
            this.contactQuery()
        }
    },
    contactQuery(){
        const path = api + 'contact_info'
      axios.post(path, this.addContactForm)
          // eslint-disable-next-line no-unused-vars
          .then((res) => {
                toastr.success('', '¡Tu consulta ha sido enviada!',
                  {timeOut: 2500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right',preventDuplicates: true})
                this.$router.push({path: '/'})
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.log(error)
            toastr.error('', 'Algo no salió como se esperaba... prueba de nuevo mas tarde.',
                {timeOut: 1500, progressBar: true, newestOnTop: true, positionClass: 'toast-bottom-right',preventDuplicates: true})
            this.$router.push({path: '/'})
          })
    },
    validateEmail(email) {
      var re = /\S+@\S+\.\S+/;
      return re.test(email);
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@font-face {
  font-family: 'LogoFont';
  src: url('../assets/logo_font.woff')
}

h1 {
  margin: 50px 0;
}

form {
  margin: 50px auto;
  width: 80% /* value of your choice which suits your alignment */
}

</style>
