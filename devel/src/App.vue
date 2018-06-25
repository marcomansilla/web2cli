<template>
    <div id="app" class="container-fluid">
	<h2>People fetch from service, testing paths</h2>
	<people></people>
    </div>
</template>

<script>
 import People from './components/People.vue';
 export default {

     components:{People},
     name: 'app',
     data () {
	 return {
	     msg: 'Welcome to Your Vue.js App'
	 }
     }
 }
</script>

<style>

</style>
