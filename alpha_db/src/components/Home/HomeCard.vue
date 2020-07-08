<template>
  <div>
    <div class="card">
      <div class="card-header">
        Boards
      </div>
      <div class="card-body scroll">
        <ul class="list-group">
          <div v-bind:key="board.id" v-for="(board, index) in boards">
            <li
              class="list-group-item d-flex justify-content-between align-items-center"
            >
              {{ board.title }}
              <button
                @click="viewBoard(index)"
                to="/board"
                type="submit"
                name="submit"
                class="btn btn-outline-dark btn-md align-self-center"
              >
                Open Board
              </button>
            </li>
          </div>
        </ul>
      </div>
      <div class="card-footer">
        <div class="alert alert-danger" v-if="error" role="alert">
          {{message}}
        </div>
        <AddHome v-on:add-home="addHome" v-on:join-home="joinHome"></AddHome>
      </div>
    </div>
  </div>
</template>

<script>
import AddHome from "@/components/Home/AddHome.vue";
import { axiosInstance } from "@/http.js";
import { store } from "@/store.js";
import router from "@/router/index.js";
export default {
  name: "HomeCard",
  components: {
    AddHome,
  },
  // props: ["boards"],\
  data() {
    return {
      boards: [],
      error: false,
      message: "",
    };
  },
  methods: {
    viewBoard(index) {
      store.setBoard(this.boards[index]);
      router.push({ path: `board/${this.boards[index].id}` });
    },

    addHome(title) {
      axiosInstance
        .post(
          "boards/",
          { title },
          {
            headers: {
              Authorization:
                "Token " + window.sessionStorage.getItem("authToken"),
            },
          }
        )

        .then((response) => this.boards.push(response.data))
        .catch((err) => console.log(err));
    },
    joinHome(id) {
      axiosInstance
        .get(
          `boards/${id}/join`,

          {
            headers: {
              Authorization:
                "Token " + window.sessionStorage.getItem("authToken"),
            },
          }
        )

        .then((response) => this.boards.push(response.data))
        .catch((err) => {
          this.error = true;
          this.message = err.response.data;
        });
    },
  },
  created() {
    if (store.state.auth.token) {
      let token = "Token " + store.state.auth.token;
      axiosInstance
        .get("boards/", {
          headers: {
            Authorization: token,
          },
        })
        .then((response) => {
          this.boards = response.data;
        })
        .catch((e) => console.log(e));
    } else {
      console.log("yolo");
    }
  },
};
</script>

<style scoped></style>
