var app = angular.module('registergenresApp', []).config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

app.controller('registergenresCtrl', ['$scope', '$window','$rootScope', function ($scope, $window, $rootScope) {
    //console.log($rootScope.registration);

	$scope.remainigGenres = 3;

	$scope.selectedGenres = 0;

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
		}];

		$scope.countSelected = function() {
			$scope.counter = 0;
			for (i=0;i<$scope.genres.length; i++) {
				if($scope.genres[i].selected) {
					$scope.counter++;
				}
			}
			if ($scope.counter < 3) {
				return(true);
			}else {
				return(false)
			}
		}

		$scope.selectGenre = function(genreIndex, cssID) {
			if ($scope.genres[genreIndex].selected) {
					$scope.genres[genreIndex].selected = false;
					document.getElementById(cssID).style.backgroundColor = '#eeeeee';
					document.getElementById(cssID).style.color = '#2b2b2b';
					$scope.remainigGenres++;
			} else {
				if ($scope.countSelected()) {
				console.log('dalhe')
				$scope.genres[genreIndex].selected = true;
				document.getElementById(cssID).style.backgroundColor = '#006400';
				document.getElementById(cssID).style.color = '#eeeeee';
				$scope.remainigGenres--;

			}
			}
			
		}

}]);