<template>
	<div class="card">
		<div class="card-header cards-title">
			Links
		</div>
		<div class="card-body scroll">
			<ul class="list-group">
				<div v-bind:key="loop.id" v-for="loop in link">
					<li
						class="list-group-item d-flex justify-content-between align-items-center"
					>
						{{ loop.title }}
						<button
							@click="$emit('del-link', loop.id)"
							type="button"
							class="close"
							aria-label="Close"
						>
							<span aria-hidden="true">&times;</span>
						</button>
					</li>
				</div>
			</ul>
		</div>
		<div class="card-footer text-muted">
			<AddLink v-on:add-link="addLink"></AddLink>
		</div>
	</div>
</template>

<script>
import AddLink from "@/components/Link/AddLink.vue";
import axios from "axios";

export default {
	name: "LinkCard",
	components: {
		AddLink,
	},
	props: ["link"],

	methods: {
		addLink(newLink) {
			const { title } = newLink;

			axios
				.post("https://jsonplaceholder.typicode.com/todos", { title })

				.then((res) => (this.link = [...this.link, res.data]))
				.catch((err) => console.log(err));
		},
	},
};
</script>

<style scoped></style>
