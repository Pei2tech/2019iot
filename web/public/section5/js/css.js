$(function(){
    var backgroundColor = $('li:first-of-type').css('background-color');
    $('ul').append('<p>Color was:' + backgroundColor + '</p>');
    $('li').css({
        "background-color":"#c5a996",
        "border":"1px solid #fff",
        "color":"#000",
        "font-family":"Georgia",
        "padding-left": "+=75"
    });
});