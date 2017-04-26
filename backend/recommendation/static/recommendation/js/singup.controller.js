var app = angular.module('singupApp', []).config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

app.controller('singupCtrl', ['$scope', function ($scope) {
	$scope.footerID = document.getElementById('footer');
    $scope.bodyID = document.getElementById('body');
    $scope.footerID.style.position = 'absolute';
    $scope.footerID.style.bottom = '0';
    $scope.footerID.style.width = '100%';
    $scope.bodyID.style.backgroundColor = '#eee';
}]);