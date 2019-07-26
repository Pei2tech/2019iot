var elUl = document.getElementById('shoppingList');
elUl.addEventListener(
    'click',
    function(event){
       if(event.target.localName == "a"){
           var liElement = event.target.parentNode;
           elUl.removeChild(liElement);
       }else{
           console.log("other");
       }

        event.preventDefault();
    },
    false);