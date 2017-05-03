var app = angular.module('registergenresApp', []).config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

app.controller('registergenresCtrl', ['$scope', '$window','$rootScope', function ($scope, $window, $rootScope) {
    console.log($rootScope.registration);

	$scope.remainigGenres = 3;

}]);