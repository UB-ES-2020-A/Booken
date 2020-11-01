<style>
@import url("../assets/toastr.css");
@import url("../assets/animate.min.css");

</style>
<template>
  <div>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
          integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
    <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
    <link href='https://fonts.googleapis.com/css?family=Lato' rel='stylesheet' type='text/css'>
    <h1>Contacto</h1>
    <form>
      <div class="form-group">
        <label for="exampleFormControlInput1">Nombre y apellido</label>
        <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Name Surname">
      </div>
      <div class="form-group">
        <label for="exampleFormControlInput2">Correo electrónico</label>
        <input type="email" class="form-control" id="exampleFormControlInput2" placeholder="name@example.com">
      </div>
      <div class="form-group">
        <label for="exampleFormControlInput3">Teléfono de contacto</label>
        <input type="number" class="form-control" id="exampleFormControlInput3" placeholder="">
      </div>

      <div class="form-group">
        <label for="exampleFormControlTextarea1">Consulta</label>
        <textarea class="form-control" id="exampleFormControlTextarea1" rows="10"></textarea>
      </div>
      <div class="form-group row">
          <div class="form-check" style="margin-top: 30px">
            <input class="form-check-input" type="checkbox" id="gridCheck1">
            <label class="form-check-label" for="gridCheck1">
              He leído y acepto <a href="https://pdfhost.io/v/ElKYUhMFl_privacidadpdf.pdf">la política de privacidad</a>
            </label>
          </div>
        </div>

      <div class="form-group row justify-content-center align-items-center">
          <button type="submit" class="btn btn-primary" style="max-width: 300px; margin: 30px 0">Submit</button>
        </div>

    </form>

  </div>
</template>

<script>
export default {
  name: 'Location',
  props: {
    msg: String
  }, methods: {
    getYear() {
      return new Date().getFullYear()
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
