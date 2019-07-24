var newEl = document.createElement('li');
var newText = document.createTextNode("new add");
newEl.appendChild(newText);
var todoEl = document.getElementsByTagName('ul')[0];
var liEl = document.querySelector('#todo #three');
todoEl.insertBefore(newEl, liEl);