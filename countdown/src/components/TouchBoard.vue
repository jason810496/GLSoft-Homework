<template>
    <div id="touch-board" @click="touch" :class="status"></div>
</template>
  
<script>


export default {
    name: 'TouchBoard',
    data() {
        return {
            status : "show", // hidden
            zIndex : 0,
        };
    },
    methods: {
        touch(){
            this.status = "hidden";
            // emit event to parent ( App.vue)
            this.$emit('pause');
        },
        show(){
            this.status = "show";
        },
    },
};
</script>

<style>

#touch-board.show{
    position: fixed;
    top : 0;
    right: 0;
    width: 100vw;
    height: 100vh;
    z-index: 999;
}

#touch-board.hidden{
    position: fixed;
    visibility: hidden;
    z-index: -999;
    width: 0;
    height: 0;
}

</style>
  