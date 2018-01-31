var base_url = 'http://127.0.0.1:1337';

function RequestServerAction(url) {
    $.get(url, function (data, textstatus, jqXHR) {
        console.log('callback returned result of type ' + typeof(data));
        console.log('text message: ' + textstatus);
    });
}

$('#open-gate').click(function () {
    RequestServerAction(base_url + '/open-gate');
});

$('#close-gate').click(function () {
    RequestServerAction(base_url + '/close-gate');
});

$('#reset-gate').click(function () {
    RequestServerAction(base_url + '/reset-gate');
});

function UpdateGateStatus() {
    console.log("Now updating gate status");
    $.get(base_url + "/gate-status", null,
        function (data) {
            $('#gate-status').html(data.status);
        })
}

$(document).ready(function () {
    console.log("Now starting periodic data retrieval");
    UpdateGateStatus();  // Ensure graph is properly loaded right away
    self.setInterval(UpdateGateStatus, 1000);
});
