<template>
  <div id="dashboard" class="inline-flex w-full flex-col items-center">
    <Header />

    <div v-if="needUpgrade" class="w-3/4 flex items-center mt-4 justify-center">
      <div class="w-auto bg-white pt-4 rounded shadow-xl">
        <div class="w-auto border-b border-gray-200">
          <div class="w-auto inline-flex px-3 mb-2">
            <div class="text-gray-700 pb-1 ml-4">
              You are using a <b>{{ user.plan.id }} version</b>.<br />
              The <b>{{ user.plan.id }} version</b> is limited to
              <b>{{ user.plan.emailsPerCampaign }} emails</b> and you are reach
              the limit
              <span class="text-white bg-red-400 px-1 py-1 rounded"
                >{{ campaign.total }}/{{ user.plan.emailsPerCampaign }}</span
              >
              <br /><br />
              Go to your
              <router-link class="underline text-gray-800" to="/account"
                >account</router-link
              >
              to upgrade your subscription 😎
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Embed -->
    <div
      v-if="campaign.id"
      class="w-3/4 mt-8 inline-flex flex-col cursor-pointer items-center justify-center"
      @click="openEmbed = !openEmbed"
    >
      <div
        class="rounded bg-white w-full p-4 fill-current text-green-700 inline-flex shadow mb-4"
      >
        <svg
          class="w-6 h-6 align-middle"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
          <polyline points="22 4 12 14.01 9 11.01"></polyline>
        </svg>
        <div class="text-gray-900 ml-4">Code to embed on your website</div>
      </div>
      <div class="w-full" v-if="openEmbed">
        <Embed :campaignId="campaign.id" />
      </div>
    </div>

    <!-- Delete confirmation -->
    <div v-if="wantDelete" class="w-2/4 flex items-center my-4 justify-center">
      <div class="w-full bg-white py-4 rounded shadow">
        <div class="w-full inline-flex flex-col px-3 mb-2">
          <div class="font-bold text-gray-700 pb-1 ml-4 mb-4">
            Are you sure ?
          </div>
          <div
            class="w-full text-center inline-flex flex-row justify-between mt-2 px-16"
          >
            <div
              class="w-16 hover:bg-gray-800 bg-gray-700 text-white text-sm py-1 px-2 border border-gray-700 rounded cursor-pointer outline-none"
              @click="wantDelete = !wantDelete"
            >
              No
            </div>
            <div
              class="w-16 hover:bg-red-600 bg-red-500 text-white text-sm py-1 px-2 border border-red-500 rounded cursor-pointer outline-none"
              @click="deleteCampaign()"
            >
              Yes
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Info -->
    <div class="w-3/4 flex items-center mt-2 justify-center">
      <div class="w-full bg-white pt-4 rounded shadow">
        <div class="w-full border-b border-gray-200">
          <div
            class="w-full inline-flex justify-between px-3 mb-2 font-bold text-gray-700"
          >
            <div class="px-2 mb-2">Info</div>
            <div
              class="hover:bg-red-600 bg-red-500 text-white text-sm py-1 px-2 border border-red-500 rounded cursor-pointer outline-none"
              @click="wantDelete = !wantDelete"
            >
              Delete
            </div>
          </div>
        </div>

        <div
          class="w-full py-3 inline-flex justify-around flex-col md:flex-row lg:flex-row px-8"
        >
          <div
            class="md:w-3/5 lg:w-3/5 border border-gray-200 m-1 rounded h-24 bg-gray-100 mt-2 py-2 px-3 text-gray-800 py-4"
          >
            <div class="mb-2">Campaign: {{ campaign.name }}</div>
            <div>
              Site:
              <a :href="campaign.site" target="_blank" class="underline">{{
                campaign.site
              }}</a>
            </div>
          </div>
          <div
            class="md:w-3/5 lg:w-3/5 border border-gray-200 m-1 rounded h-24 bg-gray-100 mt-2 py-2 px-3 py-4"
          >
            <div class="mb-2">Collected Emails: {{ campaign.total }}</div>
            <div>Campaign Id: {{ campaign.id }}</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Chart -->
    <div
      v-if="campaign"
      class="w-3/4 flex items-center mt-8 justify-center"
    >
      <div class="w-full bg-white pt-4 rounded shadow">
        <div class="w-full">
          <div
            class="w-full border-b border-gray-200 inline-flex justify-between px-3 font-bold text-gray-700"
          >
            <div class="px-2 mb-2">Emails of this {{ filterBy }}</div>
            <div class="px-2 mb-2 inline-flex flex-row justify-between">
              <div
                class="hover:bg-gray-800 bg-gray-700 text-white text-center text-sm py-1 px-2 border border-gray-700 rounded cursor-pointer outline-none mr-2"
                v-for='filter in ["day", "month", "year", "all"]'
                @click="changeFilter(filter)"
              >
                {{ filter }}
              </div>

            </div>
          </div>
          <div class="w-full py-3 px-3 flex flex-col">
            <TrendChart
              v-if="datasets && labels.yLabels >= 2"
              :interactive="true"
              :datasets="datasets"
              :labels="labels"
              :min="0"
              :grid="grid"
            >
            </TrendChart>
            <div v-else>
              No email for this period :(
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Emails -->

    <div
      v-if="campaign.emails"
      class="w-3/4 flex items-center my-6 justify-center"
    >
      <div class="w-full bg-white pt-4 rounded shadow">
        <div class="w-full border-b border-gray-200">
          <div
            class="w-full inline-flex justify-between px-3 font-bold text-gray-600 mb-2"
          >
            <div class="">Emails</div>
            <download-csv
              class="hover:bg-gray-800 bg-gray-700 text-white text-sm py-1 px-2 border border-gray-700 rounded cursor-pointer outline-none"
              :data="campaign.emails"
            >
              + Export
            </download-csv>
          </div>
        </div>
        <vue-good-table
          class="w-full"
          :columns="columns"
          :rows="campaign.emails"
          :search-options="searchOptions"
          :totalRows='campaign.emails.length'
          :pagination-options="{
            enabled: true,
            mode: 'records',
            perPage: 10,
            position: 'top',
            perPageDropdown: [10, 50, 100],
            dropdownAllowAll: false,
            setCurrentPage: 1,
            nextLabel: 'next',
            prevLabel: 'prev',
            rowsPerPageLabel: 'Rows per page',
            ofLabel: 'of',
            pageLabel: 'page',
            allLabel: 'All'
          }"
        />
      </div>
    </div>
  </div>
