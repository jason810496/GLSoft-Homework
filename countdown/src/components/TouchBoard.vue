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

div#touch-board.show{
    position: fixed;
    width: 100%;
    height: 100%;
    z-index: 999;
}

div#touch-board.hidden{
    position: fixed;
    visibility: hidden;
    z-index: -999;
    width: 0;
    height: 0;
}
</style>
  