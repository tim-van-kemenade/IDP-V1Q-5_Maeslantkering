/*
Template Name: Admin Pro Admin
Author: Wrappixel
Email: niravjoshi87@gmail.com
File: js
*/

    // ============================================================== 
    // Sales chart
    // ============================================================== 
    Morris.Area({
        element: 'sales-chart',
        data: [{
                period: 'Past hour',
                Sales: 50,
                Earning: 80,
                Marketing: 20
            }, {
                period: '2 hours ago',
                Sales: 130,
                Earning: 100,
                Marketing: 80
            }, {
                period: '3 hours ago',
                Sales: 80,
                Earning: 60,
                Marketing: 70
            }, {
                period: '4 hours ago',
                Sales: 70,
                Earning: 200,
                Marketing: 140
            }, {
                period: '5 hours ago',
                Sales: 180,
                Earning: 150,
                Marketing: 140
            }, {
                period: '6 hours ago',
                Sales: 105,
                Earning: 100,
                Marketing: 80
            },
            {
                period: '7 hours ago',
                Sales: 250,
                Earning: 150,
                Marketing: 200
            }
        ],
        xkey: 'period',
        ykeys: ['Sales', 'Earning', 'Marketing'],
        labels: ['Site A', 'Site B', 'Site C'],
        pointSize: 0,
        fillOpacity: 0,
        pointStrokeColors: ['#20aee3', '#24d2b5', '#6772e5'],
        behaveLikeLine: true,
        gridLineColor: '#e0e0e0',
        lineWidth: 3,
        hideHover: 'auto',
        lineColors: ['#20aee3', '#24d2b5', '#6772e5'],
        xLabelAngle: 50,  // These lines were added by the IDP groups SIE department
        parseTime: false, // It is to make the x-axis contain text and change the angle at which they are displayed.
        gridTextSize: 15, // Also the text is re-sized to improve readability.
        resize: true

    });

$(".counter").counterUp({
    delay: 100,
    time: 1200
});