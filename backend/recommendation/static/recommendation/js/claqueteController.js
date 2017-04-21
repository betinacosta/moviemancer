var app = angular.module('myApp', ['ngRateIt']).config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

app.controller('mainCtrl', ['$scope', '$http', function ($scope, $http) {

	$scope.init = function () {

			$scope.getRecommendation();
			$scope.loadCommingSoon();
			$scope.model = {
				basic: 0,
				readonly: 2.5,
				readonly_enables: true,
				minMaxStep: 6,
				minMaxStep2: 8.75,
				pristine: 3,
				resetable: 1,
				heightWidth: 1.5,
				callbacks: 5,
				custom: 4,
			};
		},

		$scope.validateModel = function () {
			console.log($scope.movies)
			if ($scope.movies.length == 6) {
				return true;
			} else {
				return false;
			}
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

		$scope.showFilterBar = function () {

			filterBar = document.getElementById('filterBar');
			toggleUp = document.getElementById('toggleUp');
			toggleDown = document.getElementById('toggleDown');

			if (filterBar.style.display == 'block') {
				filterBar.style.display = 'none';
				toggleUp.style.display = 'none';
				toggleDown.style.display = 'inline-block';
			} else {
				filterBar.style.display = 'block';
				toggleUp.style.display = 'inline-block';
				toggleDown.style.display = 'none';
			}

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
				"movie_title":title
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
		setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}

}]);