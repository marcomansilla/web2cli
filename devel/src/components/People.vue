<template>
    <div>
	<table class="table table-striped table-hover table-bordered">
	    <thead>
		<tr>
		    <th>Name</th>
		    <th>Lastname</th>
		    <th>Age</th>
		    <th>Address</th>
		</tr>
	    </thead>
	    <tbody>
		<tr v-for="person in people">
		    <td>{{person.name}}</td>
		    <td>{{person.lastname}}</td>
		    <td>{{person.age}}</td>
		    <td>{{person.address}}</td>
		</tr>
	    </tbody>
	</table>
    </div>
</template>

<script>
 import axios from 'axios';
 export default {
     data() {
	 return {
	     people:null,
	 }
     },

     methods:{
	 fetchPeople(){
	     axios.get(`/services/api/person`)
		  .then(res=>this.people=res.data.rows);
	 }
     },
     mounted(){
	 this.fetchPeople();
     }
 }

</script>
