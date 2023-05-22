import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ProfileView from '../views/ProfileView.vue'
import LoginView from '../views/LoginView.vue'
import { isAuthenticated } from '../modules'

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
            if( isAuthenticated()) next("/profile");
            else next()
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
    if (to.meta.requiresAuth && !isAuthenticated() ) {
        return {
            path: '/login',
            query: { redirect: to.fullPath },
        }
    }
})

export default router;