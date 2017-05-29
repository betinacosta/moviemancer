var app = angular.module('recommendationApp', []).config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

app.controller('recoCtrl', ['$scope', '$http', '$rootScope', 'MoviemancerService', '$location', function ($scope, $http, $rootScope, MoviemancerService, $location) {
	$rootScope.prop.menu = false;

	//--------------------------------------------Get Recommendation Handler--------------------------------------------

	$scope.getRecommendation = function () {
		$http.post("getrecommendation/", {
			"user_id": $rootScope.globals.currentUser.user_id
		}, {
				'Content-Type': 'application/json; charset=utf-8'
			})
			.then(
			function (response) {
				$scope.fullRecommendation = [];
				$scope.index = [];

				for (i = 0; i < response.data.length; i++) {
					$scope.fullRecommendation.push({
						title: response.data[i].tmdb_title,
						poster: response.data[i].tmdb_poster,
						movie_id: response.data[i].movie_id,
						tmdb_id: response.data[i].tmdb_movie_id
					});
				}

				$scope.chunk_size = 6;
				$scope.fullList = $scope.fullRecommendation.map(function (e, i) {
					return i % $scope.chunk_size === 0 ? $scope.fullRecommendation.slice(i, i + $scope.chunk_size) : null;
				})
					.filter(function (e) { return e; });

				for (i = 0; i < $scope.fullList.length; i++) {
					$scope.index.push(i);
				}
			},
			function (response) {
				console.log('Error: ', response)
			});


	}

	//--------------------------------------------Filter Box Handlers--------------------------------------------
	$scope.filterVisible = false;
	$scope.toggle = true;

	$scope.yearSlider = {
		minValue: 1920,
		maxValue: 2017,
		options: {
			floor: 1920,
			ceil: 2017,
		}
	};

	$scope.runtimeSlider = {
		minValue: 50,
		maxValue: 300,
		options: {
			floor: 50,
			ceil: 300,
		}
	};

	$scope.genresSelector = MoviemancerService.getGenres();
	$scope.languages = MoviemancerService.getLanguages();

	$scope.selectPT = function () {
		$scope.languages = MoviemancerService.selectPT($scope.languages);
	}

	$scope.selectEN = function () {
		$scope.languages = MoviemancerService.selectEN($scope.languages);
	}

	$scope.selectDE = function () {
		$scope.languages = MoviemancerService.selectDE($scope.languages);
	}

	$scope.selectIT = function () {
		$scope.languages = MoviemancerService.selectIT($scope.languages);
	}

	$scope.selectJA = function () {
		$scope.languages = MoviemancerService.selectJA($scope.languages);
	}

	$scope.selectFR = function () {
		$scope.languages = MoviemancerService.selectFR($scope.languages);
	}

	$scope.selectGenre = function (id, index) {
		$scope.genresSelector = MoviemancerService.selectGenre(id, index, $scope.genresSelector);
	}

	$scope.showFilterBar = function () {
		$scope.filterVisible = !$scope.filterVisible;
		$scope.toggle = !$scope.toggle;
	},
		//--------------------------------------------Filter Request Handlers--------------------------------------------

		$scope.handleFilters = function (genres, yearMin, yearMax, runtimeMin, runtimeMax, languages) {
			MoviemancerService.handleFilters(genres, yearMin, yearMax, runtimeMin, runtimeMax, languages);
		}

	//--------------------------------------------Rating Handler--------------------------------------------

	$scope.setUserRating = function (rating, movieID) {
		MoviemancerService.setUserRating(rating, movieID, $rootScope.globals.currentUser.user_id, function (response) {
			if (response.status == 200) {
				$scope.getRecommendation();
				console.log('Success: ', response.data)
				$scope.toastMessege("Filme Adicionado a Lista de Vistos")
			} else {
				$scope.toastMessege("Erro ao Classificar Filme")
			}
		});
	}

	//--------------------------------------------Add to watchlist Handler--------------------------------------------
	$scope.addWatchlist = function (movieID) {

		MoviemancerService.addWatchlist(movieID, $rootScope.globals.currentUser.user_id, function (response) {
			if (response.status == 200) {
				console.log('Success: ', response.data)
				$scope.getRecommendation();
				$scope.toastMessege("Filme Adicionado a Quero Ver")
			} else {
				$scope.toastMessege("Erro ao Adicionar a Watchlist")
			}
		});
	}

	//--------------------------------------------Search--------------------------------------------
	$scope.searchMovie = function (query) {
		$location.path('/search/' + query);
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

	//--------------------------------------------Init--------------------------------------------
	$scope.init = function () {

		$scope.getRecommendation();
	},

		$scope.init();

}]);
