<template>
  <div class="card">
    <div class="card-header cards-title">
      Images
    </div>
    <div class="card-body scroll">
      <ul class="list-group">
        <li v-bind:key="image.id" v-for="image in images" class="list-group-item">
          <a target="_blank" :href="image.src" >
            <img class="img-size" :src="image.src" />

          </a>
          <button
              @click="deleteImage(image.id)"
              type="button"
              class="close"
              aria-label="Close"
            >
              <span aria-hidden="true">&times;</span>
          </button>

        </li>
      </ul>
    </div>
    <div class="card-footer image-footer text-muted">
      <AddImage v-on:add-image="addImage"></AddImage>
    </div>
  </div>

</template>

<script>
import AddImage from "@/components/Image/AddImage.vue";
// import axios from "axios";
import { store } from "@/store.js";
import { axiosInstance } from "@/http.js";
export default {
  name: "DisplayImage",
  components: { AddImage },

  data() {
    return {
      images: [],
      storeState: store.state,
    };
  },

  methods: {
    deleteImage(id) {
      let token = "Token " + this.storeState.auth.token;
      axiosInstance
        .delete(`boards/${this.storeState.board.id}/images/${id}`, {
          headers: {
            Authorization: token,
          },
        })
        .then(
          (this.images = this.images.filter(function(item) {
            return item.id != id;
          }))
        )
        .catch((e) => console.log(e));
    },
    addImage(image) {
      let token = "Token " + window.sessionStorage.getItem("authToken");
      let formData = new FormData();

      /*
                Add the form data we need to submit
            */
      formData.append("src", image);
      axiosInstance
        .post(
          `boards/${this.storeState.board.id}/images`,
          formData,
          {
            headers: {
              Authorization: token,
              'Content-Type': 'multipart/form-data;  boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW'
            },
          }
        )
        .then((response) => {
          this.images.push(response.data);
        }).catch(e=>console.log(e));
    },
  },

  created() {
    let token = "Token " + this.storeState.auth.token;
    axiosInstance
      .get(`boards/${this.storeState.board.id}/images`, {
        headers: {
          Authorization: token,
        },
      })
      .then((response) => (this.images = response.data))
      .catch((e) => console.log(e));
  },
};
</script>

<style scoped>
.img-size {
  max-width: 150px;
  max-height: 150px;
}
</style>
