<template>
  <div>
    <h2>{{name}}</h2>
    <h2>{{address}}</h2>
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
    },
    methods: {
      showStudentName(data) {
        console.log('收到学生名称：', data)
      }
    },
    mounted() {
      this.$bus.$on('showStuName', this.showStudentName)
    },
    beforeDestroy() {
      this.$bus.$off('showStuName')
    }
  }
</script>