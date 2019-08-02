$(function(){
    var $newItemButton = $('#newItemButton');
    var $newItemForm = $('#newItemForm');
    var $textInput = $('input:text');

    $newItemButton.show();
    $newItemForm.hide();

    $('#showForm').on("click",function(event) {
        $newItemButton.hide();
        $newItemForm.show();
    });

    $newItemForm.on("submit",function(event){
        event.preventDefault();
        var newText = $textInput.val();
        $('li:last-of-type').after('<li>' + newText + '</li>');
        $newItemForm.hide();
        $newItemButton.show();
        $textInput.val("");
    });
});