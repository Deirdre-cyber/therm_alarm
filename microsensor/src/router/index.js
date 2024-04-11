import { createRouter, createWebHistory } from 'vue-router'

import HelloWord from '@/components/HelloWorld.vue'
import TempData from '@/views/TempData.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: HelloWord
    },
    {
        path: '/tempdata',
        name: 'TempData',
        component: TempData
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router
