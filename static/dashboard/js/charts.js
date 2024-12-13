document.addEventListener("DOMContentLoaded", () => {
    const dir = document.documentElement.getAttribute("dir");
    const theme = document.body.classList.contains("dark") ? "dark" : "light";
    const assetSeries = [{
        data: [
            [1327359600000, 30.95],
            [1327446000000, 31.34],
            [1327532400000, 31.18],
            [1327618800000, 31.05],
            [1327878000000, 31.0],
            [1327964400000, 30.95],
            [1328050800000, 31.24],
            [1328137200000, 31.29],
            [1328223600000, 31.85],
            [1328482800000, 31.86],
            [1328569200000, 32.28],
            [1328655600000, 32.1],
            [1328742000000, 32.65],
            [1328828400000, 32.21],
            [1329087600000, 32.35],
            [1329174000000, 32.44],
            [1329260400000, 32.46],
            [1329346800000, 32.86],
            [1329433200000, 32.75],
            [1329778800000, 32.54],
            [1329865200000, 32.33],
            [1329951600000, 32.97],
            [1330038000000, 33.41],
            [1330297200000, 33.27],
            [1330383600000, 33.27],
            [1330470000000, 32.89],
            [1330556400000, 33.1],
            [1330642800000, 33.73],
            [1330902000000, 33.22],
            [1330988400000, 31.99],
            [1331074800000, 32.41],
            [1331161200000, 33.05],
            [1331247600000, 33.64],
            [1331506800000, 33.56],
            [1331593200000, 34.22],
            [1331679600000, 33.77],
            [1331766000000, 34.17],
            [1331852400000, 33.82],
            [1332111600000, 34.51],
            [1332198000000, 33.16],
            [1332284400000, 33.56],
            [1332370800000, 33.71],
            [1332457200000, 33.81],
            [1332712800000, 34.4],
            [1332799200000, 34.63],
            [1332885600000, 34.46],
            [1332972000000, 34.48],
            [1333058400000, 34.31],
            [1333317600000, 34.7],
            [1333404000000, 34.31],
            [1333490400000, 33.46],
            [1333576800000, 33.59],
            [1333922400000, 33.22],
            [1334008800000, 32.61],
            [1334095200000, 33.01],
            [1334181600000, 33.55],
            [1334268000000, 33.18],
            [1334527200000, 32.84],
            [1334613600000, 33.84],
            [1334700000000, 33.39],
            [1334786400000, 32.91],
            [1334872800000, 33.06],
            [1335132000000, 32.62],
            [1335218400000, 32.4],
            [1335304800000, 33.13],
            [1335391200000, 33.26],
            [1335477600000, 33.58],
            [1335736800000, 33.55],
            [1335823200000, 33.77],
            [1335909600000, 33.76],
            [1335996000000, 33.32],
            [1336082400000, 32.61],
            [1336341600000, 32.52],
            [1336428000000, 32.67],
            [1336514400000, 32.52],
            [1336600800000, 31.92],
            [1336687200000, 32.2],
            [1336946400000, 32.23],
            [1337032800000, 32.33],
            [1337119200000, 32.36],
            [1337205600000, 32.01],
            [1337292000000, 31.31],
            [1337551200000, 32.01],
            [1337637600000, 32.01],
            [1337724000000, 32.18],
            [1337810400000, 31.54],
            [1337896800000, 31.6],
            [1338242400000, 32.05],
            [1338328800000, 31.29],
            [1338415200000, 31.05],
            [1338501600000, 29.82],
            [1338760800000, 30.31],
            [1338847200000, 30.7],
            [1338933600000, 31.69],
            [1339020000000, 31.32],
            [1339106400000, 31.65],
            [1339365600000, 31.13],
            [1339452000000, 31.77],
            [1339538400000, 31.79],
            [1339624800000, 31.67],
            [1339711200000, 32.39],
            [1339970400000, 32.63],
            [1340056800000, 32.89],
            [1340143200000, 31.99],
            [1340229600000, 31.23],
            [1340316000000, 31.57],
            [1340575200000, 30.84],
            [1340661600000, 31.07],
            [1340748000000, 31.41],
            [1340834400000, 31.17],
            [1340920800000, 32.37],
            [1341180000000, 32.19],
            [1341266400000, 32.51],
            [1341439200000, 32.53],
            [1341525600000, 31.37],
            [1341784800000, 30.43],
            [1341871200000, 30.44],
            [1341957600000, 30.2],
            [1342044000000, 30.14],
            [1342130400000, 30.65],
            [1342389600000, 30.4],
            [1342476000000, 30.65],
            [1342562400000, 31.43],
            [1342648800000, 31.89],
            [1342735200000, 31.38],
            [1342994400000, 30.64],
            [1343080800000, 30.02],
            [1343167200000, 30.33],
            [1343253600000, 30.95],
            [1343340000000, 31.89],
            [1343599200000, 31.01],
            [1343685600000, 30.88],
            [1343772000000, 30.69],
            [1343858400000, 30.58],
            [1343944800000, 32.02],
            [1344204000000, 32.14],
            [1344290400000, 32.37],
            [1344376800000, 32.51],
            [1344463200000, 32.65],
            [1344549600000, 32.64],
            [1344808800000, 32.27],
            [1344895200000, 32.1],
            [1344981600000, 32.91],
            [1345068000000, 33.65],
            [1345154400000, 33.8],
            [1345413600000, 33.92],
            [1345500000000, 33.75],
            [1345586400000, 33.84],
            [1345672800000, 33.5],
            [1345759200000, 32.26],
            [1346018400000, 32.32],
            [1346104800000, 32.06],
            [1346191200000, 31.96],
            [1346277600000, 31.46],
            [1346364000000, 31.27],
            [1346709600000, 31.43],
            [1346796000000, 32.26],
            [1346882400000, 32.79],
            [1346968800000, 32.46],
            [1347228000000, 32.13],
            [1347314400000, 32.43],
            [1347400800000, 32.42],
            [1347487200000, 32.81],
            [1347573600000, 33.34],
            [1347832800000, 33.41],
            [1347919200000, 32.57],
            [1348005600000, 33.12],
            [1348092000000, 34.53],
            [1348178400000, 33.83],
            [1348437600000, 33.41],
            [1348524000000, 32.9],
            [1348610400000, 32.53],
            [1348696800000, 32.8],
            [1348783200000, 32.44],
            [1349042400000, 32.62],
            [1349128800000, 32.57],
            [1349215200000, 32.6],
            [1349301600000, 32.68],
            [1349388000000, 32.47],
            [1349647200000, 32.23],
            [1349733600000, 31.68],
            [1349820000000, 31.51],
            [1349906400000, 31.78],
            [1349992800000, 31.94],
            [1350252000000, 32.33],
            [1350338400000, 33.24],
            [1350424800000, 33.44],
            [1350511200000, 33.48],
            [1350597600000, 33.24],
            [1350856800000, 33.49],
            [1350943200000, 33.31],
            [1351029600000, 33.36],
            [1351116000000, 33.4],
            [1351202400000, 34.01],
            [1351638000000, 34.02],
            [1351724400000, 34.36],
            [1351810800000, 34.39],
            [1352070000000, 34.24],
            [1352156400000, 34.39],
            [1352242800000, 33.47],
            [1352329200000, 32.98],
            [1352415600000, 32.9],
            [1352674800000, 32.7],
            [1352761200000, 32.54],
            [1352847600000, 32.23],
            [1352934000000, 32.64],
            [1353020400000, 32.65],
            [1353279600000, 32.92],
            [1353366000000, 32.64],
            [1353452400000, 32.84],
            [1353625200000, 33.4],
            [1353884400000, 33.3],
            [1353970800000, 33.18],
            [1354057200000, 33.88],
            [1354143600000, 34.09],
            [1354230000000, 34.61],
            [1354489200000, 34.7],
            [1354575600000, 35.3],
            [1354662000000, 35.4],
            [1354748400000, 35.14],
            [1354834800000, 35.48],
            [1355094000000, 35.75],
            [1355180400000, 35.54],
            [1355266800000, 35.96],
            [1355353200000, 35.53],
            [1355439600000, 37.56],
            [1355698800000, 37.42],
            [1355785200000, 37.49],
            [1355871600000, 38.09],
            [1355958000000, 37.87],
            [1356044400000, 37.71],
            [1356303600000, 37.53],
            [1356476400000, 37.55],
            [1356562800000, 37.3],
            [1356649200000, 36.9],
            [1356908400000, 37.68],
            [1357081200000, 38.34],
            [1357167600000, 37.75],
            [1357254000000, 38.13],
            [1357513200000, 37.94],
            [1357599600000, 38.14],
            [1357686000000, 38.66],
            [1357772400000, 38.62],
            [1357858800000, 38.09],
            [1358118000000, 38.16],
            [1358204400000, 38.15],
            [1358290800000, 37.88],
            [1358377200000, 37.73],
            [1358463600000, 37.98],
            [1358809200000, 37.95],
            [1358895600000, 38.25],
            [1358982000000, 38.1],
            [1359068400000, 38.32],
            [1359327600000, 38.24],
            [1359414000000, 38.52],
            [1359500400000, 37.94],
            [1359586800000, 37.83],
            [1359673200000, 38.34],
            [1359932400000, 38.1],
            [1360018800000, 38.51],
            [1360105200000, 38.4],
            [1360191600000, 38.07],
            [1360278000000, 39.12],
            [1360537200000, 38.64],
            [1360623600000, 38.89],
            [1360710000000, 38.81],
            [1360796400000, 38.61],
            [1360882800000, 38.63],
            [1361228400000, 38.99],
            [1361314800000, 38.77],
            [1361401200000, 38.34],
            [1361487600000, 38.55],
            [1361746800000, 38.11],
            [1361833200000, 38.59],
            [1361919600000, 39.6],
        ],
    }, ];
    // Progress chart
    const progressCharts = document.querySelectorAll(".progress-chart");
    if (progressCharts.length) {
        progressCharts.forEach((el) => {
            const chart = new ApexCharts(el, {
                chart: {
                    type: "radialBar",
                    width: "45%",
                    height: 140,
                    sparkline: {
                        enabled: false,
                    },
                },
                series: ["33.5"],
                legend: {
                    show: false,
                },
                stroke: {
                    lineCap: "round",
                },
                colors: ["#20B757"],
                plotOptions: {
                    radialBar: {
                        dataLabels: {
                            value: {
                                show: false,
                            },
                            name: {
                                offsetY: 5,
                            },
                        },
                        hollow: {
                            size: "55%",
                        },
                    },
                },
                labels: ["33.5%"],
            });
            chart.render();
        });
    }

    const assetChartEl = document.getElementById("asset-chart");
    if (assetChartEl) {
        const chartData = {
            chart: {
                id: "area-datetime",
                type: "area",
                height: 350,
                zoom: {
                    autoScaleYaxis: true,
                },
                toolbar: {
                    show: false,
                },
            },
            series: assetSeries,
            stroke: {
                width: 2,
                colors: ["#20B757"],
                curve: "smooth",
            },
            dataLabels: {
                enabled: false,
            },
            markers: {
                size: 0,
            },
            xaxis: {
                type: "datetime",
                min: new Date("01 Mar 2012").getTime(),
                tickAmount: 6,
                axisBorder: {
                    show: false,
                },
            },
            yaxis: {
                labels: {
                    offsetX: dir == "rtl" ? -40 : -17,
                },
            },
            tooltip: {
                x: {
                    format: "dd MMM yyyy",
                },
            },
            colors: ["#20B757"],
            fill: {
                type: "gradient",
                gradient: {
                    shadeIntensity: 1,
                    opacityFrom: 0.8,
                    opacityTo: 0.1,
                    stops: [0, 100],
                },
            },
            grid: {
                strokeDashArray: 5,
                padding: {
                    left: -6,
                },
            },
            responsive: [{
                breakpoint: 992,
                options: {
                    chart: {
                        height: 300,
                    },
                },
            }, ],
        };

        const chart = new ApexCharts(assetChartEl, chartData);
        chart.render();
        const resetCssClasses = function(activeEl) {
            const els = document.querySelectorAll(".asset-btn");
            Array.prototype.forEach.call(els, function(el) {
                el.classList.remove("active");
            });

            activeEl.target.classList.add("active");
        };

        document
            .querySelector("#one_month")
            .addEventListener("click", function(e) {
                resetCssClasses(e);

                chart.zoomX(
                    new Date("28 Jan 2013").getTime(),
                    new Date("27 Feb 2013").getTime()
                );
            });

        document
            .querySelector("#six_months")
            .addEventListener("click", function(e) {
                resetCssClasses(e);

                chart.zoomX(
                    new Date("27 Sep 2012").getTime(),
                    new Date("27 Feb 2013").getTime()
                );
            });

        document.querySelector("#one_year").addEventListener("click", function(e) {
            resetCssClasses(e);
            chart.zoomX(
                new Date("27 Feb 2012").getTime(),
                new Date("27 Feb 2013").getTime()
            );
        });

        document.querySelector("#ytd").addEventListener("click", function(e) {
            resetCssClasses(e);

            chart.zoomX(
                new Date("01 Jan 2013").getTime(),
                new Date("27 Feb 2013").getTime()
            );
        });

        document.querySelector("#all").addEventListener("click", function(e) {
            resetCssClasses(e);

            chart.zoomX(
                new Date("23 Jan 2012").getTime(),
                new Date("27 Feb 2013").getTime()
            );
        });
    }

    const style2StatChartEl = document.querySelectorAll(".style2-stats-chart");
    if (style2StatChartEl) {
        style2StatChartEl.forEach((el) => {
            const chart = new ApexCharts(el, {
                chart: {
                    height: "60",
                    type: "area",
                    sparkline: {
                        enabled: true,
                    },
                    toolbar: {
                        show: false,
                    },
                    animations: {
                        enabled: true,
                        easing: "easeinout",
                        speed: 800,
                    },
                },
                grid: {
                    show: false,
                },
                dataLabels: {
                    enabled: false,
                },
                stroke: {
                    width: 2,
                    curve: "smooth",
                },
                series: [{
                    name: "Series 1",
                    data: [
                        24, 26, 32, 36, 37, 44, 50, 49, 44, 40, 32, 28, 32, 34, 28, 23,
                        22, 28, 34, 35,
                    ],
                }, ],
                tooltip: {
                    enabled: false,
                },
                colors: ["#20B757"],
                fill: {
                    colors: ["#20B757"],
                    opacity: 1,
                    type: "gradient",
                    gradient: {
                        shade: "dark",
                        type: "vertical",
                        shadeIntensity: 0.3,
                        gradientToColors: undefined,
                        inverseColors: false,
                        opacityFrom: 0.4,
                        opacityTo: 0,
                        stops: [0, 100],
                        colorStops: [],
                    },
                },
                xaxis: {
                    tooltip: {
                        enabled: false,
                    },
                    axisBorder: {
                        show: false,
                    },
                    axisTicks: {
                        show: false,
                    },
                    labels: {
                        show: false,
                    },
                },
                yaxis: {
                    min: 0,
                    max: 50,
                    tooltip: {
                        enabled: false,
                        // followCursor: true
                    },
                    labels: {
                        show: false,
                    },
                },
            });
            chart.render();
        });
    }
    // Home 2 income chart
    const incomeChart = document.querySelector(".income-chart");
    if (incomeChart) {
        const chartData = {
            series: [{
                    name: "Total Income",
                    type: "line",
                    data: [20, 38, 38, 73, 55, 63, 44, 75, 53, 80, 40, 80],
                },
                {
                    name: "Total Expense",
                    type: "line",
                    data: [85, 66, 76, 38, 86, 35, 62, 40, 40, 64, 50, 87],
                },
            ],
            chart: {
                height: 300,
                type: "line",
                toolbar: {
                    show: false,
                },
            },
            legend: {
                show: false,
            },
            colors: ["#63CC8A", "#FFC861"],
            stroke: {
                width: [3, 3],
                curve: "smooth",
                lineCap: "round",
                dashArray: [0, 5],
            },
            xaxis: {
                type: "category",
                categories: [
                    "Jan",
                    "Feb",
                    "Mar",
                    "Apr",
                    "May",
                    "Jun",
                    "Jul",
                    "Aug",
                    "Sep",
                    "Oct",
                    "Nov",
                    "Dec",
                ],
                tickAmount: 12,
                labels: {},
                axisTicks: {
                    show: false,
                },
                axisBorder: {
                    show: false,
                },
            },
            yaxis: {
                min: 0,
                max: 100,
                tickAmount: 5,
                labels: {
                    offsetX: -17,
                },
            },
            fill: {
                opacity: 1,
            },
            grid: {
                padding: {
                    left: -10,
                    bottom: -10,
                },
                show: true,
                xaxis: {
                    lines: {
                        show: true,
                    },
                },
            },
            responsive: [{
                    breakpoint: 768,
                    options: {
                        chart: {
                            height: 300,
                        },
                    },
                },
                {
                    breakpoint: 570,
                    options: {
                        chart: {
                            height: 240,
                        },
                    },
                },
            ],
        };
        const chart = new ApexCharts(incomeChart, chartData);
        chart.render();
    }

    const transactionOverviewHome3 = document.querySelector(
        ".transaction-overview-home3"
    );
    if (transactionOverviewHome3) {
        const chartData = {
            chart: {
                width: "100%",
                height: 350,
                type: "line",
                toolbar: {
                    show: false,
                },
                animations: {
                    enabled: true,
                    easing: "easeinout",
                    speed: 800,
                },
            },
            series: [{
                    name: "Website Blog",
                    type: "column",
                    data: [40, 50, 44, 31, 22, 43, 20, 35, 22, 32, 30, 16],
                },
                {
                    name: "chart 2",
                    type: "area",
                    data: [15, 28, 20, 25, 18, 30, 22, 36, 32, 46, 30, 27],
                },
                {
                    name: "Social Media",
                    type: "line",
                    data: [5, 8, 6, 5, 7, 8, 7, 6, 8, 4, 6, 3],
                },
            ],
            plotOptions: {
                bar: {
                    columnWidth: window.innerWidth < 768 ?
                        "10" :
                        window.innerWidth < 1400 ?
                        "13" :
                        "20",
                    dataLabels: {
                        position: "center",
                    },
                },
            },
            dataLabels: {
                enabled: false,
            },
            stroke: {
                width: [0, 3, 3],
                colors: ["#20B757", "#FFC861", "#4371E9"],
                dashArray: [0, 0, 10],
                curve: ["straight", "straight", "smooth"],
            },

            legend: {
                show: false,
            },
            xaxis: {
                categories: [
                    "Jan",
                    "Feb",
                    "Mar",
                    "Apr",
                    "May",
                    "Jun",
                    "Jul",
                    "Aug",
                    "Sep",
                    "Oct",
                    "Nov",
                    "Dec",
                ],
                axisBorder: {
                    show: false,
                },
            },
            yaxis: [{
                    seriesName: "Website Blog",
                    labels: {
                        offsetX: -40,
                        show: window.innerWidth > 768 ? true : false,
                    },
                },
                {
                    seriesName: "chart 2",
                    max: 70,
                    labels: {
                        show: false,
                    },
                },
                {
                    seriesName: "Social Media",
                    max: 30,
                    labels: {
                        show: false,
                    },
                },
            ],
            colors: ["#20B757", "#FFC861"],
            fill: {
                colors: ["#20B757", "#FFC861", "#4371E9"],
                opacity: [1, 0.1, 1],
            },
            responsive: [{
                    breakpoint: 1500,
                    options: {
                        chart: {
                            height: 300,
                        },
                    },
                },
                {
                    breakpoint: 992,
                    options: {
                        chart: {
                            height: 350,
                        },
                    },
                },
                {
                    breakpoint: 570,
                    options: {
                        chart: {
                            height: 250,
                        },
                    },
                },
            ],
            grid: {
                padding: {
                    left: -20,
                },
            },
        };
        const chart = new ApexCharts(transactionOverviewHome3, chartData);
        chart.render();
    }
    const incomeChartHome3 = document.querySelector(".income-chart-home3");
    if (incomeChartHome3) {
        const chartData = {
            chart: {
                height: 330,
                type: "area",
                toolbar: {
                    show: false,
                },
                animations: {
                    enabled: true,
                    easing: "easeinout",
                    speed: 800,
                },
            },
            series: [{
                    name: "This Years",
                    data: [490, 300, 390, 200, 490, 200, 390, 320, 530, 190],
                },
                {
                    name: "Last Years",
                    data: [240, 390, 300, 390, 200, 390, 200, 320, 200, 330],
                },
            ],
            dataLabels: {
                enabled: false,
            },
            stroke: {
                curve: "smooth",
                lineCap: "round",
                width: 3,
                colors: ["#20B757", "#FFC861"],
            },
            xaxis: {
                categories: [
                    "Week 01",
                    "Week 02",
                    "Week 03",
                    "Week 04",
                    "Week 05",
                    "Week 06",
                    "Week 07",
                    "Week 08",
                    "Week 09",
                    "Week 010",
                ],
                axisBorder: {
                    show: false,
                },
            },
            yaxis: {
                min: 160,
                max: 560,

                labels: {
                    formatter: function(v) {
                        return v + "k";
                    },
                    offsetX: dir == "rtl" ? -20 : 0,
                },
            },
            legend: {
                show: false,
            },
            colors: ["rgba(32, 183, 87, 0.21)", "rgba(255, 200, 97, 0.21)"],
            responsive: [{
                    breakpoint: 1820,
                    options: {
                        chart: {
                            height: 340,
                        },
                    },
                },
                {
                    breakpoint: 1600,
                    options: {
                        chart: {
                            height: 308,
                        },
                    },
                },
                {
                    breakpoint: 570,
                    options: {
                        chart: {
                            height: 280,
                        },
                    },
                },
            ],
            grid: {
                show: false,
            },
        };
        const chart = new ApexCharts(incomeChartHome3, chartData);
        chart.render();
    }

    // live users
    const liveUsermapEl = document.getElementById("live-users");

    if (liveUsermapEl) {
        let markers = [{
                name: "Egypt",
                coords: [26.8, 30.8],
                style: {
                    fill: "#20B757",
                    stroke: "rgba(255, 255, 255, 0.50)",
                },
            },
            {
                name: "Canada",
                coords: [56.1304, -106.3468],
                style: {
                    fill: "#20B757",
                    stroke: "rgba(255, 255, 255, 0.50)",
                },
            },
            {
                name: "Brazil",
                coords: [-14.235, -51.9253],
                style: {
                    fill: "#20B757",
                    stroke: "rgba(255, 255, 255, 0.50)",
                },
            },
            {
                name: "China",
                coords: [35.8617, 104.1954],
                style: {
                    fill: "#20B757",
                    stroke: "rgba(255, 255, 255, 0.50)",
                },
            },
            {
                name: "United States",
                coords: [37.0902, -95.7129],
                style: {
                    fill: "#20B757",
                    stroke: "rgba(255, 255, 255, 0.50)",
                },
            },
            {
                name: "Russia",
                coords: [61, 105],
                style: {
                    fill: "#20B757",
                    stroke: "rgba(255, 255, 255, 0.50)",
                },
            },
            {
                name: "Greenland",
                coords: [71.706936, -42.604303],
                style: {
                    fill: "#20B757",
                    stroke: "rgba(255, 255, 255, 0.50)",
                },
            },
            {
                name: "Norway",
                coords: [60.472024, 8.468946],
                style: {
                    fill: "#20B757",
                    stroke: "rgba(255, 255, 255, 0.50)",
                },
            },
            {
                name: "Ukraine",
                coords: [48.379433, 31.16558],
                style: {
                    fill: "#20B757",
                    stroke: "rgba(255, 255, 255, 0.50)",
                },
            },
        ];
        let lines = [{
                from: "Egypt",
                to: "Canada"
            },
            {
                from: "Egypt",
                to: "Russia"
            },
            {
                from: "Egypt",
                to: "China"
            },
            {
                from: "Egypt",
                to: "United States"
            },
            {
                from: "Egypt",
                to: "Greenland"
            },
            {
                from: "Egypt",
                to: "Norway"
            },
            {
                from: "Egypt",
                to: "Ukraine"
            },
            {
                from: "Egypt",
                to: "Brazil"
            },
        ];
        new jsVectorMap({
            map: "world",
            selector: "#live-users",
            markers: markers,
            lines: lines,
            zoomButtons: false,
            onLoaded(map) {
                window.addEventListener("resize", () => {
                    map.updateSize();
                });
            },
            lineStyle: {
                stroke: "#20B757",
                strokeWidth: 1,
                fill: "#20B757",
                strokeDasharray: "6 3 6", // OR: [6, 2, 6]
                animation: true, // Enables animation
            },
            regionStyle: {
                initial: {
                    fill: "rgba(32, 183, 87, 0.3)",
                },
                hover: {
                    fill: "rgba(32, 183, 87, 1)"
                },
            },
        });
    }

    const statChartHome4 = document.querySelectorAll(".stat-chart-home4");
    if (statChartHome4.length) {
        const chartData = {
            chart: {
                type: "bar",
                height: 60,
                width: 126,
                sparkline: {
                    enabled: true,
                },
                toolbar: {
                    show: false,
                },
                animations: {
                    enabled: true,
                    easing: "easeinout",
                    speed: 800,
                },
            },
            grid: {
                show: false,
            },
            dataLabels: {
                enabled: false,
            },
            stroke: {
                show: false,
            },
            series: [{
                name: "Series 1",
                data: [8, 16, 12, 34, 22, 18],
            }, ],
            tooltip: {
                enabled: false,
            },
            fill: {
                colors: [
                    function({
                        value
                    }) {
                        return value > 31 ?
                            "rgba(32, 183, 87, 1)" :
                            "rgba(32, 183, 87, 0.21)";
                    },
                ],
                // colors: ["rgba(32, 183, 87, 0.30)"],
            },
            plotOptions: {
                bar: {
                    borderRadius: 4,
                    borderRadiusApplication: "end",
                },
            },
            xaxis: {
                tooltip: {
                    enabled: false,
                },
                axisBorder: {
                    show: false,
                },
                axisTicks: {
                    show: false,
                },
                labels: {
                    show: false,
                },
            },
            yaxis: {
                min: 0,
                max: 34,
                tooltip: {
                    enabled: false,
                    // followCursor: true
                },
                labels: {
                    show: false,
                },
            },
        };
        statChartHome4.forEach((el) => {
            const chart = new ApexCharts(el, chartData);
            chart.render();
        });
    }

    // income chart home4
    const incomeExpenseChartHome4 = document.querySelector(
        ".income-expense-home4"
    );
    if (incomeExpenseChartHome4) {
        const chartData = {
            chart: {
                height: 289,
                type: "line",
                toolbar: {
                    show: false,
                },
                animations: {
                    enabled: true,
                    easing: "easeinout",
                    speed: 800,
                },
            },
            series: [{
                    name: "This Years",
                    data: [77, 78, 38, 38, 38, 73, 73, 54, 54, 17, 17, 58],
                    type: "line",
                },
                {
                    name: "Last Years",
                    data: [36, 36, 63, 63, 13, 13, 60, 60, 40, 40, 82, 82],
                    type: "line",
                },
            ],
            dataLabels: {
                enabled: false,
            },
            stroke: {
                curve: "smooth",
                lineCap: "round",
                width: 2,
                colors: ["#20B757", "#FFC861"],
            },
            xaxis: {
                categories: [
                    "01 Jan",
                    "02 Jan",
                    "03 Jan",
                    "04 Jan",
                    "05 Jan",
                    "06 Jan",
                    "07 Jan",
                    "08 Jan",
                    "09 Jan",
                    "10 Jan",
                    "11 Jan",
                    "12 Jan",
                ],
                axisBorder: {
                    show: false,
                },
            },
            yaxis: {
                min: 0,
                max: 100,
                tickAmount: 5,
                labels: {
                    formatter: function(v) {
                        return v + "";
                    },
                },
            },
            legend: {
                show: false,
            },
            colors: ["rgba(32, 183, 87)", "rgba(255, 200, 97)"],
            responsive: [{
                    breakpoint: 1820,
                    options: {
                        chart: {
                            height: 340,
                        },
                    },
                },
                {
                    breakpoint: 1600,
                    options: {
                        chart: {
                            height: 308,
                        },
                    },
                },
                {
                    breakpoint: 992,
                    options: {
                        chart: {
                            height: 350,
                        },
                    },
                },
                {
                    breakpoint: 570,
                    options: {
                        chart: {
                            height: 250,
                        },
                    },
                },
                {
                    breakpoint: 400,
                    options: {
                        chart: {
                            height: 200,
                        },
                    },
                },
            ],
        };
        const chart = new ApexCharts(incomeExpenseChartHome4, chartData);
        chart.render();
    }

    const weeklyTransactionsChart = document.querySelector(
        ".weekly-transactions"
    );
    if (weeklyTransactionsChart) {
        const chartData = {
            series: [44, 55, 41, 17, 15],
            chart: {
                type: "donut",
            },
            fill: {
                colors: ["#5D69F4", "#20B757", "#FFC861", "#FF6161", "#775DD0"],
            },
            plotOptions: {
                pie: {
                    donut: {
                        labels: {
                            show: true,
                            value: {
                                fontSize: "14px",
                                offsetY: 2,
                            },
                            total: {
                                show: true,
                                label: "Bank",
                                fontSize: "20px",
                                formatter: () => "Transactions",
                            },
                        },
                    },
                },
            },
            legend: {
                position: "bottom",
                itemMargin: {
                    vertical: 8,
                    horizontal: 20,
                },
                horizontalAlign: "center",
                markers: {
                    width: 5,
                    height: 5,
                    offsetX: dir == "rtl" ? 5 : -5,
                },
            },
            labels: [
                "Completed",
                "In Progress",
                "Yet to Start",
                "Pending",
                "Canceled",
            ],
            dataLabels: {
                style: {
                    fontSize: "10px",
                    fontWeight: 400,
                },
            },
        };
        const chart = new ApexCharts(weeklyTransactionsChart, chartData);
        chart.render();
    }

    // stat charts home 5
    const statChartsHome5 = document.querySelectorAll(".stat-chart-home5");
    if (statChartsHome5) {
        const chartData = {
            series: [{
                data: [
                    [1327359600000, 30.95],
                    [1327446000000, 31.34],
                    [1327532400000, 31.18],
                    [1327618800000, 31.05],
                    [1327878000000, 31.0],
                    [1327964400000, 30.95],
                    [1328050800000, 31.24],
                    [1328137200000, 31.29],
                    [1328223600000, 31.85],
                    [1328482800000, 31.86],
                    [1328569200000, 32.28],
                    [1328655600000, 32.1],
                    [1328742000000, 32.65],
                    [1328828400000, 32.21],
                    [1329087600000, 32.35],
                    [1329174000000, 32.44],
                    [1329260400000, 32.46],
                    [1329346800000, 32.86],
                    [1329433200000, 32.75],
                    [1329778800000, 32.54],
                    [1329865200000, 32.33],
                    [1329951600000, 32.97],
                    [1330038000000, 33.41],
                    [1330297200000, 33.27],
                    [1330383600000, 33.27],
                    [1330470000000, 32.89],
                    [1330556400000, 33.1],
                    [1330642800000, 33.73],
                    [1330902000000, 33.22],
                    [1330988400000, 31.99],
                    [1331074800000, 32.41],
                    [1331161200000, 33.05],
                    [1331247600000, 33.64],
                    [1331506800000, 33.56],
                    [1331593200000, 34.22],
                    [1331679600000, 33.77],
                    [1331766000000, 34.17],
                    [1331852400000, 33.82],
                    [1332111600000, 34.51],
                    [1332198000000, 33.16],
                    [1332284400000, 33.56],
                    [1332370800000, 33.71],
                    [1332457200000, 33.81],
                    [1332712800000, 34.4],
                    [1332799200000, 34.63],
                    [1332885600000, 34.46],
                    [1332972000000, 34.48],
                    [1333058400000, 34.31],
                    [1333317600000, 34.7],
                    [1333404000000, 34.31],
                    [1333490400000, 33.46],
                    [1333576800000, 33.59],
                    [1333922400000, 33.22],
                    [1334008800000, 32.61],
                    [1334095200000, 33.01],
                    [1334181600000, 33.55],
                    [1334268000000, 33.18],
                    [1334527200000, 32.84],
                    [1334613600000, 33.84],
                    [1334700000000, 33.39],
                    [1334786400000, 32.91],
                    [1334872800000, 33.06],
                    [1335132000000, 32.62],
                    [1335218400000, 32.4],
                    [1335304800000, 33.13],
                    [1335391200000, 33.26],
                    [1335477600000, 33.58],
                    [1335736800000, 33.55],
                    [1335823200000, 33.77],
                    [1335909600000, 33.76],
                    [1335996000000, 33.32],
                    [1336082400000, 32.61],
                    [1336341600000, 32.52],
                    [1336428000000, 32.67],
                    [1336514400000, 32.52],
                    [1336600800000, 31.92],
                    [1336687200000, 32.2],
                    [1336946400000, 32.23],
                    [1337032800000, 32.33],
                    [1337119200000, 32.36],
                    [1337205600000, 32.01],
                    [1337292000000, 31.31],
                    [1337551200000, 32.01],
                    [1337637600000, 32.01],
                    [1337724000000, 32.18],
                    [1337810400000, 31.54],
                    [1337896800000, 31.6],
                    [1338242400000, 32.05],
                    [1338328800000, 31.29],
                    [1338415200000, 31.05],
                    [1338501600000, 29.82],
                    [1338760800000, 30.31],
                    [1338847200000, 30.7],
                    [1338933600000, 31.69],
                    [1339020000000, 31.32],
                    [1339106400000, 31.65],
                    [1339365600000, 31.13],
                    [1339452000000, 31.77],
                    [1339538400000, 31.79],
                    [1339624800000, 31.67],
                    [1339711200000, 32.39],
                    [1339970400000, 32.63],
                    [1340056800000, 32.89],
                    [1340143200000, 31.99],
                    [1340229600000, 31.23],
                    [1340316000000, 31.57],
                    [1340575200000, 30.84],
                    [1340661600000, 31.07],
                    [1340748000000, 31.41],
                    [1340834400000, 31.17],
                    [1340920800000, 32.37],
                    [1341180000000, 32.19],
                    [1341266400000, 32.51],
                    [1341439200000, 32.53],
                    [1341525600000, 31.37],
                    [1341784800000, 30.43],
                    [1341871200000, 30.44],
                    [1341957600000, 30.2],
                    [1342044000000, 30.14],
                    [1342130400000, 30.65],
                    [1342389600000, 30.4],
                    [1342476000000, 30.65],
                    [1342562400000, 31.43],
                    [1342648800000, 31.89],
                    [1342735200000, 31.38],
                    [1342994400000, 30.64],
                    [1343080800000, 30.02],
                    [1343167200000, 30.33],
                    [1343253600000, 30.95],
                    [1343340000000, 31.89],
                    [1343599200000, 31.01],
                    [1343685600000, 30.88],
                    [1343772000000, 30.69],
                    [1343858400000, 30.58],
                    [1343944800000, 32.02],
                    [1344204000000, 32.14],
                    [1344290400000, 32.37],
                    [1344376800000, 32.51],
                    [1344463200000, 32.65],
                    [1344549600000, 32.64],
                    [1344808800000, 32.27],
                    [1344895200000, 32.1],
                    [1344981600000, 32.91],
                    [1345068000000, 33.65],
                    [1345154400000, 33.8],
                    [1345413600000, 33.92],
                    [1345500000000, 33.75],
                    [1345586400000, 33.84],
                    [1345672800000, 33.5],
                    [1345759200000, 32.26],
                    [1346018400000, 32.32],
                    [1346104800000, 32.06],
                    [1346191200000, 31.96],
                    [1346277600000, 31.46],
                    [1346364000000, 31.27],
                    [1346709600000, 31.43],
                    [1346796000000, 32.26],
                    [1346882400000, 32.79],
                    [1346968800000, 32.46],
                    [1347228000000, 32.13],
                    [1347314400000, 32.43],
                    [1347400800000, 32.42],
                    [1347487200000, 32.81],
                    [1347573600000, 33.34],
                    [1347832800000, 33.41],
                    [1347919200000, 32.57],
                    [1348005600000, 33.12],
                    [1348092000000, 34.53],
                    [1348178400000, 33.83],
                    [1348437600000, 33.41],
                    [1348524000000, 32.9],
                    [1348610400000, 32.53],
                    [1348696800000, 32.8],
                    [1348783200000, 32.44],
                    [1349042400000, 32.62],
                    [1349128800000, 32.57],
                    [1349215200000, 32.6],
                    [1349301600000, 32.68],
                    [1349388000000, 32.47],
                    [1349647200000, 32.23],
                    [1349733600000, 31.68],
                    [1349820000000, 31.51],
                    [1349906400000, 31.78],
                    [1349992800000, 31.94],
                    [1350252000000, 32.33],
                    [1350338400000, 33.24],
                    [1350424800000, 33.44],
                    [1350511200000, 33.48],
                    [1350597600000, 33.24],
                    [1350856800000, 33.49],
                    [1350943200000, 33.31],
                    [1351029600000, 33.36],
                    [1351116000000, 33.4],
                    [1351202400000, 34.01],
                    [1351638000000, 34.02],
                    [1351724400000, 34.36],
                    [1351810800000, 34.39],
                    [1352070000000, 34.24],
                    [1352156400000, 34.39],
                    [1352242800000, 33.47],
                    [1352329200000, 32.98],
                    [1352415600000, 32.9],
                    [1352674800000, 32.7],
                    [1352761200000, 32.54],
                    [1352847600000, 32.23],
                    [1352934000000, 32.64],
                    [1353020400000, 32.65],
                    [1353279600000, 32.92],
                    [1353366000000, 32.64],
                    [1353452400000, 32.84],
                    [1353625200000, 33.4],
                    [1353884400000, 33.3],
                    [1353970800000, 33.18],
                    [1354057200000, 33.88],
                    [1354143600000, 34.09],
                    [1354230000000, 34.61],
                    [1354489200000, 34.7],
                    [1354575600000, 35.3],
                    [1354662000000, 35.4],
                    [1354748400000, 35.14],
                    [1354834800000, 35.48],
                    [1355094000000, 35.75],
                    [1355180400000, 35.54],
                    [1355266800000, 35.96],
                    [1355353200000, 35.53],
                    [1355439600000, 37.56],
                    [1355698800000, 37.42],
                    [1355785200000, 37.49],
                    [1355871600000, 38.09],
                    [1355958000000, 37.87],
                    [1356044400000, 37.71],
                    [1356303600000, 37.53],
                    [1356476400000, 37.55],
                    [1356562800000, 37.3],
                    [1356649200000, 36.9],
                    [1356908400000, 37.68],
                    [1357081200000, 38.34],
                    [1357167600000, 37.75],
                    [1357254000000, 38.13],
                    [1357513200000, 37.94],
                    [1357599600000, 38.14],
                    [1357686000000, 38.66],
                    [1357772400000, 38.62],
                    [1357858800000, 38.09],
                    [1358118000000, 38.16],
                    [1358204400000, 38.15],
                    [1358290800000, 37.88],
                    [1358377200000, 37.73],
                    [1358463600000, 37.98],
                    [1358809200000, 37.95],
                    [1358895600000, 38.25],
                    [1358982000000, 38.1],
                    [1359068400000, 38.32],
                    [1359327600000, 38.24],
                    [1359414000000, 38.52],
                    [1359500400000, 37.94],
                    [1359586800000, 37.83],
                    [1359673200000, 38.34],
                    [1359932400000, 38.1],
                    [1360018800000, 38.51],
                    [1360105200000, 38.4],
                    [1360191600000, 38.07],
                    [1360278000000, 39.12],
                    [1360537200000, 38.64],
                    [1360623600000, 38.89],
                    [1360710000000, 38.81],
                    [1360796400000, 38.61],
                    [1360882800000, 38.63],
                    [1361228400000, 38.99],
                    [1361314800000, 38.77],
                    [1361401200000, 38.34],
                    [1361487600000, 38.55],
                    [1361746800000, 38.11],
                    [1361833200000, 38.59],
                    [1361919600000, 39.6],
                ],
            }, ],
            chart: {
                id: "area-datetime",
                type: "area",
                height: 100,
                width: 180,
                zoom: {
                    autoScaleYaxis: true,
                },
                toolbar: {
                    show: false,
                },
            },
            stroke: {
                width: 1,
                colors: ["#20B757"],
            },
            dataLabels: {
                enabled: false,
            },
            markers: {
                size: 0
            },
            xaxis: {
                type: "datetime",
                min: new Date("01 Mar 2012").getTime(),
                tickAmount: 6,
                labels: {
                    show: false,
                },
                axisBorder: {
                    show: false,
                },
                axisTicks: {
                    show: false,
                },
            },
            yaxis: {
                labels: {
                    show: false,
                },
            },
            tooltip: {
                x: {
                    format: "dd MMM yyyy",
                },
            },
            colors: ["#20B757"],
            fill: {
                type: "gradient",
                colors: ["#20B757"],
                gradient: {
                    shadeIntensity: 1,
                    opacityFrom: 0.7,
                    opacityTo: 0.3,
                    stops: [50, 100, 100],
                },
            },
            grid: {
                show: false,
                padding: {
                    bottom: -20,
                    top: -10,
                    left: -10,
                    right: -10,
                },
            },
        };
        statChartsHome5.forEach((el) => {
            const chart = new ApexCharts(el, chartData);
            chart.render();
        });
    }

    // balance chart home 5
    const balanceChartHome5 = document.querySelector(".balance-chart-home5");
    if (balanceChartHome5) {
        const chartData = {
            chart: {
                height: 289,
                type: "area",
                toolbar: {
                    show: false,
                },
                animations: {
                    enabled: true,
                    easing: "easeinout",
                    speed: 800,
                },
            },
            series: [{
                    name: "This Years",
                    data: [25, 32, 38, 43, 47, 53, 75, 105, 152, 172, 208, 258],
                },
                {
                    name: "Last Years",
                    data: [20, 24, 50, 42, 34, 40, 48, 65, 78, 104, 120, 140],
                },
            ],
            dataLabels: {
                enabled: false,
            },
            stroke: {
                curve: "smooth",
                lineCap: "round",
                width: 3,
                colors: ["#20B757", "#FFC861"],
            },
            xaxis: {
                categories: [
                    "Jan",
                    "Feb",
                    "Mar",
                    "Apr",
                    "May",
                    "Jun",
                    "Jul",
                    "Aug",
                    "Sep",
                    "Oct",
                    "Nov",
                    "Dec",
                ],
                axisBorder: {
                    show: false,
                },
            },
            yaxis: {
                min: 0,
                max: 260,
                tickAmount: 5,
                labels: {
                    formatter: function(v) {
                        return "$" + v + "k";
                    },
                    offsetX: dir == "rtl" ? -40 : -10,
                },
            },
            legend: {
                show: false,
            },
            colors: ["rgba(32, 183, 87, 0.21)", "rgba(255, 200, 97, 0.21)"],
            responsive: [{
                    breakpoint: 1820,
                    options: {
                        chart: {
                            height: 340,
                        },
                    },
                },
                {
                    breakpoint: 1600,
                    options: {
                        chart: {
                            height: 308,
                        },
                    },
                },
                {
                    breakpoint: 992,
                    options: {
                        chart: {
                            height: 350,
                        },
                    },
                },
                {
                    breakpoint: 570,
                    options: {
                        chart: {
                            height: 250,
                        },
                    },
                },
                {
                    breakpoint: 400,
                    options: {
                        chart: {
                            height: 200,
                        },
                    },
                },
            ],
        };
        const chart = new ApexCharts(balanceChartHome5, chartData);
        chart.render();
    }

    // browser sessions
    const browserSessionChartEl = document.querySelector(".browser-session");
    if (browserSessionChartEl) {
        const chartData = {
            xaxis: {
                categories: [
                    "Chrome",
                    "Firefox",
                    "Safari",
                    "Opera",
                    "Edge",
                    "Explorer",
                ],
            },
            series: [{
                name: "Browser Sessions",
                data: [80, 50, 30, 40, 60, 20],
            }, ],
            chart: {
                type: "radar",
                height: 400,
                toolbar: {
                    show: false,
                },
            },
            dataLabels: {
                enabled: true,
            },
            colors: ["#20B757"],
            plotOptions: {
                radar: {
                    polygons: {
                        strokeWidth: "2px",
                    },
                },
            },
        };
        const chart = new ApexCharts(browserSessionChartEl, chartData);
        chart.render();
    }

    // account payment overview
    const accountPaymentOverview = document.querySelector(
        ".account-payment-overview"
    );
    if (accountPaymentOverview) {
        const chartData = {
            chart: {
                height: 330,
                type: "area",
                toolbar: {
                    show: false,
                },
                animations: {
                    enabled: true,
                    easing: "easeinout",
                    speed: 800,
                },
            },
            series: [{
                    name: "This Years",
                    data: [0, 100, 30, 165, 85, 205, 105, 245, 75, 225, 150, 230],
                },
                {
                    name: "Last Years",
                    data: [0, 60, 24, 88, 50, 112, 57, 130, 36, 108, 70, 120],
                },
            ],
            dataLabels: {
                enabled: false,
            },
            stroke: {
                curve: "smooth",
                lineCap: "round",
                width: 2,
                dashArray: [5, 0],
                colors: ["#FFC861", "#20B757"],
            },
            xaxis: {
                categories: [
                    "Jan",
                    "Feb",
                    "Mar",
                    "Apr",
                    "May",
                    "Jun",
                    "Jul",
                    "Aug",
                    "Sep",
                    "Oct",
                    "Nov",
                    "Dec",
                ],
                axisBorder: {
                    show: false,
                },
            },
            yaxis: {
                min: 0,
                max: 300,
                tickAmount: 5,
                labels: {
                    formatter: function(v) {
                        return v + "";
                    },
                },
            },
            legend: {
                show: false,
            },
            colors: ["#FFC861", "#20B757"],
            fill: {
                type: "gradient",
                colors: ["rgba(255, 200, 97, 0.31)", "rgba(32, 183, 87, 0.31)"],
                gradient: {
                    shadeIntensity: 1,
                    opacityFrom: 0.9,
                    opacityTo: 0.3,
                    stops: [0, 100],
                },
            },
            responsive: [{
                    breakpoint: 1820,
                    options: {
                        chart: {
                            height: 340,
                        },
                    },
                },
                {
                    breakpoint: 1600,
                    options: {
                        chart: {
                            height: 308,
                        },
                    },
                },
                {
                    breakpoint: 992,
                    options: {
                        chart: {
                            height: 350,
                        },
                    },
                },
                {
                    breakpoint: 570,
                    options: {
                        chart: {
                            height: 250,
                        },
                    },
                },
                {
                    breakpoint: 400,
                    options: {
                        chart: {
                            height: 200,
                        },
                    },
                },
            ],
        };
        const chart = new ApexCharts(accountPaymentOverview, chartData);
        chart.render();
    }
    // account payment overview
    const DepositsAccount = document.querySelector(".deposits-account");
    if (DepositsAccount) {
        const chartData = {
            series: [{
                data: [{
                        x: "Savings Deposit",
                        y: [2800, 4500],
                    },
                    {
                        x: "Checking Deposit",
                        y: [3200, 4100],
                    },
                    {
                        x: "Fixed Deposit",
                        y: [2950, 7800],
                    },
                    {
                        x: "Joint Deposit",
                        y: [3000, 4600],
                    },
                    {
                        x: "Corporate Deposit",
                        y: [3500, 4100],
                    },
                    {
                        x: "Foreign Deposit",
                        y: [4500, 6500],
                    },
                    {
                        x: "No Interest",
                        y: [4100, 5600],
                    },
                ],
            }, ],
            chart: {
                height: 390,
                type: "rangeBar",
                zoom: {
                    enabled: false,
                },
                toolbar: {
                    show: false,
                },
            },
            colors: ["#20B757", "#FFC861"],
            plotOptions: {
                bar: {
                    horizontal: true,
                    isDumbbell: true,
                    dumbbellColors: [
                        ["#20B757", "#FFC861"]
                    ],
                },
            },
            dataLabels: {
                enabled: false,
            },
            legend: {
                show: false,
            },
            fill: {
                type: "gradient",
                gradient: {
                    gradientToColors: ["#FFC861"],
                    inverseColors: false,
                    stops: [0, 100],
                },
            },
            grid: {
                xaxis: {
                    lines: {
                        show: true,
                    },
                },
                yaxis: {
                    lines: {
                        show: false,
                    },
                },
            },
            xaxis: {
                axisTicks: {
                    show: false,
                },
            },
            yaxis: {
                labels: {
                    show: window.innerWidth > 500 ? true : false,
                    offsetX: dir == "rtl" ? -100 : 0,
                },
            },
        };
        const chart = new ApexCharts(DepositsAccount, chartData);
        chart.render();
    }

    // Acount Balance chart
    const AccountBalance = document.querySelector(".account-balance-chart");
    if (AccountBalance) {
        const chartData = {
            series: [23232.52, 12326.12, 9325.32, 11458.36],
            chart: {
                type: "donut",
            },
            fill: {
                colors: ["#4371E9", "#FFC861", "#20B757", "#FF6161"],
            },
            stroke: {
                lineCap: "round",
            },
            plotOptions: {
                pie: {
                    donut: {
                        size: "85px",
                        labels: {
                            show: true,
                            value: {
                                fontSize: "16px",
                                offsetY: 2,
                            },
                            total: {
                                show: true,
                                label: "99,800.35",
                                fontWeight: 600,
                                fontSize: "26px",
                                formatter: () => "Total Balance",
                            },
                        },
                    },
                },
            },
            legend: {
                position: "bottom",
                itemMargin: {
                    vertical: 8,
                    horizontal: 5,
                },
                horizontalAlign: "center",
                markers: {
                    width: 4,
                    height: 4,
                    offsetX: -3,
                },
            },
            dataLabels: {
                enabled: false,
            },
            labels: ["23,232 USD", "12,326 EUR", "9,235 GBP", "11,458 RUB"],
        };
        const chart = new ApexCharts(AccountBalance, chartData);
        chart.render();
    }

    // Deposit Balance
    const DepositsBalance = document.querySelector(".deposits-balance-chart");
    if (DepositsBalance) {
        const chartData = {
            chart: {
                height: 390,
                type: "radialBar",
            },
            series: [76, 67, 61, 90],
            plotOptions: {
                radialBar: {
                    offsetY: 0,
                    startAngle: 0,
                    endAngle: 270,
                    hollow: {
                        margin: 5,
                        size: "30%",
                        background: "transparent",
                        image: undefined,
                    },
                    dataLabels: {
                        name: {
                            show: false,
                        },
                        value: {
                            show: false,
                        },
                    },
                },
            },
            colors: ["#4371E9", "#FFC861", "#20B757", "#FF6161"],
            labels: ["23,232 USD", "12,326 EUR", "9,235 GBP", "11,458 RUB"],
            legend: {
                show: true,
                floating: true,
                fontSize: "13px",
                position: "left",
                offsetX: 55,
                offsetY: 0,
                markers: {
                    width: 6,
                    height: 6,
                    offsetY: -3,
                    offsetX: dir == "rtl" ? 4 : -4,
                },
                width: 200,
                labels: {
                    useSeriesColors: true,
                },
                formatter: function(seriesName, opts) {
                    return seriesName;
                },
                itemMargin: {
                    vertical: 3,
                },
            },
            responsive: [{
                breakpoint: 480,
                options: {
                    legend: {
                        show: false,
                    },
                },
            }, ],
        };
        const chart = new ApexCharts(DepositsBalance, chartData);
        chart.render();
    }

    // Card history chart
    const CardHistoryChart = document.querySelector(".card-history-chart");
    if (CardHistoryChart) {
        const chartData = {
            series: [44, 55, 41, 17, 15],
            chart: {
                type: "donut",
            },
            fill: {
                colors: ["#4371E9", "#FFC861", "#20B757", "#FF6161"],
            },
            plotOptions: {
                pie: {
                    donut: {
                        labels: {
                            show: true,
                            value: {
                                fontSize: "16px",
                                offsetY: 2,
                            },
                            total: {
                                show: true,
                                label: "Card",
                                fontSize: "24px",
                                formatter: () => "Transaction",
                            },
                        },
                    },
                },
            },
            legend: {
                position: window.innerWidth > 1400 ? "right" : "bottom",
                itemMargin: {
                    vertical: window.innerWidth > 1500 ? 4 : 2,
                },
                offsetY: window.innerWidth > 1830 ? 40 : window.innerWidth > 1700 ? 20 : 0,
                horizontalAlign: "center",
                markers: {
                    width: 8,
                    height: 8,
                    offsetX: dir == "rtl" ? 5 : -5,
                },
            },
            labels: [
                "Completed",
                "In Progress",
                "Yet to Start",
                "Pending",
                "Canceled",
            ],
            dataLabels: {
                style: {
                    fontSize: "10px",
                    fontWeight: 400,
                },
            },
        };
        const chart = new ApexCharts(CardHistoryChart, chartData);
        chart.render();
    }

    // Card transaction chart
    const CardTransactionChart = document.querySelector(
        ".card-transaction-chart"
    );
    if (CardTransactionChart) {
        const chartData = {
            chart: {
                type: "bar",
                height: 370,
                toolbar: {
                    show: false,
                },
            },
            series: [{
                    name: "Payment Transaction",
                    data: [44, 55, 41, 64, 22, 43, 21],
                },
                {
                    name: "Cashout Transaction",
                    data: [53, 32, 33, 52, 13, 44, 32],
                },
            ],
            plotOptions: {
                bar: {
                    barHeight: 14,
                    horizontal: true,
                    dataLabels: {
                        position: "top",
                    },
                },
            },
            dataLabels: {
                enabled: true,
                offsetX: -6,
                style: {
                    fontSize: "12px",
                    colors: ["#fff"],
                },
            },
            fill: {
                colors: ["#20B757", "#FFC861"],
            },
            colors: ["#20B757", "#FFC861"],
            stroke: {
                show: true,
                width: 1,
            },
            tooltip: {
                shared: true,
                intersect: false,
            },
            xaxis: {
                categories: [2001, 2002, 2003, 2004, 2005, 2006, 2007],
                axisBorder: {
                    show: false,
                },
            },
            yaxis: {
                labels: {
                    offsetX: 0,
                },
            },
            legend: {
                itemMargin: {
                    horizontal: 20,
                },
                markers: {
                    offsetX: 0,
                    width: 6,
                    height: 6,
                    radius: 20,
                },
            },
            grid: {
                padding: {
                    bottom: 20,
                },
            },
        };
        const chart = new ApexCharts(CardTransactionChart, chartData);
        chart.render();
    }

    // Payment overview
    const paymentOverview = document.querySelector(".payment-overview");
    if (paymentOverview) {
        const chartData = {
            series: [{
                    name: "This Year",
                    type: "line",
                    data: [38, 120, 80, 42, 30, 75, 36, 35, 78, 80, 40, 80],
                },
                {
                    name: "Previous Years",
                    type: "line",
                    data: [94, 32, 20, 135, 68, 22, 40, 43, 30, 64, 50, 87],
                },
                {
                    name: "Last 5 Years",
                    type: "line",
                    data: [10, 40, 34, 50, 48, 61, 68, 90, 148, 48, 90, 30],
                },
            ],
            chart: {
                height: 350,
                type: "line",
                toolbar: {
                    show: false,
                },
            },
            legend: {
                show: true,
                position: "bottom",
                itemMargin: {
                    horizontal: 15,
                },
                markers: {
                    width: 6,
                    height: 6,
                    offsetX: -6,
                },
            },
            colors: ["#63CC8A", "#FFC861", "#4371E9"],
            stroke: {
                width: [3, 3, 3],
                curve: "smooth",
                lineCap: "round",
            },
            xaxis: {
                type: "category",
                categories: [
                    "Jan",
                    "Feb",
                    "Mar",
                    "Apr",
                    "May",
                    "Jun",
                    "Jul",
                    "Aug",
                    "Sep",
                    "Oct",
                    "Nov",
                    "Dec",
                ],
                tickAmount: 12,
                axisTicks: {
                    show: false,
                },
                axisBorder: {
                    show: false,
                },
            },
            yaxis: {
                min: 0,
                max: 150,
                tickAmount: 5,
                labels: {
                    offsetX: -17,
                },
            },
            fill: {
                opacity: 1,
            },
            grid: {
                padding: {
                    left: -10,
                    bottom: 15,
                },
                show: true,
            },
        };
        const chart = new ApexCharts(paymentOverview, chartData);
        chart.render();
    }

    // usd to euro chart

    const usdToEuroChart = document.querySelector(".usdeuro-chart");
    if (usdToEuroChart) {
        const chartData = {
            chart: {
                id: "area-datetime",
                type: "area",
                height: 410,
                zoom: {
                    autoScaleYaxis: true,
                },
                toolbar: {
                    show: false,
                },
            },
            series: assetSeries,
            stroke: {
                width: 4,
                colors: ["#20B757"],
                curve: "smooth",
            },
            dataLabels: {
                enabled: false,
            },
            markers: {
                size: 0,
            },
            colors: ["#20B757"],
            xaxis: {
                type: "datetime",
                min: new Date("01 Mar 2012").getTime(),
                tickAmount: 6,
                axisBorder: {
                    show: false,
                },
            },
            yaxis: {
                tickAmount: 10,
                labels: {
                    offsetX: -17,
                    formatter(val, opts) {
                        return val.toFixed(0) + "M";
                    },
                },
            },
            tooltip: {
                x: {
                    format: "dd MMM yyyy",
                },
            },
            fill: {
                type: "gradient",
                colors: ["#20B757"],
                gradient: {
                    shadeIntensity: 1,
                    opacityFrom: 0.9,
                    opacityTo: 0.3,
                    stops: [0, 100],
                },
            },
            grid: {
                padding: {
                    left: -6,
                },
            },
            responsive: [{
                breakpoint: 992,
                options: {
                    chart: {
                        height: 300,
                    },
                },
            }, ],
        };
        const chart = new ApexCharts(usdToEuroChart, chartData);
        chart.render();
        const resetCssClasses = function(activeEl) {
            const els = document.querySelectorAll(".asset-btn");
            Array.prototype.forEach.call(els, function(el) {
                el.classList.remove("active");
            });

            activeEl.target.classList.add("active");
        };

        document
            .querySelector("#one_month")
            .addEventListener("click", function(e) {
                resetCssClasses(e);

                chart.zoomX(
                    new Date("28 Jan 2013").getTime(),
                    new Date("27 Feb 2013").getTime()
                );
            });

        document
            .querySelector("#six_months")
            .addEventListener("click", function(e) {
                resetCssClasses(e);

                chart.zoomX(
                    new Date("27 Sep 2012").getTime(),
                    new Date("27 Feb 2013").getTime()
                );
            });

        document.querySelector("#one_year").addEventListener("click", function(e) {
            resetCssClasses(e);
            chart.zoomX(
                new Date("27 Feb 2012").getTime(),
                new Date("27 Feb 2013").getTime()
            );
        });

        document.querySelector("#ytd").addEventListener("click", function(e) {
            resetCssClasses(e);

            chart.zoomX(
                new Date("01 Jan 2013").getTime(),
                new Date("27 Feb 2013").getTime()
            );
        });

        document.querySelector("#all").addEventListener("click", function(e) {
            resetCssClasses(e);

            chart.zoomX(
                new Date("23 Jan 2012").getTime(),
                new Date("27 Feb 2013").getTime()
            );
        });
    }

    const totalTransfer = document.querySelector(".total-transfer");
    if (totalTransfer) {
        const chartData = {
            chart: {
                id: "area-datetime",
                type: "area",
                height: 420,
                zoom: {
                    autoScaleYaxis: true,
                },
                toolbar: {
                    show: false,
                },
            },
            series: assetSeries,
            stroke: {
                width: 2,
                colors: ["#20B757"],
                curve: "smooth",
            },
            dataLabels: {
                enabled: false,
            },
            markers: {
                size: 0,
            },
            colors: ["#20B757"],
            xaxis: {
                type: "datetime",
                min: new Date("01 Mar 2012").getTime(),
                tickAmount: 6,
                axisBorder: {
                    show: false,
                },
            },
            yaxis: {
                labels: {
                    offsetX: -17,
                },
            },
            tooltip: {
                x: {
                    format: "dd MMM yyyy",
                },
            },
            fill: {
                type: "gradient",
                colors: ["#20B757"],
                gradient: {
                    shadeIntensity: 1,
                    opacityFrom: 1,
                    opacityTo: 0.3,
                    stops: [0, 100],
                },
            },
            grid: {
                padding: {
                    left: -6,
                },
            },
            responsive: [{
                breakpoint: 992,
                options: {
                    chart: {
                        height: 300,
                    },
                },
            }, ],
        };
        const chart = new ApexCharts(totalTransfer, chartData);
        chart.render();
    }

    // Recent transfer chart
    const recentTransferChart = document.querySelector(".recent-transfer");
    if (recentTransferChart) {
        const series = [{
            name: "Peter",
            data: [
                null,
                44,
                31,
                38,
                null,
                34,
                55,
                51,
                67,
                21,
                35,
                null,
                null,
                12,
                4,
                16,
                null,
                8,
                36,
                null,
                null,
                16,
                null,
            ],
        }, ];
        const chartData = {
            series,
            chart: {
                height: 470,
                type: "line",
                zoom: {
                    enabled: false,
                },
                toolbar: {
                    show: false,
                },
                animations: {
                    enabled: true,
                    easing: "easeout",
                },
            },
            annotations: {
                xaxis: [{
                    strokeDashArray: 0,
                    borderWidth: 0,
                    label: {
                        borderColor: "#775DD0",
                        borderWidth: 0,
                        offsetX: -40,
                        offsetY: 120,
                        style: {
                            color: "#fff",
                            background: "none",
                            fontSize: "12px",
                        },
                        text: "Average Transfer",
                    },
                }, ],
            },
            markers: {
                width: 8,
                height: 8,
                radius: 50,
                shape: "circle",
                size: 8,
            },
            stroke: {
                width: [4],
                curve: "straight",
            },
            legend: {
                show: false,
            },
            labels: [
                "23 Dec",
                "25 Dec",
                "29 Dec",
                "31 Dec",
                "02 Jan",
                "04 Jan",
                "06 Jan",
                "08 Jan",
                "10 Jan",
                "12 Jan",
                "15 Dec",
                "19 Dec",
                "21 Dec",
                "22 Jan",
                "24 Jan",
                "26 Jan",
                "28 Jan",
                "31 Jan",
                "02 Feb",
                "04 Feb",
                "06 Feb",
                "04 Feb",
                "08 Feb",
            ],
            colors: ["#20B757"],
            xaxis: {
                tickAmount: 11,
                axisBorder: {
                    show: false,
                },
            },
            responsive: [{
                    breakpoint: 1500,
                    options: {
                        chart: {
                            height: 340,
                        },
                    },
                },
                {
                    breakpoint: 768,
                    options: {
                        chart: {
                            height: 360,
                        },
                    },
                },
                {
                    breakpoint: 570,
                    options: {
                        chart: {
                            height: 280,
                        },
                    },
                },
            ],
            yaxis: {
                tickAmount: 4,
                min: 0,
                max: 80,
                labels: {
                    offsetX: 20,
                },
            },
            grid: {
                padding: {
                    left: 30,
                },
            },
        };
        const chart = new ApexCharts(recentTransferChart, chartData);
        chart.render();
    }

    // trading stat charts
    const tradingStatCharts = document.querySelectorAll(".trading-stat-chart");
    if (tradingStatCharts.length > 0) {
        const options = {
            chart: {
                height: 60,
                width: "120",
                type: "area",
                sparkline: {
                    enabled: true,
                },
                toolbar: {
                    show: false,
                },
                animations: {
                    enabled: true,
                    easing: "easeinout",
                    speed: 800,
                },
            },
            grid: {
                show: false,
            },
            dataLabels: {
                enabled: false,
            },
            stroke: {
                curve: "smooth",
                width: 1,
            },
            series: [{
                name: "Series 1",
                data: [
                    40, 42, 35, 38, 52, 17, 15, 19, 29, 35, 30, 40, 35, 45, 35, 29, 38,
                    51, 56, 48, 53, 57, 69, 65, 53, 39, 53, 38, 52, 51, 49, 50, 36, 63,
                    90, 72, 75, 89, 96, 72, 91, 83, 71, 61, 52, 45, 49,
                ],
            }, ],
            tooltip: {
                enabled: false,
            },
            colors: ["#20B757"],
            fill: {
                colors: ["#20B757"],
                opacity: 1,
                type: "gradient",
                gradient: {
                    shade: "dark",
                    type: "vertical",
                    shadeIntensity: 0.3,
                    gradientToColors: undefined,
                    inverseColors: false,
                    opacityFrom: 1,
                    opacityTo: 0.1,
                    stops: [0, 90, 100],
                    colorStops: [],
                },
            },
            xaxis: {
                tooltip: {
                    enabled: false,
                },
                axisBorder: {
                    show: false,
                },
                axisTicks: {
                    show: false,
                },
                labels: {
                    show: false,
                },
            },
            yaxis: {
                tooltip: {
                    enabled: false,
                    // followCursor: true
                },
                labels: {
                    show: false,
                },
            },
        };
        tradingStatCharts.forEach((el) => {
            const chart = new ApexCharts(el, options);
            chart.render();
        });
    }
    const tradingStatChartsTable = document.querySelectorAll(
        ".trading-stat-chart-table"
    );
    if (tradingStatChartsTable.length > 0) {
        const options = {
            chart: {
                height: 40,
                width: "120",
                type: "area",
                sparkline: {
                    enabled: true,
                },
                toolbar: {
                    show: false,
                },
                animations: {
                    enabled: true,
                    easing: "easeinout",
                    speed: 800,
                },
            },
            grid: {
                show: false,
            },
            dataLabels: {
                enabled: false,
            },
            stroke: {
                curve: "smooth",
                width: 1,
            },
            series: [{
                name: "Series 1",
                data: [
                    40, 42, 35, 38, 52, 17, 15, 19, 29, 35, 30, 40, 35, 45, 35, 29, 38,
                    51, 56, 48, 53, 57, 69, 65, 53, 39, 53, 38, 52, 51, 49, 50, 36, 63,
                    90, 72, 75, 89, 96, 72, 91, 83, 71, 61, 52, 45, 49,
                ],
            }, ],
            tooltip: {
                enabled: false,
            },
            colors: ["#20B757"],
            fill: {
                colors: ["#20B757"],
                opacity: 1,
                type: "gradient",
                gradient: {
                    shade: "dark",
                    type: "vertical",
                    shadeIntensity: 0.3,
                    gradientToColors: undefined,
                    inverseColors: false,
                    opacityFrom: 1,
                    opacityTo: 0.1,
                    stops: [0, 90, 100],
                    colorStops: [],
                },
            },
            xaxis: {
                tooltip: {
                    enabled: false,
                },
                axisBorder: {
                    show: false,
                },
                axisTicks: {
                    show: false,
                },
                labels: {
                    show: false,
                },
            },
            yaxis: {
                tooltip: {
                    enabled: false,
                    // followCursor: true
                },
                labels: {
                    show: false,
                },
            },
        };
        tradingStatChartsTable.forEach((el) => {
            const chart = new ApexCharts(el, options);
            chart.render();
        });
    }
    // USD vs EUR chart
    const usdVsEur = document.querySelector(".usd-vs-eur");
    if (usdVsEur) {
        const series = [{
                name: "USD",
                data: [0, 100, 30, 165, 85, 205, 105, 245, 75, 225, 150, 230],
            },
            {
                name: "EUR",
                data: [0, 60, 24, 88, 50, 112, 57, 130, 36, 108, 70, 120],
            },
        ];
        const chartData = {
            chart: {
                height: 280,
                type: "area",
                toolbar: {
                    show: false,
                },
                animations: {
                    enabled: true,
                    easing: "easeinout",
                    speed: 800,
                },
            },
            series: series,
            dataLabels: {
                enabled: false,
            },
            stroke: {
                curve: "smooth",
                lineCap: "round",
                width: 2,
                dashArray: [5, 0],
                colors: ["#FFC861", "#20B757"],
            },
            xaxis: {
                categories: [
                    "Jan",
                    "Feb",
                    "Mar",
                    "Apr",
                    "May",
                    "Jun",
                    "Jul",
                    "Aug",
                    "Sep",
                    "Oct",
                    "Nov",
                    "Dec",
                ],
                axisBorder: {
                    show: false,
                },
            },
            yaxis: {
                min: 0,
                max: 300,
                tickAmount: 5,
                labels: {
                    formatter: function(v) {
                        return v + "";
                    },
                },
            },
            legend: {
                show: true,
                itemMargin: {
                    horizontal: 15,
                },
                markers: {
                    width: 6,
                    height: 6,
                    offsetX: dir == "rtl" ? 5 : -5,
                },
            },
            colors: ["#FFC861", "#20B757"],
            fill: {
                type: "gradient",
                colors: ["rgba(255, 200, 97, 0.21)", "rgba(32, 183, 87, 0.21)"],
                gradient: {
                    shadeIntensity: 1,
                    opacityFrom: 0.7,
                    opacityTo: 0.3,
                    stops: [0, 100],
                },
            },
            grid: {
                padding: {
                    bottom: 15,
                },
            },
        };
        const chart = new ApexCharts(usdVsEur, chartData);
        chart.render();
    }

    // daily highlightchart
    const highlightchart = document.querySelector(".daily-highlight");
    if (highlightchart) {
        const chartData = {
            series: [{
                    name: "USD",
                    type: "column",
                    data: [23, 11, 22, 27, 13, 22, 37, 21, 44, 22, 30],
                },
                {
                    name: "EUR",
                    type: "area",
                    data: [44, 55, 41, 67, 22, 43, 21, 41, 56, 27, 43],
                },
                {
                    name: "GBP",
                    type: "line",
                    data: [30, 25, 36, 30, 45, 35, 64, 52, 59, 36, 39],
                },
            ],
            chart: {
                height: 290,
                type: "line",
                stacked: false,
                toolbar: {
                    show: false,
                },
            },
            legend: {
                itemMargin: {
                    horizontal: 20,
                },
                offsetY: 8,
                markers: {
                    height: 6,
                    width: 6,
                    offsetX: dir == "rtl" ? 5 : -5,
                },
            },
            stroke: {
                width: [0, 2, 3],
                curve: "smooth",
                colors: ["#FFC861", "#4371E9"],
            },
            plotOptions: {
                bar: {
                    columnWidth: "50%",
                },
            },
            fill: {
                opacity: [0.85, 0.05, 1],
                colors: ["#20B757", "#4371E9"],
                gradient: {
                    shadeIntensity: 1,
                    opacityFrom: 1,
                    opacityTo: 0.3,
                    stops: [0, 100, 100],
                },
            },
            labels: [
                "01/01/2003",
                "02/01/2003",
                "03/01/2003",
                "04/01/2003",
                "05/01/2003",
                "06/01/2003",
                "07/01/2003",
                "08/01/2003",
                "09/01/2003",
                "10/01/2003",
                "11/01/2003",
            ],
            xaxis: {
                type: "datetime",
                axisBorder: {
                    show: false,
                },
            },
            yaxis: {
                min: 0,
            },
            tooltip: {
                shared: true,
                intersect: false,
                y: {
                    formatter: function(y) {
                        if (typeof y !== "undefined") {
                            return y.toFixed(0) + " points";
                        }
                        return y;
                    },
                },
            },
            grid: {
                padding: {
                    bottom: 20,
                },
            },
        };
        const chart = new ApexCharts(highlightchart, chartData);
        chart.render();
    }
    // performance chart
    const performanceChart = document.querySelector(".performance-chart");
    if (performanceChart) {
        const chartData = {
            series: [14, 23, 21, 17, 15, 10, 12, 17, 21],
            chart: {
                height: 355,
                type: "polarArea",
            },
            colors: [
                "#5D69F4",
                "#00998B",
                "#FFC861",
                "#FF6161",
                "#8169D3",
                "#5D69F4",
                "#00998B",
                "#FFC861",
                "#FF6161",
            ],
            labels: [
                "US Dollar (USD)",
                "Euro (EUR)",
                "British Pound (GBP)",
                "Japanese Yen (JPY)",
                "Chinese Yuan (CNY)",
                "Canadian Dollar (CAD)",
                "Russian Ruble (RUB)",
                "Swedish Krona (SEK)",
                "Spanish Pesatas (ESP)",
            ],
            stroke: {
                width: 2,
            },
            fill: {
                opacity: 1,
            },
            responsive: [{
                    breakpoint: 1820,
                    options: {
                        chart: {
                            height: 450,
                        },
                    },
                },
                {
                    breakpoint: 1200,
                    options: {
                        chart: {
                            height: 500,
                        },
                    },
                },
            ],
            dataLabels: {
                enabled: true,
                style: {
                    fontSize: "12px",
                },
                textAnchor: "end",
                background: {
                    enabled: false,
                },
            },
            yaxis: {
                labels: {
                    formatter: function(val) {
                        return val + "%";
                    },
                },
            },
            plotOptions: {
                polarArea: {
                    rings: {
                        strokeWidth: 1,
                    },
                    spokes: {
                        strokeWidth: 1,
                    },
                },
            },
            legend: {
                offsetX: window.innerWidth > 1500 ? 10 : 0,
                offsetY: window.innerWidth > 767 ? 6 : window.innerWidth > 1500 ? 14 : 0,
                itemMargin: {
                    vertical: window.innerWidth > 767 ? 2 : window.innerWidth > 1500 ? 4 : 0,
                },
                horizontalAlign: "center",
                position: window.innerWidth > 1500 ? "right" : "bottom",
                markers: {
                    width: 5,
                    height: 5,
                    offsetX: dir == "rtl" ? 6 : -6,
                },
            },
        };
        const chart = new ApexCharts(performanceChart, chartData);
        chart.render();
    }

    // usdChart
    const usdChart = document.querySelector(".usd-chart");
    if (usdChart) {
        const candlestick = {
            series: [{
                data: [{
                        x: "2019-06-21T00:00:00.000Z",
                        y: [171.82, 172.54, 166.34, 169.87],
                    },
                    {
                        x: "2019-06-24T00:00:00.000Z",
                        y: [170.23, 170.64, 164.12, 165.3],
                    },
                    {
                        x: "2019-06-25T00:00:00.000Z",
                        y: [165.94, 165.94, 155.64, 158.59],
                    },
                    {
                        x: "2019-06-26T00:00:00.000Z",
                        y: [160.5, 161.75, 150.29, 150.69],
                    },
                    {
                        x: "2019-06-27T00:00:00.000Z",
                        y: [150.88, 153.35, 148.04, 151.49],
                    },
                    {
                        x: "2019-06-28T00:00:00.000Z",
                        y: [151.91, 152.78, 145.26, 152.09],
                    },
                    {
                        x: "2019-07-01T00:00:00.000Z",
                        y: [155.32, 155.32, 143.85, 147.67],
                    },
                    {
                        x: "2019-07-02T00:00:00.000Z",
                        y: [145.62, 154.41, 144.38, 154.05],
                    },
                    {
                        x: "2019-07-03T00:00:00.000Z",
                        y: [155.44, 158.45, 153.46, 154.98],
                    },
                    {
                        x: "2019-07-05T00:00:00.000Z",
                        y: [152.42, 156.02, 151.34, 155.9],
                    },
                    {
                        x: "2019-07-08T00:00:00.000Z",
                        y: [154.94, 158.68, 153.01, 157.04],
                    },
                    {
                        x: "2019-07-09T00:00:00.000Z",
                        y: [156.56, 158.06, 154.39, 157.72],
                    },
                    {
                        x: "2019-07-10T00:00:00.000Z",
                        y: [159, 161.38, 156.44, 157.23]
                    },
                    {
                        x: "2019-07-11T00:00:00.000Z",
                        y: [157.26, 159.33, 154.33, 158.04],
                    },
                    {
                        x: "2019-07-12T00:00:00.000Z",
                        y: [157.24, 158.49, 151.03, 153.1],
                    },
                    {
                        x: "2019-07-15T00:00:00.000Z",
                        y: [153.29, 157.1, 152.39, 153.17],
                    },
                    {
                        x: "2019-07-16T00:00:00.000Z",
                        y: [153.05, 155.46, 146.65, 151.79],
                    },
                    {
                        x: "2019-07-17T00:00:00.000Z",
                        y: [152.4, 161.77, 151.57, 160.79],
                    },
                    {
                        x: "2019-07-18T00:00:00.000Z",
                        y: [159.77, 163.17, 157.15, 162.93],
                    },
                    {
                        x: "2019-07-19T00:00:00.000Z",
                        y: [164.88, 166.41, 161, 164]
                    },
                    {
                        x: "2019-07-22T00:00:00.000Z",
                        y: [164.39, 166.3, 160.23, 160.86],
                    },
                    {
                        x: "2019-07-23T00:00:00.000Z",
                        y: [162.56, 163.1, 154.34, 155.97],
                    },
                    {
                        x: "2019-07-24T00:00:00.000Z",
                        y: [155.12, 158, 152.18, 156.02]
                    },
                    {
                        x: "2019-07-25T00:00:00.000Z",
                        y: [156, 158.58, 153.33, 155.7]
                    },
                    {
                        x: "2019-07-26T00:00:00.000Z",
                        y: [156.73, 159.5, 155.5, 158.06],
                    },
                    {
                        x: "2019-07-29T00:00:00.000Z",
                        y: [157.9, 158.52, 143.45, 144.89],
                    },
                    {
                        x: "2019-07-30T00:00:00.000Z",
                        y: [144.01, 146.08, 140, 142.03]
                    },
                    {
                        x: "2019-07-31T00:00:00.000Z",
                        y: [143, 146.9, 140.88, 143.22]
                    },
                    {
                        x: "2019-08-01T00:00:00.000Z",
                        y: [142.93, 148.78, 138.12, 143.66],
                    },
                    {
                        x: "2019-08-02T00:00:00.000Z",
                        y: [142.23, 143.5, 137.35, 140.78],
                    },
                    {
                        x: "2019-08-05T00:00:00.000Z",
                        y: [135.87, 141.14, 134.32, 135.88],
                    },
                    {
                        x: "2019-08-06T00:00:00.000Z",
                        y: [137.98, 141.09, 137.2, 139]
                    },
                    {
                        x: "2019-08-07T00:00:00.000Z",
                        y: [135.78, 143.2, 135.41, 142.63],
                    },
                    {
                        x: "2019-08-08T00:00:00.000Z",
                        y: [144.06, 150.79, 144.06, 149.51],
                    },
                    {
                        x: "2019-08-09T00:00:00.000Z",
                        y: [148.78, 151.37, 146.48, 148.9],
                    },
                    {
                        x: "2019-08-12T00:00:00.000Z",
                        y: [148.47, 148.47, 142.16, 143.51],
                    },
                    {
                        x: "2019-08-13T00:00:00.000Z",
                        y: [142.02, 147.82, 142.02, 146.23],
                    },
                    {
                        x: "2019-08-14T00:00:00.000Z",
                        y: [142.92, 145.15, 138.36, 142.28],
                    },
                    {
                        x: "2019-08-15T00:00:00.000Z",
                        y: [142.7, 144.5, 139.8, 141.65]
                    },
                    {
                        x: "2019-08-16T00:00:00.000Z",
                        y: [143.23, 146.73, 142.51, 143.79],
                    },
                    {
                        x: "2019-08-19T00:00:00.000Z",
                        y: [146.67, 147.69, 140.34, 140.58],
                    },
                    {
                        x: "2019-08-20T00:00:00.000Z",
                        y: [140, 140.9, 137.34, 139.19]
                    },
                    {
                        x: "2019-08-21T00:00:00.000Z",
                        y: [141.95, 149.51, 140.75, 148.08],
                    },
                    {
                        x: "2019-08-22T00:00:00.000Z",
                        y: [148.11, 149.27, 142.16, 142.34],
                    },
                    {
                        x: "2019-08-23T00:00:00.000Z",
                        y: [141.97, 146, 138.62, 139.37]
                    },
                    {
                        x: "2019-08-26T00:00:00.000Z",
                        y: [142.36, 146.92, 140.38, 146.65],
                    },
                    {
                        x: "2019-08-27T00:00:00.000Z",
                        y: [153.05, 158.25, 149.15, 150.21],
                    },
                    {
                        x: "2019-08-28T00:00:00.000Z",
                        y: [154.26, 156.89, 145.35, 147.98],
                    },
                    {
                        x: "2019-08-29T00:00:00.000Z",
                        y: [150.5, 155.91, 148.25, 154.36],
                    },
                    {
                        x: "2019-08-30T00:00:00.000Z",
                        y: [155.59, 157.19, 148, 152.31]
                    },
                    {
                        x: "2019-09-03T00:00:00.000Z",
                        y: [150.7, 155, 147.35, 149.94]
                    },
                    {
                        x: "2019-09-04T00:00:00.000Z",
                        y: [152.98, 160.41, 152.98, 158.66],
                    },
                    {
                        x: "2019-09-05T00:00:00.000Z",
                        y: [156.66, 159, 142.35, 150.44]
                    },
                    {
                        x: "2019-09-06T00:00:00.000Z",
                        y: [149.66, 150.33, 140.17, 140.63],
                    },
                    {
                        x: "2019-09-09T00:00:00.000Z",
                        y: [140.62, 142.56, 125.2, 131.37],
                    },
                    {
                        x: "2019-09-10T00:00:00.000Z",
                        y: [127.43, 136.25, 126.14, 129.02],
                    },
                    {
                        x: "2019-09-11T00:00:00.000Z",
                        y: [128.58, 132.49, 126.45, 130.58],
                    },
                    {
                        x: "2019-09-12T00:00:00.000Z",
                        y: [133, 135.8, 128.3, 128.53]
                    },
                    {
                        x: "2019-09-13T00:00:00.000Z",
                        y: [127.74, 128.18, 121.12, 123.29],
                    },
                    {
                        x: "2019-09-16T00:00:00.000Z",
                        y: [121.29, 132.12, 120.05, 132]
                    },
                    {
                        x: "2019-09-17T00:00:00.000Z",
                        y: [131.56, 136.08, 129.71, 136]
                    },
                    {
                        x: "2019-09-18T00:00:00.000Z",
                        y: [136.06, 136.74, 131.19, 134.28],
                    },
                    {
                        x: "2019-09-19T00:00:00.000Z",
                        y: [134.21, 135, 130.36, 131.46]
                    },
                    {
                        x: "2019-09-20T00:00:00.000Z",
                        y: [133.01, 134.9, 129.52, 131.82],
                    },
                ],
            }, ],
            chart: {
                toolbar: {
                    show: false,
                },
                type: "candlestick",
                height: "380",
            },
            responsive: [{
                breakpoint: 580,
                options: {
                    chart: {
                        height: 280,
                    },
                },
            }, ],
            plotOptions: {
                candlestick: {
                    colors: {
                        upward: "#20B757",
                        downward: "#FFC861",
                    },
                },
            },

            xaxis: {
                type: "numeric",
                categories: [
                    "Jan",
                    "Feb",
                    "Mar",
                    "Apr",
                    "May",
                    "Jun",
                    "Jul",
                    "Aug",
                    "Sep",
                    "Oct",
                    "Nov",
                    "Dec",
                ],
                tooltip: {
                    enabled: false,
                },
                axisBorder: {
                    show: false,
                },
            },
            yaxis: {
                tooltip: {
                    enabled: false,
                    // followCursor: true
                },
                labels: {
                    // show: window.innerWidth > 768 ? true : false,
                    formatter: function(val) {
                        return val.toFixed(0);
                    },
                },
            },
            grid: {
                xaxis: {
                    lines: {
                        show: false,
                    },
                },
                yaxis: {
                    lines: {
                        show: true,
                    },
                },
            },
            tooltip: {
                enabled: true,
            },
        };
        const chart = new ApexCharts(usdChart, candlestick);
        chart.render();
    }

    // reports 2 stat chart
    const reportsStatCharts = document.querySelectorAll(".reports-stat-chart");
    if (reportsStatCharts.length > 0) {
        const chartData = {
            chart: {
                height: "60",
                width: "140",
                type: "area",
                sparkline: {
                    enabled: true,
                },
                toolbar: {
                    show: false,
                },
                animations: {
                    enabled: true,
                    easing: "easeinout",
                    speed: 800,
                },
            },
            grid: {
                show: false,
            },
            dataLabels: {
                enabled: false,
            },
            stroke: {
                width: 3,
                lineCap: "round",
                curve: "smooth",
            },
            series: [{
                name: "Series 1",
                data: [26, 36, 50, 28, 32, 23, 34],
            }, ],
            tooltip: {
                enabled: false,
            },
            colors: ["#20B757"],
            fill: {
                colors: ["#20B757"],
                opacity: 1,
                type: "gradient",
                gradient: {
                    shade: "dark",
                    type: "vertical",
                    shadeIntensity: 0.3,
                    gradientToColors: undefined,
                    inverseColors: false,
                    opacityFrom: 0.4,
                    opacityTo: 0,
                    stops: [0, 100],
                    colorStops: [],
                },
            },
            xaxis: {
                tooltip: {
                    enabled: false,
                },
                axisBorder: {
                    show: false,
                },
                axisTicks: {
                    show: false,
                },
                labels: {
                    show: false,
                },
            },
            yaxis: {
                min: 0,
                max: 50,
                tooltip: {
                    enabled: false,
                    // followCursor: true
                },
                labels: {
                    show: false,
                },
            },
        };
        reportsStatCharts.forEach((el) => {
            const chart = new ApexCharts(el, chartData);
            chart.render();
        });
    }

    // reports ac balance
    const reportsAcBalance = document.querySelector(".reports-ac-balance");
    if (reportsAcBalance) {
        const chartData = {
            series: [{
                    name: "Recent Year",
                    type: "line",
                    data: [20, 38, 38, 73, 55, 63, 44, 75, 53, 80, 40, 80],
                },
                {
                    name: "Last 5 Years",
                    type: "line",
                    data: [85, 66, 76, 38, 86, 35, 62, 40, 40, 64, 50, 87],
                },
            ],
            annotations: {
                xaxis: [{
                    strokeDashArray: 0,
                    borderWidth: 0,
                    label: {
                        borderColor: "#775DD0",
                        borderWidth: 0,
                        offsetX: -40,
                        offsetY: 120,
                        style: {
                            color: "#fff",
                            background: "none",
                            fontSize: "12px",
                        },
                        text: "Account Balance",
                    },
                }, ],
            },
            chart: {
                height: 500,
                type: "line",
                toolbar: {
                    show: false,
                },
            },
            legend: {
                show: true,
                itemMargin: {
                    horizontal: 15,
                },
                markers: {
                    width: 6,
                    height: 6,
                    offsetX: dir == "rtl" ? 5 : -5,
                },
            },
            colors: ["#63CC8A", "#FFC861"],
            stroke: {
                width: [3, 3],
                curve: "smooth",
                lineCap: "round",
                dashArray: [0, 5],
            },
            xaxis: {
                type: "category",
                categories: [
                    "Jan",
                    "Feb",
                    "Mar",
                    "Apr",
                    "May",
                    "Jun",
                    "Jul",
                    "Aug",
                    "Sep",
                    "Oct",
                    "Nov",
                    "Dec",
                ],
                tickAmount: 12,
                axisTicks: {
                    show: false,
                },
                axisBorder: {
                    show: false,
                },
            },
            yaxis: {
                min: 0,
                max: 100,
                tickAmount: 5,
                labels: {
                    offsetX: 15,
                },
            },
            fill: {
                opacity: 1,
            },
            grid: {
                padding: {
                    left: 30,
                    bottom: 20,
                },
                show: true,
                xaxis: {
                    lines: {
                        show: true,
                    },
                },
            },
            responsive: [{
                    breakpoint: 1500,
                    options: {
                        chart: {
                            height: 350,
                        },
                    },
                },
                {
                    breakpoint: 992,
                    options: {
                        chart: {
                            height: 350,
                        },
                    },
                },
                {
                    breakpoint: 570,
                    options: {
                        chart: {
                            height: 280,
                        },
                    },
                },
            ],
        };
        const chart = new ApexCharts(reportsAcBalance, chartData);
        chart.render();
    }
});