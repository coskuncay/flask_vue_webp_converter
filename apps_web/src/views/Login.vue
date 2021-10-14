<template>
<div>
    <div class="header">
        <h3><b>Login Page</b></h3>
    </div>
    <div class="p-field p-grid mt-3">
        <img src="@/assets/person.png" style="width: 150px;height: auto;" /><br>
        <label class="p-col-fixed mt-5" style="width:100px">Username</label>
        <div class="p-col">
            <InputText v-model="username" type="text" />
        </div>
    </div>
    <div class="p-field p-grid mt-3">
        <label class="p-col-fixed" style="width:100px">Password</label>
        <div class="p-col">
            <InputText v-model="password" type="password" />
        </div>
    </div>
    <div class="p-field p-grid mt-3">
        <Button v-if="isLoginState" class="mt-4" style="width:200px" type="button" label="Login" @click="tryLogin" :disabled="username.length == 0 || password.length == 0" />
        <div v-else>
            <label class="p-col-fixed" style="width:100px">Re-Password</label>
            <div class="p-col">
                <InputText v-model="rePassword" type="password" />
            </div>
        </div>
    </div>
    <Button class="mt-4" style="width:200px" type="button" label="Sign Up" @click="signUp()" :disabled="!isLoginState && (rePassword === '' || password === '' || username === '')" />
    <br>
    <Button v-if="!isLoginState" class="mt-4" style="width:200px" type="button" label="Back" @click="function () {isLoginState = true}" />
</div>
</template>

<script>
import {
    store
} from '@/store/'

import Swal from "sweetalert2"
import axios from 'axios'
export default {
    name: "Login",
    data() {
        return {
            username: "",
            password: "",
            rePassword: "",
            isLoginState: true,
        }
    },
    methods: {
        backClick() {
            this.isLoginState = true
        },
        tryLogin() {
            axios.post('http://127.0.0.1:5000/login', {
                username: this.username,
                password: this.password
            }).then(res => {
                if (!res.data.success) {
                    const Toast = Swal.mixin({
                        toast: true,
                        position: 'center-center',
                        showConfirmButton: false,
                        timer: 3000,
                        timerProgressBar: true,
                        didOpen: (toast) => {
                            toast.addEventListener('mouseenter', Swal.stopTimer)
                            toast.addEventListener('mouseleave', Swal.resumeTimer)
                        }
                    })
                    Toast.fire({
                        icon: 'error',
                        title: `${res.data.msg}`
                    })
                } else {
                    store.dispatch('authmodule/login', this.username)
                    const Toast = Swal.mixin({
                        toast: true,
                        position: 'center-center',
                        showConfirmButton: false,
                        timer: 1500,
                        timerProgressBar: true,

                    })

                    Toast.fire({
                        icon: 'success',
                        title: 'Logged in successfully'
                    })
                }
            }).catch(err => {
                console.log(err)
            });
        },
        signUp() {

            if (!this.isLoginState) {
                if (this.password !== this.rePassword) {
                    const Toast = Swal.mixin({
                        toast: true,
                        position: 'center-center',
                        showConfirmButton: false,
                        timer: 2000,
                        timerProgressBar: true,
                        didOpen: (toast) => {
                            toast.addEventListener('mouseenter', Swal.stopTimer)
                            toast.addEventListener('mouseleave', Swal.resumeTimer)
                        }
                    })
                    Toast.fire({
                        icon: 'error',
                        title: `Passwords not match`
                    })
                } else {
                    axios.post('http://127.0.0.1:5000/register', {
                        username: this.username,
                        password: this.password
                    }).then(res => {
                        if (res.data.success) {
                            const Toast = Swal.mixin({
                                toast: true,
                                position: 'center-center',
                                showConfirmButton: false,
                                timer: 1500,
                                timerProgressBar: true,

                            })
                            Toast.fire({
                                icon: 'success',
                                title: `${res.data.msg}`
                            })
                            this.isLoginState = !this.isLoginState
                            this.rePassword = ""
                        } else {
                            const Toast = Swal.mixin({
                                toast: true,
                                position: 'center-center',
                                showConfirmButton: false,
                                timer: 3000,
                                timerProgressBar: true,
                                didOpen: (toast) => {
                                    toast.addEventListener('mouseenter', Swal.stopTimer)
                                    toast.addEventListener('mouseleave', Swal.resumeTimer)
                                }
                            })
                            Toast.fire({
                                icon: 'error',
                                title: `${res.data.msg}`
                            })
                        }
                    }).catch(err => {
                        const Toast = Swal.mixin({
                            toast: true,
                            position: 'center-center',
                            showConfirmButton: false,
                            timer: 3000,
                            timerProgressBar: true,
                            didOpen: (toast) => {
                                toast.addEventListener('mouseenter', Swal.stopTimer)
                                toast.addEventListener('mouseleave', Swal.resumeTimer)
                            }
                        })
                        Toast.fire({
                            icon: 'error',
                            title: `Error`
                        })
                    })
                }
            } else {
                this.isLoginState = !this.isLoginState
            }

        }
    },
}
</script>

<style>
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
</style>
