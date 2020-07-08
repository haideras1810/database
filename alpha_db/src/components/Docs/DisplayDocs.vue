<template>
  <div class="card">
    <div class="card-header cards-title">
      Documents
    </div>
    <div class="card-body scroll">
      <ul class="list-group">
        <div v-bind:key="doc.id" v-for="doc in docs">
          <li
            class="list-group-item d-flex justify-content-between align-items-center"
          >
            <a class="link" :href="doc.src" >{{doc.title}}</a>
            <button
              @click="deleteDocument(doc.id)"
              type="button"
              class="close"
              aria-label="Close"
            >
              <span aria-hidden="true">&times;</span>
            </button>
          </li>
        </div>
      </ul>
    </div>
    <div class="card-footer image-footer text-muted">
      <AddDoc v-on:add-doc="addDocument"></AddDoc>
    </div>
  </div>
  <!-- <div>
		<ImageCard v-bind:images="images" v-on:del-image="deleteImage" />
	</div> -->
</template>

<script>
import AddDoc from "@/components/Docs/AddDocs.vue";
// import axios from "axios";
import { store } from "@/store.js";
import { axiosInstance } from "@/http.js";
export default {
  name: "DisplayDoc",
  components: { AddDoc },

  data() {
    return {
      docs: [],
      storeState: store.state,
    };
  },

  methods: {
    deleteDocument(id) {
      let token = "Token " + this.storeState.auth.token;
      axiosInstance
        .delete(`boards/${this.storeState.board.id}/docs/${id}`, {
          headers: {
            Authorization: token,
          },
        })
        .then(
          (this.docs = this.docs.filter(function(item) {
            return item.id != id;
          }))
        )
        .catch((e) => console.log(e));
    },
    addDocument(doc, title) {
      let token = "Token " + window.sessionStorage.getItem("authToken");
      let formData = new FormData();

      /*
                Add the form data we need to submit
            */
      formData.append("src", doc);
      formData.append("title", title);
      axiosInstance
        .post(`boards/${this.storeState.board.id}/docs`, formData, {
          headers: {
            Authorization: token,
            "Content-Type":
              "multipart/form-data;  boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
          },
        })
        .then((response) => {
          this.docs.push(response.data);
        })
        .catch((e) => console.log(e));
    },
  },

  created() {
    let token = "Token " + window.sessionStorage.getItem("authToken");
    axiosInstance
      .get(`boards/${this.storeState.board.id}/docs`, {
        headers: {
          Authorization: token,
        },
      })
      .then((response) => (this.docs = response.data))
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
