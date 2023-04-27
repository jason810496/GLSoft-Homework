<template>
  <div class="calculator">
    <div class="display">{{current || '0'}}</div>
    <button @click="memeryAdd" class="btn">M+</button>
    <button @click="memeryMinus" class="btn">M-</button>
    <button @click="memeryRead" class="btn">MR</button>
    <button @click="memeryClear" class="btn">MC</button>
    <button @click="clear" class="btn">C</button>
    <button @click="sign" class="btn">+/-</button>
    <button @click="percent" class="btn">%</button>
    <button @click="div" class="btn operator">÷</button>
    <button @click="append('1')" class="btn">1</button>
    <button @click="append('2')" class="btn">2</button>
    <button @click="append('3')" class="btn">3</button>
    <button @click="times" class="btn operator">x</button>
    <button @click="append('4')" class="btn">4</button>
    <button @click="append('5')" class="btn">5</button>
    <button @click="append('6')" class="btn">6</button>
    <button @click="minus" class="btn operator">-</button>
    <button @click="append('7')" class="btn">7</button>
    <button @click="append('8')" class="btn">8</button>
    <button @click="append('9')" class="btn">9</button>
    <button @click="add" class="btn operator">+</button>
    <button @click="append('0')" class="btn">0</button>
    <button @click="dot" class="btn">.</button>
    <button @click="del" class="btn">DEL</button>
    <button @click="equal" class="btn operator">=</button>
  </div>
</template>

<script>

import Big from 'big.js';
export default {
  data() {
    return {
      memery : localStorage.getItem('memery') || '0',
      previous: null,
      current: '0',
      operator: null,
      operatorClicked: false,
    }
  },
  methods: {
    // normal calculation
    clear() {
      this.current = '0';
    },
    sign() {
      this.current = new Big(this.current).times(-1).toString();
    },
    percent() {
      this.current = new Big(this.current).div(100).toString();
    },
    append(number) {
      if(number === '0' && this.current === '0' ) return;
      if (this.operatorClicked) {
        this.current = '';
        this.operatorClicked = false;
      }

      if( this.current === '0' ) this.current = '';
      this.current = `${this.current}${number}`;
    },
    dot() {
      if (this.current.indexOf('.') === -1) {
        if(this.current === '0') this.current = '0.';
        else this.append('.');
      }
    },
    setPrevious() {
      this.previous = this.current;
      this.operatorClicked = true;
    },
    div() {
      this.operator = (a, b) => {
        const BigA = new Big(a);
        return BigA.div(new Big(b)).toString();
      };
      this.setPrevious();
    },
    times() {
      this.operator = (a, b) => {
        const BigA = new Big(a);
        return BigA.times(new Big(b)).toString();
      };
      this.setPrevious();
    },
    minus() {
      this.operator = (a, b) => {
        const BigA = new Big(a);
        return BigA.minus(new Big(b)).toString();
      };
      this.setPrevious();
    },
    add() {
      this.operator = (a, b) => { 
        const BigA = new Big(a);
        return BigA.plus(new Big(b)).toString();
      };
      this.setPrevious();
    },
    equal() {
      this.current = `${this.operator(
        this.previous, 
        this.current
      )}`;
      this.previous = null;
    },
    del(){
      if( this.current.length === 2 && this.current[0] === '-' ) this.current = '0';
      else if(this.current.length === 1) this.current = '0';
      else this.current = this.current.slice(0, -1);
      this.current = new Big(this.current).toString();
    },
    // memery calculation
    memeryAdd() {
      this.memery = new Big(this.memery).plus(new Big(this.current || '0')).toString();
      localStorage.setItem('memery', this.memery);
    },

    memeryMinus() {
      this.memery = new Big(this.memery).minus(new Big(this.current || '0' )).toString();
      localStorage.setItem('memery', this.memery);
    },

    memeryRead() {
      this.current = localStorage.getItem('memery') || '0';
    },

    memeryClear() {
      localStorage.setItem('memery', '0');
      this.current = '0';
      this.memery = '0';
    },
  }
}
</script>

<style scoped>

.calculator {
  margin: 0 auto;
  width: 450px;
  padding: 30px 10px 30px 10px;
  font-size: 40px;
  margin-top: 50px;

  border-radius: 0.5rem;
  background-color: #a57e7e;
  
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: minmax(50px, auto);
  /* shadow */
  box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;
}

.display {
  padding: 20px 0;
  margin: 0px 10px 20px 10px;

  border-radius: 0.5rem;
  grid-column: 1 / 5;
  background-color: #333;
  color: white;
  overflow: scroll;
  /* shadow */
  box-shadow: rgb(124, 124, 124) 3px 3px 6px 0px inset, rgba(188, 188, 188, 0.5) -3px -3px 6px 1px inset;
  /* box-shadow: rgba(0, 0, 0, 0.06) 0px 2px 4px 0px inset; */
  /* box-shadow: rgba(50, 50, 93, 0.25) 0px 30px 60px -12px inset, rgba(0, 0, 0, 0.3) 0px 18px 36px -18px inset; */
}

/* .zero {
  grid-column: 1 / 3;
} */

button {
  font-size: 20px;
  margin: 6px;
  padding: 20px 0px;

  border: 0px ;
  background-color: #F2F2F2;
  border-radius: 1rem;
  /* shadow */
  box-shadow: rgba(0, 0, 0, 0.24) 0px 5px 8px;
  transition: 0.5s;
}

/* .operator {
  background-color: orange;
  color: white;
} */


/* RWD Sizing */

@media (max-width: 800px) {
  .calculator {
    font-size: 30px;
    width: 350px;
    padding: 25px 8px 30px 8px;
    margin-top: 30px;
  }
  button {
    font-size: 15px;
    margin: 4px;
    padding: 15px 0px;
  }
  .display {
    padding: 10px 0;
    margin: 0px 8px 10px 8px;
  }
}

@media (max-width: 400px) {
  .calculator {
    font-size: 25px;
    width: 250px;
    padding: 20px 5px 15px 5px;
  }
  button {
    font-size: 12px;
    margin: 3px;
    padding: 10px 0px;
  }
  .display {
    padding: 10px 0;
    margin: 0px 10px 14px 10px;
  }
}

</style>