</template>

<script>
import Header from "@/components/Header.vue";
import Embed from "@/components/Embed.vue";
import axios from "axios";
import moment from "moment";

Array.prototype.unique = function() {
  return this.filter(function(value, index, self) {
    return self.indexOf(value) === index;
  });
};

export default {
  components: {
    Header,
    Embed
  },
  data() {
    return {
      wantDelete: false,
      grid: {
        verticalLines: true,
        verticalLinesNumber: 1,
        horizontalLines: true,
        horizontalLinesNumber: 1
      },
      columns: [
        {
          label: "id",
          field: "id",
          type: "number"
        },
        {
          label: "Email",
          field: "email"
        },
        {
          label: "Created On",
          field: "created_at"
          // TODO fix date format
          // type: 'date',
          // dateInputFormat: 'dddd DOM YYYY hh:mm:ss',
          // dateOutputFormat: 'dddd DOM YYYY hh:mm',
        }
      ],
      api: null,
      token: null,
      campaign: {},
      openEmbed: false,
      needUpgrade: false,
      datasets: null,
      filterBy: 'month', // day, month, year, all
      labels: {
        xLabels: [],
        yLabels: 0,
        yLabelsTextFormatter: val => Math.round(val)
      },
      searchOptions: {
        enabled: true,
        trigger: '',
        skipDiacritics: true,
        placeholder: 'Search Email'
      },
    };
  },
  mounted() {
    this.user = this.$store.getters.user;
    this.api = this.$store.getters.api;
    this.token = this.$store.getters.token;
    
    this.getCampaign();
  },
  methods: {
    async getCampaign() {
      axios.defaults.headers.common["Authorization"] = this.token;
      const response = await axios({
        url: `${this.api}/campaign/${this.$route.params.id}`,
        method: "GET"
      });
      const data = response.data;
      if (data.error) {
        throw new Error(data.error);
      }
      
      this.campaign = data;
      this.searchOptions.trigger = this.campaign.emails.length >= 1000 ? 'enter' : '' 

      let i = 1;
      this.campaign.emails = this.campaign.emails.map(cmp => {
        cmp.moment = moment(new Date(cmp.created_at));
        cmp.created_at = cmp.moment.format("dddd MMM YYYY hh:mm:ss");
        cmp.id = i++;
        return cmp;
      });

      if (this.campaign.total > this.campaign.emails.length) {
        this.needUpgrade = true;
      }
      this.formatchartData();
    },
    export() {
      return this.campaign.emails.map((email) => {
        return {
          id: email.id,
          created_at: email.moment.toString(),
          email: email.email,
        }
      })
    },
    formatchartData() {

      let datasets = this.campaign.emails.map(e => {
        if (!e.moment) {
          return null; 
        }
        const value = {
          dataset: e.moment.toString(),
          labels: e.moment.format("MMM-DD")
        };
        if (this.filterBy === 'day') {
          if (e.moment.format("DD-MM-YY") == moment(new Date()).format('DD-MM-YY')) {
            return value;
          }
            
        }
        if (this.filterBy === 'month') {
          if (e.moment.format("MM-YY") == moment(new Date()).format('MM-YY')) {
            return value;
          }
        }
        if (this.filterBy === 'year') {
          if (e.moment.format("YY") == moment(new Date()).format('YY')) {
            return value;
          }
        }
        if (this.filterBy === 'all') {
          return value;
        }

        return null
      }).filter((d) => d);
      
      datasets.reverse();
      
      let item = {};
      datasets
        .map(d => d.labels)
        .forEach(function(v) {
          item[v] = (item[v] || 0) + 1;
        });

      this.datasets = [
        {
          data: Object.values(item),
          smooth: true,
          fill: true,
          showPoints: true
        }
      ];
      const uniqueDataset = datasets.map(d => d.labels).unique();
      this.labels.xLabels = uniqueDataset;
      this.labels.yLabels = uniqueDataset.length;
    },
    changeFilter(val) {
      this.filterBy = val
      this.formatchartData()
    }, 
    async deleteCampaign() {
      axios.defaults.headers.common["Authorization"] = this.token;
      const response = await axios({
        url: `${this.api}/campaign/${this.$route.params.id}`,
        method: "DELETE"
      });
      this.$router.push("/dashboard");
    }
  }
};
</script>
