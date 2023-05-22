import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ProfileView from '../views/ProfileView.vue'
import LoginView from '../views/LoginView.vue'
import axios from 'axios';

const routes = [
    {
        path: '/',
        name: 'Home',
        component: HomeView,
        meta: { requiresAuth: false },
    },
    {
        path: '/login',
        name: 'Login',
        component: LoginView,
        meta: { requiresAuth: false },
        beforeEnter: (to, from, next ) => {
            const token = localStorage.getItem('access_token');
            axios.get('http://localhost:5001/verify',
            {
                headers: { "Authorization": `Bearer ${token}` , "Accept": 'application/json' , "Access-Control-Allow-Origin": '*' }
            }).then((response) => {
                console.log(response);
                if (response.status === 200){
                    next('/profile');
                }
            }).catch((err) => {
                console.log(err);
            });
        }
    },
    {
        path: '/profile',
        name: 'Profile',
        component: ProfileView,
        meta: { requiresAuth: true },
    },
]

const router = createRouter({
    history: createWebHashHistory(),
    routes, // short for `routes: routes`
})

router.beforeEach((to, from) => {
// instead of having to check every route record with
// to.matched.some(record => record.meta.requiresAuth)
    if (to.meta.requiresAuth ) {
        const token = localStorage.getItem('access_token');
        axios.get('http://localhost:5001/verify',
        {
            headers: { "Authorization": `Bearer ${token}` , "Accept": 'application/json' , "Access-Control-Allow-Origin": '*' }
        }).then((response) => {
            console.log(response);
        }).catch((err) => {
            console.log(err);
            this.$router.push('/login');
        });
    }
})

export default router;