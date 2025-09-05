<template>
  <div>
    <h1>{{ name }}</h1>
    <hr>
    <Student name="zhangsan" :age="20" sex="男"></Student>
  </div>
</template>

<script>
import Student from './components/Student.vue'

export default {
  name: 'App',
  data() {
    return {
      name: 'Vue!'
    }
  },
  components: {Student}
}
</script>