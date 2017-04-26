'use strict';
var app = angular.module('loginApp', []).config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

app.controller('loginCtrl', ['$scope', '$rootScope', '$location', 'AuthenticationService', function ($scope, $rootScope, $location, AuthenticationService) {
	$rootScope.prop.menu = false;

    $scope.footerID = document.getElementById('footer');
    $scope.bodyID = document.getElementById('body');
    $scope.footerID.style.position = 'absolute';
    $scope.footerID.style.bottom = '0';
    $scope.footerID.style.width = '100%';
    $scope.bodyID.style.backgroundColor = '#eee';

	// reset login status
        AuthenticationService.ClearCredentials();
  
        $scope.login = function (email, password) {
            $scope.dataLoading = true;
            AuthenticationService.Login(email, password, function(response) {
                if(response != 'Erro') {
					console.log(response.email);
                    AuthenticationService.SetCredentials(email, password, response.user_id, response.name);
                    $location.path('/moviemancer');
                } else {
                    $scope.error = response;
                    $scope.dataLoading = false;
                }
            });
        };
}]);