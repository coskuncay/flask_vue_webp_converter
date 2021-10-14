import Vue from 'vue'
import Vuex from 'vuex'

import {authmodule} from './auth.module'

Vue.use(Vuex)

export const store = new Vuex.Store({
    modules:{
        authmodule
    }
});