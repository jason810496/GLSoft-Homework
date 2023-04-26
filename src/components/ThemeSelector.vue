<template>
    <div id="theme-selector">
        <select id="theme-select" v-model="selectedTheme" @change="onThemeChanged">
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
            themeList:[
                { id : 'default', name: 'default'},
                { id : 'tokyonight', name: 'tokyonight' },
            ],
        }
    },
    name: 'ThemeSelector',
    methods: {
        onThemeChanged() {
            this.$emit('theme-changed', this.selectedTheme);
        }
    },
    watch: {
        selectedTheme(newTheme) {
        this.$emit('theme-changed', newTheme);
        }
    }
}




</script>