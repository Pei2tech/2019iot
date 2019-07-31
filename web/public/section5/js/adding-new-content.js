$(function(){
    $('ul').before('<p class="notice">Juset updated</p>');
    $('li.hot').prepend("+ ");
    var $newListItem = $("<li><em>gluten-free</em> soy sauce</li>");
    $('li:last-of-type').after($newListItem);
});