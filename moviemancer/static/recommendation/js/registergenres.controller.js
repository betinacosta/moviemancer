var app = angular.module('registergenresApp', []).config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

app.controller('registergenresCtrl', ['$scope', '$window', '$rootScope', '$http', 'MoviemancerService', function ($scope, $window, $rootScope, $http, MoviemancerService) {
	//console.log($rootScope.registration);

	$scope.footerID = document.getElementById('footer');
	$scope.bodyID = document.getElementById('body');
	$scope.footerID.style.display = 'none';
	$scope.bodyID.style.backgroundColor = 'white';

	$scope.sendRGBtn = true;
	$scope.forwardBtn = true;
	$scope.backBtn = false;

	$scope.counter = 0;
	$scope.index = 0;

	$scope.getRatedMovies = function () {
		$http.get("getratedmovies/")
			.then(function (response) {
				$scope.movies = []

				for (i = 0; i < response.data.length; i++) {
					$scope.movies.push(response.data[i])
				}
			});
	}
	$scope.getRatedMovies();

	$scope.getRateListLength = function (callback) {
		$http.get("getratedmovies/")
			.then(function (response) {
				callback(response.data.length)
			});
	}

	$scope.back = function () {
		$scope.index--;
		$scope.forwardBtn = true;
		if ($scope.index < 1) {
			$scope.backBtn = false;
		}
	}

	$scope.forward = function () {
		$scope.index++;
		$scope.backBtn = true;
		$scope.getRateListLength(function (length) {
			if ($scope.index > length - 1) {
				$scope.forwardBtn = false;

			}
		});
	}

	$scope.displayBtn = function () {
		$scope.sendRGBtn = false
	}

	$scope.setUserRating = function (rating, movieID) {
		if (rating > 2) {
			$scope.counter++;
		}

		if ($scope.counter > 0) {
			$scope.displayBtn();
		}

		MoviemancerService.setUserRating(rating, movieID, $rootScope.registration_id, function (response) {
			if (response.status == 200) {
				console.log('Success: ', response.data)
			} else {
				console.log('Error: ', response.data)
			}
		});
	}
	$scope.register = function () {
		$window.location.href = '#/';
	}
}]);