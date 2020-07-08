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
							<router-link
								to="/Home"
								type="submit"
								name="submit"
								class="nav-link"
							>
								Home
							</router-link>
						</li>
					</ul>
				</div>
			</div>
		</nav>

		<!-- <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
			<a class="navbar-brand" href="#">Alpha</a>
			<button
				class="navbar-toggler"
				type="button"
				data-toggle="collapse"
				data-target="#navbarText"
				aria-controls="navbarText"
				aria-expanded="false"
				aria-label="Toggle navigation"
			>
				<span class="navbar-toggler-icon"></span>
			</button>
			<div class="collapse navbar-collapse" id="navbarText">
				<ul class="navbar-nav mr-auto">
					<li class="nav-item active">
						<a class="nav-link" href="#"
							>Home <span class="sr-only">(current)</span></a
						>
					</li>
					<li class="nav-item">
						<a class="nav-link" href="#">Features</a>
					</li>
					<li class="nav-item">
						<a class="nav-link" href="#">Pricing</a>
					</li>
				</ul>
				<span class="navbar-text">
					This is a board.
				</span>
			</div>
		</nav> -->
	</div>
</template>

<script>
export default {
	name: "BoardNav",
	components: {},
};
</script>

<style scoped>
.nav-title {
	font-family: Helvetica, sans-serif;
}
</style>
