function faculty_login() {

    returnStatus = 1;
    
    var email1 = document.getElementById('email')
    var email_span = document.getElementById("email_err")
    
    var psd_err = document.getElementById('pswrd')
    var pswrd_span = document.getElementById('pswrd_err')
    
    
    if (email1.value == "") {
        email_span.innerHTML = "*please fill the email"
        email_span.style.color = "red"
        email1.style.border = "solid 1px red"
        returnStatus = 0
    }
    else {
        email_span.innerHTML = ""
        email1.style.border = "solid 1px black"
        
    }
    
    if (psd_err.value == "") {
        returnStatus = 0
        pswrd_span.innerHTML = "*please fill the pasword"
        pswrd_span.style.color = "red"
        psd_err.style.border = "solid 1px red"
        
    }
    else {
        psd_err.innerHTML = ""
        psd_err.style.border = "solid 1px red"
    }
    
    
    if (returnStatus == 0) {
    return false
    }
    
    
    }