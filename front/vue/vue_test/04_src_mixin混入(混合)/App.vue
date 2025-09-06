<template>
  <div>
    <h1>{{ name }}</h1><hr>
    <School></School><hr>
    <Student></Student>
  </div>
</template>

<script>
import School from './components/School.vue'
import Student from './components/Student.vue'

export default {
  name: 'App',
  data() {
    return {
      name: 'Vue!'
    }
  },
  components: {
    School,
    Student
  }
}
</script>