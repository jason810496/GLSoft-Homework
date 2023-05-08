<template>
    <div id="display" :class="colorTag">
        <div class="digit">
            <span> {{ remainingTime.tenMinute }}</span>
        </div>
        <div class="digit">
            <span> {{ remainingTime.minute }}</span>
        </div>
        <div class="digit">
            <span> : </span>
        </div>
        <div class="digit">
            <span> {{ remainingTime.tenSecond }}</span>
        </div>
        <div class="digit">
            <span> {{ remainingTime.second }}</span>
        </div>
    </div>
</template>
  
<script>
import { setCountDown ,setStopWatch  } from './helper.js';

export default {
    name: 'CountDown',
    data() {
        return {
            timeUp: false,
            colorTag:'even',
            countDownFunction : null,
            stopWatchFunction : null,
            remainingTime: {
                tenMinute: 0,
                minute: 0,
                tenSecond: 0,
                second: 0,
            },
        };
    },
    methods: {
        startCountDown(){
            let totalTime = localStorage.getItem('countdown') || 0;
            this.countDownFunction = setInterval( async () => {

                if( this.timeUp ){
                    totalTime++;
                }
                else{
                    totalTime--;
                }

                if( totalTime == 0 ){
                    this.timeUp = true;
                }
                // localStorage.setItem('countdown', totalTime);
                setCountDown(totalTime);

                // update UI 
                if( this.timeUp ){
                    if( totalTime%2 === 1 ){
                        this.colorTag = 'odd';
                    }
                    else{
                        this.colorTag = 'even';
                    }
                }
                
                this.remainingTime.tenMinute = Math.floor(totalTime / 600);
                this.remainingTime.minute = Math.floor(totalTime / 60) % 10;
                this.remainingTime.tenSecond = Math.floor(totalTime % 60 / 10);
                this.remainingTime.second = Math.floor(totalTime % 60 % 10);

            }, 1000);
        },
        pauseCountDown(){
            clearInterval(this.countDownFunction);
        },
        startStopWatch(){
            let totalTime = localStorage.getItem('stopwatch') || 0;
            this.stopWatchFunction = setInterval( async () => {

                totalTime++;
                // localStorage.setItem('countdown', totalTime);
                setStopWatch(totalTime);
                
                this.remainingTime.tenMinute = Math.floor(totalTime / 600);
                this.remainingTime.minute = Math.floor(totalTime / 60) % 10;
                this.remainingTime.tenSecond = Math.floor(totalTime % 60 / 10);
                this.remainingTime.second = Math.floor(totalTime % 60 % 10);

            }, 1000);
        },
        pauseStopWatch(){
            clearInterval(this.stopWatchFunction);
        },

    },
};
</script>
  

<style>
#display{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
}
#display .digit span{
    font-size: 85vh;
    font-family: digital-7;
}

#display .digit span{
    color : #fff;
}
</style>