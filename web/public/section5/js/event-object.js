$(function () {
    $('li').on('click', function(event){
        $('li span').remove();
        var date = new Date();
        date.setTime(event.timeStamp);
        var clicked = date.toDateString();
        $(this).append('<span class="date">' + clicked +'</span>');
    });
});