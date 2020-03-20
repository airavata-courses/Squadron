<template>
<div @keydown.enter="handleSubmit">
<p>
<router-link to="/view">View sessions</router-link>
</p>
      <br></br>
      <p> <b>Please enter the Area of your House in square feet (Sqft)</b></p>
Area:<br>
<input v-model="Area" name="Area" placeholder="Enter Area">
      <br></br>
      <p> <b> Please select the months</b> </p>
    <input type="checkbox" name="0" value="0" v-model="checkedNames">
    <label for="1"> January</label><br>
    <input type="checkbox" name="1" value="1" v-model="checkedNames">
    <label for="2"> February</label><br>
    <input type="checkbox" name="2" value="2" v-model="checkedNames">
    <label for="3"> March</label><br>
    <input type="checkbox" name="3" value="3" v-model="checkedNames">
    <label for="4">April</label><br>
    <input type="checkbox" name="4" value="4" v-model="checkedNames">
    <label for="5">May</label><br>
    <input type="checkbox" name="5" value="5" v-model="checkedNames">
    <label for="6">June</label><br>
    <input type="checkbox" name="6" value="6" v-model="checkedNames">
    <label for="7">July</label><br>
    <input type="checkbox" name="7" value="7" v-model="checkedNames">
    <label for="8">August</label><br>
    <input type="checkbox" name="8" value="8" v-model="checkedNames">
    <label for="9">September</label><br>
    <input type="checkbox" name="9" value="9" v-model="checkedNames">
    <label for="10">October</label><br>
    <input type="checkbox" name="10" value="10" v-model="checkedNames">
    <label for="11">November</label><br>
    <input type="checkbox" name="11" value="11" v-model="checkedNames">
    <label for="12">December</label><br>
    <p><b> Enter valid Zipcode </b></p>
    <input v-model="zipcode" type="text" name="Area" placeholder="Zipcode">
    <br></br>
    <button @click="handleSubmit" >Submit</button>
    <br></br>
    <p>
      <router-link to="/login">Logout</router-link>
    </p>
</div>
</template>

<script>
import config from 'config';
import { username } from '../_helpers';

export default {
  name: 'app',
  data() {
    return {
      username: username(),
      Area:'',
      checkedNames:[],
      zipcode:''
    };
  },
  methods: {
    handleSubmit(e) {
      console.log(this.Area)
      console.log(this.checkedNames)
      console.log(this.zipcode)
      console.log(this.username)
      e.preventDefault();
                    let currentObj = this;
                    axios.post(`${config.apiUrl}experiments/`, {
                        username: this.username,
                        house_area:this.Area,
                        pincode: this.zipcode,
                        months: this.checkedNames
                    })
                    .then(function (response) {
                        currentObj.output = response.data;
                    })
                    .catch(function (error) {
                        currentObj.output = error;
                    });


    }
  }
}
</script>
