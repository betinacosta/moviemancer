var claqueteApp = angular.module('claqueteApp', ['ngRoute', 'myApp', 'myApp2','myApp3','vistoApp']);

claqueteApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
        when('/', {
            templateUrl: 'main',  
            controller: 'mainCtrl'
        }).
        when('/full-recommendation', {
            templateUrl: 'full-recommendation',  
            controller: 'recoCtrl'
        }).
        when('/moviedetails/:tmdbID/:userID', {
            templateUrl: 'moviedetails',
            controller: 'movieCtrl'
        }).
        when('/watchedlistview', {
            templateUrl: 'watchedlist',
            controller: 'watchedListCtrl'
        });
    }

]);

claqueteApp.config([
    '$httpProvider', function ($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrfToken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }
]);