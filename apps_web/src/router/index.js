import Vue from 'vue'
import Router from 'vue-router'
import GameCompare from '../views/GameCompare.vue'
import Converter from '../views/Converter.vue'
import Login from '../views/Login.vue'

import {
  store
} from '@/store/'

Vue.use(Router)

const routes = [{
    path: '/',
    name: 'Discover',
    component: GameCompare,
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/converter',
    name: 'Converter',
    component: Converter,
    meta: {
      requiresLogin: true
    }
  }, {
    path: '/login',
    name: 'Login',
    component: Login
  },
]

const router = new Router({
  mode: 'history',
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(t => t.meta.requiresLogin)) {
    let loginSuccess = sessionStorage.getItem('user') == null ? false : true;
    if (!loginSuccess) {
      next({
        path: '/login'
      })
    } else {
        next()
    }
  }
  else{
    next()
  }
})


export default router