<template>

  <div class="big-wrapper h-100">
    <BoardNav></BoardNav>

    <div class="container wrapper-card">
      <div class="row">
        <div class="card-deck">
          <DisplayNews />
          <DisplayImage />
          <DisplayDocs />
          <DisplayLink />
          <!-- <div class="card h-100 w-100 wrapper-card">
            <DisplayNews />
          </div>

          <div class="card h-100 w-100 wrapper-card"><DisplayLink /></div>

          <div class="card h-100 w-100 wrapper-card">
            <DisplayImage />
          </div>
          <div class="card h-100 w-100 wrapper-card">
            <DisplayDocs />
          </div> -->
        </div>
      </div>

      <!-- <div class="row">
        <div class="card-deck">
          <div class="card wrapper-card">
            <DisplayDocs />
          </div>

          <div class="card wrapper-card">
            <DisplayNews />
          </div>

          <div class="card wrapper-card">
            <DisplayLink />
          </div>
        </div>
      </div> -->
    </div>
  </div>



</template>

<script>
import BoardNav from "@/components/BoardNav.vue";
import DisplayNews from "@/components/News/DisplayNews.vue";
import DisplayLink from "@/components/Link/DisplayLink.vue";
import DisplayImage from "@/components/Image/DisplayImage.vue";
import DisplayDocs from "@/components/Docs/DisplayDocs.vue";

//import CreatePoll from "@/components/Poll/CreatePoll.vue";
//import ViewPoll from "@/components/Poll/ViewPoll.vue";
//import axios from "axios";
import { store } from "@/store.js";
import { axiosInstance } from "@/http.js";
export default {
  name: "Board",
  components: {
    BoardNav,
    DisplayNews,
    DisplayLink,
    DisplayImage,
    DisplayDocs,

    //CreatePoll,
  },

  data() {
    return {};
  },
  created() {
    axiosInstance
      .get(`boards/${this.$route.params.id}/`, {
        headers: {
          Authorization: "Token " + window.sessionStorage.getItem("authToken"),
        },
      })
      .then((response) => {
        store.state.board = response.data;
        console.log(store.state.board);
      });
  },
};
</script>

<style >
.link {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.big-wrapper {
  background-color: seagreen;

}

.cards-title {
  font-family: Impact, Haettenschweiler, "Arial Narrow Bold", sans-serif;
}

.wrapper-card {
   margin-top:20px;
  margin-bottom:20px;
  /* height: 500px; */
  border-color: transparent;
  background-color: seagreen;
}

.scroll {
  height: 200px;
  overflow-y: auto;
}
</style>
