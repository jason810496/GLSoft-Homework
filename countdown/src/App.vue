<template>
  <div id="timer">
    <CountDown />
    <CountDownButton @change-status="onChangeStatus" />
    <StopWatchButton @change-status="onChangeStatus" />
    <DisplayItem />
    <ResetButton />
    <SettingButton @change-status="onChangeStatus" />
    <SettingPage/>
    <StartButton @start-child="onStartChild"/>
    <TouchBoard @pause="onPause" />
  </div>
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
import { COUNTDOWN, STOPWATCH } from './components/constant.js';



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

</style>
