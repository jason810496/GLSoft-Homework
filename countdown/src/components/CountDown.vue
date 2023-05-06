<template>
    <div>
        <div :style="{ color: colorTag}"> {{ days }} days, {{ hours }} hours, {{ minutes }} minutes, {{ seconds }} seconds</div>
    </div>
    <input type="time" v-model="timeInput" @change="selectTime" />
</template>
  
<script>
import moment from 'moment';

export default {
    name: 'CountDown',
    data() {
        return {
            colorTag : 'hsl(0, 0%, 50%)',
            startDate: moment(),
            targetDate: moment().add(10, 'minutes'),
            origDiff : null,
            remainingTime: {
                days: 0,
                hours: 0,
                minutes: 0,
                seconds: 0,
            },
        };
    },
    methods: {
        updateTime() {
            const now = moment();
            const duration = moment.duration(this.targetDate.diff(now));
            this.remainingTime.days = Math.floor(duration.asDays());
            this.remainingTime.hours = duration.hours();
            this.remainingTime.minutes = duration.minutes();
            this.remainingTime.seconds = duration.seconds();
            
            const rate = this.targetDate.diff(this.now) / this.targetDate.diff(this.startDate);
            
            this.colorTag = `hsl(0, ${Math.floor(rate)}%, 50%)`;
            console.log( Math.floor(rate));
            console.log(this.colorTag);
        },
        selectTime(){
            this.startDate = moment();
            const newTime = moment(this.timeInput, 'HH:mm:ss');
            // update remaining time
            this.targetDate.hours(newTime.hours());
            this.targetDate.minutes(newTime.minutes());
            this.targetDate.seconds(newTime.seconds());
            // update original difference
            this.origDiff = this.targetDate.diff(this.startDate);
            this.updateTime();
        }
    },
    created() {
        this.updateTime();
        setInterval(() => {
            this.updateTime();
        }, 1000);
    },
    computed: {
        days() {
            return this.remainingTime.days;
        },
        hours() {
            return this.remainingTime.hours;
        },
        minutes() {
            return this.remainingTime.minutes;
        },
        seconds() {
            return this.remainingTime.seconds;
        },
    },
};
</script>
  