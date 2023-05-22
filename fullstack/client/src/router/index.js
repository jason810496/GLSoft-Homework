import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ProfileView from '../views/ProfileView.vue'
import LoginView from '../views/LoginView.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: HomeView,
    },
    {
        path: '/login',
        name: 'Login',
        component: LoginView,
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
    if (to.meta.requiresAuth) {
    // this route requires auth, check if logged in
    // if not, redirect to login page.
        return {
            path: '/',
            query: { redirect: to.fullPath },
        }
    }
})

export default router;