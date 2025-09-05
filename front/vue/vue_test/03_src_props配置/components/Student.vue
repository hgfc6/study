<template>
  <div>
    <h2>{{ msg }}</h2>
    <h2>{{ name }}</h2>
    <h2>{{ sex }}</h2>
    <h2>{{ myAge + 1 }}</h2>
    <button @click="changeAge">修改年龄,会警告</button><br/>
    <button @click="changeMyAge">修改年龄,不会警告</button>
  </div>
</template>

<script>
export default {
  name: 'Student',
  data() {
    return {
      msg: 'Hello Vue!',
      // name: "zs",
      // sex: '男',
      // age: 18
      myAge: this.age
    }
  },
  methods: {
    changeAge() {//能改但是会警告，不建议
      this.age = 99// vue.runtime.esm.js:4482 [Vue warn]: Avoid mutating a prop directly since the value will be overwritten whenever the parent component re-renders.
      // Instead, use a data or computed property based on the prop's value. Prop being mutated: "age"
    },
    changeMyAge() {
      this.myAge++
    }
  },
  // props: ['name', 'age','sex']//简单接收

  // props: {//接收时对类型进行限制
  //   name: String,
  //   age: Number,
  //   sex: String
  // }

  props: {//接收时对类型，默认值，是否必填 进行限制
    name: {
      type: String,
      required: true,
    },
    age: {
      type: Number,
      required: false,
      default: 100
    },
    sex: {
      type: String,
      required: false,
      default: 'unknown'
    }
  }
}
</script>