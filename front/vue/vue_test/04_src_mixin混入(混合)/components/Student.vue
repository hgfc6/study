<template>
  <div>
    <h2 @click="showName">{{ name }}</h2>
    <h2>{{ age }}</h2>
  </div>
</template>

<script>
// import {mixin} from '../mixin'
export default {
  name: 'Student',
  data() {
    return {
      // name: "张三",
      age: 18
    }
  },
  // mixins: [mixin]
}
</script>