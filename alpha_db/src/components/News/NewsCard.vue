<template>
	<div class="card">
		<div class="card-header cards-title">
			News
		</div>
		<div class="card-body scroll">
			<ul class="list-group">
				<div v-bind:key="loop.id" v-for="loop in content">
					<li
						class="list-group-item d-flex justify-content-between align-items-center"
					>
						{{ loop.title }}
						<button
							@click="$emit('del-content', loop.id)"
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
			<AddContent v-on:add-content="addContent"></AddContent>
		</div>
	</div>
</template>

<script>
import AddContent from "@/components/News/AddContent.vue";
import axios from "axios";

export default {
	name: "NewsCard",
	components: {
		AddContent,
	},
	props: ["content"],

	methods: {
		addContent(newContent) {
			const { title } = newContent;

			axios
				.post("https://jsonplaceholder.typicode.com/todos", { title })

				.then((res) => (this.content = [...this.content, res.data]))
				.catch((err) => console.log(err));
		},
	},
};
</script>

<style scoped></style>
