<template>
  <div>
    <Test></Test>
    <hr/>
    <Test2></Test2>
  </div>
</template>

<script>
import Test from './components/Test'
import Test2 from './components/Test2'
export default {
  name: 'App',
  data() {
    return {
      name: 'Vue!'
    }
  },
  components: {Test, Test2}
}
</script>