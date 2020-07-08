<template>
  <div>
    <!-- <input type="file" @change="onFileChanged" />
		<button @click="onUpload" class="btn btn-primary">+</button> -->

    <button
      type="button"
      class="btn btn-outline-success btn-lg btn-block"
      data-toggle="modal"
      data-target="#imageModal"
    >
      Upload new image
    </button>

    <div
      class="modal fade"
      id="imageModal"
      tabindex="-1"
      role="dialog"
      aria-labelledby="imageModal"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Upload new image</h5>
            <button
              type="button"
              class="close"
              data-dismiss="modal"
              aria-label="Close"
            >
              <span aria-hidden="true">&times;</span>
            </button>
          </div>

          <form @submit="addImage" enctype="multipart/form-data">
            <div class="modal-body">
              <input type="file" ref="file" @change="onFileChanged" />
            </div>

            <div class="modal-footer">
              <button @click="addImage" class="btn btn-outline-success">
                Done
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import { axiosInstance } from "@/http.js";
// import { store } from "@/store.js";
export default {
  name: "AddImage",
  data() {
    return {
      file: null,
    };
  },
  methods: {
    addImage(e) {
      e.preventDefault();
    //   let formData = new FormData();

    //   /*
    //             Add the form data we need to submit
    //         */
    //   formData.append("src", this.file);
    //   let token = "Token " + window.sessionStorage.getItem("authToken");
    //   axiosInstance
    //     .post(
    //       `boards/${store.state.board.id}/images`,
    //       formData,
    //       {
    //         headers: {
    //           Authorization: token,
    //           "Content-Type":
    //             "multipart/form-data;  boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    //         },
    //       }
    //     )
    //     .then((response) => {
    //       this.images.push(response.data);
    //     })
    //     .catch((e) => console.log(e));
        this.$emit("add-image", this.file);
    },

    onFileChanged() {
      this.file = this.$refs.file.files[0];
    },

    // onUpload() {
    // 	const formData = new FormData();
    // 	formData.append("myFile", this.selectedFile, this.selectedFile.name);
    // 	axios.post("my-domain.com/file-upload", formData);
    // },
  },
};
</script>

<style scoped></style>
