var base_url = 'http://127.0.0.1:1337';

function RequestServerAction(url) {
    $.get(url, function (data, textstatus, jqXHR) {
        console.log('callback returned result of type ' + typeof(data) );
        console.log('text message: ' + textstatus);
    });
}

$('#open-gate').click(function () {
    console.log('Force opening gate');
    RequestServerAction(base_url + '/open-gate');  // TODO: dunno if this works or not
});

$('#close-gate').click(function () {
    console.log('Force closing gate');
    RequestServerAction(base_url + '/close-gate');  // TODO: same as previous todo
});

$('#reset-gate').click(function () {
    console.log('Force resetting gate');
    RequestServerAction(base_url + '/reset-gate');  // TODO: same as previous todo
});

function UpdateGateStatus() {
    console.log("Now updating gate status");
    $.get(base_url + "/gate-status", null,  // TODO: check if url is the path where the actual json is located
        function (data, textstatus, jqXHR) {
            console.log(data);
            $('#gate-status').html(data.status);
            console.log('Updated gate status')
        })
}

$( document ).ready(function() {
    console.log( "Now starting periodic data retrieval" );
    UpdateGateStatus();  // Ensure graph is properly loaded right away
    self.setInterval(UpdateGateStatus, 1000);
});
