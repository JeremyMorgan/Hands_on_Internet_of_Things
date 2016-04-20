(function () {
    'use strict';

    angular.module('angularstrapApp.homeServices', [])
        .service('asyncService', asyncService);

    asyncService.$inject = ['CONFIG', '$q', 'requestService', 'moment'];

    function asyncService(CONFIG, $q, requestService, moment) {

        var sm = this;
        sm.DebugMode = CONFIG.DebugMode;
        sm.retrievedData = [];
        sm.tempData = [];
        sm.timeLabels = [];
        sm.averageTemp = "";

        sm.topGraphLast30 = topGraphLast30;
        sm.getfullDataSet = getfullDataSet;

        function getfullDataSet() {

            var deferred = $q.defer();

            var parameters = {Url: CONFIG.APIHost + "/weather/api/v1/readings", Verb: "GET", PostData: ""};

            requestService.sendRequest(parameters)
                .then(function (sendresult) {
                    sm.retrievedData = sendresult;
                    deferred.resolve(sendresult);
                }, function (error) {
                    if (sm.DebugMode) {
                        console.log("requestService Error: " + JSON.stringify(error));
                    }
                    deferred.reject(error);
                });

            return deferred.promise;
        }


        function topGraphLast30() {

            var deferred = $q.defer();

            //console.log("SWEET : " + JSON.stringify(factory.retrievedData));

            /*

             {
             'Temp2': '22.3999996185',
             'Temp1': '21.9000000000',
             'SeaLevelPressure': '100150.0000000000',
             'TempSensorAvg': '22.1499998093',
             'Pressure': '47.9000015259',
             'TimeStamp':
             '2016-04-13 21:00:02',
             'readingID': 3,
             'Humidity': '100150.0000000000'
             }"

             */

            var tempData = [];
            var humData = [];
            var timeLabels = [];
            var runningtemp = 0;
            sm.counter = 0;

            angular.forEach(sm.retrievedData, function (value, key) {

                // convert to F
                var temp = (value.TempSensorAvg * 9 / 5 + 32);

                // push temp into array
                tempData.push(parseFloat(temp).toFixed(2));

                // stack timestamps
                timeLabels.push(moment(value.TimeStamp, "YYYY-MM-DD HH:mm").format("hh:mm"));

                // add up running temperature
                runningtemp += temp;

                // increment counter
                sm.counter++;
            });

            // get a running average
            sm.averageTemp = runningtemp / sm.counter;
            // enclose the 30 minute temp data for the line graph
            sm.tempData = [tempData];
            // set up the labels for the line graph
            sm.timeLabels = timeLabels;

            // now we'll gather the last values for each to get current reading
            sm.humidity = parseFloat(sm.retrievedData[sm.retrievedData.length - 1].Humidity).toFixed(2);
            sm.tempAvg = parseFloat((sm.retrievedData[sm.retrievedData.length - 1].TempSensorAvg * 9 / 5 + 32)).toFixed(2);
            sm.pressure = parseFloat(sm.retrievedData[sm.retrievedData.length - 1].Pressure).toFixed(2);
            sm.sealevelpressure = parseFloat(sm.retrievedData[sm.retrievedData.length - 1].SeaLevelPressure).toFixed(2);
            sm.timestamp = sm.retrievedData[sm.retrievedData.length - 1].TimeStamp;

            deferred.resolve();

            return deferred.promise;
        }

        return sm;
    }
})();