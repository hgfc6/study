<template>
  <div>
    <h1>当前求和为：{{ $store.state.sum }}</h1>
    <h2>当前和乘10为：{{ $store.getters.bigSum }}</h2>
    <h2>当前和乘10为：{{ bigSum }}</h2><!--借助mapGetter实现-->
    <h2>我来自{{ school }}，在学习{{ subject }}</h2><!--借助mapState实现-->

    <h2 style="color: red">下方组件人数：{{ personList.length }}</h2>
    <select v-model.number="n">
      <option value="1">1</option>
      <option value="2">2</option>
      <option value="3">3</option>
    </select>
    <button @click="increment">+</button>
    <button @click="mapIncrement(n)">map+</button>
    <button @click="decrement">-</button>
    <button @click="mapDecrement(n)">map-</button><!--通过mapMutations生成的方法如果不传参的话，默认会把event作为参数传递过去，所以一般要写参数-->
    <button @click="incrementOdd">当前求和为奇数再加</button>
    <button @click="mapIncrementOdd(n)">map当前求和为奇数再加</button>
    <button @click="incrementWait">等一等再加</button>
    <button @click="mapIncrementWait(n)">map等一等再加</button>
  </div>
</template>

<script>
import {mapState, mapGetters, mapMutations, mapActions} from 'vuex'

export default {
  name: 'Count',
  data() {
    return {
      n: 1, //用户选择的数字
    }
  },
  methods: {
    increment() {
      // this.$store.dispatch('jia',this.n) //因为action中的jia没有做任何附加处理，所以可以直接调用mutations中的JIA处理数据
      this.$store.commit('JIA', this.n)
    },
    decrement() {
      // this.$store.dispatch('jian',this.n)
      this.$store.commit('JIAN', this.n)
    },
    incrementOdd() {
      this.$store.dispatch('jiaOdd', this.n)
    },
    incrementWait() {
      this.$store.dispatch('jiaWait', this.n)
    },
    //靠mapMutations生成：mapIncrement、mapDecrement（对象形式）
    ...mapMutations({mapIncrement: 'JIA', mapDecrement: 'JIAN'}),//k:v > 方法名：mutations中的方法名
    //...mapMutations(['JIA','JIAN']),//（数组形式）方法名相同才能用

    //靠mapActions生成：mapIncrementOdd、mapIncrementWait（对象形式）
    ...mapActions({mapIncrementOdd: 'jiaOdd', mapIncrementWait: 'jiaWait'})
    //...mapActions(['jiaOdd','jiaWait'])//（数组形式）方法名相同才能用
  },
  computed: {
    //借助mapState生成计算属性，从state中读取数据
    // ...mapState({school: 'school', subject: 'subject'}),//对象写法
    ...mapState(['school', 'subject', 'personList']),//数组写法
    ...mapGetters({bigSum: 'bigSum'}),//对象写法
    //...mapGetters({bigSum: 'bigSum'}),//数组写法
  }
}
</script>

<style lang="css">
button {
  margin-left: 5px;
}
</style>
