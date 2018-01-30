function RequestServerAction(url) {
    $.get(url, function (data, textstatus, jqXHR) {
        console.log('callback returned result of type ' + typeof(data) );
        console.log('text message: ' + textstatus);
    });
}

$('#open-gate').click(function () {
    console.log('Force opening gate');
    RequestServerAction('192.168.42.1:1337/open-gate');  // TODO: dunno if this works or not
});

$('#close-gate').click(function () {
    console.log('Force closing gate');
    RequestServerAction('192.168.42.1:1337/close-gate');  // TODO: same as previous todo
});

$('#reset-gate').click(function () {
    console.log('Force resetting gate');
    RequestServerAction('192.168.42.1:1337/reset-gate');  // TODO: same as previous todo
});
