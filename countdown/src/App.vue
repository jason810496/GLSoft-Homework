<template>
  <div>
    <CountDown />
    <TimerItem />
    <SetTime />
    <RestartItem />
    <SettingItem />
  </div>
</template>

<script>
import CountDown from './components/CountDown.vue';
import TimerItem from './components/TimerItem.vue';
import SetTime from './components/SetTime.vue';
import RestartItem from './components/RestartItem.vue';
import SettingItem from './components/SettingItem.vue';


export default {
  name: 'App',
  components: {
    CountDown,
    TimerItem,
    SetTime,
    RestartItem,
    SettingItem
  }
};
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
