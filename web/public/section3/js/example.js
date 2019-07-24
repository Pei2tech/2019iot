
var ulElement = document.getElementById("one").parentNode;

//加入一個元素到li的最後面
var newItemLast = document.createElement('li');
var newTextLast = document.createTextNode("cream");
newItemLast.appendChild(newTextLast);
ulElement.appendChild(newItemLast);


//加入一個元素到li的最前面
var newItemFirst = document.createElement("li");
var newTextFirst = document.createTextNode("kale");
newItemFirst.appendChild(newTextFirst);
ulElement.insertBefore(newItemFirst,ulElement.firstChild);

//將所有li className改為cool
var liItems = document.querySelectorAll('li');
for(var i = 0; i<liItems.length;i++){
    liItems[i].className = "cool";
}

//將item的數量加入至head
var h2Element = document.querySelector('h2');
var h2ElementText = h2Element.textContent;
var totalItems = liItems.length;
var newHeading = h2ElementText + '<span>' + totalItems + '</span>';
h2Element.innerHTML = newHeading;