<template>
	<div>
		<nav class="navbar navbar-expand-lg py-3 navbar-dark bg-dark shadow-sm">
			<div class="container">
				<a href="#" class="navbar-brand">
					<img
						src="@/assets/logo.png"
						width="45"
						alt=""
						class="d-inline-block align-middle mr-2"
					/>
					<span class="font-weight-light nav-title">Alpha</span>
				</a>

				<button
					type="button"
					data-toggle="collapse"
					data-target="#navbarSupportedContent"
					aria-controls="navbarSupportedContent"
					aria-expanded="false"
					aria-label="Toggle navigation"
					class="navbar-toggler"
				>
					<span class="navbar-toggler-icon"></span>
				</button>

				<div id="navbarSupportedContent" class="collapse navbar-collapse">
					<ul class="navbar-nav ml-auto">
						<li class="nav-item active">
							<a @click = "signOut" to="/" type="submit" name="submit" class="nav-link">
								Log Out
							</a>
						</li>
					</ul>
				</div>
			</div>
		</nav>


	</div>
</template>

<script>
import router from '@/router/index.js'
export default {
	name: "BoardNav",
	components: {},
	methods:{
		signOut(){
			window.sessionStorage.removeItem('authToken')
			router.push({name:"login"})
		}

	}
};
</script>

<style scoped>
.nav-title {
	font-family: Helvetica, sans-serif;
}
</style>
