<template>
  <div>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
    <link rel="stylesheet" href="../assets/cool_buttons.css">
    <link rel="stylesheet" href="../assets/typewriter_a.css">
    <link href='https://fonts.googleapis.com/css?family=Lato' rel='stylesheet' type='text/css'>
    <b-navbar toggleable="lg" variant="info" style="background-color: #2bc4ed !important;">
      <b-navbar-brand href="#" class="logo-text line-1 anim-typewriter">booken</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="mx-auto">
          <b-nav-form>
            <b-form-input class="mr-sm-2" placeholder="Busca por autor, título, género, ISBN"
                          style="width: 30rem"></b-form-input>
            <b-button size="sm" class="my-2 my-sm-0" type="submit"><i class="fas fa-search"></i>
            </b-button>
          </b-nav-form>
        </b-navbar-nav>
        <b-navbar-nav class="ml-auto">
          <b-button class="btn btn-1 btn-sep icon-info">Button</b-button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: 'Front',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
@font-face {
  font-family: "Logo";
  src: url('../assets/logofont.woff')

}

.logo-text {
  font-size: 3em;
  font-family: Logo;
  color: #3b494d;
}
</style>
