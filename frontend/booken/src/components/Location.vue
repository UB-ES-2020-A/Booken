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
    <h1>Ubicación</h1>
    <div class="container my-5">
      <div class="card mb-3">
        <iframe
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d47934.93292795734!2d2.069679273505837!3d41.33206356109684!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x7ed60c3f0d5633b4!2sAbacus%20cooperativa!5e0!3m2!1ses!2ses!4v1603633929559!5m2!1ses!2ses"></iframe>

        <div class="card-body">
          <h5 class="card-title">Carrer de la Creu Coberta, 93, 08014 Barcelona</h5>
          <br>
          <p class="card-text">L-J de 9.00 h a 21.00 h</p>
          <p class="card-text">V-S de 9.00 h a 22.00 h</p>
        </div>
      </div>
      <div class="card mb-3">
        <iframe
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d47438.6851340534!2d2.070573263303511!3d41.33266885455343!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x625bcc9bd331c76b!2sAbacus%20cooperativa!5e0!3m2!1ses!2ses!4v1603633962958!5m2!1ses!2ses"></iframe>

        <div class="card-body">
          <h5 class="card-title">Carrer d'Ausiàs Marc, 16, 08010 Barcelona</h5>
          <br>
          <p class="card-text">L-J de 9.00 h a 21.00 h</p>
          <p class="card-text">V-S de 9.00 h a 22.00 h</p>
        </div>
      </div>

    </div>
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

iframe {
  min-height: 400px;
}

h1{
  margin-top: 50px;
}


</style>
