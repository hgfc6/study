<template>
  <div>
    <h1>{{ name }}</h1><hr>
    <h1>{{ x }}</h1><hr>
    <School></School>
  </div>
</template>

<script>
import School from './components/School.vue'
export default {
  name: 'App',
  data() {
    return {
      name: 'Vue!'
    }
  },
  components: {School}
}
</script>