<template>
	<div class="big-wrapper">
		<BoardNav />

		<div class="row home-card">
			<div class="col-sm-3" />
			<div class="col-sm-6">
				<HomeCard />
			</div>
			<div class="col-sm-3" />
		</div>

		<Footer />
	</div>
</template>

<script>
import BoardNav from "@/components/Home/BoardNav.vue";
import HomeCard from "@/components/Home/HomeCard.vue";
import Footer from "@/components/Home/Footer.vue";

export default {
	name: "Home",
	components: { BoardNav, HomeCard, Footer },

	data() {
		return {};
	},
};
</script>

<style scoped>
.home-card {
	margin: 2%;
}
</style>
