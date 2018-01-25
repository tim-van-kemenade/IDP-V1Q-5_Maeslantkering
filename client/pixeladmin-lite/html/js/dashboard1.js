Morris.Area({
    element: 'morris-area-chart2',
    data: [{
        period: '2010',
        Current: 0,
        AllTime: 0

    }, {
        period: '2011',
        Current: 130,
        AllTime: 100

    }, {
        period: '2012',
        Current: 80,
        AllTime: 60

    }, {
        period: '2013',
        Current: 70,
        AllTime: 200

    }, {
        period: '2014',
        Current: 180,
        AllTime: 150

    }, {
        period: '2015',
        Current: 105,
        AllTime: 90

    }, {
        period: '2016',
        Current: 250,
        AllTime: 150

    }],
    xkey: 'period',
    ykeys: ['Current', 'AllTime'],
    labels: ['Current', 'All Time'],
    pointSize: 0,
    fillOpacity: 0.7,
    pointStrokeColors: ['#cc1111', '#ff5637'],
    behaveLikeLine: true,
    gridLineColor: '#e0e0e0',
    lineWidth: 0,
    smooth: false,
    hideHover: 'auto',
    lineColors: ['#68b5cc', '#2d8eff'],
    resize: true

});

$(".counter").counterUp({
    delay: 100,
    time: 1200
});
