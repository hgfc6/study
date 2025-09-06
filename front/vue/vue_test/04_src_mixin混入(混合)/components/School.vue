<template>
  <div>
    <h2 @click="showName">{{name}}</h2>
    <h2>{{address}}</h2>
  </div>
</template>

<script>
// import {mixin} from '../mixin'
  export default {
    name: 'School',
    data() {
      return {
        name: "QH",
        address:"BeiJing"
      }
    },
    // mixins: [mixin]
  }
</script>