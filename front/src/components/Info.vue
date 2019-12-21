<template>
	<div class="w-2/4 flex items-center mt-2 -mb-2 justify-center">
    <div class="w-full bg-white pt-4 rounded shadow">
      <div class="w-full border-b border-gray-200">
        <div class="w-full inline-flex px-3 mb-2">
          <div class="font-bold text-green-600">
            <svg class="w-6 h-6 align-middle" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
          </div>
          <div class="text-gray-700 pb-1 ml-4">{{ message }}</div>
       </div>
     </div>
   </div>
 </div>
</template>

<script>
export default {
  props: {
   message: String
 }
}
</script>