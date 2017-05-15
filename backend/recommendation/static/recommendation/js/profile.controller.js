var app = angular.module('profileApp', []).config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

app.controller('profileCtrl', ['$scope', '$http', '$rootScope', function ($scope, $http, $rootScope) {

}]);