<template>
	<div>
		<button
			type="button"
			class="btn btn-outline-success btn-lg btn-block"
			data-toggle="modal"
			data-target="#linkModal"
		>
			Add a new link
		</button>

		<div
			class="modal fade"
			id="linkModal"
			tabindex="-1"
			role="dialog"
			aria-labelledby="linkModal"
			aria-hidden="true"
		>
			<div class="modal-dialog modal-dialog-centered" role="document">
				<div class="modal-content">
					<div class="modal-header">
						<h5 class="modal-title">Add a new link</h5>
						<button
							type="button"
							class="close"
							data-dismiss="modal"
							aria-label="Close"
						>
							<span aria-hidden="true">&times;</span>
						</button>
					</div>

					<form @submit="addLink">
						<div class="modal-body">
							<input
								type="url"
								required
								v-model="src"
								name="title"
								class="form-control"
								placeholder="Enter URL"
								aria-label="Enter URL"
								aria-describedby="basic-addon2"
							/>
						</div>
						<div class="modal-footer">
							<input
								type="submit"
								value="Done"
								class="btn btn-outline-success btn-lg"
							/>
						</div>
					</form>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: "AddLink",
	data() {
		return {
			src: "",
		};
	},
	methods: {
		addLink(e) {
			e.preventDefault();

			this.$emit("add-link", this.src);

			this.src = "";
		},
	},
};
</script>

<style scoped></style>
