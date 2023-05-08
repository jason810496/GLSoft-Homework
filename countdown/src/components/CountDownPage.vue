<template>
    <div id="countdown" :class="[font,color,status]" v-bind:style="{opacity: `${opacity}%`}">
        <div class="digit">
            <svg class="add" @click="add10m" xmlns="http://www.w3.org/2000/svg" version="1.1" width='100' height='100' fill="#fff">
                <path d="M 50,5 95,97.5 5,97.5 z"/>
            </svg>
            <span> {{ remainingTime.tenMinute }}</span>
            <svg class="sub" @click="sub10m" xmlns="http://www.w3.org/2000/svg" version="1.1"  width='100' height='100' fill="#fff">
                <path d="M 50,97.5 95,5 5,5 Z"/>
            </svg>
        </div>
        <div class="digit">
            <svg class="add" @click="addm" xmlns="http://www.w3.org/2000/svg" version="1.1" width='100' height='100' fill="#fff">
                <path d="M 50,5 95,97.5 5,97.5 z"/>
            </svg>
            <span> {{ remainingTime.minute }}</span>
            <svg class="sub" @click="subm" xmlns="http://www.w3.org/2000/svg" version="1.1"  width='100' height='100' fill="#fff">
                <path d="M 50,97.5 95,5 5,5 Z"/>
            </svg>
        </div>
        <div class="digit">
            <span> : </span>
        </div>
        <div class="digit">
            <svg class="add" @click="add10s" xmlns="http://www.w3.org/2000/svg" version="1.1" width='100' height='100' fill="#fff">
                <path d="M 50,5 95,97.5 5,97.5 z"/>
            </svg>
            <span> {{ remainingTime.tenSecond }}</span>
            <svg class="sub" @click="sub10s" xmlns="http://www.w3.org/2000/svg" version="1.1"  width='100' height='100' fill="#fff">
                <path d="M 50,97.5 95,5 5,5 Z"/>
            </svg>
        </div>
        <div class="digit">
            <svg class="add" @click="adds" xmlns="http://www.w3.org/2000/svg" version="1.1" width='100' height='100' fill="#fff">
                <path d="M 50,5 95,97.5 5,97.5 z"/>
            </svg>
            <span> {{ remainingTime.second }}</span>
            <svg class="sub" @click="subs" xmlns="http://www.w3.org/2000/svg" version="1.1"  width='100' height='100' fill="#fff">
                <path d="M 50,97.5 95,5 5,5 Z"/>
            </svg>
        </div>
    </div>
</template>
  
<script>
import { addTime , subTime , setCountDown } from './helper.js';

export default {
    name: 'CountDownPage',
    data() {
        return {
            status: 'hidden', // show
            color : localStorage.getItem('color') || 'red',
            font : localStorage.getItem('font') || 'digital-7',
            opacity : localStorage.getItem('opacity') || 100,
            countdown : localStorage.getItem('countdown') || 0,
            remainingTime: {
                tenMinute: Math.floor( Math.abs(this.countdown) / 600) || 0 ,
                minute :  Math.floor( Math.abs( Math.abs(this.countdown) )/ 60) % 10 || 0 ,
                tenSecond :  Math.floor( Math.abs(this.countdown) % 60 / 10) || 0 ,
                second : Math.floor( Math.abs(this.countdown) % 60 % 10) || 0 ,
            },
        };
    },
    methods: {
        loadSetting(){
            // console.log('countdown load setting');
            this.opacity = localStorage.getItem('opacity') || 100;
            this.color = localStorage.getItem('color') || 'red';
            this.font = localStorage.getItem('font') || 'digital-7';
            this.$forceUpdate();
        },
        updateTime(){
            this.remainingTime.tenMinute = Math.floor( Math.abs(localStorage.getItem('countdown') || 0) / 600) ;
            this.remainingTime.minute =  Math.floor( Math.abs( Math.abs(localStorage.getItem('countdown') || 0) )/ 60) % 10  ;
            this.remainingTime.tenSecond =  Math.floor( Math.abs(localStorage.getItem('countdown') || 0) % 60 / 10) ;
            this.remainingTime.second = Math.floor( Math.abs(localStorage.getItem('countdown') || 0) % 60 % 10) ;
        },
        setTime(){
            let totalTime = this.remainingTime.tenMinute * 600 + this.remainingTime.minute * 60 + this.remainingTime.tenSecond * 10 + this.remainingTime.second;
            setCountDown(totalTime);
        },
        add10m(){
            this.remainingTime.tenMinute = addTime(this.remainingTime.tenMinute);
            this.setTime();
        },
        sub10m(){
            this.remainingTime.tenMinute = subTime(this.remainingTime.tenMinute);
            this.setTime();
        },
        addm(){
            this.remainingTime.minute = addTime(this.remainingTime.minute);
            this.setTime();
        },
        subm(){
            this.remainingTime.minute = subTime(this.remainingTime.minute);
            this.setTime();
        },
        add10s(){
            this.remainingTime.tenSecond = addTime(this.remainingTime.tenSecond);
            this.setTime();
        },
        sub10s(){
            this.remainingTime.tenSecond = subTime(this.remainingTime.tenSecond);
            this.setTime();
        },
        adds(){
            this.remainingTime.second = addTime(this.remainingTime.second);
            this.setTime();
        },
        subs(){
            this.remainingTime.second = subTime(this.remainingTime.second);
            this.setTime();
        },
        show(){
            // console.log('condownpage show')
            this.status = "show";
        },
        hidden(){
            this.status = "hidden";
        },
    },
};
</script>
  

<style>
#countdown{
    display: flex;
    z-index: 999;
}
#countdown button{
    display: block;
}
#countdown span{
    display: block;
}
.digit{
    justify-content: center;
    text-align: center;
}

.digit span{
    font-size: 85vh;
    font-family: digital-7;
}
.digit svg{
    transform: scale(0.5);
}
.add{
    margin-bottom: -40px;
}
.sub{
    margin-top: -70px;
}
#countdown.digital-7 :nth-child(3) span{
    top: 50%; transform: translateY(25%);
}

#countdown.normal .digit span{
    font-family: 'Secular One', sans-serif;
    font-size: 60vh;
}
#countdown.normal .digit {
    margin: auto;
}
.normal .add{
    margin-bottom: -90px;
}
.normal .sub{
    margin-top: -160px;
}
</style>