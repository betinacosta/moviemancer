var app = angular.module('moviedetailsApp', ['ngRateIt', 'youtube-embed']).config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

app.controller('moviedetailsCtrl', ['$scope', '$http', '$routeParams', '$rootScope', 'MoviemancerService', '$location', function ($scope, $http, $routeParams, $rootScope, MoviemancerService, $location) {
	$rootScope.prop.menu = false;
	//--------------------------------------------Get Movie Information--------------------------------------------

	$scope.loadMovieDetails = function () {

		$scope.detailsUrl = 'http://api.themoviedb.org/3/movie/' + $routeParams.tmdbID + '?api_key=5880f597a9fab4f284178ffe0e1f0dba&language=pt-BR';

		$scope.requestDetails = $http.get($scope.detailsUrl);

		$scope.requestDetails.then(
			function (payload) {
				$scope.movieDetails = {};
				$scope.movieGenres = [];
				$scope.imagePath = 'http://image.tmdb.org/t/p/original/';

				for (i = 0; i < payload.data.genres.length; i++) {
					$scope.movieGenres.push(payload.data.genres[i].name);
				}

				$scope.movieDetails = {
					title: payload.data.title,
					poster_path: 'http://image.tmdb.org/t/p/original/' + payload.data.poster_path,
					original_title: payload.data.original_title,
					overview: payload.data.overview,
					year: new Date(payload.data.release_date).getFullYear(),
					runtime: payload.data.runtime + 'min',
					genres: $scope.movieGenres.toString(),
					imdb_link: 'http://www.imdb.com/title/' + payload.data.imdb_id,
					imdb_id: payload.data.imdb_id
				}
			});
	};

	$scope.loadMovieVideo = function () {

		$scope.videoUrl = 'http://api.themoviedb.org/3/movie/' + $routeParams.tmdbID + '/videos?api_key=5880f597a9fab4f284178ffe0e1f0dba';
		$scope.requestVideo = $http.get($scope.videoUrl);

		$scope.requestVideo.then(
			function (payload) {
				$scope.movieVideo = {
					video_title: payload.data.results[0].name,
					youtube_id: payload.data.results[0].key,
				}
			});
	};

	$scope.loadCast = function () {

		$scope.castUrl = 'http://api.themoviedb.org/3/movie/' + $routeParams.tmdbID + '/credits?api_key=5880f597a9fab4f284178ffe0e1f0dba';
		$scope.requestCast = $http.get($scope.castUrl);

		$scope.requestCast.then(
			function (payload) {
				$scope.movieCast = [];

				for (i = 0; i < 6; i++) {
					$scope.movieCast.push({
						character: payload.data.cast[i].character,
						actor: payload.data.cast[i].name,
						profile_img: 'http://image.tmdb.org/t/p/original/' + payload.data.cast[i].profile_path
					});
				}
			});
	};

	$scope.loadCrew = function () {

		$scope.crewUrl = 'http://api.themoviedb.org/3/movie/' + $routeParams.tmdbID + '/credits?api_key=5880f597a9fab4f284178ffe0e1f0dba';
		$scope.requestCrew = $http.get($scope.crewUrl);

		$scope.requestCrew.then(
			function (payload) {
				$scope.director = [];
				$scope.writer = [];

				for (i = 0; i < payload.data.crew.length; i++) {

					if (payload.data.crew[i].job == "Director") {
						$scope.director.push(payload.data.crew[i].name);
					}
					if (payload.data.crew[i].job == "Writer" || payload.data.crew[i].job == "Screenplay") {
						$scope.writer.push(payload.data.crew[i].name);
					}
				}

				$scope.movieCrew = {
					director: $scope.director.toString(),
					writer: $scope.writer.toString()
				}

			});
	};

	$scope.loadKeywords = function () {

		$scope.keywordsUrl = 'http://api.themoviedb.org/3/movie/' + $routeParams.tmdbID + '/keywords?api_key=5880f597a9fab4f284178ffe0e1f0dba';
		$scope.requestKeywords = $http.get($scope.keywordsUrl);

		$scope.requestKeywords.then(
			function (payload) {
				$scope.movieKeywords = [];

				for (i = 0; i < 5; i++) {
					$scope.movieKeywords.push(payload.data.keywords[i].name);
				}
			});
	};

	$scope.loadSimilarMovies = function () {

		$scope.similarUrl = 'http://api.themoviedb.org/3/movie/' + $routeParams.tmdbID + '/similar?api_key=5880f597a9fab4f284178ffe0e1f0dba&language=pt-BR';
		$scope.requestSimilar = $http.get($scope.similarUrl);

		$scope.requestSimilar.then(
			function (payload) {
				$scope.similarMovies = [];

				for (i = 0; i < 5; i++) {
					$scope.similarMovies.push({
						title: payload.data.results[i].title,
						poster_path: 'http://image.tmdb.org/t/p/original/' + payload.data.results[i].poster_path,
						tmdb_id: payload.data.results[i].id
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