var base_url = 'http://192.168.42.1:1337';

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
    $.get(base_url + "/gate-status", null,
        function (data) {
            $('#gate-status').html(data.status);
        })
}

$(document).ready(function () {
    console.log("Now starting periodic data retrieval");
    UpdateGateStatus();  // Ensure graph is properly loaded right away
    self.setInterval(UpdateGateStatus, 1000);


    if (annyang) {
        console.log('Listening!');
        // Let's define our first command. First the text we expect, and then the function it should call
        var commands = {
            'open the gate': function () {
                console.log('OPEN!');
                RequestServerAction(base_url + '/open-gate');
            },
            'close the gate': function () {
                console.log('CLOSING!');
                RequestServerAction(base_url + '/close-gate');
            },
            'reset the gate': function() {
                RequestServerAction(base_url + '/reset-gate')
            }
        };

        annyang.addCommands(commands);
        annyang.start();
    }
});