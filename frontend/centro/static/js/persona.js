

var url_api = 'http://localhost:9010/venta/';
var lo_path = 'personas/';

function leer() {
    var rut = document.getElementById('txRut').value;
    var pathUrl = url_api + lo_path + rut;

    $.ajax({
        type: "GET",
        async: false,
        url: pathUrl,
        cache: false,
        dataType: "json",
        beforeSend: function() {
            console.log('... cargando...');
        },
        error: function(data) {
            console.log('Tenemos problemas Houston ' + JSON.stringify(data));
            // Reset fields on error
            document.getElementById('txDv').value = "";
            document.getElementById('txNombre').value = "";
            document.getElementById('txPApellido').value = "";
            document.getElementById('txSApellido').value = "";
            document.getElementById('txEmail').value = "";
            document.getElementById('cbComuna').value = "";
            document.getElementById('cbGenero').value = "";
            document.getElementById('txFechaNacimiento').value = "";
            document.getElementById('cbPais').value = "";
            document.getElementById('txEstado').value = "";
            habilitaLeer();
        },
        success: function (data) {
            const json = data;
            if (!json) {
                console.log('No se recibió respuesta');
                return;
            }
        
            document.getElementById('txRut').value = json.rut;
            document.getElementById('txDv').value = json.dv;
            document.getElementById('txNombre').value = json.nombre;
            document.getElementById('txPApellido').value = json.papellido;
            document.getElementById('txSApellido').value = json.sapellido;
            document.getElementById('txEmail').value = json.email;
            document.getElementById('cbComuna').value = json.comuna;
            document.getElementById('cbGenero').value = json.genero;
            document.getElementById('txFechaNacimiento').value = json.fechaNacimiento;
            document.getElementById('cbPais').value = json.pais;
            // Asegúrate de manejar el valor null de fechaNacimiento si es necesario
            document.getElementById('txEstado').value = ""; // Ajusta según corresponda
        }
    });


    function empleadoActualizar(){
        var parametros=""
        // Creo Texto con los datos en formato json
        parametros = "{"
        parametros += ' "rut":"' + document.getElementById('txRut').value + '"';
        parametros += ',"dv":"' + document.getElementById('txDv').value + '"';
        parametros += ',"nombre":"' + document.getElementById('txNombres').value+ '"';
        parametros += ',"papellido":"' + document.getElementById('txPaterno').value+ '"';
        parametros += ',"sapellido":"' + document.getElementById('txMaterno').value+ '"';
        parametros += ',"email":"'  + document.getElementById('txEMail').value+ '"';
        parametros += ',"comuna":"'+ document.getElementById('cbComuna').value +'"' 
        parametros += ',"genero":"' + document.getElementById('cbGenero').value  +'"' 
        parametros += "}"
        //alert("hola" + parametros)
        //*********** Ejecuto Ajax Sincrónico
        $.ajax({
            type: "PUT",      // GET, PUT, POST, DELETE
            data: parametros,  // Envio deParámetro
            async: false,      // Sincrónico
            url: url_api + lo_path +  document.getElementById('txRut').value  ,  // Url de la API
            cache: false,
            dataType: "json",             // Formato de envio
            beforeSend: function (data){
                // Método de ejecuta antes de enviar
                console.log('... cargando...');
            }
            , error: function (data) {
                //alert("Error " + data)
                //si hay un error mostramos un mensaje
                console.log('Tenemos problemas Houston ' + JSON.stringify(data));
            },
            success: function (data) {
                json = data;
                // Si no es Ok envia Mensaje
                if (!json.OK){
                    alert(json.msg)
                    return
                }
                //alert("Success" + JSON.stringify(data))
                alert(json.msg)
                limpiar()
            }
        });
    }
}
function clienteActualizar(){
    var parametros=""
    // Creo Texto con los datos en formato json
    parametros = "{"
    parametros += ' "rut":"' + document.getElementById('txRut').value + '"';
    parametros += ',"dv":"' + document.getElementById('txDv').value + '"';
    parametros += ',"nombre":"' + document.getElementById('txNombres').value+ '"';
    parametros += ',"papellido":"' + document.getElementById('txPaterno').value+ '"';
    parametros += ',"sapellido":"' + document.getElementById('txMaterno').value+ '"';
    parametros += ',"email":"'  + document.getElementById('txEMail').value+ '"';
    parametros += ',"comuna":"'+ document.getElementById('cbComuna').value +'"' 
    parametros += ',"genero":"' + document.getElementById('cbGenero').value  +'"' 
    parametros += "}"
    //alert("hola" + parametros)
    //*********** Ejecuto Ajax Sincrónico
    $.ajax({
        type: "PUT",      // GET, PUT, POST, DELETE
        data: parametros,  // Envio deParámetro
        async: false,      // Sincrónico
        url: url_api + lo_path +  document.getElementById('txRut').value  ,  // Url de la API
        cache: false,
        dataType: "json",             // Formato de envio
        beforeSend: function (data){
            // Método de ejecuta antes de enviar
            console.log('... cargando...');
        }
        , error: function (data) {
            //alert("Error " + data)
            //si hay un error mostramos un mensaje
            console.log('Tenemos problemas Houston ' + JSON.stringify(data));
        },
        success: function (data) {
            json = data;
            // Si no es Ok envia Mensaje
            if (!json.OK){
                alert(json.msg)
                return
            }
            //alert("Success" + JSON.stringify(data))
            alert(json.msg)
            limpiar()
        }
    });
}

function habilitaLeer(){
    document.getElementById('btLeer').disabled=true
    document.getElementById('btModificar').disabled=false
    document.getElementById('btAgregar').disabled=false
    document.getElementById('btEliminar').disabled=false
    document.getElementById('btLimpiar').disabled=false

    document.getElementById('txRut').disabled=true
    document.getElementById('txDv').disabled=true
    document.getElementById('txNombres').disabled=false
    document.getElementById('txPaterno').disabled=false
    document.getElementById('txMaterno').disabled=false
    document.getElementById('txEMail').disabled=false
    document.getElementById('cbComuna').disabled=false
    document.getElementById('cbRegion').disabled=false
    document.getElementById('cbProvincia').disabled=false
    document.getElementById('cbGenero').disabled=false


}