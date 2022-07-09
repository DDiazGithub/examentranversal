$("#formularioinicio").validate({
    rules: {
        correo:{
            required: true,
            email: true,
        },
        clave:{
            required: true,
            minlength:6,
            maxlength:20,
        }
    }
})



$("#enviar").click(function() {
    if ($("#formularioinicio").valid() == false) {
        return;
    }
    let correo = $("#correo").val()
    let clave = $("#clave").val()
})