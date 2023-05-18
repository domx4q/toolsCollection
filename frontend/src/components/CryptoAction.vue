<template>
  <div id="cryptoAction">
      <FormKit
          type="text"
          placeholder="Nachricht"
          v-model="text"
          @submit="submit"
          @keydown.enter="submit"
          :label="name"
      />
    <FormKit
        type="submit"
        @submit="submit"
        @click="submit"
        :label="name"
    />
    <div id="result">{{result}}</div>
  </div>
</template>
<script>
export default {
  name: 'CryptoAction',
  components: {},
  props: {
    name: String,
    path: String,
    kee: String, // key is a reserved word
    mode: String
  },
  data() {
    return {
      text: null,
      result: null
    }
  },
  methods: {
    submit() {
      this.axios.get(this.fullUrl).then(response => {
        console.log(response)
        if (this.mode === 'encrypt') {
          this.result = response.data["encrypted"]
        } else {
          this.result = response.data
        }
        this.$emit('action', this.result)
      }).catch(error => {
        console.log(error)
      })
    }
  },
  computed: {
    fullUrl() {
      return "http://127.0.0.1:8000" + this.path + "?text=" + this.text + "&key=" + this.kee
    },
  },
  mounted() {},
  watch: {}
}
</script>
<style scoped>
#cryptoAction {
  max-width: 300px;
}
#result {
  max-width: 250px;
  word-wrap: break-word;
  font-family: monospace;
  border: 1px solid black;
  border-radius: 5px;
  background-color: hsla(0, 0%, 0%, 0.3);
}
</style>