'use strict';
var app = angular.module('loginApp', []).config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

app.controller('loginCtrl', ['$scope', '$rootScope', '$location', 'AuthenticationService', function ($scope, $rootScope, $location, AuthenticationService) {
	console.log('bananaan')
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