<template>
    <div class="wrap">
        <h1 class="title">TU CESTA</h1>
        <div class="row" style="margin-top: 5%">
            <div v-if="this.is_empty==1">
                <table style="width:100%;text-align: center">
                    <thead>
                        <tr style="background: #2bc4ed; border: 1px solid rgba(0, 0, 0, 0.5)">
                            <th>Titulo del libro</th>
                            <th>Cantidad</th>
                            <th>Precio(€)</th>
                            <th></th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody >
                        <tr v-for="(book,i) in cart" :key="book.id" >
                            <td>{{ book.name }}</td>
                            <td> <button class="btn" @click="addTciket(i,book)"> + </button>
                                {{ cart_quantity[i] }}
                                <button class="btn" @click="returnTicket(i,book)"> - </button>
                            </td>
                            <td>{{ book.price }}</td>
                            <td>{{ cart_total_price[i] }}</td>
                            <td>
                                <button type="button" style="margin-right: 20%" class="close" @click="deleteBook(i)" aria-label="Close">
                                  <span aria-hidden="true">&times;</span>
                                </button>
                            </td>
                            <td></td>
                        </tr>
                    </tbody>
                </table>
                <div class="subtotal cf" style="list-style:none; margin-right: 2%; text-align: center">
                    <ul>
                        <h6 class="totalRow"><span class="label">Subtotal: </span><span class="value">{{ getSubTotal() }}</span></h6>
                        <h6 class="totalRow"><span class="label">Envío: </span><span class="value">{{ shipping }}</span></h6>
                        <h6 class="totalRow final"><span class="label">Total: </span><span class="value">{{ getTotal() }}</span></h6>
                    </ul>
                </div>
                <div class="row" style="width:100%; align-content: center">
                  <button class="btn btn-lg" style="background-color: #2bc4ed;color: white" @click="checkout()">Ir a pagar</button>
                  <button class="btn btn-lg" style="background-color: #328399; color: white" @click="returnMainPage()">Volver</button>
                </div>
        </div>
            <div v-if="this.is_empty==0">
                <table style="width:100%;text-align: center">
                    <thead>
                        <tr>
                          <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Tu cesta está vacía</td>
                        </tr>
                    </tbody>
                    <button class="btn btn-lg" style="background-color: #328399; color: white" @click="returnMainPage()">Volver</button>
                </table>
            </div>
        </div>

    </div>
</template>

<script>
    export default {
        name: 'ShoppingCart',
        data () {
            return {
              is_empty: 1,
              cart: [{'name':"Prueba", "price":10},{'name':"Prueba", "price":10},{'name':"Prueba", "price":10},{'name':"Prueba", "price":10},{'name':"Prueba", "price":10},{'name':"Prueba", "price":10}],
              cart_quantity: [1,1,1,1,1,1],
              cart_total_price: [10,10,10,10,10,10],
              subtotal: 0,
              shipping: 5.00
            }
        },
        methods: {
            addTciket (i,book) {
                this.cart_quantity[i] = this.cart_quantity[i] + 1
                this.cart_total_price[i] = this.cart_total_price[i] + book.price
            },
            returnTicket (i, book) {
                if (this.cart_quantity[i] > 0) {
                    this.cart_quantity[i] = this.cart_quantity[i]-1
                    this.cart_total_price[i] = this.cart_total_price[i] - book.price
                    if (this.cart_quantity[i] === 0) {
                        this.deleteBook()
                    }
                }
            },
            deleteBook (i) {
                this.cart.splice(i,1)
                this.cart_quantity.splice(i,1)
                this.cart_total_price.splice(i,1)
                if ( this.cart_quantity.length < 1 ) {
                    this.is_empty = 0
                }
            },
            getSubTotal () {
                this.subtotal = 0
                for (let i = 0; i < this.cart_total_price.length; i += 1) {
                    this.subtotal = this.subtotal + this.cart_total_price[i]
                }
                return this.subtotal
            },
            getTotal () {
                return this.getSubTotal() + this.shipping
            },
            checkout () {
                if ( this.$route.query.logged === "false") {
                    this.$router.replace({ path: '/access', query: { logged: false } })
                }
            },
            returnMainPage () {
                this.$router.replace({ path: '/'})
            }
        }
    }

</script>

<style scoped>
    .wrap {
        width: 75%;
        max-width: 960px;
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

    a.btn.continue {
        width: 100%;
        text-align: center;
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