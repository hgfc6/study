<template>
  <div>
    <h2 class="demo">{{ name }}</h2>
    <h2>{{ address }}</h2>
  </div>
</template>

<script>
export default {
  name: 'School',
  data() {
    return {
      name: "QH",
      address: "BeiJing"
    }
  }
}
</script>

<style scoped>
.demo {
  background-color: yellow;
}
</style>