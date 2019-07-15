var greeting = "Howdy";
var name = "Molly";
var message = ", please check your order:";

var welcome = greeting + name + message;

//sign
var sign = 'Montague House';
var tiles = sign.length;
var subTotal = tiles * 5;
var shipping = 7;
var grandTotal = subTotal + shipping;
console.log("grandTotal:" + grandTotal);

//get element
var el = document.getElementById("greeting");
el.textContent = welcome;

var elSign = document.getElementById("userSign");
elSign.textContent = sign;

var elTitles = document.getElementById("tiles");
elTitles.textContent = tiles.toString();

var elSubTotal = document.getElementById('subTotal');
elSubTotal.textContent = '$' + subTotal;

var elShipping = document.getElementById('shipping');
elShipping.textContent = '$' + shipping;

var elGrandTotal = document.getElementById('grandTotal');
elGrandTotal.textContent = '$' + grandTotal;