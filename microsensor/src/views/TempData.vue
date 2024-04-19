<template>
  <div class="tempdata">
    <h1>{{ msg }}</h1>
    <div class="intro">
      <p>{{ intro }}</p>
    </div>

    <router-view></router-view>

  </div>

  <div class="table-container">
    <table>
      <tr>
        <th>Sensor</th>
        <th>Time and Date</th>
        <th>Current Temperature</th>
        <th>Threshold Exceeded?</th>
        <th>Where?</th>
        <th>Max Threshold</th>
        <th>Min Threshold</th>
      </tr>
      <tr v-for="(item, index) in displayedTempData" :key="index">
        <td id = "sense">{{ item.SensorID }}</td>
        <td>{{ item.TimeDate }}</td>
        <td>{{ item.CurrTemp }}</td>
        <td>{{ item.IsExceeded }}</td>
        <td>{{ item.LocationID }}</td>
        <td id = "hot">{{ item.MaxThreshold }}</td>
        <td id = "cold">{{ item.MinThreshold }}</td>
      </tr>
    </table>

    <div class="pagination">
      <button @click="prevPage" :disabled="currentPage === 1">Previous</button>
      <span>Page {{ currentPage }}</span>
      <button @click="nextPage" :disabled="currentPage * 10 >= allTempData.length">Next</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TempData',
  props: {
    msg: {
      type: String,
      default: "Temperature Data History",
    },
    intro: {
      type: String,
      default: "Here, you'll find a history of the temperature readings from all connected sensors.",
    },
  },
  data() {
    return {
      allTempData: [],
      currentPage: 1
    };
  },
  async created() {
    try {
      const response = await fetch(process.env.VUE_APP_API_ENDPOINT, {
        method: 'GET',
        mode: 'cors'
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const responsebody = await response.json();
      this.allTempData = JSON.parse(responsebody.body)

      this.allTempData.sort((a, b) => new Date(a.TimeDate) - new Date(b.TimeDate));
      
      for (let item of this.allTempData) {
        item.TimeDate = new Date(item.TimeDate).toUTCString();
        item.CurrTemp = item.CurrTemp + '\xB0C';
        item.IsExceeded = item.IsExceeded ? 'Yes' : 'No';
        item.MaxThreshold = item.MaxThreshold + '\xB0C';
        item.MinThreshold = item.MinThreshold + '\xB0C';
      }
      
    } catch (error) {
      console.error('Error fetching data from API Gateway:', error);
    }
  },
  computed: {
    displayedTempData() {
      const startIndex = (this.currentPage - 1) * 10;
      const endIndex = startIndex + 10;

      return this.allTempData.slice(startIndex, endIndex);
    },
  },
  methods: {
    prevPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },
    nextPage() {
      if (this.currentPage * 10 < this.allTempData.length) {
        this.currentPage++;
      }
    },
  }
};
</script>

<style scoped>

.table-container {
  overflow-x: auto;
  max-width: 100%;
}

table {
  border-collapse: collapse;
  margin: auto;
}

th, #sense {
  border: 2px solid black;
  padding: 0.8rem;
  font-size: 1.2rem;
  font-weight: normal;
  background-color: rgb(244, 222, 188);
  color: #000;
}

td {
  border: 1px solid black;
  text-align: center;
  padding: 0.8rem;
  background-color: #f8f8ed;
}

#hot {
  background-color: rgb(237, 171, 166);
  color: rgb(93, 22, 8);
}

#cold {
  background-color: rgb(169, 241, 241);
  color: rgb(8, 93, 93);
}



</style>