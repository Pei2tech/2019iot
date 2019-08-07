$(function(){
    $('.signIn').on('click',function(event){

        let windowWidth = window.innerWidth;
        let windowHeight = window.innerHeight;
        let $newDom = $("<div></div>");
        $newDom.innerHeight(windowHeight).innerWidth(windowWidth);
        $newDom.css({
            backgroundColor:'#aaa',
            position:'absolute',
            top:'0px',
            let:'0px',
            opacity:0.5,
        });
        $("body").append($newDom);
        event.preventDefault();
    });
});