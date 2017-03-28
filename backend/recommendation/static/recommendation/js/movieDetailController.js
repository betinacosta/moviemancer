var app = angular.module('myApp3', ['ngRateIt', 'youtube-embed']).config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    });

app.controller('movieCtrl', ['$scope', '$http', '$routeParams', function ($scope, $http, $routeParams) {

     
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

    $scope.loadMovieDetails = function () {
			oParams = {
				"language": "pt-BR"
			};

			$scope.movieDetails = {};
            $scope.movieGenres = [];
			$scope.imagePath = 'https://image.tmdb.org/t/p/original/';

			tmdb.call("/movie/" + $routeParams.tmdbID, oParams,
				function (details, movieDetails, imagePath, movieGenres) {
					
                    for (i = 0; i < details.genres.length; i++) {
                        $scope.movieGenres.push(details.genres[i].name);
                    }

					$scope.hours = Math.floor( details.runtime / 60);
					$scope.minutes = details.runtime % 60;
					$scope.runtime = $scope.hours.toString() + 'h' + $scope.minutes.toString() + 'min';

                    $scope.movieDetails = {
                            title: details.title,
                            poster_path: 'https://image.tmdb.org/t/p/original/' + details.poster_path,
                            original_title: details.original_title,
                            overview: details.overview,
                            year: new Date(details.release_date).getFullYear(),
                            runtime: $scope.runtime,
                            genres: $scope.movieGenres.toString(),
                            imdb_link: 'http://www.imdb.com/title/' + details.imdb_id,
                            imdb_id: details.imdb_id
						}

				},
				function (e) {
					console.log("Error: " + e)
				}
			);
            console.log($scope.movieDetails)
		};

    $scope.loadMovieVideo = function () {
			
			$scope.movieVideo = {};
            oParams = {};

			tmdb.call("/movie/" + $routeParams.tmdbID + '/videos', oParams,
				function (video, movieVideo) {
					$scope.movieVideo = {
                            video_title: video.results[0].name,
                            youtube_id: video.results[0].key,
                    }
				},
				function (e) {
					console.log("Error: " + e)
				}
			);
		};

    $scope.loadCast = function () {
			
			$scope.movieCast = [];
            oParams = {};

			tmdb.call("/movie/" + $routeParams.tmdbID + '/credits', oParams,
				function (casting, movieCast) {

                    for(i=0; i < 6; i++) {
                        $scope.movieCast.push({
                            character: casting.cast[i].character,
                            actor: casting.cast[i].name,
                            profile_img: 'https://image.tmdb.org/t/p/original/' + casting.cast[i].profile_path
                        });
                    }
				},
				function (e) {
					console.log("Error: " + e)
				}
			);
		};

    $scope.loadCrew = function () {
			
			$scope.movieCrew = {};
            oParams = {};
            $scope.director = [];
            $scope.writer = [];

			tmdb.call("/movie/" + $routeParams.tmdbID + '/credits', oParams,
				function (crew, movieCrew, director, writer) {
                    

                    for(i=0; i < crew.crew.length; i++) {

                        if (crew.crew[i].job == "Director") {
                            $scope.director.push(crew.crew[i].name);
                        }
                        if (crew.crew[i].job == "Writer" || crew.crew[i].job == "Screenplay") {
                            $scope.writer.push(crew.crew[i].name);
                        }
                    }

                    $scope.movieCrew = {
                        director: $scope.director.toString(),
                        writer: $scope.writer.toString()
                    }
                    console.log($scope.movieCrew);
				},
				function (e) {
					console.log("Error: " + e)
				}
			);
		};

    $scope.loadKeywords = function () {
			
			$scope.movieKeywords = [];
            oParams = {};

			tmdb.call("/movie/" + $routeParams.tmdbID + '/keywords', oParams,
				function (keywords, movieKeywords) {

                    for(i=0; i < 5; i++) {
                        $scope.movieKeywords.push(keywords.keywords[i].name);
                    }
				},
				function (e) {
					console.log("Error: " + e)
				}
			);
		};

     $scope.loadSimilarMovies = function () {
			
			$scope.similarMovies = [];
            oParams = {
				"language": "pt-BR"
			};

			tmdb.call("/movie/" + $routeParams.tmdbID + '/similar', oParams,
				function (similar, similarMovies) {

                    for(i=0; i < 5; i++) {
                        $scope.similarMovies.push({
                            title: similar.results[i].title,
                            poster_path: 'https://image.tmdb.org/t/p/original/' + similar.results[i].poster_path,
                            tmdb_id: similar.results[i].id
                        });
                    }
				},
				function (e) {
					console.log("Error: " + e)
				}
			);
		};

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

app.filter('trusted', ['$sce', function ($sce) {
    return function(url) {
        return $sce.trustAsResourceUrl(url);
    };
}]);