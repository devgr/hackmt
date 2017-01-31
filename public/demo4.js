var app = new Vue({
	el: '#app',
	data: {
		headerText: 'Hello HackMT!',
		description: 'Vue.js makes web development fun.',
		magic: '',
		items:[
			{
				name: 'Thing 1',
				description: 'description description description'
			},
			{
				name: 'Thing 2',
				description: 'another really cool thing'
			}
		],
		isHorizontal: false,
		numbers: [42, 55, 68],
		whichButton: '',
		theNumber: ''
	},
	methods: {
		buttonClick: function(index){
			this.whichButton = index;
			this.theNumber = this.numbers[index];
		}
	}
});