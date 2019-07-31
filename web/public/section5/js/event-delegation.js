$(function(){
    $('ul').on(
        "click",
        ':not(#four)',
        {status:'important'},
        function (event) {
        var listItem = "Item: " + event.target.textContent + "<br/>";
        var itemStatus = "Status: " + event.data.status + "<br />";
        var eventTyp = "Event:" + event.type;
        $("#notes").html(listItem + itemStatus + eventTyp);
    });
});