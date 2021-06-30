import Vue from 'vue'
import VueRouter from 'vue-router' 
import provedor from '@/provedor.js'

Vue.use(VueRouter)

const routes = [
  {
    path: '',
    name: 'home',
    component: () => import ( /*webpackChunkName: Home */
      '../views/Home.vue'),
      meta: {
        publica : true
      }
  },
  {
    path: '/gerentes',
    name: 'gerentes',
    component: () => import ( /*webpackChunkName: Home */
      '../views/Gerentes.vue'),
  },
  {
    path: '/cadastre-se',
    name: 'novo.usuario',
    component: () => import ( /*webpackChunkName: Login */
      '../views/NovoUsuario.vue'),
    meta: {
      publica : true
    }
  },
  {
    path: '/login',
    name: 'login',
    component: () => import ( /*webpackChunkName: Registrar*/
    '../views/Login.vue'),
    meta: {
      publica : true
    }
  }
]

const router = new VueRouter({
  routes
})

router.beforeEach((routeTo, routeFrom, next) => {
  if (!routeTo.meta.publica && !provedor.state.token) {
      return next({ path: '/login' })
  }
  next()
})

export default router