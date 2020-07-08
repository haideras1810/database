<template>
  <div>
    <!-- <input type="file" @change="onFileChanged" />
		<button @click="onUpload" class="btn btn-primary">+</button> -->

    <button
      type="button"
      class="btn btn-outline-success btn-lg btn-block"
      data-toggle="modal"
      data-target="#documentModal"
    >
      Upload a doc
    </button>

    <div
      class="modal fade"
      id="documentModal"
      tabindex="-1"
      role="dialog"
      aria-labelledby="documentModal"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Upload new document</h5>
            <button
              type="button"
              class="close"
              data-dismiss="modal"
              aria-label="Close"
            >
              <span aria-hidden="true">&times;</span>
            </button>
          </div>

          <form @submit="addDoc" enctype="multipart/form-data">
            <div class="modal-body">
              <input
                type="url"
                required
                v-model="title"
                name="title"
                class="form-control"
                placeholder="Enter a title"
                aria-label="Enter URL"
                aria-describedby="basic-addon2"
              />
              <div class="form-group">
                <input
                  class="form-control-file"
                  type="file"
                  ref="file"
                  @change="onFileChanged"
                />
              </div>
            </div>

            <div class="modal-footer">
              <button @click="addDoc" class="btn btn-outline-success">
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
  name: "AddDoc",
  data() {
    return {
      file: null,
      title: "",
    };
  },
  methods: {
    addDoc(e) {
      e.preventDefault();

      this.$emit("add-doc", this.file, this.title);
      this.title = "";
    },

    onFileChanged() {
      this.file = this.$refs.file.files[0];
    },
  },
};
</script>

<style scoped></style>
