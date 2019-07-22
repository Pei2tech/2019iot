/*
var ulElement = document.getElementsByTagName("ul")[0];
var firstItem = ulElement.firstChild;
var lastItem = ulElement.lastChild;

firstItem.setAttribute('class', 'complete');
lastItem.setAttribute('class', 'cool');

 */

var startItem = document.getElementById('two');
var prevItem = startItem.previousSibling;
var nextItem = startItem.nextSibling;

prevItem.setAttribute('class', 'complete');
nextItem.setAttribute('class', 'cool');