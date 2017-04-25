var app = angular.module('singupApp', []).config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

app.controller('singupCtrl', ['$scope', function ($scope) {

}]);