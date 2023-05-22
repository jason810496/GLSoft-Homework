<template>
    <h1>Login View</h1>
</template>
  
<script>
export default {
    name: 'LoginView',
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