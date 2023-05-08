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
            countdown : localStorage.getItem('countdown') || 0,
            stopwatch : localStorage.getItem('stopwatch') || 0,
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
            let totalTime = Math.abs( localStorage.getItem('countdown') ) || 0;
            this.timeUp = false;

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
                console.log('totalTime', totalTime);

                // update UI 
                if( this.timeUp ){
                    if( totalTime%2 === 1 ){
                        this.colorTag = 'odd';
                    }
                    else{
                        this.colorTag = 'even';
                    }
                }
                
                this.remainingTime.tenMinute =  Math.floor( Math.abs(totalTime) / 600) ;
                this.remainingTime.minute =  Math.floor( Math.abs( Math.abs(totalTime) )/ 60) % 10 ;
                this.remainingTime.tenSecond =  Math.floor( Math.abs(totalTime) % 60 / 10);
                this.remainingTime.second = Math.floor( Math.abs(totalTime) % 60 % 10);

            }, 1000);
        },
        resetCountDown(){
            this.remainingTime.tenMinute = 0;
            this.remainingTime.minute = 0;
            this.remainingTime.tenSecond = 0;
            this.remainingTime.second = 0;
            this.timeUp = false;
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
        resetStopWatch(){
            this.remainingTime.tenMinute = 0;
            this.remainingTime.minute = 0;
            this.remainingTime.tenSecond = 0;
            this.remainingTime.second = 0;
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