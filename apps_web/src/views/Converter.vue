<template>
<div style="padding: 40px;">
    <h3>Convert your image to Webp</h3>
    <hr class="rounded">
    <div class="p-card">
        <div class="p-card-body">
            <div @dragover.prevent="" @dragleave.prevent="" @drop.prevent="onDropUpload">
                <div class="upload-buttonbar">
                    <span class="p-buttonset">
                        <Button label="Convert" icon="pi pi-refresh" :disabled="!file" @click="convertClick" />
                        <Button label="Cancel" icon="pi pi-times" :disabled="!file" @click="cancelClick" />
                    </span>
                </div>
                <label style="width: 100%;">
                    <div class="upload-content" v-show="!file">
                        <p>Drag and drop your image to here to convert.</p>
                    </div>

                    <input v-if="!file" type="file" name="myImage" accept="image/*" @change="onSelectUpload" style="display:none" />
                </label>
            </div>

            <div class="row">
                <div class="col-md-6">
                    <div v-show="file">
                        <h5 v-if="file"> <b>{{this.file.name}}</b> </h5>
                        <img style="width:300px;height:auto" id="blah" src="#" alt="your image" />
                    </div>
                </div>
                <div class="col-md-6">
                    <h5 v-if="readyWebp"><b>Converted file is ready , click on image to download</b></h5>
                    <a v-if="file" id="downloadButton" style="width: 300px;height: auto;"></a>
                </div>
            </div>
        </div>

        <!-- 
        <FileUpload name="demo[]" ref="uploader" :customUpload="true" @uploader="onDropUpload" @clear="onClear" @select="onSelect" :multiple="false" accept="image/*" :previewWidth="150" :fileLimit="1" :maxFileSize="1000000" chooseLabel="Choose" uploadLabel="Convert" cancelLabel="Cancel">
            <template #empty>
                <p>Drag and drop your image to here to convert.</p>
            </template>
        </FileUpload> -->
    </div>
</div>
</template>

<script>
export default {
    mounted() {

    },
    data() {
        return {
            chooseDisabled: false,
            file: null,
            readyWebp: false,
            loading: false,
        }
    },
    methods: {
        convertClick() {
            this.loading = true;
            this.processFile(this.file)
            this.readyWebp = true
        },
        cancelClick() {
            this.file = null
            this.readyWebp = false
        },
        onClear() {
            this.chooseDisabled = false;
        },
        onSelectUpload(event) {
            console.log("on upload", event)
            this.file = event.srcElement.files[0]
            let a = document.getElementById('blah')
            console.log("🚀 ~ file: Converter.vue ~ line 61 ~ onDropUpload ~ a", a)
            a.setAttribute("src", window.URL.createObjectURL(this.file));
        },
        onDropUpload(event) {
            console.log("on upload", event)
            this.file = event.dataTransfer.files[0]
            let a = document.getElementById('blah')
            console.log("🚀 ~ file: Converter.vue ~ line 61 ~ onDropUpload ~ a", a)
            a.setAttribute("src", window.URL.createObjectURL(this.file));
        },
        processFile(file) {
            if (!file) {
                return;
            }
            console.log(file);

            // let imageBox = addImageBox(refs.imagePreviews);

            // Load the data into an image
            new Promise(function (resolve, reject) {
                    let rawImage = new Image();

                    rawImage.addEventListener("load", function () {
                        resolve(rawImage);
                    });

                    rawImage.src = URL.createObjectURL(file);
                })
                .then(function (rawImage) {
                    // Convert image to webp ObjectURL via a canvas blob
                    return new Promise(function (resolve, reject) {
                        let canvas = document.createElement('canvas');
                        let ctx = canvas.getContext("2d");

                        canvas.width = rawImage.width;
                        canvas.height = rawImage.height;
                        ctx.drawImage(rawImage, 0, 0);

                        canvas.toBlob(function (blob) {
                            resolve(URL.createObjectURL(blob));
                        }, "image/webp");
                    });
                })
                .then(function (imageURL) {
                    // Load image for display on the page
                    return new Promise(function (resolve, reject) {
                        let scaledImg = new Image();
                        scaledImg.addEventListener("load", function () {
                            resolve({
                                imageURL,
                                scaledImg
                            });
                        });
                        scaledImg.setAttribute("src", imageURL);
                    });
                })
                .then(function (data) {
                    console.log("🚀 ~ file: Converter.vue ~ line 87 ~ data", data)
                    // Inject into the DOM
                    let imageLink = document.getElementById("downloadButton");

                    imageLink.setAttribute("href", data.imageURL);
                    imageLink.setAttribute('download', `${file.name}.webp`);
                    imageLink.appendChild(data.scaledImg);

                    // imageBox.innerHTML = "";
                    // imageBox.appendChild(imageLink);
                });
            this.loading = false
        }

    },
    watch: {
        chooseDisabled() {}
    }
}
</script>

<style>
.disabled-button {
    display: none !important;
}

#downloadButton>img {
    width: 300px;
    height: auto;
    margin: 0 auto;
}

.upload-buttonbar {
    background: #efefef;
    padding: 1rem 1.25rem;
    border: 1px solid #dee2e6;
    color: #212529;
    border-bottom: 0 none;
    border-top-right-radius: 4px;
    border-top-left-radius: 4px;
    height: 80px;
}

.upload-content {
    background: #ffffff;
    padding: 2rem 1rem;
    border: 1px solid #dee2e6;
    color: #212529;
    border-bottom-right-radius: 4px;
}
</style>
