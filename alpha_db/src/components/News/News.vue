<template>
<div class="row">
  <div class="col-4">
    <div class="list-group" id="list-tab" role="tablist">

      <a v-for="news in newsList"
      v-bind:key="news.id"
        class="list-group-item list-group-item-action active"
        id="list-home-list"
        data-toggle="list"
        href="#list-home"
        role="tab"
        aria-controls="home"
        >{{news.content}}</a
      >
      <a
        class="list-group-item list-group-item-action"
        id="list-profile-list"
        data-toggle="list"
        href="#list-profile"
        role="tab"
        aria-controls="profile"
        >Profile</a
      >
      <a
        class="list-group-item list-group-item-action"
        id="list-messages-list"
        data-toggle="list"
        href="#list-messages"
        role="tab"
        aria-controls="messages"
        >Messages</a
      >
      <a
        class="list-group-item list-group-item-action"
        id="list-settings-list"
        data-toggle="list"
        href="#list-settings"
        role="tab"
        aria-controls="settings"
        >Settings</a
      >
    </div>
  </div>
  <div class="col-8">
    <div class="tab-content" id="nav-tabContent">
      <div
        class="tab-pane fade show active"
        id="list-home"
        role="tabpanel"
        aria-labelledby="list-home-list"
      >
        asdjfokakdfjaklsdjflk;asdjfkl;jasdkl;fjaskl;dfjklasdjflkjasdkl;fjaskl;dfjklas;djfkl;asdjfkl;asdjfkl;jasdkl;fjasl;dkfjakl;sdfjkl;asjdfkl;ajs
      </div>
      <div
        class="tab-pane fade"
        id="list-profile"
        role="tabpanel"
        aria-labelledby="list-profile-list"
      >
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
      </div>
      <div
        class="tab-pane fade"
        id="list-messages"
        role="tabpanel"
        aria-labelledby="list-messages-list"
      >
        ...
      </div>
      <div
        class="tab-pane fade"
        id="list-settings"
        role="tabpanel"
        aria-labelledby="list-settings-list"
      >
        ...
      </div>
    </div>
  </div>
</div>
</template>

<script>
// import AddNews from "@/components/News/AddNews.vue";
// import axios from "axios";
import { store } from "@/store.js";
import { axiosInstance } from "@/http.js";
export default {
  name: "DisplayNews",
//   components: { AddNews },

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
