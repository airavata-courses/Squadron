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
			<tr v-for="session in this.sessions">
				<td> {{ session.request_id }} </td>
				<td> {{ session.username }} </td>
				<td> {{ session.house_area }} </td>
				<td> {{ session.months }} </td>
				<td> {{ session.username }} </td>


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
			sessions: []
            }
		},
    created () {
			axios.get('http://localhost:7000/api/experiments', {
				params: {
					username: "admin"
				}
			})
			.then(
				response => {
					this.sessions = response.data
					console.log(this.sessions)
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
