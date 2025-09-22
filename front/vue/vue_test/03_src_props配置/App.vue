<template>
  <div>
    <h1>{{ name }}</h1>
    <hr>
    <Student name="zhangsan" :age="20" sex="男"></Student>
    <!--这里用:age是因为age在Student中被定义为Number,如果不加:那么age会被当作字符串处理-->
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