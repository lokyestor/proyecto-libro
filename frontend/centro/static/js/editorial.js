

var url_api = 'http://localhost:9010/venta/';
var lo_path = 'editorial/';


function limpiarFormulario() {
    document.getElementById('idEditorial').value = '';
    document.getElementById('nombre').value = '';
}

function agregarEditorial() {
    var data = {
        idEditorial: document.getElementById('idEditorial').value,
        nombre: document.getElementById('nombre').value
    };

    $.ajax({
        type: "POST",
        url: url_api + lo_path,
        data: JSON.stringify(data),
        contentType: "application/json",
        dataType: "json",
        success: function(response) {
            console.log('Respuesta del servidor:', response);
            swal({
                title: "¡Éxito!",
                text: "Editorial agregada correctamente",
                icon: "success",
                button: "Aceptar"
            });
            limpiarFormulario();
        },
        error: function(xhr, status, error) {
            console.error('Error:', error);
            console.log('Detalles del error:', xhr.responseText);
            swal({
                title: "Error",
                text: "Error al agregar la editorial: " + xhr.responseText,
                icon: "error",
                button: "Aceptar"
            });
        }
    });
}

function mostrarMensaje(icono, titulo, mensaje) {
    Swal.fire({
        icon: icono,
        title: titulo,
        text: mensaje,
        showConfirmButton: false,
        timer: 1500
    });
}


function eliminarEditorial() {
    var idEditorial = document.getElementById('idEditorial').value;

    $.ajax({
        type: "DELETE",
        url: url_api + lo_path + idEditorial + '/',
        contentType: "application/json",
        dataType: "json",
        success: function(response) {
            console.log('Respuesta del servidor:', response);
            alert('Editorial eliminada correctamente');
            limpiarFormulario(); // Opcional: Limpia los campos después de eliminar la editorial
        },
        error: function(xhr, status, error) {
            console.error('Error:', error);
            console.log('Detalles del error:', xhr.responseText);
            alert('Error al eliminar editorial: ' + xhr.responseText);
        }
    });
}


{/* <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
function listarEditoriales() {
    $.ajax({
        type: "GET",
        url: url_api,
        dataType: "json",
        success: function(data) {
            var tbodyEditoriales = document.getElementById('editoriales-table').getElementsByTagName('tbody')[0];
            tbodyEditoriales.innerHTML = ''; // Limpiar contenido previo

            if (data.length === 0) {
                var newRow = tbodyEditoriales.insertRow();
                var cell = newRow.insertCell(0);
                cell.colSpan = 2;
                cell.textContent = 'No hay editoriales disponibles';
                return;
            }

            data.forEach(function(editorial) {
                var newRow = tbodyEditoriales.insertRow();
                newRow.insertCell(0).textContent = editorial.id;
                newRow.insertCell(1).textContent = editorial.nombre;
            });

            $('#listarEditorialesModal').modal('show'); // Mostrar el modal después de llenar las editoriales
        },
        error: function(xhr, status, error) {
            console.error('Error al obtener las editoriales:', error);
            alert('Hubo un problema al obtener las editoriales. Inténtalo de nuevo más tarde.');
        }
    });
} */}
