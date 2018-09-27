var app = angular.module('moviedetailsApp', ['ngRateIt', 'youtube-embed', 'tmdb']).config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

app.controller('moviedetailsCtrl', ['$scope', '$http', '$routeParams', '$rootScope', 'MoviemancerService', '$location', 'tmdbMovie', function ($scope, $http, $routeParams, $rootScope, MoviemancerService, $location, tmdbMovie) {
	$rootScope.prop.menu = false;

	(function () {
		window.tmdb = {
			"api_key": "5880f597a9fab4f284178ffe0e1f0dba",
			"base_uri": "https://api.themoviedb.org/3",
			"images_uri": "https://image.tmdb.org/t/p",
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




	//--------------------------------------------Get Movie Information--------------------------------------------


	$scope.getTMDBData = function (url, done) {
		var xhr = new XMLHttpRequest();
		xhr.open("GET", url, false);
		xhr.onload = function () {
			done(null, xhr.response);
		};
		xhr.onerror = function () {
			done(xhr.response);
		};
		xhr.send();
	}

	$scope.loadMovieDetails = function () {
		$scope.detailsUrl = 'https://api.themoviedb.org/3/movie/' + $routeParams.tmdbID + '?api_key=5880f597a9fab4f284178ffe0e1f0dba&language=pt-BR';

		$scope.getTMDBData($scope.detailsUrl, function (err, response) {
			if (err) { throw err; }
			payload = JSON.parse(response)
			$scope.movieDetails = {};
			$scope.movieGenres = [];
			$scope.imagePath = 'https://image.tmdb.org/t/p/original/';

			for (i = 0; i < payload.genres.length; i++) {
				$scope.movieGenres.push(payload.genres[i].name);
			}

			$scope.movieDetails = {
				title: payload.title,
				poster_path: 'https://image.tmdb.org/t/p/original/' + payload.poster_path,
				original_title: payload.original_title,
				overview: payload.overview,
				year: new Date(payload.release_date).getFullYear(),
				runtime: payload.runtime + 'min',
				genres: $scope.movieGenres.toString(),
				imdb_link: 'https://www.imdb.com/title/' + payload.imdb_id,
				imdb_id: payload.imdb_id,
				rating: $scope.formatRating(payload.vote_average)
			}
		});
	};

	$scope.formatRating = function(r){
		r = parseInt(r);
		if (r < 3) {
			$scope.rating = 1;
		}else if (r < 5) {
			$scope.rating = 2;
		}else if (r < 7) {
			$scope.rating = 3;
		}else if (r < 9) {
			$scope.rating = 4;
		}else {
			$scope.rating = 5;
		}

		return $scope.rating;
	}

	$scope.loadMovieVideo = function () {
		$scope.videoUrl = 'https://api.themoviedb.org/3/movie/' + $routeParams.tmdbID + '/videos?api_key=5880f597a9fab4f284178ffe0e1f0dba';

		$scope.getTMDBData($scope.videoUrl, function (err, response) {
			if (err) { throw err; }
			payload = JSON.parse(response)
			$scope.movieVideo = {
				video_title: payload.results[0].name,
				youtube_id: payload.results[0].key,
			}
		})
	};

	$scope.loadCast = function () {
		$scope.castUrl = 'https://api.themoviedb.org/3/movie/' + $routeParams.tmdbID + '/credits?api_key=5880f597a9fab4f284178ffe0e1f0dba';

		$scope.getTMDBData($scope.castUrl, function (err, response) {
			if (err) { throw err; }
			payload = JSON.parse(response)
			$scope.movieCast = [];

			for (i = 0; i < 6; i++) {
				$scope.movieCast.push({
					character: payload.cast[i].character,
					actor: payload.cast[i].name,
					profile_img: 'https://image.tmdb.org/t/p/original/' + payload.cast[i].profile_path
				});
			}
		});
	};

	$scope.loadCrew = function () {
		$scope.crewUrl = 'https://api.themoviedb.org/3/movie/' + $routeParams.tmdbID + '/credits?api_key=5880f597a9fab4f284178ffe0e1f0dba';
		$scope.getTMDBData($scope.crewUrl, function (err, response) {
			if (err) { throw err; }
			payload = JSON.parse(response)
			$scope.director = [];
			$scope.writer = [];

			for (i = 0; i < payload.crew.length; i++) {

				if (payload.crew[i].job == "Director") {
					$scope.director.push(payload.crew[i].name);
				}
				if (payload.crew[i].job == "Writer" || payload.crew[i].job == "Screenplay") {
					$scope.writer.push(payload.crew[i].name);
				}
			}

			$scope.movieCrew = {
				director: $scope.director.toString(),
				writer: $scope.writer.toString()
			}
		});
	};

	$scope.loadKeywords = function () {
		$scope.keywordsUrl = 'https://api.themoviedb.org/3/movie/' + $routeParams.tmdbID + '/keywords?api_key=5880f597a9fab4f284178ffe0e1f0dba';
		
		$scope.getTMDBData($scope.keywordsUrl, function (err, response) {
			if (err) { throw err; }
			payload = JSON.parse(response)
			$scope.movieKeywords = [];

			for (i = 0; i < 5; i++) {
				$scope.movieKeywords.push(payload.keywords[i].name);
			}
		});
	};

	$scope.loadSimilarMovies = function () {
		$scope.similarUrl = 'https://api.themoviedb.org/3/movie/' + $routeParams.tmdbID + '/similar?api_key=5880f597a9fab4f284178ffe0e1f0dba&language=pt-BR';
		
		$scope.getTMDBData($scope.similarUrl, function (err, response) {
			if (err) { throw err; }
			payload = JSON.parse(response)
				$scope.similarMovies = [];

				for (i = 0; i < 5; i++) {
					$scope.similarMovies.push({
						title: payload.results[i].title,
						poster_path: 'https://image.tmdb.org/t/p/original/' + payload.results[i].poster_path,
						tmdb_id: payload.results[i].id
					});
				}
			});
	};

	//--------------------------------------------Rating Handler--------------------------------------------

	$scope.setUserRatingExternal = function (rating, poster, title, id) {
		MoviemancerService.setUserRatingExternal(rating, poster, title, $routeParams.tmdbID, $rootScope.globals.currentUser.user_id, function (response) {
			if (response.status == 200) {
				console.log('Success: ', response.data)
				$scope.toastMessege("Filme Adicionado a Lista de Vistos")
			} else {
				$scope.toastMessege("Erro ao Classificar Filme")
			}
		});
	}

	//--------------------------------------------Add to watchlist Handler--------------------------------------------

	$scope.addWatchlistExternal = function (poster, title) {

		MoviemancerService.addWatchlistExternal($routeParams.tmdbID, poster, title, $rootScope.globals.currentUser.user_id, function (response) {
			if (response.status == 200) {
				console.log('Success: ', response.data)
				$scope.toastMessege("Filme Adicionado a Quero Ver")
			} else {
				$scope.toastMessege("Erro ao Adicionar a Watchlist")
			}
		});
	}

	//--------------------------------------------Toast Message Handler--------------------------------------------

	$scope.toastMessege = function (msg) {
		$scope.toastMessage = msg;
		// Get the snackbar DIV
		var x = document.getElementById("snackbar")

		// Add the "show" class to DIV
		x.className = "show";

		// After 3 seconds, remove the show class from DIV
		setTimeout(function () {
			x.className = x.className.replace("show", "");
		}, 3000);
	}

	//--------------------------------------------Comments---------------------------------------------------------
	$scope.allComments = false;

	$scope.showAllComments = function () {
		$scope.loadComments();
		$scope.allComments = true;
	}

	$scope.hideAllComments = function () {
		$scope.allComments = false;
	}

	$scope.loadComments = function () {
		$http.post("getcomments/", {
			"tmdb_movie_id": $routeParams.tmdbID
		}, {
				'Content-Type': 'application/json; charset=utf-8'
			})
			.then(
			function (response) {
				$scope.comments = []
				for (i = response.data.length - 1; i > -1; i--) {
					if (response.data[i].user_name == $rootScope.globals.currentUser.name) {
						$scope.isUserComment = true;
					} else {
						$scope.isUserComment = false;
					}

					$scope.comments.push({
						"user_name": response.data[i].user_name,
						"rate": response.data[i].rate,
						"comment": response.data[i].comment,
						"comment_id": response.data[i].comment_id,
						"isUserComment": $scope.isUserComment,
						"color": $scope.color
					});
				}
			},
			function (response) {
				console.log('Error: ', response)
			});
	}

	$scope.deleteComment = function (commentID) {

		$http.post("deletecomment/", {
			"comment_id": commentID
		}, {
				'Content-Type': 'application/json; charset=utf-8'
			})
			.then(
			function (response) {
				$scope.loadComments();
				$scope.toastMessege('Comentário Deletado');
			},
			function (response) {
				$scope.toastMessege('Erro ao Deletar Comentário');
			});

	}

	$scope.clearField = function (fieldID) {
		$scope.nameID = document.getElementById(fieldID);
		$scope.nameID.style.borderColor = '#7d7b7b';
	}

	$scope.invalidateField = function (fieldID) {
		$scope.nameID = document.getElementById(fieldID);
		$scope.nameID.style.borderColor = 'red';
	}

	$scope.createComment = function () {
		$http.post("addcomment/", {
			"tmdb_movie_id": $routeParams.tmdbID,
			"user_id": $rootScope.globals.currentUser.user_id,
			"comment": $scope.userComment
		}, {
				'Content-Type': 'application/json; charset=utf-8'
			})
			.then(
			function (response) {
				console.log('Success: ', response.data)
				$scope.loadComments();
				$scope.toastMessege('Obrigada pelo Comentário')
			},
			function (response) {
				console.log('Error: ', response)
			});
	}

	$scope.validateComment = function () {
		if ($scope.userComment == '' || $scope.userComment == ' ' || $scope.userComment == undefined) {
			$scope.invalidateField('userComment');
		} else {
			$scope.createComment();
		}
	}

	//--------------------------------------------Search--------------------------------------------
	$scope.searchMovie = function (query) {
		$location.path('/search/' + query);
	}

	//--------------------------------------------Init--------------------------------------------
	$scope.init = function () {
		$scope.loadMovieDetails();
		$scope.loadMovieVideo();
		$scope.loadCast();
		$scope.loadCrew();
		$scope.loadKeywords();
		$scope.loadSimilarMovies();
	}

	$scope.init();
}]);