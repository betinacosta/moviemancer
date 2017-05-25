var app = angular.module('searchApp', ['ngRateIt', 'rzModule']).config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

app.controller('searchCtrl', ['$scope', '$http', '$routeParams', '$rootScope', function ($scope, $http, $routeParams, $rootScope) {

    //--------------------------------------------Search Handler--------------------------------------------

	$scope.searchMovie = function (query) {
		$location.path('/search/' + query);
	}

    $scope.search = function() {
        $scope.searchUrl = 'https://api.themoviedb.org/3/search/movie?api_key=5880f597a9fab4f284178ffe0e1f0dba&language=pt-BR&query=' 
                            + $routeParams.query;

		$scope.searchDetails = $http.get($scope.searchUrl);

		$scope.searchDetails.then(
			function (payload) {
                $scope.searchResults = [];
				$scope.index = [];
                $scope.imagePath = 'https://image.tmdb.org/t/p/original/';

				for (i = 0; i < payload.data.results.length; i++) {
					$scope.searchResults.push({
						title: payload.data.results[i].title,
						poster: $scope.imagePath + payload.data.results[i].poster_path,
						tmdb_id: payload.data.results[i].id
					});
				}

				$scope.chunk_size = 6;
				$scope.fullList = $scope.searchResults.map(function (e, i) {
					return i % $scope.chunk_size === 0 ? $scope.searchResults.slice(i, i + $scope.chunk_size) : null;
				})
					.filter(function (e) { return e; });

				for (i = 0; i < $scope.fullList.length; i++) {
					$scope.index.push(i);
				}
            });
    }

    $scope.search();

    //--------------------------------------------Add to watchlist Handler--------------------------------------------
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

}]);