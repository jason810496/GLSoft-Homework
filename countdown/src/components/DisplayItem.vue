<template>
    <div id="display" :class="[font,color,colorTag]" v-bind:style="{opacity: `${opacity}%`}">
        <div class="digit" >
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
            opacity: localStorage.getItem('opacity') || 100,
            color : localStorage.getItem('color') || 'red',
            font : localStorage.getItem('font') || 'digital-7',
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
        loadSetting(){
            console.log('display load setting');
            this.opacity = localStorage.getItem('opacity') || 100;
            this.color = localStorage.getItem('color') || 'red';
            this.font = localStorage.getItem('font') || 'digital-7';
            this.$forceUpdate();
        },
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

</style>