//修改element 內容
var firstItem = document.getElementById("one");
var itemContent = firstItem.innerHTML;
firstItem.innerHTML = '<a href=\"http://www.w3school.com.cn\">' + itemContent + '</a>';

//新增element
var newEl = document.createElement('li');
var newText = document.createTextNode("妹妹");
newEl.appendChild(newText);
newEl.setAttribute('id', "five");
var ulPosition = document.getElementsByTagName("ul")[0];
ulPosition.appendChild(newEl);
