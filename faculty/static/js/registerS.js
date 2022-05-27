function student_register(){

    returnStatus = 1;

    var name1=document.getElementById('name')
    var name_s=document.getElementById("name_span")

    var eno1=document.getElementById('eno')
    var eno_s=document.getElementById("eno_span")

    var dob1=document.getElementById('dob')
    var dob_s=document.getElementById("dob_span")

    var gender1=document.getElementById('gender')
    var gender_s=document.getElementById("gender_span")

    var dpt1=document.getElementById('dpt')
    var dpt_s=document.getElementById("dpt_span")

    var sem1=document.getElementById('sem')
    var sem_s=document.getElementById("sem_span")

    var email1=document.getElementById('email')
    var email_s=document.getElementById("email_span")

    var phone1=document.getElementById('phn')
    var phone_s=document.getElementById("phn_span")

    var pwd1=document.getElementById('pwd')
    var pwd_s=document.getElementById("pwd_span")

    var cpwd1=document.getElementById('cpwd')
    var cpwd_s=document.getElementById("cpwd_span")


    console.log(gender1.value)
    console.log(dpt1.value)
    console.log(sem1.value)


    if(name1.value == ""){
        name_s.innerHTML="*please fill the name"
        name_s.style.color="red"
        name1.style.border="solid 1px red"
        returnStatus = 0
       
       }
   else{
       name_s.innerHTML=""
       name1.style.border="solid 1px black"
       }






    if(eno1.value == ""){
        eno_s.innerHTML="*please fill the name"
        eno_s.style.color="red"
        eno1.style.border="solid 1px red"
        returnStatus = 0
       
       }
   else{
       eno_s.innerHTML=""
       eno1.style.border="solid 1px black"
       }




    if(dob1.value == ""){
        dob_s.innerHTML="*please fill the name"
        dob_s.style.color="red"
        dob1.style.border="solid 1px red"
        returnStatus = 0
       
       }
   else{
       dob_s.innerHTML=""
       dob1.style.border="solid 1px black"
       }



    if(gender1.value == ""){
        gender_s.innerHTML="*please fill the name"
        gender_s.style.color="red"
        gender1.style.border="solid 1px red"
        returnStatus = 0
       
       }
   else{
       gender_s.innerHTML=""
       gender1.style.border="solid 1px black"
       }




    if(dpt1.value == ""){
        dpt_s.innerHTML="*please fill the name"
        dpt_s.style.color="red"
        dpt1.style.border="solid 1px red"
        returnStatus = 0
       
       }
   else{
       dpt_s.innerHTML=""
       dpt1.style.border="solid 1px black"
       }





    if(sem1.value == ""){
        sem_s.innerHTML="*please fill the name"
        sem_s.style.color="red"
        sem1.style.border="solid 1px red"
        returnStatus = 0
       
       }
   else{
       sem_s.innerHTML=""
       sem1.style.border="solid 1px black"
       }




    if(email1.value == ""){
        email_s.innerHTML="*please fill the name"
        email_s.style.color="red"
        email1.style.border="solid 1px red"
        returnStatus = 0
       
       }
   else{
       email_s.innerHTML=""
       email1.style.border="solid 1px black"
       }





    if(phone1.value == ""){
        phone_s.innerHTML="*please fill the name"
        phone_s.style.color="red"
        phone1.style.border="solid 1px red"
        returnStatus = 0
       
       }
   else{
       phone_s.innerHTML=""
       phone1.style.border="solid 1px black"
       }





       if(pwd1.value == ""){
        pwd_s.innerHTML="*please fill the password"
        pwd_s.style.color="red"
        pwd1.style.border="solid 1px red"
        returnStatus = 0
       }
    else if(pwd1.value.length<8){
       pwd_s.innerHTML="*should contain 8 characters"
       pwd_s.style.color="red"
       pwd1.style.border="solid 1px red"
       returnStatus = 0
     }
    else{
       pwd_s.innerHTML=""
       pwd1.style.border="solid 1px black"  
     }





     if(cpwd1.value == ""){
        cpwd_s.innerHTML="*please fill the password"
        cpwd_s.style.color="red"
        cpwd1.style.border="solid 1px red"
        returnStatus = 0       
       }
      else if(pwd1.value!=cpwd1.value){
       cpwd_s.innerHTML="*password does not match"
       cpwd_s.style.color="red"
       cpwd1.style.border="solid 1px red"
       returnStatus = 0
   
      }
      else {
       cpwd_s.innerHTML=""
       cpwd1.style.border="solid 1px black"
      }






//     if(pwd1.value == ""){
//         pwd_s.innerHTML="*please fill the name"
//         pwd_s.style.color="red"
//         pwd1.style.border="solid 1px red"
//         returnStatus = 0
       
//        }
//    else{
//        pwd_s.innerHTML=""
//        pwd1.style.border="solid 1px black"
//        }




//     if(cpwd1.value == ""){
//         cpwd_s.innerHTML="*please fill the name"
//         cpwd_s.style.color="red"
//         cpwd1.style.border="solid 1px red"
//         returnStatus = 0
       
//        }
//    else{
//        cpwd_s.innerHTML=""
//        cpwd1.style.border="solid 1px black"
//        }

if (returnStatus == 0) {
     return false
}



}