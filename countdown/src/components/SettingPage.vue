<template>
    <div id="setting-page">
        <div class="choose font">
            <div class="just-center" :class="fontFirst" @click="selectFont('digit')"></div>
            <div class="just-center" :class="fontSecond" @click="selectFont('normal')"></div>
        </div>

        <div class="choose colors">
            <div class="just-center red"></div>
            <div class="just-center green"></div>
            <div class="just-center yellow"></div>
            <div class="just-center blue"></div>
            <div class="just-center white"></div>
        </div>

        <div class="choose darkroom">

        </div>

        <div class="choose">
            <div class="cancel border">Cancel</div>
            <div class="save border">Save</div>
        </div>
    </div>

</template>
  
<script>

import { setFont } from './helper.js';

export default {
    name: 'SettingPage',
    data() {
        return {
            fontFirst : "selected",
            fontSecond : "none",
        }
    },
    methods:{
        selectFont(f){
            if( f == 'digit' ){
                this.fontFirst = "selected";
                this.fontSecond = "none";
                setFont('digit');
            }
            else if( f == 'normal' ){
                this.fontFirst = "none";
                this.fontSecond = "selected";
                setFont('normal');
            }
        },
    }
};
</script>

<style>
.choose{
    display: flex;
}
.just-center{
    justify-content: center
}
.border{
    border: 1px solid #fff;
}
.selected{
    border: 1px solid #fff;
}
.none{
    border: none;
}

.colors div{
    border-radius: 5rem;
    width: 20px;
    height: 20px;
}
.red{
    background-color: red;
}
.green{
    background-color: rgb(0, 255, 0);
}
.yellow{
    background-color: yellow;
}
.blue{
    background-color: rgb(0, 255, 255);
}
.white{
    background-color: #fff;
}

#setting-page{
    position: fixed;
    visibility: hidden;
}

</style>


  