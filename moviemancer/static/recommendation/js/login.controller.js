'use strict';
var app = angular.module('loginApp', []).config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

app.controller('loginCtrl', ['$scope', '$rootScope', '$location', 'AuthenticationService', '$http',function ($scope, $rootScope, $location, AuthenticationService, $http) {
    $rootScope.prop.menu = false;

    $scope.dataLoading = false;
    $scope.loginGroup = true;

    $scope.footerID = document.getElementById('footer');
    $scope.bodyID = document.getElementById('body');
    $scope.footerID.style.display = 'block';
    $scope.footerID.style.bottom = '0';
    $scope.footerID.style.width = '100%';
    $scope.bodyID.style.backgroundColor = '#eee';

    $scope.sEmail = $rootScope.registration_email;


    // reset login status
    AuthenticationService.ClearCredentials();

    $scope.login = function (email, password) {
        $scope.loginGroup = false;
        $scope.dataLoading = true;
        $scope.footerID.style.position = 'absolute';

        AuthenticationService.Login(email, password, function (response) {
            if (response.status == 500) {
                if (response.data == 'Usuário e Senha não combinam') {
                    $scope.toastMessege(response.data);
                }else {
                    $scope.toastMessege('Erro ao fazer o logins');
                }
                
                $scope.loginGroup = true;
                $scope.dataLoading = false;
            } else {
                AuthenticationService.SetCredentials(email, password, response.data.user_id, response.data.name);
               $location.path('/moviemancer');
            }
        });
    };


    //--------------------------------------------Toast Message Handler--------------------------------------------

    $scope.toastMessege = function (msg) {
        $scope.toastMessage = msg;
        // Get the snackbar DIV
        var x = document.getElementById("snackbar")

        // Add the "show" class to DIV
        x.className = "show";

        // After 3 seconds, remove the show class from DIV
        setTimeout(function () { x.className = x.className.replace("show", ""); }, 3000);
    }
}]);