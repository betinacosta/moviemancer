var app = angular.module('loginApp', []).config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

app.controller('loginCtrl', ['$scope', function ($scope) {

}]);