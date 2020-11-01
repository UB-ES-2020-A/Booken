<template>
  <div>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
          integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
    <link href='https://fonts.googleapis.com/css?family=Lato' rel='stylesheet' type='text/css'>
    <h1 style="margin-top: 1em">Tu cesta</h1>
    <div class="container mb-4" v-if="this.is_empty==1">
      <div class="row">
        <div class="col-12">
          <div class="table-responsive">
            <table class="table table-striped" style="text-align: left">
              <thead>
              <tr>
                <th scope="col"></th>
                <th scope="col">Artículo</th>
                <th scope="col">Precio</th>
                <th scope="col" class="text-center">Cantidad</th>
                <th scope="col" class="text-right">Total</th>
                <th></th>
              </tr>
              </thead>
              <tbody>
              <tr v-for="(book,i) in cart" :key="book.id">
                <td></td>
                <!--<td><img :src="image" style="width: 10%"></td>-->
                <td>{{ book.name }}</td>
                <td>{{ book.price }} €</td>
                <td class="text-center">
                  <button class="btn my-2 my-sm-0" style="background-color: #3b494d; margin-right: 0.5rem" type="submit"
                          @click="decrease(i, book)"><i
                      class="fas fa-minus" style="color: #FFF"/></button>
                  {{ cart_quantity[i] }}
                  <button class="btn my-2 my-sm-0" style="background-color: #3b494d; margin-left: 0.5rem" type="submit"
                          @click="increase(i, book)"><i
                      class="fas fa-plus" style="color: #FFF"/></button>
                </td>
                <td class="text-right">{{ book.price * cart_quantity[i] }} €</td>
                <td class="text-right">
                  <button class="btn btn-sm btn-danger" @click="deleteBook(i)"><i class="fas fa-trash"></i></button>
                </td>
              </tr>

              <tr>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td>IVA (21%)</td>
                <td class="text-right">{{ subtotal1 * 0.21 }} €</td>
              </tr>
              <tr>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td>Envío</td>
                <td class="text-right">{{ shipping }} €</td>
              </tr>
              <tr>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td><strong>TOTAL</strong></td>
                <td class="text-right"><strong>{{ total }} €</strong></td>
              </tr>
              </tbody>
            </table>
          </div>
        </div>
        <div class="col mb-2">
          <div class="row">
            <div class="col-sm-12  col-md-6">
              <button class="btn btn-lg btn-block" style="background-color:#3b494d; color: white; margin-top: 0.5rem"
                      @click="returnMainPage">
                Continuar comprando
              </button>
            </div>
            <div class="col-sm-12 col-md-6 text-right">
              <button class="btn btn-lg btn-block" style="background-color: #2bc4ed; color: white; margin-top: 0.5rem"
                      @click="checkout">
                Pagar
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div style="margin-top: 1rem" v-if="this.is_empty==0">
      <div class="row">
        <div class="col">
          <h3 style="margin-top: 1.5rem;">Tu cesta está vacía.</h3>
          <button class="btn btn-lg animate__animated animate__bounce animate__infinite" @click="returnMainPage"
                  style="background-color:#3b494d; color: white; margin-top: 5rem; margin-bottom: 10rem">¿Compras algo?
          </button>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: 'ShoppingCart',
  created() {
    this.subtotal = this.getSubTotal()
    this.total = this.getTotal()
  },
  data() {
    return {
      is_empty: 0,
      cart: [{'name': "Prueba", "price": 10}, {'name': "Prueba", "price": 10}, {
        'name': "Prueba",
        "price": 10
      }, {'name': "Prueba", "price": 10}, {'name': "Prueba", "price": 10}, {'name': "Prueba", "price": 10}],
      cart_quantity: [1, 1, 1, 1, 1, 1],
      cart_total_price: [10, 10, 10, 10, 10, 10],
      image: 'https://static.fnac-static.com/multimedia/Images/ES/NR/22/0f/18/1576738/1507-1.jpg',
      subtotal1: 0,
      shipping: 5.00,
      total: 5.00
    }
  },
  methods: {
    increase(i, book) {
      this.cart_quantity[i] = this.cart_quantity[i] + 1
      this.cart_total_price[i] = this.cart_total_price[i] + book.price
      this.subtotal = this.subtotal + book.price
      this.total = this.total + book.price
    },
    decrease(i, book) {
      if (this.cart_quantity[i] > 0) {
        this.cart_quantity[i] = this.cart_quantity[i] - 1
        this.cart_total_price[i] = this.cart_total_price[i] - book.price
        if (this.cart_quantity[i] === 0) {
          this.deleteBook()
        } else {
          this.subtotal = this.subtotal - book.price
          this.total = this.total - book.price
        }
      }
    },
    deleteBook(i) {
      this.cart.splice(i, 1)
      this.cart_quantity.splice(i, 1)
      this.cart_total_price.splice(i, 1)
      this.subtotal = this.getSubTotal()
      this.total = this.getTotal()
      if (this.cart_quantity.length < 1) {
        this.is_empty = 0
      }
    },
    getSubTotal() {
      this.subtotal = 0
      for (let i = 0; i < this.cart_total_price.length; i += 1) {
        this.subtotal = this.subtotal + this.cart_total_price[i]
      }
      return this.subtotal
    },
    getTotal() {
      return this.getSubTotal() + this.shipping
    },
    checkout() {
      if (this.$route.query.logged === "false") {
        this.$router.replace({path: '/access', query: {logged: false}})
      }
    },
    returnMainPage() {
      this.$router.replace({path: '/'})
    }
  }
}

</script>
<style scoped>
.table-striped > tbody > tr:nth-child(2n+1) > td, .table-striped > tbody > tr:nth-child(2n+1) > th {
  background-color: #a9e5f5 !important;
}

.wrap {
  width: 75%;
  margin: 0 auto;
  padding: 5% 0;
  margin-bottom: 5em;
}

.title {
  font-family: sans-serif;
  font-weight: bold;
  text-align: center;
  font-size: 2em;
  padding: 1em 0;
  border-bottom: 1px solid #dadada;
  letter-spacing: 3px;
  text-transform: uppercase;
}

.totalRow {
  padding: .5em;
  text-align: right;
}

.label {
  font-family: sans-serif;
  font-size: .85em;
  text-transform: uppercase;
  color: #777;
}

.value {
  letter-spacing: -.025em;
  width: 35%;
}
</style>