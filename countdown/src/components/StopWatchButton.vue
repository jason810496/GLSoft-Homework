<template>
    <button id="stopwatch-button" @click="reset">
        <i class="fa-solid fa-stopwatch"></i>
    </button>
</template>
  
<script>


export default {
    name: 'StopWatchButton',
    data() {
        return {
            status : localStorage.getItem('status') || 'countdown',
        };
    },
    methods: {
        
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
}
#stopwatch-button i{
    color: #fff;
    font-size: 20px;
}

</style>
  