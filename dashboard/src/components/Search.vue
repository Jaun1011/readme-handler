<template>
  <div class="dashboard">
    <nav>
      <ul>
        <li 
          v-for="entry in entries" 
          v-on:click="select(entry.ID_Nr_)"
          :key="entry.ID_Nr_" 
          class="nav-item"
          :class="selectedId === entry.ID_Nr_? 'nav-item-selected': ''">
          
          {{entry.GE_GR_}}
          <div :class="'tag tag' + entry.Version_">{{entry.Version_}}</div>
        </li>
      </ul>
    </nav>
    <article>
      <div>
        <widget :values="selected.basic1" />
        <widget :values="selected.basic2" />
        <widget :values="selected.basic3" />
      </div>

      <div class="box texttable">
        <table>
          <tr  
            v-for="(value, i)  in selected.textFields"           
            :key="i" >
            <td>{{value.aktion}}</td>
            <td>{{value.text}}</td>
            <td>{{value.vorgabe}}</td>
          </tr>
        </table>
      </div>

    </article>
  </div>
</template>

<script>
import Widget from './Widget.vue'


export default {
  name: 'Search',

  components: {
    Widget,
  },


  data: () => {
      const entries = window.GENERATED_DATA

    return{
      selectedId: 0,
      entries,
      selected: {}
    }
  },
  methods: {
    select (id) {
        this.selectedId = id;
        
        const item = this.entries.find(v => v.ID_Nr_ === id)
        this.selected = {
            basic1: [
              {label: "WE",         value: item.WE_},
              {label: "GE / GR",    value: item.GE_GR_},
              {label: "Version",    value: item.Version_},
              {label: "Datum",      value: item.Datum_},
              {label: "WE Bauzone", value: item.Zone1_},
              {label: "WE Schutzzone", value: item.Zone2_},
              {label: "WE Gefahrenzone", value: item.Zone3_},
            ],
            basic2: [
              {label: "G_Art_",         value: item.G_Art_},
              {label: "G_OwnerTyp_",    value: item.G_OwnerTyp_},
              {label: "G_VerRaum_m2",    value: item.G_VerRaum_m2},
              {label: "G_VerPP_m2",      value: item.G_VerPP_m2},
              {label: "WE G_VerAussen_m2", value: item.G_VerAussen_m2},
              {label: "WE G_WHG_m2", value: item.G_WHG_m2},
            ],
            basic3: [
              {label: "WE_Region_",         value: item.WE_Region_},
              {label: "WE_AnmVertrag_Anz",    value: item.WE_AnmVertrag_Anz},
              {label: "WE_AnmRaum_m2",    value: item.WE_AnmRaum_m2},
              {label: "WE_AnmAussen_m2",      value: item.WE_AnmAussen_m2},
              {label: "WE WE_VerRaum_m2", value: item.WE_VerRaum_m2},
              {label: "WE WE_VerPP_m2", value: item.WE_VerPP_m2},
              {label: "WE WE_VerAussen_m2", value: item.WE_VerAussen_m2},
              {label: "WE_DrittVerRaum_m2", value: item.WE_DrittVerRaum_m2},
              {label: "WE_score_BTR", value: item.WE_score_BTR},
              {label: "WE_score_Lage", value: item.WE_score_Lage},
              {label: "WE_score_Strat_", value: item.WE_score_Strat_},
              {label: "Erfasser", value: item.Erfasser},
            ],
            textFields: [
              {text: item.Text0, vorgabe: item.Vorgabe0_, aktion: item.Aktion0_},
              {text: item.Text1, vorgabe: item.Vorgabe1_, aktion: item.Aktion1_},
              {text: item.Text2, vorgabe: item.Vorgabe2_, aktion: item.Aktion2_},
              {text: item.Text3, vorgabe: item.Vorgabe3_, aktion: item.Aktion3_},
              {text: item.Text4, vorgabe: item.Vorgabe4_, aktion: item.Aktion4_},
              {text: item.Text5, vorgabe: item.Vorgabe5_, aktion: item.Aktion5_},
              {text: item.Text6, vorgabe: item.Vorgabe6_, aktion: item.Aktion6_},
              {text: item.Text7, vorgabe: item.Vorgabe7_, aktion: item.Aktion7_},
              {text: item.Text8, vorgabe: item.Vorgabe8_, aktion: item.Aktion8_},
            ],
        }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

article {
  display: grid;
  grid-template-columns: auto auto;
  grid-template-rows: auto auto auto;
}

nav {
  background-color: lightslategray;
}

nav ul{
  list-style-type: none;
  padding: 0;
}


.nav-item{
  padding: 5px;
}

.nav-item:hover{
    background-color: rgb(216, 216, 216);
}

.nav-item-selected{
    background-color: rgb(68, 64, 64);
}

.tag{
  display:inline;
  margin: 5px;
  padding: 5px;
  border-radius: 5px;
}


.tag1{
  background-color: darkolivegreen;
}

.tag2{
  background-color: cornflowerblue;
}

.dashboard{
  display: grid;
  grid-template-columns: 140px auto;
  grid-template-rows: 100%;
  height: 100%;
  width: 100%;
}


table, tr, td{
  border: solid 1px black;
  border-collapse: collapse; 
  margin: 0;
}



.texttable{
  padding-right: 1em;
}

</style>
