import { createRouter, createWebHistory } from 'vue-router'
import { useAngelStore } from '../stores/angel'
import InputView from '../views/InputView.vue'
import WizardLayout from '../views/wizard/WizardLayout.vue'
import DashboardView from '../views/DashboardView.vue'

const routes = [
  {
    path: '/',
    name: 'input',
    component: InputView,
  },
  {
    path: '/wizard',
    name: 'wizard',
    component: WizardLayout,
    meta: { requiresResult: true },
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: DashboardView,
    meta: { requiresResult: true },
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  if (to.meta.requiresResult) {
    // Pinia store must be accessed after app is created, so use a lazy import pattern
    const store = useAngelStore()
    if (!store.result) {
      next('/')
      return
    }
  }
  next()
})

export default router
