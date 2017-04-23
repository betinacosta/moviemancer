var app = angular.module('homeApp', []).config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

app.controller('homeCtrl', ['$scope','$window', function ($scope, $window) {
    $scope.menu = false;

$scope.showMenu = function(){
    $scope.menu = !$scope.menu;
}


}]);