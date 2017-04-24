var app = angular.module('homeApp', []).config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

app.controller('homeCtrl', ['$scope','$window', 'AuthenticationService', '$location', '$rootScope', function ($scope, $window, AuthenticationService, $location, $rootScope) {
    
    $scope.logedMenu = function() {
        if($rootScope.globals.currentUser) {
            $scope.sanduba = true;
            $scope.userName = $rootScope.globals.currentUser.name;
        }
    }

    $scope.menu = false;
    $scope.sanduba = false;
    $scope.logedMenu();

    console.log($rootScope)

$scope.showMenu = function(){
    $scope.menu = !$scope.menu;
},

$scope.logOut = function(){
    AuthenticationService.ClearCredentials();
    $location.path('/');
}

}]);