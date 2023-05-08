<template>
    <button id="setting-button" @click="changeStatus" :class="status">
        <i class="fa-solid fa-gear"></i>
    </button>
</template>
  
<script>

export default {
    name: 'SettingButton',
    data() {
        return {
            status : 'show', // hidden
        };
    },
    methods: {
        changeStatus(){
            this.$emit('change-status','setting');
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

#setting-button{
    position: fixed;
    bottom: 0;
    left: 0;
    width: 50px;
    height: 50px;
    border: none;
    outline: none;
    cursor: pointer;
    font-size: 20px;
    background-color: #000;
}
#setting-button i{
    color: #fff;
}
</style>
  