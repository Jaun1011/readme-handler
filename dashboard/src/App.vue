<template>
  <div id="app">

    <Search v-if="!rootPage"/>
    <div v-if="rootPage">
      <h1>rootpage</h1>
      <ul>
        <li 
          v-for="(weid, index) in weidsResult" 
          v-bind:key="index">
            <a :href="weid.path">{{weid.id}}</a>
        </li>
      </ul>

    </div>
  </div>
</template>

<script>
import Search from './components/Search.vue'

export default {
  name: 'App',
  components: {
    Search,
  },
  data(){
    const weids= window.GENERATED_DATA.map(val => ({
         id: val, 
         path: "../" + val + "/index.html"}))
    return {
      rootPage: window.ROOT_PAGE,
      weids, 
      weidsResult: weids 
    }
  }
}
</script>

<style>
html, body, #app  {

  min-height: 100%;
  height: 100%;
  width: 100%;
  padding: 0;
  margin: 0;
}

.box{
  padding: 1em;
  padding-right: 0;
  padding-bottom: 0;
}
</style>
