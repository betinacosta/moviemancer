var app = angular.module('mainApp', ['ngRateIt', 'rzModule']).config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

app.controller('mainCtrl', ['$scope', '$http', '$window', '$rootScope', '$location', 'MoviemancerService', function ($scope, $http, $window, $rootScope, $location, MoviemancerService) {
	$rootScope.prop.sanduba = true;
	$rootScope.prop.menu = false;

	$scope.footerID = document.getElementById('footer');
    $scope.bodyID = document.getElementById('body');
    $scope.footerID.style.position = 'relative';
    $scope.footerID.style.bottom = '0';
    $scope.footerID.style.width = '100%';
    $scope.bodyID.style.backgroundColor = 'white';

	//--------------------------------------------Get Recommendation Handler--------------------------------------------

	$scope.getRecommendation = function () {
		$http.post("getrecommendation/", {
			"user_id": $rootScope.globals.currentUser.user_id
		}, {
				'Content-Type': 'application/json; charset=utf-8'
			})
			.then(
			function (response) {
				$scope.recommendation = [];
				$scope.rating = [];
				$scope.fullRecommendation = [];

				for (i = 0; i < 6; i++) {
					$scope.recommendation.push({
						title: response.data[i].tmdb_title,
						poster: response.data[i].tmdb_poster,
						movie_id: response.data[i].movie_id,
						tmdb_id: response.data[i].tmdb_movie_id,
						rating: 0
					});
				}
			},
			function (response) {
				console.log('Error: ', response)
			});


		}

	//--------------------------------------------Get Comming Soon Handler--------------------------------------------
	$scope.formatDate = function (date) {
			$scope.day = date.getDate()
			$scope.month = date.getMonth() + 1;
			$scope.year = date.getFullYear();

			if ($scope.day < 10) {
				$scope.day = '0' + $scope.day
			}
			if ($scope.month < 10) {
				$scope.month = '0' + $scope.month
			}

			return $scope.year + '-' + $scope.month + '-' + $scope.day;
		},

		$scope.getEndDate = function (initialDate, days) {

			initialDate.setDate(initialDate.getDate() + days);
			return initialDate;
		},

		$scope.loadCommingSoon = function () {
			$scope.today = $scope.formatDate(new Date());
			$scope.endDate = $scope.getEndDate(new Date(), 7);
			$scope.endDate = $scope.formatDate($scope.endDate);

			$scope.baseUrl = 	'https://api.themoviedb.org/3/discover/movie?api_key=5880f597a9fab4f284178ffe0e1f0dba' + 
								'&language=pt-BR&region=BR&release_date.gte=' + $scope.today + '&release_date.lte=' + 
								$scope.endDate;

			$scope.commingSoon = [];
			$scope.imagePath = 'http://image.tmdb.org/t/p/original/';

			$scope.commingSoonRequets = $http.get($scope.baseUrl);

			$scope.commingSoonRequets.then(
            function (payload) {
                for (i = 0; i < 6; i++) {
						$scope.commingSoon.push({
							img: $scope.imagePath + payload.data.results[i].poster_path,
							title: payload.data.results[i].title,
							tmdb_id: payload.data.results[i].id
						})
					}
			});
		},
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
		MoviemancerService.handleFilters (genres, yearMin, yearMax, runtimeMin, runtimeMax, languages);
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

	$scope.addWatchlistExternal = function (tmdb_id, poster, title) {

		MoviemancerService.addWatchlistExternal(tmdb_id, poster, title, $rootScope.globals.currentUser.user_id, function (response) {
            if (response.status == 200) {
                console.log('Success: ', response.data)
				$scope.getRecommendation();
				$scope.toastMessege("Filme Adicionado a Quero Ver")
            } else {
                $scope.toastMessege("Erro ao Adicionar a Watchlist")
            }
        });
	}
	//--------------------------------------------Search Handler--------------------------------------------

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
		$scope.loadCommingSoon();
	},

	$scope.init();
}]);