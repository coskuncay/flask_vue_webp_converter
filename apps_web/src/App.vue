<template>
<div id="app">
    <div class="header" v-if="onlineUser">
        <router-link to="/">Discover</router-link>
        <b style="color:black">|</b>
        <router-link to="/converter">Converter</router-link>
        <Button style="float:right;margin-right:10px;background-color:white" :label=" getUsername + ' |  Logout'" @click="logoutStore" icon="pi pi-user" />
    </div>
    <div id="nav"></div>
    <router-view />

    <div class="footer">
        <p>© Copyright 2021 JustFun - All Rights Reserved</p>
    </div>
</div>
</template>

<script>
import {
    store
} from '@/store/'

import Swal from 'sweetalert2'

export default {
    mounted() {
        window.addEventListener("storage", function (event) {
            if (event.storageArea == sessionStorage) {
                if (!sessionStorage.getItem("user")) {
                    store.dispatch("authmodule/logout")
                    Swal.fire({
                        icon: 'error',
                        title: 'Oops...',
                        text: 'Login information deleted!'
                    })
                }
            }
        })
    },
    data() {
        return {

        }
    },
    computed: {
        onlineUser() {
            return store.getters["authmodule/isLoggedIn"]
        },
        getUsername(){
            let user = sessionStorage.getItem('user')
            if(user != null){
                return user
            }
            return ""
        }
    },
    methods: {
        logoutStore() {
            store.dispatch("authmodule/logout")
        }
    },
}
</script>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
}

#nav {
    padding: 50px;
}

.header a {
    font-weight: normal;
    color: rgba(212, 211, 211, 0.692);
    text-decoration: none;
    font-size: 18px;
    padding: 10px;
}

.header a:hover {
    font-weight: 500;
    color: rgba(241, 241, 241, 0.692);
}

.header a.router-link-exact-active {
    color: white;
    font-weight: bold;
}

.header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 60px;
    text-align: center;
    padding-top: 10px;
    background-color: #8c239e;
    color: white;
    text-align: center;
}

.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #8c239e;
    color: white;
    text-align: center;
}

.header .p-button-label {
    flex: 1 1 auto;
    color: black;
    font-weight: bold;
}

.header .p-button .p-button-icon-left {
    margin-right: 0.5rem;
    color: black;
    font-weight: bold;
}
</style>
