var claqueteApp = angular.module('claqueteApp', ['ngRoute', 'myApp']);

claqueteApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
        when('/', {
            templateUrl: 'main',  
            controller: 'mainCtrl'
        }).
        when('/full-recommendation', {
            templateUrl: 'full-recommendation',  
            controller: 'mainCtrl'
        });
    }

]);

claqueteApp.config([
    '$httpProvider', function ($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrfToken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }
]);