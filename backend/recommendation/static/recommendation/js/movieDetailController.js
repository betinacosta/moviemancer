var app = angular.module('myApp3', ['ngRateIt']).config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    });

app.controller('movieCtrl', ['$scope', '$http', '$routeParams', function ($scope, $http, $routeParams) {
    console.log('vamo dale, dale vamo');
    console.log($routeParams.tmdbID);
    $scope.batata = 'batata';

}]);
