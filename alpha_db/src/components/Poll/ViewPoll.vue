<template>
	<div>
		<poll-view getPollUrl="get-poll-url" saveVoteUrl="post-save-url" />
	</div>
</template>

<script>
import { PollView } from "@updivision/vue-easy-polls";

export default {
	name: "ViewPoll",
	components: {
		PollView,
	},
};
</script>

<style scoped></style>
