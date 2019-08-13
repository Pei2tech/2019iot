

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
            $(this).attr("src","images/close.png");
        }else{
            console.log("menu close");
            $(this).attr("src","images/menu.png");
        }
    });
});