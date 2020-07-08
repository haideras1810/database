<template>
  <div class="card">
    <div class="card-header cards-title">
      News
    </div>
    <div class="card-body scroll">
      <ul class="list-group">
        <div v-bind:key="news.id" v-for="news in newsList">
          <li @click="showComments(news.id)"
            class="list-group-item d-flex justify-content-between align-items-center"
          >
            {{ news.content }}
            <button
              @click="deleteNews(news.id)"
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
    <div class="card-footer text-muted">
      <AddNews v-on:add-news="addNews"></AddNews>
    </div>
  </div>
</template>

<script>
import AddNews from "@/components/News/AddNews.vue";
// import axios from "axios";
import { store } from "@/store.js";
import { axiosInstance } from "@/http.js";
export default {
  name: "DisplayNews",
  components: { AddNews },

  data() {
    return {
      newsList: [],
      storeState: store.state,
    };
  },

  methods: {
    deleteNews(id) {
      let token = "Token " + window.sessionStorage.getItem("authToken");
      axiosInstance
        .delete(`boards/${this.storeState.board.id}/news/${id}`, {
          headers: {
            Authorization: token,
          },
        })
        .then(
          (this.newsList = this.newsList.filter(function(item) {
            return item.id != id;
          }))
        )
        .catch((e) => console.log(e));
    },
    addNews(newsContent) {
      console.log("yolo");
      let token = "Token " + window.sessionStorage.getItem("authToken");
      axiosInstance
        .post(
          `boards/${this.storeState.board.id}/news`,
          {
            content: newsContent,
          },
          {
            headers: {
              Authorization: token,
            },
          }
        )
        .then((response) => this.newsList.push(response.data))
        .catch((e) => console.log(e.response));
    },
  },

  created() {
    let token = "Token " + window.sessionStorage.getItem("authToken");
    axiosInstance
      .get(`boards/${this.storeState.board.id}/news`, {
        headers: {
          Authorization: token,
        },
      })
      .then((response) => (this.newsList = response.data))
      .catch((e) => console.log(e));
  },
};
</script>

<style scoped></style>
