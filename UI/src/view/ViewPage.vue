<template>
<div id="textExample">
  <table class="table table-bordered">
			<thead>
				<tr>
					<th> request Id</th>
					<th> User Name </th>
					<th> House Area </th>
					<th> Months </th>
					<th> Payment</th>
					<th> houseArea</th>
					<th> status</th>
				</tr>
			</thead>
			<tr v-for="i in session[0]">
				<td v-for="j in session">{{j[i]}}</td>
			</tr>
		</table>
    <p>
    <router-link to="/login">Logout</router-link>
   </p>

</div>
</template>
<script type="text/javascript">
	export default {
		data () {
			return {
session:''
            }
		},
    created () {
			axios.get('http://localhost:7000/test')
			.then(
				response => {
					this.session = response.body
					// console.log(response)
				})
			.catch(function(error){
				console.log(error)
			})
		}
	}
</script>
<p>
<router-link to="/view">View sessions</router-link>
</p>
