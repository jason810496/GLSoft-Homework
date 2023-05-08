<template>
    <button class="start-button" :class="start" @click="start"></button>
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
            // emit event to parent ( App.vue)
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
    width: 0;
    height: 0;
    border-style: solid;
    border-width: 50px 0 50px 100px;
    border-color: transparent transparent transparent #fff;
    opacity: 0.7;
    z-index: 999;
    /* position */
    position: fixed;
    top:50%;
    left:50%;
    transform: translateX(-50%) translateY(-50%);
}
</style>
  