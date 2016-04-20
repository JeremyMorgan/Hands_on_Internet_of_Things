(function () {
    'use strict';

    // service
    angular
        .module('angularstrapApp.requestServices',[])
        .service('requestService', requestService);

    requestService.$inject = ['$http', '$q', '$timeout', CONFIG];

    function requestService($http, $q, $timeout, CONFIG) {

        var vm = this;

        return {
            sendRequest: sendRequest,
            returnData: []
        };

        function sendRequest(parameters){

            vm.DebugMode = CONFIG.DebugMode;

            var Url = parameters.Url;
            var Verb = parameters.Verb;
            var PostData = parameters.PostData;

            var deferred = $q.defer();

            switch (Verb) {
                case 'GET':
                    $http.get(Url).
                        then(function(response) {
                            deferred.resolve(response.data);
                        }, function(error) {
                            if (CONFIG.DebugMode){
                                console.log("\tERROR: requestService: GET sendRequest" + JSON.stringify(error));
                            }
                            deferred.reject(error);
                        });
                    break;

                case 'DELETE':
                    if (CONFIG.DebugMode){
                        console.log("\tSending Delete");
                        console.log("\tUsing URL: " + Url);
                        CONFIG.StepCounter++;
                    }

                    if (PostData){
                        var config = { data: JSON.stringify(PostData) };

                        return $http.delete(Url,config).then(function(response) {
                            return response.data;
                        });
                    }else{
                        return $http.delete(Url).then(function(response) {
                            return response.data;
                        });
                    }

                    break;

                case 'POST':

                    // var serializedData = JSON.stringify(PostData);

                    $http({
                        method: 'POST',
                        url: Url,
                        data: PostData,
                        headers: {
                            //'Host' : 'hqse10testapp',
                            'Connection' : 'keep-alive',
                            'Cache-Control' : 'no-cache',
                            //'Content-Type': 'application/x-www-form-urlencoded'
                            'Content-Type' : 'application/json'
                        }}).then(function(result) {
                        console.log("good!" + result);
                    }, function(error) {
                        if(vm.DebugMode){
                            console.log("Request Error: " + JSON.stringify(error));
                        }
                        deferred.reject(error);
                    });

                    break;
            }
            return deferred.promise;
        }
    }

})().config(function($httpProvider){
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/json';
    //$httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
});
