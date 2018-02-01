var base_url = 'http://192.168.42.1:1337';

$.ajax({
    url: base_url + '/water',
    success: function (data) {
        console.log(data);
        Morris.Area({
            element: 'morris-area-water',
            data: data,
            xkey: 'epoch',
            ykeys: ['average_height'],
            labels: ['Current height'],
            pointSize: 0,
            fillOpacity: 0.7,
            pointStrokeColors: ['#2153ff'],
            behaveLikeLine: true,
            gridLineColor: '#e0e0e0',
            lineWidth: 0,
            smooth: false,
            hideHover: 'auto',
            lineColors: ['#2153ff'],
            resize: true

        });
    }
});

var graph_wind = Morris.Area({
    element: 'morris-area-wind',
    data: [{
        period: 'No date',
        wind_speed: 0,
        wind_burst: 0
    }, {
        period: 'No date',
        wind_speed: 0,
        wind_burst: 0
    }, {
        period: 'No date',
        wind_speed: 0,
        wind_burst: 0
    }, {
        period: 'No date',
        wind_speed: 0,
        wind_burst: 0
    }, {
        period: 'No date',
        wind_speed: 0,
        wind_burst: 0
    }, {
        period: 'No date',
        wind_speed: 0,
        wind_burst: 0
    },
        {
            period: 'No date',
            wind_speed: 0,
            wind_burst: 0
        }
    ],
    xkey: 'period',
    ykeys: ['wind_speed', 'wind_burst'],
    labels: ['Burst', 'Speed'],
    pointSize: 0,
    fillOpacity: 0,
    pointStrokeColors: ['#cc1111', '#24d2b5'],
    behaveLikeLine: true,
    gridLineColor: '#e0e0e0',
    lineWidth: 3,
    hideHover: 'auto',
    lineColors: ['#cc1111', '#24d2b5'],
    xLabelAngle: 50,
    parseTime: false,
    gridTextSize: 15,
    resize: true

});
function LoadGraphData() {
    // Load json data to graphs
    console.log("Now updating data");
    $.get(base_url + "/storm", null,
        // execute function below if response is received
        // graph shows less datapoints if database doesn't contain enough information (rows)
        function (data, textstatus) {
            console.log(data);
            console.log('Callback returned result of type ' + typeof(data));
            console.log('Text message: ' + textstatus);
            // set all initial values
            var json = data;
            console.log(json);
            var data_set = [];
            var time = 0;
            var speed = 0;
            var burst = 0;
            var count = 0;
            // start for loop through all received elements
            // received JSON should contain 42 rows
            // index is index for received JSON
            for (var index = 0; index < 42; index++) {
                // get graph data based on their index in the array and key in their respective object
                // total is calculated and later the average is taken, then a reset happens count start over
                time += json[index].epoch;
                speed += json[index].windsnelheidMS;
                burst += json[index].windstotenMS;
                count += 1;
                // count to six if count is 6 then take average and write to object
                if (count === 6) {
                    count = 0;
                    console.log(time);
                    var dict = {};
                    // create date object
                    var date = new Date((time / 6)*1000);
                    var hours = date.getHours();
                    var minutes = date.getMinutes();
                    var seconds = date.getSeconds();
                    // format data object and put it into object with key period
                    dict.period = hours + ':' + minutes + ':' + seconds;
                    // take wind speed average and put it into object with key wind_speed
                    dict.wind_speed = speed / 6;
                    // take wind burst average and put it into object with key wind_burst
                    dict.wind_burst = burst / 6;
                    console.log('gonna print this dict');
                    console.log(dict);
                    console.log('printed dict');
                    // add object to array this happens a total of 7 times which create 7 datapoints
                    data_set.push(dict);
                    console.log(data_set);
                    graph_wind.setData(data_set);
                    // reset counts to start over
                    time = 0;
                    speed = 0;
                    burst = 0;
                }
            }
            console.log(data_set);
            // put array with correct object into the wind_graph
            graph_wind.setData(data_set);
        })
}

$(document).ready(function () {
    console.log("Now starting periodic data retrieval");
    LoadGraphData();  // Ensure graph is properly loaded right away
    self.setInterval(LoadGraphData, 600000);  // reload graph each 10 minutes
});
