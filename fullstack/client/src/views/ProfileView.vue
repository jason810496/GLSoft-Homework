<template>
    <h1>Profile View</h1>
</template>
  
<script>
export default {
    name: 'ProfileView',
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