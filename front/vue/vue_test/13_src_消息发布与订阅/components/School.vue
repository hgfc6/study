<template>
  <div>
    <h2>{{ name }}</h2>
    <h2>{{ address }}</h2>
  </div>
</template>

<script>
import pubsub from 'pubsub-js'

export default {
  name: 'School',
  data() {
    return {
      name: "QH",
      address: "BeiJing"
    }
  },
  methods: {
    showStudentName(msgName, data) {
      console.log('收到学生名称：', data)
    }
  },
  mounted() {
    this.pubId = pubsub.subscribe('showStuName', this.showStudentName)
  },
  beforeDestroy() {
    pubsub.unsubscribe(this.pubId)
  }
}
</script>