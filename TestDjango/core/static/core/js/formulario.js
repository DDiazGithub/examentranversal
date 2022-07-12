
$(document).ready(function(){
    $("#enviar").click(function(){
      var correo = $("#correo").val();
      var clave = $("#clave").val();

      if((correo.length == 0) || (clave.length == 0)){
        alert("Introducir nuevamente");
      }
      else{
        $(location).attr("href","http://www.google.cl")
      }
    });

    $("#crear").click(function(){
      var nombre = $("#nombre").val();
      var apellido = $("#apellido").val();
      var correo = $("#correo").val();
      var clave = $("#clave").val();
      if(nombre.length == 0){
          alert("Introduzca su nombre")
      }
      if(apellido.length == 0){
          alert("Introduzca su apellido")
      }
      if(correo.length == 0){
          alert("Introduzca su correo")
      }
      
      if(clave.length == 0){
          alert("Introduzca una clave")
      }
    });
      
    
})



