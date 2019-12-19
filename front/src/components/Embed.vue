<template>
	<textarea class="rounded-b-lg bg-gray-800 h-32 py-2 overflow-hidden text-gray-100 select-all w-full resize-none" disabled>
		<div>
			<input id="email" type="text" data-campaign="{{ campaignId }}">
			<button id="send">Send</button>
		</div>
		<script type="text/javascript" src='https://emailing.co/lib.min.js'></script>
	</textarea>
</template>
<script>
	export default {
		props: {
			campaignId: String
		}
	}
</script>