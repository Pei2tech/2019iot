

$(function(){
    let $alertMessage = $(".alertMessage");
    $alertMessage.hide();
    $('.signIn').on('click',function(event){
         $alertMessage.slideDown(400);
        event.preventDefault();
        $('.cancel').on("click",function(event){
            $alertMessage.slideUp(400);
        })
    });

});

$(function(){
    var menuState = false;
    $("#menu").on("click",function(event){
        menuState = !menuState;
        if (menuState) {
            console.log("menu open");
        }else{
            console.log("menu close");
        }
    });
});