<template>
    <button id="stopwatch-button" @click="updateStatus" :class="UIstatus">
        <i class="fa-solid fa-stopwatch"></i>
    </button>
</template>
  
<script>

import { setStatus  } from './helper.js';
import {  STOPWATCH } from './constant.js';

export default {
    name: 'StopWatchButton',
    data() {
        return {
            UIstatus : 'show', // hidden
        };
    },
    methods: {
        show(){
            this.UIstatus = "show";
        },
        hidden(){
            this.UIstatus = "hidden";
        },
        updateStatus(){
            setStatus(STOPWATCH);
            this.$emit('show-stopwatch');
            this.$emit('change-status',STOPWATCH);
        }
    },
};
</script>

<style>

#stopwatch-button{
    position: fixed;
    top: 0;
    left: 0;
    width: 50px;
    height: 50px;
    border: none;
    outline: none;
    cursor: pointer;
    background-color: #000;
    z-index: 999;
}
#stopwatch-button i{
    color: #fff;
    font-size: 20px;
}

</style>
  