<template>
  <div>
    <!-- <HomeCard v-bind:boards="boards" /> -->
  </div>
</template>

<script>
import HomeCard from "@/components/Home/HomeCard.vue";
// import axios from 'axios'
// import { store } from "@/store.js";
// import { axiosInstance } from "@/http.js";

export default {
  name: "DisplayHome",
  // components: { HomeCard },

  data() {
    return {
      boards: [],
      error: false,

    };
  },

  methods: {
    // deleteHome(id) {
    // 	axios
    // 		.delete(`https://jsonplaceholder.typicode.com/photos/${id}`)
    // 		.then(() => (this.home = this.home.filter((loop) => loop.id !== id)))
    // 		.catch((err) => console.log(err));
    // },
  },

  created() {

  },
};
</script>

<style scoped></style>
