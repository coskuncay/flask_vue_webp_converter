import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";

import Vuex from 'vuex'
Vue.use(Vuex)
import 'es6-promise/auto'

Vue.use(VueRouter)

Vue.config.productionTip = false


import 'primevue/resources/themes/bootstrap4-light-purple/theme.css'
import 'primevue/resources/primevue.min.css'
import 'primeicons/primeicons.css'

import Button from 'primevue/button'
import InputText from 'primevue/inputtext';
import AutoComplete from 'primevue/autocomplete';
import Divider from 'primevue/divider';
import Carousel from 'primevue/carousel';
import FileUpload from 'primevue/fileupload';

import router from './router'

Vue.component('FileUpload',FileUpload)
Vue.component('Carousel',Carousel)
Vue.component('Button',Button)
Vue.component('InputText',InputText)
Vue.component('AutoComplete',AutoComplete)
Vue.component('Divider',Divider)

import {store} from "./store"


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
