<template>
  <div id="action">
    <button type="button" @click="action">{{name}}</button>
  </div>
</template>
<script>

export default {
  name: 'Action',
  components: {},
  props: {
    name: String,
    path: String,
    type: String
  },
  data() {
    return {}
  },
  methods: {
    action() {
      if (this.type === 'simple') {
        this.axios.get(this.fullUrl).then(response => {
          console.log(response)
          this.$emit('action', response.data)
        }).catch(error => {
          console.log(error)
        })
      }
    }
  },
  computed: {
    fullUrl() {
      return "http://127.0.0.1:8000" + this.path
    }
  },
  mounted() {},
  watch: {}
}
</script>
<style scoped>
#action {

}
button {
  background: none;
  border: none;
  font-family: monospace;
  font-size: 18px;
  white-space: pre-wrap;
  max-width: 200px;
  width: min-content;

  transition: color 0.2s;
}
button:hover {
  cursor: pointer;
  color: #3ba43c;
}
</style>