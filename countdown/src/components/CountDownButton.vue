<template>
    <button id="countdown-button" @click="updateStatus" :class="status">
        <i class="fa-solid fa-clock"></i>
    </button>
</template>
  
<script>

import { setStatus  } from './helper.js';
import { COUNTDOWN} from './constant.js';

export default {
    name: 'CountDownButton',
    data() {
        return {
            status : 'show', // hidden
        };
    },
    methods: {
        show(){
            this.status = "show";
        },
        hidden(){
            this.status = "hidden";
        },
        updateStatus(){
            console.log('CountDownButton updateStatus');
            setStatus(COUNTDOWN);
            this.$emit('show-countdown');
        }
    },
};
</script>

<style>

#countdown-button{
    position: fixed;
    top: 0;
    right: 0;
    width: 50px;
    height: 50px;
    border: none;
    outline: none;
    cursor: pointer;
    background-color: #000;
    z-index: 999;
}
#countdown-button i{
    color: #fff;
    font-size: 20px;
}

</style>
  