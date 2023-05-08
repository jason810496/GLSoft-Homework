<template>
    <CountDown />
    <CountDownButton @change-status="onChangeStatus" />
    <StopWatchButton @change-status="onChangeStatus" />
    <DisplayItem />
    <ResetButton />
    <SettingButton @change-status="onChangeStatus" />
    <SettingPage ref="settingPage"/>
    <StartButton @start-child="onStartChild"/>
    <TouchBoard @pause="onPause" />
</template>

<script>
import CountDown from './components/CountDown.vue';
import DisplayItem from './components/DisplayItem.vue';
import ResetButton from './components/ResetButton.vue';
import SettingButton from './components/SettingButton.vue';
import SettingPage from './components/SettingPage.vue';
import StartButton from './components/StartButton.vue';
import TouchBoard from './components/TouchBoard.vue';
import CountDownButton from './components/CountDownButton.vue';
import StopWatchButton from './components/StopWatchButton.vue';

import { setStatus  } from './components/helper.js';
import { COUNTDOWN, STOPWATCH ,  SETTING } from './components/constant.js';



export default {
  name: 'App',
    components: {
    CountDown,
    DisplayItem,
    ResetButton,
    SettingButton,
    SettingPage,
    StartButton,
    TouchBoard,
    CountDownButton,
    StopWatchButton
},
  data(){
    return {
      status : localStorage.getItem('status') || 'countdown',
    };
  },
  methods: {
    onChangeStatus(newStatus) {
      if( newStatus === SETTING ){
        this.$refs.settingPage.show();
      }
      this.status = newStatus;
    },
    onStartChild(){
      if( this.status  === COUNTDOWN ){
        setStatus(COUNTDOWN);
      }
      else if( this.status === STOPWATCH ){
        setStatus(STOPWATCH);
      }
    },
    onPause(){
      if( this.status  === COUNTDOWN ){
        setStatus(COUNTDOWN);
      }
      else if( this.status === STOPWATCH ){
        setStatus(STOPWATCH);
      }
    }
  }
};
</script>


<style>
#app{
  height: 100vh;
  width: 100vw;
  background: #000;
}
</style>
