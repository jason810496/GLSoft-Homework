
async function setCountDown(t) {
    localStorage.setItem('countdown', t); // store total second
}

async function setStopWatch(t) {
    localStorage.setItem('stopwatch', t); // store total second
}

async function setColor(c) {
    localStorage.setItem('color', c);
}

async function setFont(f) {
    localStorage.setItem('font', f);
}

async function setDarkroom(d) {
    localStorage.setItem('darkroom', d);
}

async function setStatus(s) {
    // countdown , stopwatch ( defult: countdown )
    localStorage.setItem('status', s);
}

async function resetCountDown() {
    localStorage.setItem('countdown', 0);
}

async function resetStopWatch() {
    localStorage.setItem('stopwatch', 0);
}

async function saveAll(font,color,darkroom) {
    localStorage.setItem('font', font);
    localStorage.setItem('color', color);
    localStorage.setItem('darkroom', darkroom);
}

function addTime(digit) {
    if (digit === 9) return 0;
    return digit + 1;
}

function subTime(digit) {
    if (digit === 0) return 9;
    return digit - 1;
}


export { setCountDown, setStopWatch, setColor, setFont, setDarkroom, setStatus, resetCountDown, resetStopWatch, saveAll, addTime, subTime };