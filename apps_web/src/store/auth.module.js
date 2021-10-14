import router from "../router"

const user = sessionStorage.getItem('user')

const state = {
    user : user,
}

const getters = {
    isLoggedIn: state => state.user != null ? true : false
}

const actions = {
    login({
        commit
    },user)
    {
        commit('login',user)
        router.push("/").catch(err => console.error(err))
    },
    
    logout({commit}){
        commit("logout")
    }
}

const mutations = {
    login(state,user){
        state.user = user
        sessionStorage.setItem('user',user)
    },
    logout(state){
        sessionStorage.removeItem('user')
        state.user = null
        router.push("/login")
    }
}

export const authmodule = {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}