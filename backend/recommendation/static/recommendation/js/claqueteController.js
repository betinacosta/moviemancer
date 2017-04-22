var app = angular.module('myApp', ['ngRateIt', 'rzModule']).config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

app.controller('mainCtrl', ['$scope', '$http', '$window', function ($scope, $http, $window) {

	$scope.init = function () {

		$scope.getRecommendation();
		$scope.loadCommingSoon();
	},

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

	$scope.genresSelector = [
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
	];

	$scope.languages = [
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
	]

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

	$scope.handleFilters = function (genres, yearMin, yearMax, runtimeMin, runtimeMax, languages) {
		$scope.selectedGenres = [];
		$scope.selectedLanguage = '';
		$scope.aux = 0;

		for (i = 0; i < genres.length; i++) {
			if (genres[i].selected) {
				$scope.selectedGenres.push(genres[i].id);
			}
		}

		$scope.selectedGenres = $scope.selectedGenres.join(",");

		for (i = 0; i < languages.length; i++) {
			if (languages[i].selected) {
				$scope.selectedLanguage = languages[i].code;
			}
		}

		$scope.selectedMinYear = yearMin + '-' + '01' + '-' + '01';
		$scope.selectedMaxYear = yearMax + '-' + '12' + '-' + '31'

		$window.location.href = '#/filtersview/' + $scope.selectedGenres + '/' + $scope.selectedLanguage + '/' + $scope.selectedMinYear + '/' + $scope.selectedMaxYear + '/' + runtimeMin + '/' + runtimeMax;
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

		//tmdb wrapper
		(function () {
			window.tmdb = {
				"api_key": "5880f597a9fab4f284178ffe0e1f0dba",
				"base_uri": "http://api.themoviedb.org/3",
				"images_uri": "http://image.tmdb.org/t/p",
				"timeout": 5000,
				call: function (url, params, success, error) {
					var params_str = "api_key=" + tmdb.api_key;
					for (var key in params) {
						if (params.hasOwnProperty(key)) {
							params_str += "&" + key + "=" + encodeURIComponent(params[key]);
						}
					}
					var xhr = new XMLHttpRequest();
					xhr.timeout = tmdb.timeout;
					xhr.ontimeout = function () {
						throw ("Request timed out: " + url + " " + params_str);
					};
					xhr.open("GET", tmdb.base_uri + url + "?" + params_str, true);
					xhr.setRequestHeader('Accept', 'application/json');
					xhr.responseType = "text";
					xhr.onreadystatechange = function () {
						if (this.readyState === 4) {
							if (this.status === 200) {
								if (typeof success == "function") {
									success(JSON.parse(this.response));
								} else {
									throw ('No success callback, but the request gave results')
								}
							} else {
								if (typeof error == "function") {
									error(JSON.parse(this.response));
								} else {
									throw ('No error callback')
								}
							}
						}
					};
					xhr.send();
				}
			}
		})()
	//tmdb wrapper

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
			$scope.endDate = $scope.getEndDate(new Date(), 15);
			$scope.endDate = $scope.formatDate($scope.endDate);
			oParams = {
				"primary_release_date.gte": $scope.today,
				"primary_release_date.lte": $scope.endDate,
				"language": "pt-BR"
			};

			$scope.commingSoon = [];
			$scope.imagePath = 'https://image.tmdb.org/t/p/original/';

			tmdb.call("/discover/movie", oParams,
				function (soon, commingSoon, imagePath) {
					for (i = 0; i < 6; i++) {
						$scope.commingSoon.push({
							img: $scope.imagePath + soon.results[i].poster_path,
							title: soon.results[i].title,
							tmdb_id: soon.results[i].id
						})
					}
				},
				function (e) {
					console.log("Error: " + e)
				}
			);
		},

		$scope.getRecommendation = function (movies) {
			$scope.recommendation = [];
			$scope.rating = [];
			$scope.fullRecommendation = [];

			$http.get('reco').success(function (data) {

				for (i = 0; i < 6; i++) {
					$scope.recommendation.push({
						title: data[i].tmdb_title,
						poster: data[i].tmdb_poster,
						movie_id: data[i].movie_id,
						tmdb_id: data[i].tmdb_movie_id,
						rating: 0
					});
				}

				for (i = 0; i < data.length; i++) {
					$scope.fullRecommendation.push({
						title: data[i].tmdb_title,
						poster: data[i].tmdb_poster,
						movie_id: data[i].movie_id,
						tmdb_id: data[i].tmdb_movie_id,
						rating: 0
					});
				}
			});
		},

		// Call init function
		$scope.init();

	$scope.setUserRating = function (rating, movieID) {

		$http.post("ratemovie/", {
			"movie_id": movieID,
			"rate_id": rating,
			"user_id": 1
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

	$scope.addWatchlist = function (movieID) {

		$http.post("addwatchlist/", {
			"movie_id": movieID,
			"user_id": 1
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
			"user_id": 1,
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