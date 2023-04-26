<template>
  <div id="app" :class="selectedTheme">
    <ThemeSelector v-model="selectedTheme" @theme-changed="onThemeChanged" />
    <CalculatorItem />
  </div>
</template>

<script>
import CalculatorItem from './components/CalculatorItem.vue'
import ThemeSelector from './components/ThemeSelector.vue';
import "@/assets/ThemeList.css"

export default {
  name: 'app',
  components: {
    ThemeSelector,
    CalculatorItem,
  },
  data(){
    return {
      selectedTheme: localStorage.getItem('theme') || 'light'
    }
  },
  methods: {
    onThemeChanged(newTheme) {
      this.selectedTheme = newTheme;
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 0;
  padding: 0;
  height: 100vh;
  width: 100vw;
}

body{
  margin: 0;
}
</style>