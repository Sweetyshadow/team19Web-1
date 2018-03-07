<template>
  <ul>
    <li v-for="item in dishes" :key="item.id">
      <p>{{ item.name }}</p>
      <p>{{ item.price }}</p>
      <button v-on:click="highlight">order</button>
    </li>
  </ul> 
</template>
<script>
export default {
  name: 'DishMenu',
  data () {
    return {
      dishes: [
        { id: 1,
          name: 'pizza',
          price: 50
        },
        {
          id: 2,
          name: 'bread',
          price: 10
        }
      ]
    }
  },
  methods: {
    highlight: function (event) {
      event.target.style.background = 'red'
    }
  }
}
</script>
<style scoped>
  ul{
    list-style: none;
    text-align: left;
  }
  li{
    display: inline-block;
    width: 100px;
    text-align: left;
  }
</style>

