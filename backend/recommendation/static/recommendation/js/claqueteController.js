var app = angular.module('myApp', ['ngRateIt', 'rzModule']).config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

app.controller('mainCtrl', ['$scope', '$http', '$window', '$rootScope', function ($scope, $http, $window, $rootScope) {
	$rootScope.prop.sanduba = true;
	$rootScope.prop.menu = false;
	$scope.userName = $rootScope.globals.currentUser.name;

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
			$scope.imagePath = 'https://image.tmdb.org/t/p/original/';

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

	$scope.getGenres = function() {
		return([
		{
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
		},
	])
	}

	$scope.getLanguages = function() {
		return([
		{
			code: 'pt',
			name: 'Português',
			selected: false
		},
		{
			code: 'en',
			name: 'Inglês',
			selected: false
		},
		{
			code: 'de',
			name: 'Alemão',
			selected: false
		},
		{
			code: 'it',
			name: 'Italiano',
			selected: false
		},
		{
			code: 'ja',
			name: 'Japonês',
			selected: false
		},
		{
			code: 'fr',
			name: 'Francês',
			selected: false
		}
	])
	}

	$scope.genresSelector = $scope.getGenres();
	$scope.languages = $scope.getLanguages();

	$scope.uncheckLanguage = function (index, id) {
		$scope.languages[index].selected = false;
		$scope.btn = document.getElementById(id);
		$scope.btn.style.backgroundColor = '#7d7b7b';
	}

	$scope.checkLanguage = function (index, id) {
		$scope.languages[index].selected = !$scope.languages[index].selected;
		if ($scope.languages[index].selected) {
			$scope.btn = document.getElementById(id);
			$scope.btn.style.backgroundColor = '#9a2726';
		} else {
			$scope.btn = document.getElementById(id);
			$scope.btn.style.backgroundColor = '#7d7b7b';
		}
	}

	$scope.selectPT = function () {
		//Selected
		$scope.checkLanguage(0, 'pt')
		//Outros
		$scope.uncheckLanguage(1, 'en');
		$scope.uncheckLanguage(2, 'de');
		$scope.uncheckLanguage(3, 'it');
		$scope.uncheckLanguage(4, 'ja');
		$scope.uncheckLanguage(5, 'fr');
	}

	$scope.selectEN = function () {
		//Selected
		$scope.checkLanguage(1, 'en')
		//Outros
		$scope.uncheckLanguage(0, 'pt');
		$scope.uncheckLanguage(2, 'de');
		$scope.uncheckLanguage(3, 'it');
		$scope.uncheckLanguage(4, 'ja');
		$scope.uncheckLanguage(5, 'fr');
	}

	$scope.selectDE = function () {
		//Selected
		$scope.checkLanguage(2, 'de')
		//Outros
		$scope.uncheckLanguage(1, 'en');
		$scope.uncheckLanguage(0, 'pt');
		$scope.uncheckLanguage(3, 'it');
		$scope.uncheckLanguage(4, 'ja');
		$scope.uncheckLanguage(5, 'fr');
	}

	$scope.selectIT = function () {
		//Selected
		$scope.checkLanguage(3, 'it')
		//Outros
		$scope.uncheckLanguage(1, 'en');
		$scope.uncheckLanguage(2, 'de');
		$scope.uncheckLanguage(0, 'pt');
		$scope.uncheckLanguage(4, 'ja');
		$scope.uncheckLanguage(5, 'fr');
	}

	$scope.selectJA = function () {
		//Selected
		$scope.checkLanguage(4, 'ja')
		//Outros
		$scope.uncheckLanguage(1, 'en');
		$scope.uncheckLanguage(2, 'de');
		$scope.uncheckLanguage(3, 'it');
		$scope.uncheckLanguage(0, 'pt');
		$scope.uncheckLanguage(5, 'fr');
	}

	$scope.selectFR = function () {
		//Selected
		$scope.checkLanguage(5, 'fr')
		//Outros
		$scope.uncheckLanguage(1, 'en');
		$scope.uncheckLanguage(2, 'de');
		$scope.uncheckLanguage(3, 'it');
		$scope.uncheckLanguage(4, 'ja');
		$scope.uncheckLanguage(0, 'pt');
	}

	$scope.selectGenre = function (id, index) {
		$scope.genresSelector[index].selected = !$scope.genresSelector[index].selected;
		$scope.btn = document.getElementById(id);

		if ($scope.genresSelector[index].selected) {
			$scope.btn.style.backgroundColor = '#9a2726';
			$scope.btn.style.color = '#fff';
		} else {
			$scope.btn.style.backgroundColor = '#7d7b7b';
			$scope.btn.style.color = '#fff';
		}

	}

	$scope.refreshSlider = function () {
		$timeout(function () {
			$scope.$broadcast('rzSliderForceRender');
		});
	};

	$scope.showFilterBar = function () {

		$scope.filterVisible = !$scope.filterVisible;
		$scope.toggle = !$scope.toggle;
		if ($scope.filterVisible)
			$scope.refreshSlider();

	},
	//--------------------------------------------Filter Request Handlers--------------------------------------------

	$scope.handleFilters = function (genres, yearMin, yearMax, runtimeMin, runtimeMax, languages) {
		$scope.selectedGenres = [];
		$scope.selectedLanguage = 'null';
		$scope.aux = 0;

		for (i = 0; i < genres.length; i++) {
			if (genres[i].selected) {
				$scope.selectedGenres.push(genres[i].id);
			}
		}

		if($scope.selectedGenres == '') {
			$scope.selectedGenres = 'null';
		}else {
			$scope.selectedGenres = $scope.selectedGenres.join(",");
		}

		for (i = 0; i < languages.length; i++) {
			if (languages[i].selected) {
				$scope.selectedLanguage = languages[i].code;
			}
		}

		$scope.selectedMinYear = yearMin + '-' + '01' + '-' + '01';
		$scope.selectedMaxYear = yearMax + '-' + '12' + '-' + '31'

		$window.location.href = '#/filtersview/' + $scope.selectedGenres + '/' + $scope.selectedLanguage + '/' + $scope.selectedMinYear + '/' + $scope.selectedMaxYear + '/' + runtimeMin + '/' + runtimeMax;
	}

	//--------------------------------------------Rating Handler--------------------------------------------

	$scope.setUserRating = function (rating, movieID) {

		$http.post("ratemovie/", {
			"movie_id": movieID,
			"rate_id": rating,
			"user_id": $rootScope.globals.currentUser.user_id
		}, {
				'Content-Type': 'application/json; charset=utf-8'
			})
			.then(
			function (response) {
				$scope.getRecommendation();
				console.log('Success: ', response.data)
				$scope.toastMessege("Filme Adicionado a Lista de Vistos")
			},
			function (response) {
				console.log('Error: ', response)
			}
			);
	}

	//--------------------------------------------Add to watchlist Handler--------------------------------------------
	$scope.addWatchlist = function (movieID) {

		$http.post("addwatchlist/", {
			"movie_id": movieID,
			"user_id": $rootScope.globals.currentUser.user_id
		}, {
				'Content-Type': 'application/json; charset=utf-8'
			})
			.then(
			function (response) {
				console.log('Success: ', response.data)
				$scope.getRecommendation();
				$scope.toastMessege("Filme Adicionado a Quero Ver")
			},
			function (response) {
				console.log('Error: ', response)
			}
			);
	}

	$scope.addWatchlistExternal = function (tmdb_id, poster, title) {

		$http.post("addwatchlistexternal/", {
			"tmdb_movie_id": tmdb_id,
			"user_id": $rootScope.globals.currentUser.user_id,
			"movie_poster": poster,
			"movie_title": title
		}, {
				'Content-Type': 'application/json; charset=utf-8'
			})
			.then(
			function (response) {
				console.log('Success: ', response.data)
				$scope.toastMessege("Filme Adicionado a Quero Ver")
			},
			function (response) {
				console.log('Error: ', response)
			}
			);
	}
	//--------------------------------------------Search Handler--------------------------------------------

	$scope.searchMovie = function (query) {
		oParams = {
			"query": query,
			"language": "pt-br"
		};

		tmdb.call("/search/movie", oParams,
			function (searchResult) {
				console.log(searchResult)
			},
			function (e) {
				console.log("Error: " + e)
			}
		);

	},

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