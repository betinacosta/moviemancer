'use strict';
angular.module('Authentication', []);
var claqueteApp = angular.module('claqueteApp', [   'ngRoute', 'mainApp', 'recommendationApp',
                                                    'moviedetailsApp','vistoApp','queroVerApp',
                                                    'filtersApp','homeApp','loginApp', 
                                                    'singupApp', 'Authentication',
                                                    'ngRoute','ngCookies']);

claqueteApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
        when('/', {
            templateUrl: 'login',  
            controller: 'loginCtrl'
        }).when('/moviemancer', {
            templateUrl: 'moviemancer',  
            controller: 'mainCtrl'
        }).when('/singup', {
            templateUrl: 'singup',  
            controller: 'singupCtrl'
        }).
        when('/recommendation', {
            templateUrl: 'recommendation',  
            controller: 'recoCtrl'
        }).
        when('/moviedetails/:tmdbID', {
            templateUrl: 'moviedetails',
            controller: 'moviedetailsCtrl'
        }).
        when('/watchedlistview', {
            templateUrl: 'watchedlist',
            controller: 'watchedListCtrl'
        }).
        when('/watchlistview', {
            templateUrl: 'watchlist',
            controller: 'watchlistCtrl'
        }).
        when('/filtersview/:genres/:language/:yearMin/:yearMax/:runtimeMin/:runtimeMax', {
            templateUrl: 'filters',
            controller: 'filtersCtrl'
        });
    }

]).run(['$rootScope', '$location', '$cookieStore', '$http',
    function ($rootScope, $location, $cookieStore, $http) {
        // keep user logged in after page refresh
        $rootScope.globals = $cookieStore.get('globals') || {};
        if ($rootScope.globals.currentUser) {
            $http.defaults.headers.common['Authorization'] = 'Basic ' + $rootScope.globals.currentUser.authdata; // jshint ignore:line
        }
  
        $rootScope.$on('$locationChangeStart', function (event, next, current) {
            // redirect to login page if not logged in
            if ($location.path() !== '/' && !$rootScope.globals.currentUser) {
                $location.path('/');
            }
        });
    }]);

claqueteApp.config([
    '$httpProvider', function ($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrfToken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }
]);
