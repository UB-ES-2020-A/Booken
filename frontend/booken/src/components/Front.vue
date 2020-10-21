<template>
  <div>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
          integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
    <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
    <link href='https://fonts.googleapis.com/css?family=Lato' rel='stylesheet' type='text/css'>

    <nav class="navbar navbar-expand-sm navbar-dark bg-dark" style="background-color:#2bc4ed !important;">
      <a class="navbar-brand mainlogo ml-5" href="#">booken<span class="badge badge-light"
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
              <button class="btn my-2 my-sm-0 mr-2" style="background-color: #3b494d" type="submit" v-if="!loggedIn">
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
              <button class="btn my-2 my-sm-0 mr-5" style="background-color: #3b494d" type="submit">
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
            <a class="nav-link categoriestxt" href="#">Cómics y manga</a>
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
</template>

<script>
export default {
  name: 'Front',
  props: {
    msg: String
  },
  data() {
    return {
      loggedIn: false
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
.footer {
  max-width: 1280px;
  margin: auto;
  display: flex;
  align-items: baseline;
  justify-content: space-around;

  flex-wrap: wrap;
  background-color: #3b494d;
  color: aliceblue;
  font-size: 14px;
  padding: 60px 20px 20px 20px;
  min-height: 400px;
  position: relative;
}

.footerContainer > *:last-child {
  margin-bottom: 0;
  color: #fff;
}

.footer1,
.footer2,
.footer3,
.footer4 {
  min-width: 250px;
  margin-bottom: 20px;
  flex-basis: 25%;
  text-align: left;
  padding-left: 50px;
}
.footer1 ul,
.footer2 ul,
.footer3 ul,
.footer4 ul {
  list-style-type: none;
  padding: 0;
}

.footer1 ul li a,
.footer2 ul li a,
.footer3 ul li a,
.footer4 ul li a {
  text-decoration: none;
}

.footerContainer hr {
  border: none;
  background: #b5b5b5;
  height: 1px;
  margin: 20px 0;
}

.footer .copyright {
  text-align: center;
}

.footer1 ul li a:hover,
.footer2 ul li a:hover,
.footer3 ul li a:hover,
.footer4 ul li a:hover {
  color: #8a8a8a;
}

.footer1 ul li a,
.footer2 ul li a,
.footer3 ul li a,
.footer4 ul li a {
  color: aliceblue;
}
</style>
