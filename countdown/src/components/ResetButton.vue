<template>
    <button id="reset-button" @click="reset" :class="UIstatus">
        <i class="fa-solid fa-rotate-left"></i>
    </button>
</template>
  
<script>

import { COUNTDOWN, STOPWATCH } from './constant.js';
import { resetCountDown , resetStopWatch } from './helper.js';

export default {
    name: 'ResetButton',
    data() {
        return {
            UIstatus : 'show', // hidden
            status : localStorage.getItem('status') || 'countdown',
        };
    },
    methods: {
        async reset(){
            if( this.status == COUNTDOWN ){
                this.$emit('reset-countdown');
                resetCountDown();
            }
            else if( this.status == STOPWATCH ){
                this.$emit('reset-stopwatch');
                resetStopWatch();
            }
        },
        show(){
            this.UIstatus = "show";
        },
        hidden(){
            this.UIstatus = "hidden";
        }
    },
};
</script>

<style>

#reset-button{
    position: absolute;
    bottom: 0;
    right: 0;
    width: 50px;
    height: 50px;
    border: none;
    outline: none;
    cursor: pointer;
    font-size: 20px;
    background-color: #000;
}
#reset-button i{
    color: #fff;
}

</style>
  