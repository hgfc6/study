<template>
  <div>
    <h2 style="color: #4CAF50">上方数值：{{ countSum }}</h2>
    <h2>人员列表</h2>
    <input type="text" v-model="name" @keydown.enter="add">
    <button @click="add">添加</button>
    <ul>
      <li v-for="(p, index) in personList" :key="p.id">{{ p.name }}</li>
    </ul>
  </div>
</template>

<script>
import {nanoid} from "nanoid";

export default {
  name: 'Person',
  data() {
    return {
      name: ''
    }
  },
  methods: {
    add() {
      const personObj = {id: nanoid(), name: this.name}
      this.$store.commit('ADD_PERSON', personObj)
      this.name = ''
    }
  },
  computed: {
    personList() {
      return this.$store.state.personList
    },
    countSum() {
      return this.$store.state.sum
    }
  }
}
</script>
