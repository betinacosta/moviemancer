var app = angular.module('searchApp', ['ngRateIt', 'rzModule']).config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

app.controller('searchCtrl', ['$scope', '$http', '$routeParams', '$rootScope', '$location', 'MoviemancerService', function ($scope, $http, $routeParams, $rootScope, $location, MoviemancerService) {

    //--------------------------------------------Search Handler--------------------------------------------

	$scope.dataLoading = false;
	$scope.noResults = false;

	$scope.searchMovie = function (query) {
		$location.path('/search/' + query);
	}

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

    $scope.search = function() {
		$scope.dataLoading = true;
        $scope.searchUrl = 'https://api.themoviedb.org/3/search/movie?api_key=5880f597a9fab4f284178ffe0e1f0dba&language=pt-BR&query=' 
                            + $routeParams.query;

		$scope.searchDetails = $http.get($scope.searchUrl);

		$scope.searchDetails.then(
			function (payload) {
                $scope.searchResults = [];
				$scope.index = [];
                $scope.imagePath = 'http://image.tmdb.org/t/p/original/';

				if(payload.data.results.length < 1){
					$scope.noResults = true;
				}

				for (i = 0; i < payload.data.results.length; i++) {
					$scope.searchResults.push({
						title: payload.data.results[i].title,
						poster: $scope.imagePath + payload.data.results[i].poster_path,
						tmdb_id: payload.data.results[i].id,
						rating: $scope.formatRating(payload.data.results[i].vote_average)
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
				$scope.dataLoading = false;
            });
    }

    $scope.search();

	 //--------------------------------------------Rating Handler--------------------------------------------

    $scope.setUserRatingExternal = function (rating, poster, title, id) {
		MoviemancerService.setUserRatingExternal(rating, poster, title, id, $rootScope.globals.currentUser.user_id, function (response) {
            if (response.status == 200) {
				console.log('Success: ', response.data)
				$scope.toastMessege("Filme Adicionado a Lista de Vistos")
            } else {
                $scope.toastMessege("Erro ao Classificar Filme")
            }
        });
	}

    //--------------------------------------------Add to watchlist Handler--------------------------------------------
	$scope.addWatchlistExternal = function (tmdb_id, poster, title) {

		MoviemancerService.addWatchlistExternal(tmdb_id, poster, title, $rootScope.globals.currentUser.user_id, function (response) {
            if (response.status == 200) {
                console.log('Success: ', response.data)
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

}]);