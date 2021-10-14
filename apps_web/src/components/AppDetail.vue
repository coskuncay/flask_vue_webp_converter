<template>
<div class="p-card mt-3" style="box-shadow: 0 2px 2px 2px rgb(0 0 0 / 20%), 0 1px 1px 0 rgb(0 0 0 / 14%), 0 1px 3px 0 rgb(0 0 0 / 12%);">
    <div class="p-card-body">
        <div class="row">
            <div class="col-md-3">
                <img :src="getAppIcon(app.icon)" style="width:150px;border-radius: 20%;border:2px solid black" />
            </div>
            <div class="col-md-9">
                <ul class="app">
                    <li>
                        <span class="app-name">{{app.name}}</span>
                    </li>
                    <li>
                        <p class="detail-1">The most funny word game.</p>
                    </li>
                    <li>
                        <p class="detail-2">JUSTFUN TEKNOLOJI ANONIM SIRKETI</p>
                    </li>
                    <li>
                        <i class="pi pi-star" style="color:orange"></i>
                        <i class="pi pi-star" style="color:orange"></i>
                        <i class="pi pi-star" style="color:orange"></i>
                        <i class="pi pi-star" style="color:orange"></i>
                        <i class="pi pi-star-o"></i>
                        <span class="detail-3"><b>4.0</b> • 89 Ratings</span>
                    </li>
                    <li>
                        <p class="detail-5">Published at <i>{{getCreateDate}}</i></p>
                    </li>
                    <li>
                        <p class="detail-4">Free - Offers In-App Purchases</p>
                    </li>
                    
                </ul>
            </div>
        </div>
        <hr class="rounded">
        <div class="row mt-2">
            <span class="ss-header">Screenshots</span>
            <Carousel :value="getAppImages" :numVisible="3" :numScroll="1" :responsiveOptions="responsiveOptions" class="custom-carousel" :circular="true" :autoplayInterval="3000">
                <template #item="slotProps">
                    <div class="product-item">
                        <div class="product-item-content">
                            <div class="p-mb-3">
                                <img :src="getAppScreenshots(slotProps.data.file_name)" :alt="slotProps.data.id" style="height:300px;width: 100%; display: block;" />
                            </div>
                        </div>
                    </div>
                </template>
            </Carousel>
        </div>
    </div>
</div>
</template>

<script>
import moment from 'moment'
import axios from 'axios'
export default {
    props: {
        app: Object
    },
    mounted() {
        axios.get('http://127.0.0.1:5000/api/screenshots').then(res => {
            this.allImages = res.data.data
        })
    },
    data() {
        return {
            allImages: [],
            responsiveOptions: [{
                    breakpoint: '1024px',
                    numVisible: 5
                },
                {
                    breakpoint: '768px',
                    numVisible: 3
                },
                {
                    breakpoint: '560px',
                    numVisible: 1
                }
            ]
        }
    },
    computed: {
        getAppImages() {
            return this.allImages.filter(i => i.app_id == this.app.id)
        },
        getCreateDate() {
            return moment(this.app.created_at).format('DD MMMM YYYY')
        }
    },
    methods: {
        getAppIcon(icon) {
            return require(`../assets/icons/${icon}`)
        },
        getAppScreenshots(ss) {
            return require(`../assets/ss/${ss}`)
        },
    }
}
</script>

<style>
.app-name {
    font-weight: bold;
    font-size: 20px;
}

.ss-header {
    text-align: start;
    font-weight: bold;
    font-size: 20px;
    margin-left: 10px;
}

/* Rounded border */
hr.rounded {
    border-top: 3px solid black;
    border-radius: 5px;
    margin-top: 25px;
    margin-bottom: 25px;
}

ul.app {
    text-align: start;
    list-style-type: none;
    margin: 0;
    margin-left: 20px;
    padding: 0;
}

.detail-1 {
    color: grey;
    font-size: medium;
    margin-bottom: 0;
}

.detail-2 {
    color: cornflowerblue;
    font-size: medium;

    margin-bottom: 0;
}

.detail-3 {
    color: grey;
    font-size: medium;
    margin-left: 15px;
    margin-bottom: 0;
}

.detail-4 {
    font-size: 12px;
    color: grey;
    font-style: italic;
    margin-top: 5px;
    margin-bottom: 0;
}

.detail-5 {
    font-size: 12px;
    color: rgb(98, 98, 98);
    margin-top: 5px;
    margin-bottom: 0;
}

.product-item .product-item-content {

    border: 1px solid var(--surface-d);
    border-radius: 3px;
    margin: .3rem;
    text-align: center;
}

.product-item .product-image {
    width: 50%;
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23)
}
</style>
