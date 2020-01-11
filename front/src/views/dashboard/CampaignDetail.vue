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

  <router-link :to='"/dashboard/campaign/" + campaign.id + "/connect"'
      v-if="campaign.id"
      class="w-1/2 mt-8 inline-flex flex-col cursor-pointer items-center justify-center"
    >
      <div
        class="rounded bg-white w-full pb-1 fill-current text-green-700 justify-center inline-flex shadow mb-4"
      >
        <div class="text-gray-900 pt-3 capitalize underline">
          Connect your campaign with other tools
        </div>
        <svg 
         class="w-12 h-12 ml-2 align-middle -mt-1"
         fill="#2d3748" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" version="1.1" x="0px" y="0px" viewBox="0 0 100 100"><g transform="translate(0,-952.36218)"><path style="text-indent:0;text-transform:none;direction:ltr;block-progression:tb;baseline-shift:baseline;color:#000000;enable-background:accumulate;" d="m 84.007802,977.36223 c -11.722922,4.94412 -22.989788,9.95212 -32.474795,14.27871 -0.674469,0.56468 -0.895217,1.47636 -0.510095,2.30733 l 7.923189,17.35513 c 0.474272,0.9909 1.753158,1.3972 2.686394,1.0367 l 31.216637,-13.81061 c 0.84824,-0.34926 1.45857,-1.54839 0.98614,-2.7086 -2.61765,-5.77694 -5.29933,-11.5408 -7.88917,-17.32171 -0.3651,-0.718 -1.15498,-1.14381 -1.9383,-1.13695 z m 0.13603,1.9395 c 2.7833,6.00273 5.5524,12.22585 7.95706,17.38859 -10.83858,4.95318 -22.015094,9.80938 -31.352594,13.84398 L 52.82518,993.24604 c 6.447862,0.86026 12.898488,1.69997 19.348866,2.54141 0.349122,0.0416 0.715571,-0.11859 0.918141,-0.40128 3.710415,-5.34388 7.380245,-10.71463 11.051645,-16.08444 z m -3.26448,1.37102 c -3.02794,4.37205 -6.034893,8.75808 -9.045357,13.14176 -5.305678,-0.69555 -10.610114,-1.40036 -15.914339,-2.10669 8.317772,-3.68302 16.640646,-7.35485 24.959696,-11.03507 z" fill="#2d3748" fill-opacity="1" fill-rule="evenodd" stroke="none" marker="none" visibility="visible" display="inline" overflow="visible"></path><path style="text-indent:0;text-transform:none;direction:ltr;block-progression:tb;baseline-shift:baseline;color:#000000;enable-background:accumulate;" d="m 40.873074,995.25386 -28.956223,12.20884 c -1.271481,0.7495 -0.2368,2.1657 0.771129,1.7702 l 28.956259,-12.20885 c 1.16054,-0.55594 0.291933,-2.12115 -0.771165,-1.77019 z" fill="#2d3748" fill-opacity="1" fill-rule="evenodd" stroke="none" marker="none" visibility="visible" display="inline" overflow="visible"></path><path style="text-indent:0;text-transform:none;direction:ltr;block-progression:tb;baseline-shift:baseline;color:#000000;enable-background:accumulate;" d="m 22.635673,1013.188 -16.1168029,6.7869 c -1.111393,0.5698 -0.24059,2.0641 0.771166,1.7702 l 16.1167669,-6.7869 c 1.211527,-0.5061 0.206504,-2.1873 -0.77113,-1.7702 z" fill="#2d3748" fill-opacity="1" fill-rule="evenodd" stroke="none" marker="none" visibility="visible" display="inline" overflow="visible"></path><path style="text-indent:0;text-transform:none;direction:ltr;block-progression:tb;baseline-shift:baseline;color:#000000;enable-background:accumulate;" d="m 49.856845,1014.4772 -26.295802,11.0714 c -1.288488,0.6324 -0.287823,2.0821 0.77113,1.7702 l 26.295802,-11.0715 c 1.126524,-0.5228 0.1215,-2.0535 -0.77113,-1.7701 z" fill="#2d3748" fill-opacity="1" fill-rule="evenodd" stroke="none" marker="none" visibility="visible" display="inline" overflow="visible"></path></g></svg>
      </div>
    </router-link>

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
            class="w-full inline-flex justify-between px-3 mb-2 font-medium text-gray-700"
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
            class="w-full inline-flex justify-between px-3 font-medium text-gray-600 mb-2"
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
          max-height="400px"
          :search-options="searchOptions"
          :totalRows='campaign.emails.length'
          :fixed-header="true"
          :line-numbers="true"
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
import axios from "axios";
import moment from "moment";

Array.prototype.unique = function() {
  return this.filter(function(value, index, self) {
    return self.indexOf(value) === index;
  });
};

export default {
  components: {
    Header
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
          label: "Email",
          field: "email",
          filterable: true,
        },
        {
          label: "Created On",
          field: "created_at",
          filterable: true,
          // TODO fix date format
          // type: 'date',
          // dateInputFormat: 'dddd DOM YYYY hh:mm:ss',
          // dateOutputFormat: 'dddd DOM YYYY hh:mm',
        }
      ],
      api: null,
      token: null,
      campaign: {},
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
        trigger: 'enter', // enter || ''
        skipDiacritics: true,
        placeholder: 'Search Email'
      },
    };
  },
  mounted() {
    this.user = this.$store.getters.user;
    
    if (this.user.plan.id != 'free') {
      this.columns.push({
        label: 'Valid',
        field: 'is_valid',
        filterable: true,
      })
    }

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

      this.campaign.emails = this.campaign.emails.map(email => {
        email.moment = moment(new Date(email.created_at));
        email.created_at = email.moment.format("dddd MMM YYYY hh:mm:ss");
        
        if (email.validation) {
          email.is_valid = email.validation.valid
          if (email.validation.status == null) {
            email.is_valid = 'unknown'
          }
          
          delete email.validation
        }
        
        return email;
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

<style>
  .vgt-table th.line-numbers:first-child {
    width: 35px!important;
  }
  @media screen and (max-width: 960px) {
    .vgt-table th.line-numbers:first-child {
      width: 45px!important;
    }
  }
</style>