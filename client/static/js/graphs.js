var data = [{
        period: '2010',
        Water_1: 0
    }, {
        period: '2011',
        Water_1: 130
    }, {
        period: '2012',
        Water_1: 80
    }, {
        period: '2013',
        Water_1: 70
    }, {
        period: '2014',
        Water_1: 180
    }, {
        period: '2015',
        Water_1: 105
    }, {
        period: '2016',
        Water_1: 250
    }];

Morris.Area({
    element: 'morris-area-water',
    data: data,
    xkey: 'period',
    ykeys: ['Water_1'],
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

var base_url = 'http://127.0.0.1:1337';
// TODO: if water graph is not removed from the project, create function to set it's data like the function below does for wind_graph
function LoadGraphData() {
    // Load json data to graphs
    console.log("Now updating data");
    $.get(base_url + "/storm", null,  // TODO: check if url is the path where the actual json is located
        function (data, textstatus, jqXHR) {
            console.log('Callback returned result of type ' + typeof(data) );
            console.log('Text message: ' + textstatus);
            graph_wind.setData(data);
        })
}

$( document ).ready(function() {
    console.log( "Now starting periodic data retrieval" );
    LoadGraphData();  // Ensure graph is properly loaded right away
    self.setInterval(LoadGraphData, 600000); // TODO: adjust to 30 min or 1 hour if necessary
});
