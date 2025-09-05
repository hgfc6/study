<template>
  <div>
    <h1 v-text="title" ref="tit"></h1><br>
    <button @click="showDom">Show DOM</button><br>
    <button @click="showVC">Show VueConponent</button>
    <School ref="sch"/><!--自闭和vue自定义组件标签在脚手架中可以避免后续标签不生效-->
  </div>
</template>

<script>
import School from './components/School.vue'
export default {
  name: 'App',
  components: {School},
  data() {
    return {
      title: 'Hello Vue!'
    }
  },
  methods: {
    showDom() {
      console.log(this.$refs.tit)
    },
    showVC() {
      console.log(this.$refs.sch)
    }
  }
}
</script>