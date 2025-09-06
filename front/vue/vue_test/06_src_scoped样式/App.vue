<template>
  <div>
    <h1>{{ name }}</h1>
    <hr>
    <School></School>
    <hr>
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
  components: {School, Student}
}
</script>
<!--APP中的style标签一旦配置，则该样式将作用到整个APP的样式上，而不是局限于当前组件。所以，如果想局限于当前组件，则需要在style标签中使用scoped属性。-->
<style>
h1 {
  font-size: 66px;
}

h2 {
  font-size: 36px;
}
</style>