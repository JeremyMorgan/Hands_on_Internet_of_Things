(function () {
    'use strict';

    angular.module('angularstrapApp')
        .controller('homeController', homeController);

    homeController.$inject = ["$scope", "$http", "$window", "$q", "asyncService"];

    function sorter(b, c) {
        return c - b;
    }

    function homeController($scope, $http, $window, $q, asyncService) {

            var vm = this;

            //services
            vm.angularstrapService = asyncService;

            // default to false to show loaders
            vm.dataLoaded = false;

            // from async service
            vm.HeroHeader = "IoT Dashboard";

            // Top Line Graph Config
            vm.tempGraphSeries = ['Temperature'];

        vm.angularstrapService.getfullDataSet().then(function (sendresult) {
                // start populatin
                console.log("Populated");
                vm.dataLoaded = true;

                vm.angularstrapService.topGraphLast30().then(function () {
                    //vm.tempGraphData = vm.angularstrapService.tempData;
                    vm.tempGraphData = vm.angularstrapService.tempData;
                    vm.humGraphData = vm.angularstrapService.humData;
                    vm.tempGraphLabels = vm.angularstrapService.timeLabels;
                    vm.tempstartValue = vm.angularstrapService.averageTemp - 3;
                    vm.humstartValue = 40;
                    vm.humidity = vm.angularstrapService.humidity;
                    vm.tempAvg = vm.angularstrapService.tempAvg;
                    vm.pressure = vm.angularstrapService.pressure;
                    vm.sealevelpressure = vm.angularstrapService.sealevelpressure;
                    vm.timestamp = vm.angularstrapService.timestamp;


                    $scope.chartObject = {};

                    $scope.chartObject.type = "Gauge";

                    $scope.chartObject.options = {
                        width: 960,
                        height: 300,
                        redFrom: 90,
                        redTo: 100,
                        yellowFrom: 75,
                        yellowTo: 90,
                        minorTicks: 5
                    };

                    console.log("TEMP IS " + vm.tempAvg);

                    $scope.chartObject.data = [
                        ['Label', 'Value'],
                        ['Temperature', parseInt(vm.tempAvg) ],
                        ['Humidity', parseInt(vm.humidity) ],
                        ['Barometer', parseInt(vm.pressure) ]
                    ];

                });

                }, function (error) {
                    if (CONFIG.DebugMode){
                        console.log("requestService Error: " + JSON.stringify(error));
                    }
                });

            vm.topGraphonClick = function (points, evt) {
                console.log(points, evt);
            };

            return vm;
       }
})();