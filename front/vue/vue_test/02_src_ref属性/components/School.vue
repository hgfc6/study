<template>
  <div class="school">
    <h2>{{name}}</h2>
    <h2>{{address}}</h2>
  </div>
</template>

<script>
export default {
  name: 'School',
  data() {
    return {
      name: '清华',
      address: "beijing"
    }
  }
}
</script>

<style>
.school {
  background-color: gray;
}
</style>