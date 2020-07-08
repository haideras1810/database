<template>
  <!--<div class="login"></div>-->

  <div class="login">
    <div class="sidenav">
      <div class="login-main-text">
        <h2>
          Alpha
        </h2>
        <p>Login to your account.</p>
      </div>
    </div>
    <div class="main">
      <div class="col-md-6 col-sm-12">
        <div class="alert alert-danger" v-if="error" role="alert">
          {{ message }}
        </div>
        <div class="login-form">
          <form>
            <div class="form-group">
              <label>User Name</label>
              <input
                v-model="username"
                type="text"
                class="form-control"
                placeholder="User Name"
              />
            </div>
            <div class="form-group">
              <label>Email</label>
              <input
                v-model="email"
                type="email"
                class="form-control"
                placeholder="email"
              />
            </div>
            <div class="form-group">
              <label>Password</label>
              <input
                v-model="password"
                type="password"
                class="form-control"
                placeholder="Password"
              />
            </div>

            <button
              @click="login"
              type="submit"
              name="submit"
              class="btn btn-black"
            >
              Login
            </button>

            <button @click="register" type="submit" class="btn btn-secondary">
              Register
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { store } from "@/store.js";
import { axiosInstance } from "@/http.js";

import router from "@/router/index.js";
export default {
  name: "login",
  components: {},
  data() {
    return {
      username: "",
      password: "",
      email: "",
      error: false,
      message: "",
    };
  },
  methods: {
    login() {
      axiosInstance
        .post("auth/login", {
          username: this.username,
          password: this.password,
        })
        .then((response) => {
          store.setUser(response.data);
          window.sessionStorage.setItem("authToken", response.data.token);
          router.push({ name: "Home" });
          //console.log(response)
        })
        .catch((e) => {
          this.error = true;
          this.message = e.response.data;
        });
    },

    register() {
      axiosInstance
        .post("auth/register", {
          username: this.username,
          password: this.password,
          email: this.email,
        })
        .then((response) => {
          store.setUser(response.data);
          window.sessionStorage.setItem("authToken", response.data.token);
          router.push({ name: "Home" });
        })
        .catch((e) => {
          this.error = true;
          this.message = e.response.data;
        });
    },
  },
};
</script>

<style scoped>
body {
  font-family: "Lato", sans-serif;
}

.main-head {
  height: 150px;
  background: #fff;
}

.sidenav {
  height: 100%;
  /* background-color: #000; */
  background-image: url("../assets/bulba.jpg");
  background-repeat: no-repeat;
  /* overflow-x: hidden; */
  padding-top: 20px;
}

.main {
  padding: 0px 10px;
}

@media screen and (max-height: 450px) {
  .sidenav {
    padding-top: 15px;
  }
}

@media screen and (max-width: 450px) {
  .login-form {
    margin-top: 10%;
  }

  .register-form {
    margin-top: 10%;
  }
}

@media screen and (min-width: 768px) {
  .main {
    margin-left: 40%;
  }

  .sidenav {
    width: 40%;
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
  }

  .login-form {
    margin-top: 80%;
  }

  .register-form {
    margin-top: 20%;
  }
}

.login-main-text {
  margin-top: 20%;
  padding: 60px;
  color: #fff;
}

.login-main-text h2 {
  font-weight: 300;
}

.btn-black {
  background-color: #000 !important;
  color: #fff;
}
</style>
