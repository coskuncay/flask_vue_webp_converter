<template>
<div class="container">
    <h3>Discover and Compare Apps</h3>
    <hr class="rounded" style="    margin-top: 8px;">
    <div class="row">
        <div class="col col-md-6">
            <span class="p-fluid">
                <AutoComplete v-model="selectedApp" :suggestions="filteredApps" placeholder="Search app name" @complete="searchApp($event)" :dropdown="true" field="name" forceSelection>
                    <template #item="slotProps">
                        <div class="row">
                            <div class="col-md-12">
                                <img :src="getAppIcon(slotProps.item.icon)" style="width:50px;border-radius: 50%;" />
                            </div>
                            <div class="col-md-12">
                                <b>{{slotProps.item.name}}</b>
                            </div>
                            <Divider />
                        </div>
                    </template>
                </AutoComplete>
            </span>
        </div>
        <div class="col col-md-6" style="text-align: end;">
            <Button :disabled="!selectedApp" label="Randomize" @click="getRandomApp" />
        </div>
    </div>
    <div class="row">
        <div class="col-md-6">
            <AppDetail v-if="selectedApp" :app="selectedApp" />
        </div>
        <div class="col-md-6">
            <AppDetail v-if="otherSelectedApp" :app="otherSelectedApp" />
        </div>
    </div>
</div>
</template>

<script>
// import appService from '@/services/AppService';
import AppDetail from '@/components/AppDetail.vue'
import axios from "axios";

import Swal from "sweetalert2"

export default {
    components: {
        AppDetail
    },
    data() {
        return {
            selectedApp: null,
            otherSelectedApp: null,
            filteredApps: [],
            apps: [],
            otherApps: []
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:5000/api/apps').then(res => {
            this.apps = res.data.data
        })
    },
    methods: {
        searchApp(event) {
            if (!event.query.trim().length) {
                this.filteredApps = [...this.apps];
            } else {
                this.filteredApps = this.apps.filter((game) => {
                    return game.name.toLowerCase().startsWith(event.query.toLowerCase());
                });
            }
        },
        getAppIcon(icon) {
            return require(`../assets/icons/${icon}`)
        },
        getRandomApp() {
            if (!this.otherSelectedApp) {
                let randomIndex = Math.floor(Math.random() * this.otherApps.length)
                this.otherSelectedApp = this.otherApps[randomIndex]
            } else {
                if (this.otherApps.length == 1) {
                    Swal.fire({
                        title: "No more avaliable apps to show!",
                        text: "Please change the selected app."
                    })
                } else {
                    this.otherApps = this.otherApps.filter(t => t.id != this.otherSelectedApp.id)
                    let randomIndex = Math.floor(Math.random() * this.otherApps.length)
                    this.otherSelectedApp = this.otherApps[randomIndex]
                }
            }
        }
    },
    watch: {
        selectedApp(newVal, oldVal) {
            console.log("🚀 ~ file: GameCompare.vue ~ line 94 ~ selectedApp ~ newVal, oldVal", newVal, oldVal)
            if (oldVal) {
                if (newVal.id == oldVal.id) {
                    Swal.fire({
                        title: "Please select different app :)",
                    })
                }
            }
            this.otherApps = this.apps.filter(g => g.id != this.selectedApp.id)
            this.otherSelectedApp = null
        }
    }
}
</script>

<style>
.p-autocomplete-panel .p-autocomplete-items .p-autocomplete-item {
    margin: 0;
    /* padding: 0.5rem 1rem; */
    border: 0 none;
    color: #495057;
    background: transparent;
    transition: box-shadow 0.2s;
    border-radius: 0;
}
</style>
