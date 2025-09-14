<template>
  <div>
    <h2>{{ name }}</h2>
    <h2>{{ age }}</h2>
    <button @click="sendStuName">把学生名字交给学校</button>
  </div>
</template>

<script>
import pubsub from "pubsub-js";

export default {
  name: 'Student',
  data() {
    return {
      name: '张三',
      age: 18
    }
  },
  methods: {
    sendStuName() {
      pubsub.publish('showStuName', this.name)
    }
  }
}
</script>