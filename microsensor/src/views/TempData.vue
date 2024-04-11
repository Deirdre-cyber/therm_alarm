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
          <th>Date</th>
          <th>Time</th>
          <th>City</th>
          <th>State</th>
          <th>Shape</th>
          <th>Duration</th>
          <th>Summary</th>
          <th>Image Included?</th>
          <th>Image URL</th>
          <th>Actions</th>
        </tr>
        <tr>
            <td>""</td>
            <td>""</td>
            <td>""</td>
            <td>""</td>
            <td>""</td>
            <td>""</td>
            <td>""</td>
            <td>""</td>
            <td>""</td>
            <td>""</td>

        </tr>
      </table>
  
      <!-- <div class="pagination">
        <button @click="prevPage" :disabled="currentPage === 1">Previous</button>
        <span>Page {{ currentPage }}</span>
        <button @click="nextPage" :disabled="currentPage * 10 >= sightings.length">Next</button>
      </div> -->
    </div>
  </template>
  
  <script>

  export default {
    name: 'TempData',
    props: {
      msg: {
        type: String,
        default: "All data",
      },
      intro: {
        type: String,
        default: "Here, you'll find all the data from the sensors.",
      },
    }
    
    
    // computed: {
    //   displayedSightings() {
    //     const startIndex = (this.currentPage - 1) * 10;
    //     const endIndex = startIndex + 10;
    //     return this.sightings.slice(startIndex, endIndex);
    //   },
    // },
    // methods: {
    //   prevPage() {
    //     if (this.currentPage > 1) {
    //       this.currentPage--;
    //     }
    //   },
    //   nextPage() {
    //     if (this.currentPage) {
    //       this.currentPage++;
    //     }
    //   },
    // }
  };
  </script>
  
  <style scoped>
  #url_link {
    color: rgb(17, 132, 11);
    text-decoration: none;
    font-size: 0.8rem;
    font-weight: normal;
  }
  
  .table-container {
    overflow-x: auto;
    max-width: 100%;
  }
  
  table {
    border-collapse: collapse;
    margin: auto;
  }
  
  th {
    border: 2px solid black;
    padding: 0.3rem;
    font-size: 1.2rem;
    font-weight: normal;
    background-color: rgb(17, 132, 11);
    color: #fff;
  }
  
  td {
    border: 1px solid black;
    text-align: center;
    padding: 0.1rem 0.5rem;
    background-color: #f1f9f5;
  }
  </style>