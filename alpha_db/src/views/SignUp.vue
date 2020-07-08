<template>
	<div class="signup">
		<div class="sidenav">
			<div class="login-main-text">
				<h2>
					Alpha
				</h2>
				<p>Create your account.</p>
			</div>
		</div>
		<div class="main">
			<div class="col-md-6 col-sm-12">
				<div class="login-form">
					<form>
						<div class="form-group">
							<label>User Name</label>
							<input type="text" class="form-control" placeholder="User Name" />
						</div>
						<div class="form-group">
							<label>Password</label>
							<input
								type="password"
								class="form-control"
								placeholder="Password"
							/>
						</div>

						<!-- <router-link
							to="/Home"
							type="submit"
							name="submit"
							class="btn btn-black"
						>
							Login
						</router-link> -->

						<router-link to="/SignUp">
							<button type="submit" class="btn btn-secondary">Register</button>
						</router-link>
					</form>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {};
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
	background-color: #000;
	overflow-x: hidden;
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
