var map;
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: -33.448310, lng: -70.551795 },
        zoom: 14,
    });

    var marker = new google.maps.Marker({
        position: { lat: -33.448310, lng: -70.551795 },
        map: map,
        title: 'Estacionamiento Mobike'
    });
    var marker = new google.maps.Marker({
        position: { lat: -33.444183, lng: -70.545626 },
        map: map,
        title: 'Estacionamiento Mobike'
    });
    var marker = new google.maps.Marker({
        position: { lat: -33.444941, lng: -70.536780 },
        map: map,
        title: 'Estacionamiento Mobike'
    });
    var marker = new google.maps.Marker({
        position: { lat: -33.428914, lng: -70.546241 },
        map: map,
        title: 'Estacionamiento Mobike'
    });

    var marker = new google.maps.Marker({
        position: { lat: -33.453745, lng: -70.564002 },
        map: map,
        title: 'Estacionamiento Mobike'
    });

    var marker = new google.maps.Marker({
        position: { lat: -33.451408, lng: -70.571200 },
        map: map,
        title: 'Estacionamiento Mobike'
    });

    var marker = new google.maps.Marker({
        position: { lat: -33.457642, lng:  -70.560288},
        map: map,
        title: 'Estacionamiento Mobike'
    });

    var marker = new google.maps.Marker({
        position: { lat: -33.449184, lng:  -70.539855},
        map: map,
        title: 'Estacionamiento Mobike'
    });

    var marker = new google.maps.Marker({
        position: { lat: -33.434606 , lng:  -70.550843},
        map: map,
        title: 'Estacionamiento Mobike'
    });

    var marker = new google.maps.Marker({
        position: { lat:  -33.435375, lng:  -70.573712},
        map: map,
        title: 'Estacionamiento Mobike'
    });

    var marker = new google.maps.Marker({
        position: { lat: -33.445429 , lng:  -70.571748 },
        map: map,
        title: 'Estacionamiento Mobike'
    });

    var marker = new google.maps.Marker({
        position: { lat:  -33.443106, lng:  -70.559777},
        map: map,
        title: 'Estacionamiento Mobike'
    });
}