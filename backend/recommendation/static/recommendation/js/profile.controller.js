var app = angular.module('profileApp', []).config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

app.controller('profileCtrl', ['$scope', '$http', '$rootScope', function ($scope, $http, $rootScope) {

	$scope.init = function () {
		$scope.getProfile();
	}

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

	$scope.getGenreName = function (genreID) {
		for (i=0;i<$scope.genres.length; i++) {
			if($scope.genres[i].id == genreID) {
				return $scope.genres[i].name
			}
		}
	}

	$scope.getProfile = function () {
		$http.post("getprofile/", {
			"user_id": $rootScope.globals.currentUser.user_id
		}, {
				'Content-Type': 'application/json; charset=utf-8'
			})
			.then(
			function (response) {
				$scope.name = response.data.name;
				$scope.email = response.data.email;
				$scope.genre1 = $scope.getGenreName(response.data.genres[0]);
				$scope.genre2 = $scope.getGenreName(response.data.genres[1]);
				$scope.genre3 = $scope.getGenreName(response.data.genres[2]);
			},
			function (response) {
				console.log('Error: ', response)
			});
		}

	$scope.validateEntry = function(name, email, password, confirmedPassword) {
       
    }

	 $scope.clearField = function(fieldID){
        $scope.nameID = document.getElementById(fieldID);
        $scope.nameID.style.borderColor  = '#7d7b7b';
    }

    $scope.invalidateField = function(fieldID){
        $scope.nameID = document.getElementById(fieldID);
        $scope.nameID.style.borderColor  = 'red';
    }

	$scope.validateGenres = function() {
		if ($scope.firstG == $scope.secondG || $scope.firstG == $scope.thirdG || $scope.secondG == $scope.secondG) {
			if ($scope.firstG == $scope.secondG) {
				
			}

		} else {
			$scope.updateGenres();
		}
	}

	$scope.init();
}]);