<template>
    <CountDown />
    <CountDownButton @change-status="onChangeStatus" />
    <StopWatchButton @change-status="onChangeStatus" />
    <DisplayItem ref="displayItem" />
    <ResetButton @reset-countdown="onResetCountdown" @reset-stopwatch="onResetStopwatch" />
    <SettingButton @change-status="onChangeStatus" />
    <SettingPage ref="settingPage" @load-setting="onLoadSetting"/>
    <StartButton ref="startButton" @start-child="onStartChild"/>
    <TouchBoard ref="touchBoard" @pause="onPause" />
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
  created(){
    console.log('app created');
    localStorage.setItem('countdown',0);
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
    onResetCountdown(){
      this.$refs.displayItem.resetCountDown();
    }
    ,onResetStopwatch(){
      this.$refs.displayItem.resetStopWatch();
    },
    onStartChild(){
      this.$refs.touchBoard.show();
      if( this.status  === COUNTDOWN ){
        this.$refs.displayItem.startCountDown();
      }
      else if( this.status === STOPWATCH ){
        setStatus(STOPWATCH);
      }
    },
    onPause(){
      if( this.status  === COUNTDOWN ){
        this.$refs.displayItem.pauseCountDown();
      }
      else if( this.status === STOPWATCH ){
        this.$refs.displayItem.pauseStopWatch();
      }
      this.$refs.startButton.show();
    },
    onLoadSetting(){
      console.log('app load setting');
      this.$refs.displayItem.loadSetting();
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
