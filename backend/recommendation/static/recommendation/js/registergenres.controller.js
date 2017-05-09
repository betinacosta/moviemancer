var app = angular.module('registergenresApp', []).config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

app.controller('registergenresCtrl', ['$scope', '$window', '$rootScope','$http', function ($scope, $window, $rootScope, $http) {
	//console.log($rootScope.registration);

	$scope.remainigGenres = 3;
	$scope.displayOkBtn = false;

	$scope.genres = [{
			id: 28,
			name: "Ação",
			selected: false
		},
		{
			id: 12,
			name: "Aventura",
			selected: false
		},
		{
			id: 16,
			name: "Animação",
			selected: false
		},
		{
			id: 35,
			name: "Comédia",
			selected: false
		},
		{
			id: 80,
			name: "Crime",
			selected: false
		},
		{
			id: 99,
			name: "Documentário",
			selected: false
		},
		{
			id: 18,
			name: "Drama",
			selected: false
		},
		{
			id: 14,
			name: "Fantasia",
			selected: false
		},
		{
			id: 36,
			name: "História",
			selected: false
		},
		{
			id: 27,
			name: "Terror",
			selected: false
		},
		{
			id: 10402,
			name: "Musical",
			selected: false
		},
		{
			id: 9648,
			name: "Mistério",
			selected: false
		},
		{
			id: 10749,
			name: "Romance",
			selected: false
		},
		{
			id: 878,
			name: "Ficção Científica",
			selected: false
		},
		{
			id: 53,
			name: "Thriller",
			selected: false
		},
		{
			id: 10752,
			name: "Guerra",
			selected: false
		},
		{
			id: 37,
			name: "Faroeste",
			selected: false
		},
		{
			id: 10751,
			name: "Família",
			selected: false
		}
	];

	$scope.countSelected = function () {
		$scope.counter = 0;
		for (i = 0; i < $scope.genres.length; i++) {
			if ($scope.genres[i].selected) {
				$scope.counter++;
			}
		}
		if ($scope.counter < 3) {
			return (true);
		} else {
			return (false)
		}
	}

	$scope.selectGenre = function (genreIndex, cssID) {
		if ($scope.genres[genreIndex].selected) {
			$scope.genres[genreIndex].selected = false;
			document.getElementById(cssID).style.backgroundColor = '#eeeeee';
			document.getElementById(cssID).style.color = '#2b2b2b';
			$scope.remainigGenres++;
		} else {
			if ($scope.countSelected()) {
				$scope.genres[genreIndex].selected = true;
				document.getElementById(cssID).style.backgroundColor = '#006400';
				document.getElementById(cssID).style.color = '#eeeeee';
				$scope.remainigGenres--;

			}
		}
		if ($scope.remainigGenres == 0) {
			$scope.displayOkBtn = true;
		}else {
			$scope.displayOkBtn = false;
		}

	}

	$scope.registerUser = function () {
		$scope.selectedGenres = [];
		
		for (i = 0; i < $scope.genres.length; i++) {
			if ($scope.genres[i].selected) {
				$scope.selectedGenres.push($scope.genres[i].id);
			}
		}

		$scope.genre1 = $scope.selectedGenres[0]
		$scope.genre2 = $scope.selectedGenres[1]
		$scope.genre3 = $scope.selectedGenres[2]


		$http.post("registration/", {
			"name": $rootScope.registration.name,
			"email": $rootScope.registration.email,
			"password": $rootScope.registration.password,
			"genre_1": $scope.genre1,
			"genre_2": $scope.genre2,
			"genre_3": $scope.genre3
		}, {
				'Content-Type': 'application/json; charset=utf-8'
			})
			.then(
			function (response) {
				$window.location.href = '#/';
			},
			function (response) {
				console.log('Error: ', response)
			}
			);
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