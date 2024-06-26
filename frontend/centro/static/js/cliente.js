    var url_api = 'http://localhost:9010/venta/';
    var lo_path = 'personas/';
    var pais_path = 'pais/';
    var comuna_path = 'comuna/';
    var genero_path = 'generos/';
    var estado_path = 'estado/';


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
            success: function(data) {
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
    }

    function habilitaLeer(){
        document.getElementById('btLeer').disabled = true;
        document.getElementById('btModificar').disabled = false;
        document.getElementById('btAgregar').disabled = false;
        document.getElementById('btEliminar').disabled = false;
        document.getElementById('btLimpiar').disabled = false;

        document.getElementById('txRut').disabled = true;
        document.getElementById('txDv').disabled = true;
        document.getElementById('txNombres').disabled = false;
        document.getElementById('txPaterno').disabled = false;
        document.getElementById('txMaterno').disabled = false;
        document.getElementById('txEMail').disabled = false;
        document.getElementById('cbComuna').disabled = false;
        document.getElementById('cbRegion').disabled = false;
        document.getElementById('cbProvincia').disabled = false;
        document.getElementById('cbGenero').disabled = false;
    }

    function agregar() {
        var data = {
            rut: document.getElementById('txRut').value,
            dv: document.getElementById('txDv').value,
            nombre: document.getElementById('txNombre').value,
            papellido: document.getElementById('txPApellido').value,
            sapellido: document.getElementById('txSApellido').value,
            email: document.getElementById('txEmail').value,
            fechaNacimiento: document.getElementById('txFechaNacimiento').value,
            pais: document.getElementById('cbPais').value,
            comuna: document.getElementById('cbComuna').value,
            genero: document.getElementById('cbGenero').value,
            estado: document.getElementById('txEstado').value,
        };

        $.ajax({
            type: "POST",
            url: url_api + lo_path,
            data: JSON.stringify(data),
            contentType: "application/json",
            dataType: "json",
            success: function(response) {
                if (!response.OK) {
                    alert(response.msg);
                    return;
                }
                alert('Cliente agregado correctamente');
                limpiar(); // Limpia los campos después de agregar el cliente
            },
            error: function(xhr, status, error) {
                console.error('Error:', error);
                console.log('Detalles del error:', xhr.responseText);
                alert('Error al agregar cliente: ' + xhr.responseText);
            }
        });
    }

    function actualizar() {
        var rut = document.getElementById('txRut').value;
        var data = {
            rut: rut,
            dv: document.getElementById('txDv').value,
            nombre: document.getElementById('txNombre').value,
            papellido: document.getElementById('txPApellido').value,
            sapellido: document.getElementById('txSApellido').value,
            email: document.getElementById('txEmail').value,
            fechaNacimiento: document.getElementById('txFechaNacimiento').value,
            pais: document.getElementById('cbPais').value,
            comuna: document.getElementById('cbComuna').value,
            genero: document.getElementById('cbGenero').value,
            estado: document.getElementById('txEstado').value,
        };

        $.ajax({
            type: "PUT",
            url: url_api + lo_path + rut,
            data: JSON.stringify(data),
            contentType: "application/json",
            dataType: "json",
            success: function(response) {
                if (!response.OK) {
                    alert(response.msg);
                    return;
                }
                alert('Cliente actualizado correctamente');
            },
            error: function(xhr, status, error) {
                console.error('Error:', error);
                console.log('Detalles del error:', xhr.responseText);
                alert('Error al actualizar cliente: ' + xhr.responseText);
            }
        });
    }

    function eliminar() {
        var rut = document.getElementById('txRut').value;

        $.ajax({
            type: "DELETE",
            url: url_api + lo_path + rut,
            dataType: "json",
            success: function(response) {
                if (!response.OK) {
                    alert(response.msg);
                    return;
                }
                alert('Cliente eliminado correctamente');
            },
            error: function(xhr, status, error) {
                console.error('Error:', error);
                console.log('Detalles del error:', xhr.responseText);
                alert('Error al eliminar cliente: ' + xhr.responseText);
            }
        });
    }

    function limpiar() {
        document.getElementById('txRut').value = "";
        document.getElementById('txDv').value = "";
        document.getElementById('txNombre').value = "";
        document.getElementById('txPApellido').value = "";
        document.getElementById('txSApellido').value = "";
        document.getElementById('txEmail').value = "";
        document.getElementById('txFechaNacimiento').value = "";
        document.getElementById('cbPais').value = "";
        document.getElementById('cbComuna').value = "";
        document.getElementById('cbGenero').value = "";
        document.getElementById('txEstado').value = "";
    }