<template>
    <svg xmlns="http://www.w3.org/2000/svg" version="1.1" class="start-button" width='100' height='100' fill="#fff" :class="status" @click="start">
            <path d="M 95,50 5,95 5,5 z"/>
    </svg>
</template>
  
<script>

export default {
    name: 'SettingButton',
    data(){
        return {
            status : 'show' // hidden
        };
    },
    methods: {
        start(){
            this.hidden();
            this.$emit('start-child');
        },
        show(){
            this.status = "show";
        },
        hidden(){
            this.status = "hidden";
        }
    },
};
</script>


<style>
.start-button{
    opacity: 0.7;
    z-index: 999;
    /* position */
    position: fixed;
    top:50%;
    left:50%;
    transform: translateX(-50%) translateY(-50%);
}
.hidden{
    visibility: hidden;
    position: fixed;
}
</style>
  