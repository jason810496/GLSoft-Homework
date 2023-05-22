<template>
    <h1>Home View</h1>
</template>
  
<script>
export default {
    name: 'HomeView',
    data() {
        return {
            status : 'show', // hidden
        };
    },
    methods: {
        toggle() {
            this.status = this.status === 'show' ? 'hidden' : 'show';
        },
    },
};
</script>