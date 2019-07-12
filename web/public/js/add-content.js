/*
This is javascript;
 */
var today = new Date(); //create a new date object
var hourNow = today.getHours();
console.log(hourNow);

var greeting;
if(hourNow > 18){
     greeting = "晚安";
}else if(hourNow > 12){
    greeting = "午安";
}else if (hourNow > 0){
    greeting = "早安";
}
console.log(greeting);
document.write("<h3>" + greeting + "</h3>");
