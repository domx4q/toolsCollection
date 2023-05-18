<template>
  <div id="app">
    <Section name="Krypto">
      <div id="keyShower"><span class="noSelect"><b>SCHLÜSSEL</b>: </span>{{key}}</div>
      <div class="item">
        <Action name="Schlüssel erstellen" path="/crypto/generateKey" type="simple" @action="key=$event"/>
      </div>
      <button type="button" @click="updateKey">Schlüssel aus Zwischenablage auslesen <span class="small">only Chrome</span></button>
      <div class="item"><CryptoAction name="Verschlüsseln" path="/crypto/encrypt" mode="encrypt" :kee="key"/></div>
      <div class="item"><CryptoAction name="Entschlüsseln" path="/crypto/decrypt" mode="decrypt" :kee="key"/></div>
    </Section>
  </div>
</template>
<script>
import Section from "./components/Section.vue";
import Action from './components/Action.vue'
import CryptoAction from "./components/CryptoAction.vue";
export default {
  name: 'App',
  components: {
    Section,
    Action,
    CryptoAction
  },
  data() {
    return {
      key: "unknown"
    }
  },
  methods: {
    updateKey() {
      navigator.clipboard.readText().then(text => {
        this.key = text
        console.log('Pasted content: ', text)
      })
    }
  },
  computed: {},
  mounted() {
    // set this html[data-theme="dark"]
    document.documentElement.setAttribute('data-theme', 'dark');
  },
  watch: {}
}
</script>
<style scoped>
.item {
  margin: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border-radius: 30px;
  background-color: hsl(211, 95%, 38%);
  padding: 30px;
}
.item:nth-of-type(odd) {
  background-color: hsl(30, 95%, 38%);
}
.item:nth-of-type(4) {
  background-color: hsl(300, 95%, 38%);
}
#keyShower {
  font-family: monospace;
  font-size: 14px;
  position: absolute;
  top: 0;
}
#app {
  display: grid;
}
b {
  text-decoration: underline;
  font-weight: 9000;
  font-size: 16px;
}
.noSelect {
  user-select: none;
}
.small {
  font-size: 12px;
  border:  1px solid white;
  /*nowrap*/
  white-space: pre;
  padding: 2px;
  border-radius: 3px;
}
*::selection {
  background-color: #0022bb;
  color: white;
}
</style>
