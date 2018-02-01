var base_url = 'http://192.168.42.1:1337';  // server url to send the command and request too
// below function executes forced command on server
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
// below function updates gate status
function UpdateGateStatus() {
    $.get(base_url + "/gate-status", null,
        function (data) {
            $('#gate-status').html(data.status);
        })
}

$(document).ready(function () {
    console.log("Now starting periodic data retrieval");
    UpdateGateStatus();  // get gate status at page load
    self.setInterval(UpdateGateStatus, 1000);  // update gate status every second

    // try to use commands with speech
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
            'show me the way': function () {
                RequestServerAction(base_url + '/reset-gate')
            }
        };

        annyang.addCommands(commands);
        annyang.start();
    }
    // easter egg to close gate with arrows in the website (force-close with audio)
    cheet('↑ ↑ ↓ ↓ ← → ← →', function () {
        var audio = new Audio('/static/sound/pass.mp3');
        audio.addEventListener('ended', function() {
            RequestServerAction(base_url + '/close-gate');
        });
        audio.play();
    });
});