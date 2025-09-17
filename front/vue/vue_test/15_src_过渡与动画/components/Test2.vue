<template>
  <div>
    <button @click="show = !show">显示/隐藏</button>
    <h2 class="bt animate__animated animate__bounce" v-show="show">你好啊！</h2>

    <!--集成第三方库-->
    <transition-group
        appear
        name="animate__animated animate__bounce"
        enter-active-class="animate__swing"
        leave-active-class="animate__backOutUp"
    >
      <h2 class="bt" v-show="show" key="1">你好啊！</h2>
      <h2 class="bt" v-show="!show" key="2">Hello World!</h2>
    </transition-group>
  </div>
</template>

<script>
import 'animate.css'

export default {
  name: 'Test2',
  data() {
    return {
      show: true,
    }
  }
}
</script>

<style scoped>
.bt {
  background-color: #5afff2;
}
</style>