<template>
	<div>
		<div class="card">
			<div class="card-header cards-title">
				Documents
			</div>
			<div class="card-body scroll">
				<div v-bind:key="loop.id" v-for="loop in docs">
					<ul class="list-group">
						<div v-bind:key="loop.id" v-for="loop in docs">
							<li
								class="list-group-item d-flex justify-content-between align-items-center"
							>
								<a href="loop.thumbnailUrl" download>
									<img :src="loop.thumbnailUrl" />
								</a>

								<button
									@click="$emit('del-docs', loop.id)"
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
			</div>
			<div class="card-footer text-muted">
				<AddDocs v-on:add-docs="addDocs"></AddDocs>
			</div>
		</div>
	</div>
</template>

<script>
import AddDocs from "@/components/Docs/AddDocs.vue";
import axios from "axios";

export default {
	name: "DocsCard",
	components: {
		AddDocs,
	},
	props: ["docs"],

	methods: {
		addDocs(newDocs) {
			const { thumbnailUrl } = newDocs;

			axios
				.post("https://jsonplaceholder.typicode.com/photos", { thumbnailUrl })

				.then((res) => (this.docs = [...this.docs, res.data]))
				.catch((err) => console.log(err));
		},

		onClick() {
			alert("warning");
			// axios({
			// 	url: "http://localhost:8000/my.pdf",
			// 	method: "GET",
			// 	responseType: "blob",
			// }).then((response) => {
			// 	var fileURL = window.URL.createObjectURL(new Blob([response.data]));
			// 	var fileLink = document.createElement("a");

			// 	fileLink.href = fileURL;
			// 	fileLink.setAttribute("download", "file.pdf");
			// 	document.body.appendChild(fileLink);

			// 	fileLink.click();
			// });
		},
	},
};
</script>

<style scoped></style>
