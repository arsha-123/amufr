$(document).ready(function(){
    $('#login').click(function(){
        var a=$('#email')
        var b=$('#password')
        if(a.val()==""){
            $('#p1').show()
            $('#email').css({'border':'solid 2px red'})
            return false
        }
        else{
            $('#email').css({'border':'solid 2px black'})
            $('#p1').hide()

        }
        if(b.val()==""){
            $('#p2').show()
            $('#password').css({'border':'solid 2px red'})
            return false
        }
        else{
            $('#password').css({'border':'solid 2px red'})
            $('#p2').hide()
        }

    })


})