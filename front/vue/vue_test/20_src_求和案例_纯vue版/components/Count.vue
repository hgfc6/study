<template>
  <div>
    <h2>当前值为：{{ sum }}</h2>
    <select v-model.number="num">
      <option value="1">1</option>
      <option value="2">2</option>
      <option value="3">3</option>
    </select>
    <button @click="increment">+</button>
    <button @click="decrement">-</button>
    <button @click="incrementOdd">奇数加</button>
    <button @click="incrementWait">延迟加</button>
  </div>
</template>

<script>

export default {
  name: 'Count',
  data() {
    return {
      sum: 0,
      num: 1
    }
  },
  methods: {
    increment() {
      this.sum += this.num
    },
    decrement() {
      this.sum -= this.num
    },
    incrementOdd() {
      if (this.sum % 2) {
        this.sum += this.num
      }
    },
    incrementWait() {
      setTimeout(() => {
        this.sum += this.num
      }, 500)
    },
  }
}

</script>

<style>
button {
  margin-left: 5px;
}
</style>