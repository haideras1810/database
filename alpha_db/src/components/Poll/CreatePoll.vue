<template>
	<div class="card">
		<div class="card-header">Poll</div>
		<div class="card-body">
			<poll-creator savePollUrl="post-poll-url" />
		</div>
	</div>

	<!-- <div class="card">
		<div class="card-header">
			Links
		</div>
		<div class="card-body scroll">
			<div v-bind:key="loop.id" v-for="loop in link">
				<div class="row border-0">
					<div class="col-sm-9 align-self-center">
						<p class="card-text text-left">{{ loop.title }}</p>
					</div>

					<div class="col-sm-3 align-self-center">
						<button
							@click="$emit('del-link', loop.id)"
							class="btn btn-outline-danger btn-sm text-right"
						>
							x
						</button>
					</div>
				</div>
			</div>
		</div>
		<div class="card-footer text-muted">
			<AddLink v-on:add-link="addLink"></AddLink>
		</div>
	</div> -->

	<!-- <poll-creator savePollUrl="post-poll-url" /> -->
</template>

<script>
import { PollCreator } from "@updivision/vue-easy-polls";

export default {
	name: "CreatePoll",
	components: {
		PollCreator,
	},
};
</script>

<style scoped>
.card {
	overflow-y: auto;
}
</style>
