var elements = document.getElementsByClassName("hot");
var num = elements.length;
if(elements.length>2){
    var el = elements[2];
    el.className = 'cool';
}