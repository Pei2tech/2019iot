var userNameElement = document.getElementById('username');

function checkUsername(){
    var feedbackElement = document.getElementById('feedback');
    if(userNameElement.value.length < 5){
        feedbackElement.textContent = "喂!文字最少要5個以上"
    }else{
        feedbackElement.textContent = ""
    }
}
//console.log(window.checkUsername);
//Event Handler
userNameElement.onblur = checkUsername;

