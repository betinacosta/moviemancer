var app = angular.module('notFoundApp', []).config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

app.controller('notFoundCtrl', ['$scope', '$http', '$rootScope', function ($scope, $http, $rootScope) {
	if ($rootScope.globals.currentUser){
		$rootScope.prop.sanduba = true;
	}else {
		$rootScope.prop.sanduba = false;
	}

}]);