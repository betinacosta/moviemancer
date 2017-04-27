var app = angular.module('singupApp', []).config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

app.controller('singupCtrl', ['$scope', '$window','$rootScope', function ($scope, $window, $rootScope) {
	$scope.footerID = document.getElementById('footer');
    $scope.bodyID = document.getElementById('body');
    $scope.footerID.style.position = 'absolute';
    $scope.footerID.style.bottom = '0';
    $scope.footerID.style.width = '100%';
    $scope.bodyID.style.backgroundColor = '#eee';

    $scope.validateEntry = function(name, email, password, confirmedPassword) {
        if(name == null || email == null || password == null || confirmedPassword == null) {
            if(name == null) {
                $scope.invalidateField('name');
            }

            if(email == null) {
                $scope.invalidateField('email');
            }

            if(password == null) {
                $scope.invalidateField('password');
            }

            if(confirmedPassword == null) {
                 $scope.invalidateField('passwordConfirm');
            }
        }else {
            if(password == confirmedPassword) {
                $scope.chooseGenres(name, email, password, confirmedPassword);
            }else {
                $scope.invalidateField('passwordConfirm');
                $scope.invalidateField('password');
            }
            
        }
    }

    $scope.chooseGenres = function(name, email, password, confirmedPassword) {

        $rootScope.registration = {name: name, email: email, password: password, confirmedPassword: confirmedPassword}

        $window.location.href = '#/registergenres';
    }

    $scope.clearField = function(fieldID){
        $scope.nameID = document.getElementById(fieldID);
        $scope.nameID.style.borderColor  = '#7d7b7b';
    }

    $scope.invalidateField = function(fieldID){
        $scope.nameID = document.getElementById(fieldID);
        $scope.nameID.style.borderColor  = 'red';
    }
}]);


