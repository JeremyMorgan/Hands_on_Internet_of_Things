/**
 * Load modules for application
 */

angular
    
    .module('angularstrapApp', [
        'ui.router',
        'chart.js',
        'angularstrapApp.homeServices',
        'angularstrapApp.requestServices',
        'angularMoment',
        'googlechart'
    ])

    .constant('CONFIG', 
    {
	    DebugMode: true,
	    StepCounter: 0,
	    APIHost: 'http://internet-of-things.jeremymorgan.com:5000'
	}); 