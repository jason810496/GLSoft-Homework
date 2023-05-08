<template>
    <div id="setting-page" :class="status">
        <div class="choose font">
            <div class="just-center digital-7" :class="[fontFirst,color]" @click="selectFont('digit')" v-bind:style="{opacity: `${opacity}%`}">
                23 : 45
            </div>
            <div class="just-center normal" :class="[fontSecond,color]" @click="selectFont('normal')" style="line-height: 0.9;" v-bind:style="{opacity: `${opacity}%`}">
                23 : 45
            </div>
        </div>

        <div class="choose colors">
            <div class="just-center bg-red" @click="selectColor('red')"></div>
            <div class="just-center bg-green" @click="selectColor('green')"></div>
            <div class="just-center bg-yellow" @click="selectColor('yellow')"></div>
            <div class="just-center bg-blue" @click="selectColor('blue')"></div>
            <div class="just-center bg-white" @click="selectColor('white')"></div>
        </div>

        <div class="choose opacity">
            <input type="range" name="opacity" min="0" max="100" v-model="opacity" @change="onOpacityChanged"/>
        </div>

        <div class="choose darkroom">
            <p><span v-bind:style="{opacity: `${opacity}%`}">Darkroom:</span><input type="checkbox" name="darkroom" value="true" v-model="darkroom" @change="onDarkroomChanged"/></p>
        </div>

        <div class="choose setting" v-bind:style="{opacity: `${opacity}%`}">
            <div class="cancel border" @click="leaveSetting">Cancel</div>
            <div class="save border" @click="saveSetting">Save</div>
        </div>
    </div>

</template>
  
<script>

import { setFont , setColor , saveAll } from './helper.js';

export default {
    name: 'SettingPage',
    data() {
        return {
            fontFamily : localStorage.getItem('font') || 'digit',
            fontFirst : "selected",
            fontSecond : "none",
            status : "hidden" , 
            color : localStorage.getItem('color') || 'red',
            darkroom : localStorage.getItem('darkroom') || false,
            opacity : localStorage.getItem('opacity') || 100
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
        selectColor(c){
            console.log('select color' , c );
            this.color = c;
            setColor(c);
        },
        onOpacityChanged(){
            console.log('opacity changed' , this.opacity);
            localStorage.setItem('opacity',this.opacity);
        },
        onDarkroomChanged(){
            localStorage.setItem('darkroom',this.darkroom);
        },
        show(){
            console.log('show setting page');
            this.status = "show";
        },
        hidden(){
            this.status = "hidden";
        },
        leaveSetting(){
            this.hidden();
        },
        saveSetting(){
            saveAll(this.fontFamily, this.color, this.darkroom);
            this.$emit('load-setting');
            this.hidden();
        }
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


#setting-page.show{
    position : fixed;
    top:  0 ;
    right:  0;
    height: 100vh;
    width: 100vw;
    background-color: #000;
    visibility: visible;
    z-index: 9999;
}
#setting-page.hidden{
    position : fixed;
    visibility: hidden;
}

.choose{
    color : #fff;
    margin: auto;
    margin-bottom: 20px;
    align-items: center;
    justify-content: center;
}
.font div{
    margin: 10px;
    font-size: 5rem;
    height: min-content;
}

.colors div{
    margin: 0 10px;
}

input[type="range"] {
  height: 30px;
  width: 220px;
  overflow: hidden;
  cursor: pointer;              /* 滑鼠放上會改變鼠標樣式 */
  outline: none;                /* 取消底線效果 */
  background-color: white;      /* 為了解釋方便所設定 */
  /* background-color: grey; */ /* 我的目標樣式 */
  margin: 0 10px 0;
}


input[type="range"]::-webkit-slider-runnable-track {
  height: 6px;
  width: 220px;
  background: #aaa;
}

input[type="range"]::-webkit-slider-thumb{
  position: relative;
  height: 16px;
  width: 16px;
  margin-top: -5px;              /* 會受到寬高影響定位，需微調 */
  background-color: tomato;      /* 為了解釋方便所設定 */
  /* background-color: white; */ /* 我的目標樣式 */
  border-radius: 50%;
  border: 1px solid black;
}
input[type=”range”]::-moz-range-thumb{
  position: relative;
  height: 16px;
  width: 16px;
  margin-top: -5px;              /* 會受到寬高影響定位，需微調 */
  background-color: tomato;      /* 為了解釋方便所設定 */
  /* background-color: white; */ /* 我的目標樣式 */
  border-radius: 50%;
  border: 1px solid black;
}

input[type=”range”]::-ms-thumb{
  position: relative;
  height: 16px;
  width: 16px;
  margin-top: -5px;              /* 會受到寬高影響定位，需微調 */
  background-color: tomato;      /* 為了解釋方便所設定 */
  /* background-color: white; */ /* 我的目標樣式 */
  border-radius: 50%;
  border: 1px solid black;
}

.darkroom{
    font-size: 1.2rem;
}
.darkroom input{
    height: 20px;
    width: 20px;
    transform: translateY(5px);
}

.setting div{
    margin: 0 10px;
    line-height: 1.5;
    padding: 0 4px;
    font-size: 1.2rem;
}

</style>


  