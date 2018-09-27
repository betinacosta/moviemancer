var app = angular.module('homeApp', []).config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

app.controller('homeCtrl', ['$scope', '$window', 'AuthenticationService', '$location', '$rootScope', function ($scope, $window, AuthenticationService, $location, $rootScope) {
    $rootScope.prop = { sanduba: false };
    $rootScope.prop = { menu: false };
    $scope.logedMenu = function () {
        if ($rootScope.globals.currentUser) {
            $rootScope.prop.sanduba = true;
            $scope.userName = $rootScope.globals.currentUser.name;
        }
    }

    $scope.logedMenu();


    $scope.showMenu = function () {
        $rootScope.prop.menu = !$rootScope.prop.menu;
    },

        $scope.logOut = function () {
            $rootScope.prop = { sanduba: false };
            $rootScope.prop = { menu: false };
            AuthenticationService.ClearCredentials();
            $location.path('/');
        }

}]);