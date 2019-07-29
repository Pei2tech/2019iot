//document.getElementById("header").className = "headline";
jQuery("#header").addClass("headline");
jQuery("li:lt(3)").hide().fadeIn(1500);
jQuery('li').on('click',function(event){
    jQuery(this).remove();
});