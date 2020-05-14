var attempt = 3;    // variable to count number of attempts.
// Below function Executes on click of login button.
function validate(){
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    if ( username == "user" && password == "password"){
        alert ("Login succeeded for " + username );
        window.location = "success.html";   // redirecting to other page.
        return false;
}
else { 
    attempt --;     // decrementing by one.
    // alert("You have left "+attempt+" attempt;");
    document.getElementById("error").innerHTML = ""
    if (attempt != 0) {
        document.getElementById("error").innerHTML = "Incorrect username or password.<br>You have  " + attempt + " attempts left"
    }

    // disabling fields after 3 attempts.
    if( attempt == 0) {
        document.getElementById("username").disabled = true;
        document.getElementById("password").disabled = true;
        document.getElementById("submit").disabled = true;
        return false;
    }
}
}