<template>
	<div>
		<form @submit="joinHome">
			<div class="input-group mb-3">
				<input
					type="text"
					v-model="join"
					name="join"
					class="form-control"
					placeholder="Enter Board Code"
					aria-label="Enter Board Code"
					aria-describedby="basic-addon2"
				/>
				<div class="input-group-append">
					<input
						type="submit"
						value="Join Board"
						class="btn btn-outline-warning"
					/>
				</div>
			</div>
		</form>
		<form @submit="addHome">
			<div class="input-group mb-3">
				<input
					type="text"
					v-model="title"
					name="title"
					class="form-control"
					placeholder="Name your new board..."
					aria-label="Name your new board..."
					aria-describedby="basic-addon2"
				/>
				<div class="input-group-append">
					<input
						type="submit"
						value="Create Board"
						class="btn btn-outline-warning"
					/>
				</div>
			</div>
		</form>
	</div>
</template>

<script>
export default {
	name: "AddHome",
	data() {
		return {
			title: "",
			join:""
		};
	},
	methods: {
		addHome(e) {
			e.preventDefault();

			this.$emit("add-home", this.title);

			this.title = "";
		},

		joinHome(e) {
			e.preventDefault();

			this.$emit("join-home", this.join);

			this.title = "";
		},
	},
};
</script>

<style scoped></style>
