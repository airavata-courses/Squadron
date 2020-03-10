<template>
<div @keydown.enter="Register">
<h1>Team Squadron</h1>
<h3> Registration Page</h3>
<br> </br>
<p>Enter First Name</p>
<input type ="text" v-model="First_Name" name="First_Name" placeholder="First Name" >
<br> </br>
<p>Enter Last Name </p>
<input v-model="Last_Name" name="Last_Name" placeholder="Last Name">
<br> </br>
<p> Enter Email </p>
<input v-model="Email" name="Email" placeholder="Email ID">
<br> </br>
<p> Enter User name </p>
<input v-model="user_name" name="user_name" placeholder="User Name">
<br> </br>
<p> Enter Password </p>
<input v-model="Password" name="Password" placeholder="Password">
<br> </br>
<button @click="Register"> Finish Register </button>

<p>
  <router-link to="/login"> Login with registered credentials </router-link>
</p>

</div>
</template>
<script>
export default {
data() {
    return {
      First_Name:'',
      Last_Name:'',
      Email:'',
      user_name:'',
      Password:''
    };
},
methods:{
Register(e){
  console.log(this.First_Name)
  console.log(this.Last_Name)
  console.log(this.Email)
  console.log(this.user_name)
  console.log(this.Password)
  e.preventDefault();
                    let currentObj = this;
                    axios.post('http://localhost:7000/api/register/', {
                        username: this.user_name,
                        password: this.Password,
                        first_name: this.First_Name,
                        last_name: this.Last_Name,
                        email:this.Email
                    })
                    .then(function (response) {
                        currentObj.output = response.data;
                    })
                    .catch(function (error) {
                        currentObj.output = error;
                    });
}
}

};
</script>
<style>
 margin: auto;
</style>
