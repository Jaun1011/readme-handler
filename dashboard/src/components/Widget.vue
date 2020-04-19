<template>
      <div class="box">
          <table>
            <tr  
              v-for="value  in values"           
              :key="value.label" >
              <td>{{value.label}}</td>
              <td>{{value.value}}</td>
            </tr>
          </table>
      </div>
</template>

<script>
export default {
  name: 'Widget',
  props: {
    values: Array
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

table{
  border: black 1px solid;
  width: 100%;
}
</style>
