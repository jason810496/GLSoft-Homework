<template>
    <div id="theme-selector" class="calculator">
        <label>Theme Selector:</label>
        <select class="display" id="theme-select" v-model="selectedTheme" @change="onThemeChanged" >
            <option v-for="theme in themeList" :key="theme.id" :value="theme.id">
                {{ theme.name }}
            </option>
        </select>
    </div>
</template>

<script>

export default {
    data() {
        return {
            selectedTheme: localStorage.getItem('theme') || 'default',
            themeList:[
                { id : 'default', name: 'default'},
                { id : 'tokyonight', name: 'tokyonight' },
                { id : 'vue-dark', name: 'vue-dark' },
                { id : 'merko', name: 'merko' },
            ],
        }
    },
    name: 'ThemeSelector',
    methods: {
        onThemeChanged() {
            this.$emit('theme-changed', this.selectedTheme);
            localStorage.setItem('theme', this.selectedTheme);
        }
    }
}


</script>

<style>
#theme-selector{
    position: relative;
    display: block;
    text-align: center;
    width: fit-content;
    height: fit-content;
    left: 50%;
    transform: translateX(-50%) translateY(10px);
    padding: 10px;
    border-radius: 0.5rem;
}
#theme-selector label{
    position: relative;
    display: block;
    text-align: center;
}
#theme-selector select{
    border: none;
    margin-top: 10px;
    border-radius: 0.2rem;
}

</style>