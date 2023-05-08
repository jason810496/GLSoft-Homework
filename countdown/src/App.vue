<template>
    <CountDownPage ref="countDownPage" />
    <CountDownButton ref="countDownButton" @change-status="onChangeStatus" @show-countdown="onShowCountdown"/>
    <StopWatchButton ref="stopWatchButton" @change-status="onChangeStatus" @show-stopwatch="onShowStopwatch"/>
    <DisplayItem ref="displayItem" />
    <ResetButton ref="resetButton" @reset-countdown="onResetCountdown" @reset-stopwatch="onResetStopwatch" />
    <SettingButton ref="settingButton" @change-status="onChangeStatus" />
    <SettingPage ref="settingPage" @load-setting="onLoadSetting"/>
    <StartButton ref="startButton" @start-child="onStartChild"/>
    <TouchBoard ref="touchBoard" @pause="onPause" />
</template>

<script>
import CountDownPage from './components/CountDownPage.vue';
import DisplayItem from './components/DisplayItem.vue';
import ResetButton from './components/ResetButton.vue';
import SettingButton from './components/SettingButton.vue';
import SettingPage from './components/SettingPage.vue';
import StartButton from './components/StartButton.vue';
import TouchBoard from './components/TouchBoard.vue';
import CountDownButton from './components/CountDownButton.vue';
import StopWatchButton from './components/StopWatchButton.vue';

import { COUNTDOWN, STOPWATCH ,  SETTING } from './components/constant.js';



export default {
  name: 'App',
    components: {
    CountDownPage,
    DisplayItem,
    ResetButton,
    SettingButton,
    SettingPage,
    StartButton,
    TouchBoard,
    CountDownButton,
    StopWatchButton,
  },
  created(){
    console.log('app created');
  },
  data(){
    return {
      status : localStorage.getItem('status') || 'countdown',
    };
  },
  methods: {
    onShowCountdown(){
      console.log('apps onShowCountdown');
      this.status = COUNTDOWN;
      this.$refs.countDownPage.updateTime();
      this.$refs.countDownPage.$forceUpdate();
      this.$refs.countDownPage.show();
      this.$refs.displayItem.hidden();
    },
    onShowStopwatch(){
      console.log('apps onShowStopwatch');
      this.status = STOPWATCH;
      this.$refs.displayItem.updateStopwatch();
      this.$refs.displayItem.$forceUpdate();
    },
    onChangeStatus(newStatus) {
      if( newStatus === SETTING ){
        this.$refs.settingPage.show();
        return;
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
      console.log('apps onStartChild');

      this.$refs.countDownButton.hidden();
      this.$refs.countDownPage.hidden();
      this.$refs.stopWatchButton.hidden();
      this.$refs.resetButton.hidden();
      this.$refs.settingButton.hidden();


      if( this.status  === COUNTDOWN ){
        this.$refs.displayItem.updateCountdown();
        this.$refs.displayItem.$forceUpdate();
        this.$refs.displayItem.startCountDown();
      }
      else if( this.status === STOPWATCH ){
        this.$refs.displayItem.updateStopwatch();
        this.$refs.displayItem.$forceUpdate();
        this.$refs.displayItem.startStopWatch();
      }

      
      this.$refs.displayItem.show();
      this.$refs.touchBoard.show();
    },
    onPause(){
      this.$refs.countDownButton.show();
      this.$refs.stopWatchButton.show();
      this.$refs.resetButton.show();
      this.$refs.settingButton.show();

      if( this.status  === COUNTDOWN ){
        this.$refs.displayItem.colorTag = 'even';
        this.$refs.displayItem.$forceUpdate();

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
      this.$refs.countDownPage.loadSetting();
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
