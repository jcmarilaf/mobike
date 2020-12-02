//---------------------------------- API BIP -------------------------------------------------------
document.querySelector("#btnBuscar").addEventListener('click', function () {
    var numBip = document.getElementById("txtNumBip").value;
    console.log(numBip);
    obtener_registro(numBip);
});

function obtener_registro(numBip) {

    var datos = null;
    let url = 'http://bip-servicio.herokuapp.com/api/v1/solicitudes.json?bip=' + numBip;

    const api = new XMLHttpRequest();
    api.open('GET', url, true);
    api.send();


    api.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            let datos = JSON.parse(this.responseText);
            
            console.log(datos);
            console.log(datos.saldoTarjeta);

            var id = datos.id;
            var estado = datos.estadoContrato;
            var saldo = datos.saldoTarjeta;
            var fecha = datos.fechaSaldo;

            $('#id').html(id);
            $('#estado').html(estado);
            $('#saldo').html(saldo);
            $('#fecha').html(fecha);
        }
    };
    api.open("GET", url, true);
    api.send();
}