<template>
   <codemirror v-if='html' class='rounded-b-lg h-24 py-2 overflow-hidden select-all -mt-4 w-full resize-none' style='background-color: #263238' v-model="html" :options="htmlOptions">
   </codemirror>
</template>
<script>

import { codemirror } from 'vue-codemirror'
import 'codemirror/lib/codemirror.css'
import 'codemirror/mode/htmlmixed/htmlmixed.js'
import 'codemirror/theme/material.css'

export default {
  props: {
    campaignId: String
  },
  components: {
    codemirror
  },
  data () {
    return {
      html: "",
      htmlOptions: {
        theme: 'material',
        lineNumbers: true,
        htmlMode: true,
        mode: 'htmlmixed',
        tabSize: 4,
        line: true,
      },
    }
  },
  mounted() {
    this.html = `<div>\n\t<input id="email" type="text" data-campaign="${this.campaignId}">\n\t<button id="send">Send</button>\n</div>`;
  }
};
</script>