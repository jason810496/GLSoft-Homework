<template>
    <button id="countdown-button" @click="reset">
        <i class="fa-solid fa-clock"></i>
    </button>
</template>
  
<script>


export default {
    name: 'CountDownButton',
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
}
#countdown-button i{
    color: #fff;
    font-size: 20px;
}

</style>
  