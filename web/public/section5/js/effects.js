$(function(){
    $('h2').hide().slideDown();
    var $li = $('li');
    $li.hide().each(function(index, element){
        //console.log("index:" + index + "element:" + element);
        $(this).delay(index * 700).fadeIn();
    });

    $li.on("click",function(event){
        $(this).fadeOut(700);
    });
});