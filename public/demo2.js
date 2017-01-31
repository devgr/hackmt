var textbox = document.getElementById('myTextbox');
var label = document.getElementById('myLabel');
textbox.onkeydown = function(e){
    label.innerHTML = textbox.value;
};


var list = document.getElementById('myList');
var data = [
    'Thing 1',
    'Another thing',
    'This is really interesting...'
];
var listHtml = '';
for(var i = 0, len = data.length; i < len; i++){
    listHtml += '<li>' + data[i] + '</li>';
}
list.innerHTML = listHtml;