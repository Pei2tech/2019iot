

$(function(){
    let $alertMessage = $(".alertMessage");
    $alertMessage.hide();
    $('.signIn').on('click',function(event){
         $alertMessage.show();
        event.preventDefault();
        $('.cancel').on("click",function(event){
            $alertMessage.hide();
        })
    });
});