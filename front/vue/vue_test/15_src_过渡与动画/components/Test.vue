<template>
  <div>
    <button @click="show = !show">显示/隐藏</button>
    <transition appear>
      <!--appear属性可以写成:appear='true'也可以写成上面的简写形式-->
      <h2 class="bt" v-show="show">你好啊！</h2>
    </transition>

    <transition name="hello" appear>
      <!--transition如果有name属性，过度动画里的样式的类名.v-enter-active要改为.hello-enter-active-->
      <h2 class="bt" v-show="show">你好啊！</h2>
    </transition>

    <transition name="hello2" appear>
      <h2 class="bt" v-show="show">你好啊！</h2>
    </transition>

    <transition-group name="hello2" appear>
      <h2 class="bt" v-show="show" key="1">你好啊！</h2>
      <h2 class="bt" v-show="show" key="2">Hello World!</h2>
    </transition-group>
  </div>
</template>

<script>
export default {
  name: 'Test',
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

.v-enter-active {
  animation: cjh 0.5s linear;
}

.v-leave-active {
  animation: cjh 0.5s linear reverse;
}

.hello-enter-active {
  animation: cjh 0.5s linear;
}

.hello-leave-active {
  animation: cjh 0.5s linear reverse;
}

@keyframes cjh {
  from {
    transform: translateX(-100%);
  }
  to {
    transform: translateX(0px);
  }
}

/*过渡实现*/
/*进入的起点、离开的终点*/
.hello2-enter, .hello2-leave-to {
  transform: translateX(-100%);
}

.hello2-enter-active, .hello2-leave-active {
  transition: 2s linear;
}

/*离开的起点、进入的终点*/
.hello2-leave, .hello2-enter-to {
  transform: translateX(0px);
}
</style>