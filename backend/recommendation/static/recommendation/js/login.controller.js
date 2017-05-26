'use strict';
var app = angular.module('loginApp', []).config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

app.controller('loginCtrl', ['$scope', '$rootScope', '$location', 'AuthenticationService', function ($scope, $rootScope, $location, AuthenticationService) {
	$rootScope.prop.menu = false;

    $scope.dataLoading = true;
    $scope.loginGroup = false;

    $scope.footerID = document.getElementById('footer');
    $scope.bodyID = document.getElementById('body');
    $scope.footerID.style.position = 'absolute';
    $scope.footerID.style.display = 'block';
    $scope.footerID.style.bottom = '0';
    $scope.footerID.style.width = '100%';
    $scope.bodyID.style.backgroundColor = '#eee';
    

	// reset login status
        AuthenticationService.ClearCredentials();
  
        $scope.login = function (email, password) {
            $scope.loginGroup = false;
            $scope.dataLoading = true;

            AuthenticationService.Login(email, password, function(response) {
                if(response != 'Erro') {
                    AuthenticationService.SetCredentials(email, password, response.user_id, response.name);
                    $location.path('/moviemancer');
                } else {
                    $scope.error = response;
                    $scope.loginGroup = true;
                    $scope.dataLoading = false;
                    document.getElementById('loginGroup').style.display = 'none';
                }
            });
        };
}]);