<template>
<div id="textExample">
  <table class="table table-bordered">
			<thead>
				<tr>
					<th> request Id</th>
					<th> User Name </th>
					<th> House Area </th>
					<th> Months </th>
					<th> Status</th>
					<th> Model execution </th>
					<th> Post Processing </th>

				</tr>
			</thead>
			<tr v-for="session in this.sessions">
				<td> {{ session.request_id }} </td>
				<td> {{ session.username }} </td>
				<td> {{ session.house_area }} </td>
				<td> {{ session.months }} </td>
				<td> {{ session.status }} </td>
				<td> {{ session.model_result }} </td>
				<td> {{ session.post_processed_result }} </td>

			</tr>
		</table>
    <p>
    <router-link to="/login">Logout</router-link>
   </p>

</div>
</template>
<script type="text/javascript">
import config from 'config';
import { username } from '../_helpers';

	export default {
		data () {
			return {
			sessions: []
            }
		},
    created () {
			axios.get(`${config.apiUrl}experiments`, {
				params: {
					username: username()
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
