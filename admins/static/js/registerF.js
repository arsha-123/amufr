$(document).ready(function(){
    $('#submit').click(function(){
        var a=$('#name')
        var b=$('#dpt')
        var c=$('#gender')
        var d=$('#dob')
        var e=$('#mail')
        var f=$('#phn')
        var g=$('#pwd')
        var h=$('#cpwd')
        


        if(a.val()==""){
            $('#p1').show()
            $('#name').css({'border':'solid 2px red'})
            return false
        }
        else{
            $('#name').css({'border':'solid 2px black'})
            $('#p1').hide()

        }


        if(b.val()==""){
            $('#p2').show()
            $('#dpt').css({'border':'solid 2px red'})
            return false
        }
        else{
            $('#dpt').css({'border':'solid 2px black'})
            $('#p2').hide()
        }


        if(c.val()==""){
            $('#p3').show()
            $('#gender').css({'border':'solid 2px red'})
            return false
        }
        else{
            $('#gender').css({'border':'solid 2px black'})
            $('#p3').hide()
        }



        if(d.val()==""){
            $('#p4').show()
            $('#dob').css({'border':'solid 2px red'})
            return false
        }
        else{
            $('#dob').css({'border':'solid 2px black'})
            $('#p4').hide()
        }



        if(e.val()==""){
            $('#p5').show()
            $('#mail').css({'border':'solid 2px red'})
            return false
        }
        else{
            $('#mail').css({'border':'solid 2px black'})
            $('#p5').hide()
        }


        if(f.val()==""){
            $('#p6').show()
            $('#phn').css({'border':'solid 2px red'})
            return false
        }
        else{
            $('#phn').css({'border':'solid 2px black'})
            $('#p6').hide()
        }


       
       
       
       
       
       
        if(g.val()==""){
            $('#p7').show()
            $('#pwd').css({'border':'solid 2px red'})
            return false
        }
        else{
            $('#pwd').css({'border':'solid 2px black'})
            $('#p7').hide()
        }
        if(g.length<8){
            $('#p9').show()
            $('#pwd').css({'border':'solid 2px red'})
            return false

        }
    
            else{
                $('#pwd').css({'border':'solid 2px black'})
                $('#p9').hide()
        }
  

       
       
       
       
       
       
       
       
       
       
       
        if(h.val()==""){
            $('#p8').show()
            $('#cpwd').css({'border':'solid 2px red'})
            return false
        }
        else{
            $('#cpwd').css({'border':'solid 2px black'})
            $('#p8').hide()
        }



    })


})