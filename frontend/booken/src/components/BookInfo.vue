<style>

@import url("../assets/toastr.css");
@import url("../assets/animate.min.css");
@import url("../assets/book_info.css");

</style>
<template>
  <div>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
          integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
    <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">

    <div class = "container">
        <div class="row">
            <div class = "col-sm-1">
                <div style="display:flex; flex-direction: row">
                    <div>
                        <img ref="pic1" class="sel-picture" src="https://i1.wp.com/www.eastcoastdesigns.ca/wp-content/uploads/2018/02/black-and-white-book.png?fit=1600%2C1600&ssl=1.jpg" @click="changeImage(1)">
                        <img ref="pic2" class="sel-picture" src="https://image.shutterstock.com/image-vector/black-realistic-blank-book-cover-260nw-300099890.jpg" @click="changeImage(2)">
                    </div>
                    <div>
                        <img ref="bigPic" id="displayPic" src="https://i1.wp.com/www.eastcoastdesigns.ca/wp-content/uploads/2018/02/black-and-white-book.png?fit=1600%2C1600&ssl=1.jpg">
                    </div>
                </div>
            </div>
            <div class = "col-sm">
                <p>Book info here</p>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BookInfo',
  props: {
    msg: String
  },
  data() {
  }, methods: {
    toPrint (toPrint) {
      console.log(toPrint)
    },
    changeImage(id_image){
        this.toPrint(id_image)
        if(id_image == 1){
            this.$refs.bigPic.src = this.$refs.pic1.src
        }else{
            this.$refs.bigPic.src = this.$refs.pic2.src
        }
    }
  }
}
</script>