var app = angular.module('singupApp', []).config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

app.controller('singupCtrl', ['$scope', '$window','$rootScope', '$http', function ($scope, $window, $rootScope, $http) {
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
                $scope.validateUser(name, email, password, confirmedPassword);
            }else {
                $scope.invalidateField('passwordConfirm');
                $scope.invalidateField('password');
            }
            
        }
    }

    $scope.validateUser = function (name, email, password) {
        $http.post("validateuser/", {
			"email": email
		}, {
				'Content-Type': 'application/json; charset=utf-8'
			})
			.then(
			function (response) {
				console.log('Success: ', response.data)
				$scope.chooseGenres(name, email, password);
			},
			function (response) {
				console.log('Error: ', response)
                $scope.toastMessege("Email já cadastrado");
                $scope.invalidateField('email');
			}
			);
	}

    $scope.chooseGenres = function(name, email, password, confirmedPassword) {

        $rootScope.registration = {name: name, email: email, password: password}

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


