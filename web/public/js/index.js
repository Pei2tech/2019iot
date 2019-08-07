function newDomListener(event){
    $(this).remove();
}

$(function(){
    $('.signIn').on('click',function(event){
        let $newDom = $("<div class='alertMessage'></div>");
        $newDom.on("click", newDomListener);
        $("body").append($newDom);
        event.preventDefault();
    });
});