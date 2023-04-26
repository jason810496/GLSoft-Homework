<template>
  <div class="calculator">
    <div class="display">{{current || '0'}}</div>
    <button @click="clear" class="btn">C</button>
    <button @click="sign" class="btn">+/-</button>
    <button @click="percent" class="btn">%</button>
    <button @click="buttonide" class="btn operator">÷</button>
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
    <button @click="append('0')" class="btn zero">0</button>
    <button @click="dot" class="btn">.</button>
    <button @click="equal" class="btn operator">=</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      previous: null,
      current: '',
      operator: null,
      operatorClicked: false,
    }
  },
  methods: {
    clear() {
      this.current = '';
    },
    sign() {
      this.current = this.current.charAt(0) === '-' ? 
        this.current.slice(1) : `-${this.current}`;
    },
    percent() {
      this.current = `${parseFloat(this.current) / 100}`;
    },
    append(number) {
      if (this.operatorClicked) {
        this.current = '';
        this.operatorClicked = false;
      }
      this.current = `${this.current}${number}`;
    },
    dot() {
      if (this.current.indexOf('.') === -1) {
        this.append('.');
      }
    },
    setPrevious() {
      this.previous = this.current;
      this.operatorClicked = true;
    },
    buttonide() {
      this.operator = (a, b) => a / b;
      this.setPrevious();
    },
    times() {
      this.operator = (a, b) => a * b;
      this.setPrevious();
    },
    minus() {
      this.operator = (a, b) => a - b;
      this.setPrevious();
    },
    add() {
      this.operator = (a, b) => a + b;
      this.setPrevious();
    },
    equal() {
      this.current = `${this.operator(
        parseFloat(this.current), 
        parseFloat(this.previous)
      )}`;
      this.previous = null;
    }
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
  /* shadow */
  box-shadow: rgb(124, 124, 124) 3px 3px 6px 0px inset, rgba(188, 188, 188, 0.5) -3px -3px 6px 1px inset;
  /* box-shadow: rgba(0, 0, 0, 0.06) 0px 2px 4px 0px inset; */
  /* box-shadow: rgba(50, 50, 93, 0.25) 0px 30px 60px -12px inset, rgba(0, 0, 0, 0.3) 0px 18px 36px -18px inset; */
}

.zero {
  grid-column: 1 / 3;
}

button {
  font-size: 20px;
  margin: 6px;
  padding: 20px 0px;

  border: 0px ;
  background-color: #F2F2F2;
  border-radius: 1rem;
  /* shadow */
  box-shadow: rgba(0, 0, 0, 0.24) 0px 5px 8px;
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