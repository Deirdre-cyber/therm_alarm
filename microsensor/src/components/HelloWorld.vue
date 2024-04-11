<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <div class="intro">
      <p>{{ intro }}</p>
      <p>{{ intro_two }}</p>
      <p>{{ intro_three }}</p>
    </div>

    <nav class="navbar">
      <div class="navbar-items">
        <router-link to="/tempdata">View Temperature Data</router-link>
      </div>
    </nav>


    <router-view />

  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: {
      type: String,
      default: 'Welcome to Therm Alarm!'
    },
    intro: {
      type: String,
      default: 'This is a simple Vue.js app that displays the temperature of a room.'
    },
    intro_two: {
      type: String,
      default: 'The temperature is read from a micro:bit and is updated every 5 seconds :)'
    },
    intro_three: {
      type: String,
      default: 'Follow link beolw to see the table which contains temperature data from the connected sensors.'
    
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
