<template>
  <div class="section">
    <h2>{{name}}</h2>
    <slot/>
  </div>
</template>
<script>
export default {
  name: 'Section',
  components: {},
  props: {
    name: String,
  },
  data() {
    return {}
  },
  methods: {},
  computed: {},
  mounted() {},
  watch: {}
}
</script>
<style scoped>
.section {
  border-radius: 30px;
  background-color: #3ba43c;
  padding: 15px;
  margin: 10px;
  display: flex;
  flex-direction: row;
  gap: 10px;
  align-items: center;
  justify-content: center;
  min-width: 800px;
  max-width: 80vw;
  min-height: 200px;
  max-height: 40vh;
  position: relative;
}
.section h2 {
  position: absolute;
  top: 0;
  left: 0;
  margin: 10px;
  font-size: 24px;
  font-weight: 9000;
  font-family: inherit;
}
</style>