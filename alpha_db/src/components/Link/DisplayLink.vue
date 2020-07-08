<template>
  <div class="card">
    <div class="card-header cards-title">
      Links
    </div>
    <div class="card-body scroll">
      <ul class="list-group">
        <li v-bind:key="link.id" v-for="link in links" class="list-group-item link">


              <a :href="link.src">{{ link.src }}</a>


            <button
              @click="deleteLink(link.id)"
              type="button"
              class="close"
              aria-label="Close"
            >
              <span aria-hidden="true">&times;</span>
            </button>

        </li>
      </ul>
    </div>
    <div class="card-footer text-muted">
      <AddLink v-on:add-link="addLink"></AddLink>
    </div>
  </div>
</template>

<script>
import AddLink from "@/components/Link/AddLink.vue";

import { store } from "@/store.js";
import { axiosInstance } from "@/http.js";
export default {
  name: "DisplayLink",
  components: { AddLink },

  data() {
    return {
      links: [],
      storeState: store.state,
    };
  },
  watch: {
    storeState: function() {
      this.getLinks();
    },
  },

  methods: {
    deleteLink(id) {
      let token = "Token " + window.sessionStorage.getItem("authToken");
      axiosInstance
        .delete(`boards/${this.storeState.board.id}/links/${id}`, {
          headers: {
            Authorization: token,
          },
        })
        .then(
          (this.links = this.links.filter(function(item) {
            return item.id != id;
          }))
        )
        .catch((e) => console.log(e));
    },
    addLink(newSrc) {
      let token = "Token " + window.sessionStorage.getItem("authToken");
      axiosInstance
        .post(
          `boards/${this.storeState.board.id}/links`,
          {
            src: newSrc,
          },
          {
            headers: {
              Authorization: token,
            },
          }
        )
        .then((response) => this.links.push(response.data))
        .catch((e) => console.log(e.response));
    },
    getLinks() {
      let token = "Token " + window.sessionStorage.getItem("authToken");
      axiosInstance
        .get(`boards/${this.storeState.board.id}/links`, {
          headers: {
            Authorization: token,
          },
        })
        .then((response) => (this.links = response.data))
        .catch((e) => console.log(e));
    },
  },

  created() {
    let token = "Token " + window.sessionStorage.getItem("authToken");
    axiosInstance
      .get(`boards/${this.storeState.board.id}/links`, {
        headers: {
          Authorization: token,
        },
      })
      .then((response) => (this.links = response.data))
      .catch((e) => console.log(e));
  },
};
</script>

<style scoped>

</style>
