var elUsername = document.getElementById("username");
var feedbackElement = document.getElementById('feedback');
function checkUsername(minLength){
    if (elUsername.value.length < minLength){
        feedbackElement.textContent = "使用者的名稱必需要" + minLength + "個字以上";
    }else{
        feedbackElement.textContent = '';
    }
}

elUsername.addEventListener(
    'blur',
    function(event){
       checkUsername(5)
    },
    false);