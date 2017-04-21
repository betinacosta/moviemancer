var app = angular.module('queroVerApp', ['ngRateIt']).config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

app.controller('watchlistCtrl', ['$scope', '$http', function ($scope, $http) {

    $scope.getWatchlist = function () {

        $scope.fullList = [];
        $scope.index = [];

        $http.post("getwatchlist/", {
				"user_id": 1
			}, {
				'Content-Type': 'application/json; charset=utf-8'
			})
			.then(
				function (response) {
                    for (i = 0; i < response.data.length; i++) {
                        $scope.fullList.push ({ title: response.data[i].title, 
                                                poster: response.data[i].poster, 
                                                movie_id: response.data[i].movie_id, 
                                                tmdb_id: response.data[i].tmdb_movie_id,
                                                rating: response.data[i].rating});
                        }

                        $scope.chunk_size = 6;
                        $scope.watchlist = $scope.fullList.map( function(e,i){ 
                            return i%$scope.chunk_size===0 ? $scope.fullList.slice(i,i+$scope.chunk_size) : null; 
                        })
                        .filter(function(e){ return e; });
    
                    for (i = 0; i < $scope.watchlist.length; i++) {
                        $scope.index.push(i);
                    }
				},
				function (response) {
					console.log('Error: ', response)
				}
			);

    }

    $scope.getWatchlist();

        $scope.showFilterBar = function () {

            filterBar = document.getElementById('filterBar');
            toggleUp = document.getElementById('toggleUp');
            toggleDown = document.getElementById('toggleDown');

            if (filterBar.style.display == 'block') {
                filterBar.style.display = 'none';
                toggleUp.style.display = 'none';
                toggleDown.style.display = 'inline-block';
            }
            else {
                filterBar.style.display = 'block';
                toggleUp.style.display = 'inline-block';
                toggleDown.style.display = 'none';
            }

        },

        $scope.setUserRating = function (rating, movieID, watchedlist) {

            $http.post("ratemovie/", {
                "movie_id": movieID,
                "rate_id": rating,
                "user_id": 1
            }, {
                    'Content-Type': 'application/json; charset=utf-8'
                })
                .then(
                function (response) {
                    console.log('Success: ', response.data)
                    $scope.toastMessege("Filme Adicionado a Lista de Vistos")
                },
                function (response) {
                    console.log('Error: ', response)
                }
                );

        }

    $scope.removeFromWatchlist = function (movieID) {

        $http.post("removefromwatchlist/", {
            "movie_id": movieID,
            "user_id": 1
        }, {
                'Content-Type': 'application/json; charset=utf-8'
            })
            .then(
            function (response) {
                console.log('Success: ', response.data)
                $scope.getWatchlist();
                $scope.toastMessege("Filme Removido da Lista de Quero Ver")
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