<template>
    <div class="wrap">
        <h1 class="title">SHOPPING CART</h1>
        <div class="row">
            <div v-if="this.is_empty==1">
                <table style="width:100%;text-align: center">
                    <thead>
                        <tr class="bg-info border: 1px solid rgba(0, 0, 0, 0.5)">
                            <th>Book title</th>
                            <th>Quantity</th>
                            <th>Price(€)</th>
                            <th></th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(book,i) in cart" :key="book.id" >
                            <td>{{ book.name }}</td>
                            <td> <button class="btn" @click="addTciket(i,book)"> + </button>
                                {{ cart_quantity[i] }}
                                <button class="btn" @click="returnTicket(i,book)"> - </button>
                            </td>
                            <td>{{ book.price }}</td>
                            <td>{{ cart_total_price[i] }}</td>
                            <td>
                                <button class="btn" @click="deleteBook(i)"> x </button>
                            </td>
                            <td></td>
                        </tr>
                        <div class="subtotal cf" style="list-style:none; margin-left: 167%; text-align: center">
                            <ul>
                                <h6 class="totalRow"><span class="label">Subtotal: </span><span class="value">35.00</span></h6>
                                <h6 class="totalRow"><span class="label">Shipping: </span><span class="value">5.00</span></h6>
                                <h6 class="totalRow final"><span class="label">Total: </span><span class="value">44.00</span></h6>
                            </ul>
                        </div>
                        <div class="row">
                            <div class="col-6"></div>
                            <div class="col-6" style="margin-left: 65%">
                                <button style="width: 100%" class="bg-info"><a href="#" class="btn continue">Proced to Checkout</a></button>
                            </div>
                        </div>
                    </tbody>
                </table>
        </div>
            <div v-if="this.is_empty==0">
                <table style="width:75%;border: 1px solid black;text-align: center;margin-left: 150px">
                    <thead>
                        <tr>
                          <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Empty item on shopping cart</td>
                        </tr>
                    </tbody>
                    <button class="totalRow"><a href="#" class="btn continue">Back</a></button>
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
              cart: [{'name':"Prueba", "price":10}],
              cart_quantity: [1],
              cart_total_price: [10],
              can_ret: [false],
            }
        }, methods: {
        addTciket (i,book) {
            this.$set(this.cart_quantity, i, this.cart_quantity[i] + 1)
            this.$set(this.can_ret, i, true)
            this.$set(this.cart_total_price, i, this.cart_total_price[i] * book.price)
        },
        returnTicket (i, book) {
            if (this.cart_quantity[i] > 0) {
              this.$set(this.cart_quantity, i, this.cart_quantity[i] - 1)
              this.$set(this.cart_total_price, i, this.cart_total_price[i] * book.price)
              if (this.cart_quantity[i] === 0) {
                this.$set(this.can_ret, i, false)
              }
            }
        },
        deleteBook (i) {
            this.cart_quantity.delete(i)
            this.cart_total_price.delete(i)
            if ( this.cart_quantity.length == 0 ) {
                this.isEmpty = 0
            }
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

    .heading {
        padding: 1em 0;
        border-bottom: 1px solid #D0D0D0;
        font-family: sans-serif;
        font-size: 2em;
        float: left;
    }

    a.btn.continue {
        width: 100%;
        text-align: center;
    }

    a.remove {
        text-decoration: none;
        font-family: sans-serif;
        color: #ffffff;
        font-weight: bold;
        background: #e0e0e0;
        padding: .5em;
        font-size: .75em;
        display: inline-block;
        border-radius: 100%;
        line-height: .85;
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