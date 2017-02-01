var app = new Vue({
	el: '#app',
	data: {
		character: {}
	},
	methods: {
		loadData: function(){
			var url = 'http://swapi.co/api/people/1/';
			
			this.$http.get(url).then(function(response){
				this.character = response.body;
				console.log(response.body);
				
			}, function(error){
				console.log("These aren't the droids you're looking for.");
				console.log(error);
			});
		}
	}
});

app.loadData();