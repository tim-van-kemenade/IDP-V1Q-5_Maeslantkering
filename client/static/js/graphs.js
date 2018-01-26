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
            period: 'Past hour',
            Wind_1: 50,
            Wind_2: 80
        }, {
            period: '2 hours ago',
            Wind_1: 130,
            Wind_2: 100
        }, {
            period: '3 hours ago',
            Wind_1: 80,
            Wind_2: 60
        }, {
            period: '4 hours ago',
            Wind_1: 70,
            Wind_2: 200
        }, {
            period: '5 hours ago',
            Wind_1: 180,
            Wind_2: 150
        }, {
            period: '6 hours ago',
            Wind_1: 105,
            Wind_2: 100
        },
        {
            period: '7 hours ago',
            Wind_1: 250,
            Wind_2: 150
        }
    ],
    xkey: 'period',
    ykeys: ['Wind_1', 'Wind_2'],
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

$(".counter").counterUp({
    delay: 100,
    time: 1200
});
