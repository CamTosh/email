<template>
  <div id="dashboard" class="inline-flex w-full flex-col items-center">
    <Header selected='Account' />

		<div class="w-3/4 flex items-center mt-8 justify-center">
			<div class="w-full bg-white pt-4 rounded shadow">
				<div class="w-full border-b border-gray-200">
					<div class="w-full inline-flex justify-between px-3 mb-2 font-bold text-gray-600">
						<div class=" text-gray-700">Billing</div>
					</div>
				</div>

				<div class="w-full py-3 px-5 inline-flex px-8">
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import Header from '@/components/Header.vue';
import Info from '@/components/Info.vue';
import Error from '@/components/Error.vue';
import axios from "axios";


export default {
  components: {
    Header,
    Info,
    Error,
  },
}
</script>