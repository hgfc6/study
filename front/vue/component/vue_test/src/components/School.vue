<template>
  <div class="demo">
    <h2>{{ name }}</h2><hr>
    <button @click="showName">点击查看学校名字</button>
  </div>
</template>

<script>
export default {
  name: 'School',
  data() {
    return {
      name: 'School of Data Science and AI'
    }
  },
  methods: {
    showName() {
      alert(this.name);
    }
  },
}
</script>

<style>
.demo {
  background-color: yellow;
}
</style>