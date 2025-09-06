<template>
  <div>
    <h2>{{name}}</h2>
    <h2>{{address | myfilter}}</h2>
  </div>
</template>

<script>
  export default {
    name: 'School',
    data() {
      return {
        name: "QH",
        address:"BeiJing"
      }
    }
  }
</script>