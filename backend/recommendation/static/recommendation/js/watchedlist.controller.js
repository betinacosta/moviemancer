var app = angular.module('vistoApp', ['ngRateIt']).config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

app.controller('watchedListCtrl', ['$scope', '$http', function ($scope, $http) {

    $scope.getWatchedList = function () {

        $scope.fullList = [];
        $scope.index = [];

        $http.post("getwatchedlist/", {
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
                    //console.log($scope.fullList);

                    $scope.chunk_size = 6;
                        $scope.watchedList = $scope.fullList.map( function(e,i){ 
                            return i%$scope.chunk_size===0 ? $scope.fullList.slice(i,i+$scope.chunk_size) : null; 
                        })
                        .filter(function(e){ return e; });
    
                    //$scope.watchedList = $scope.splitRecommendations($scope.fullList, Math.ceil($scope.fullList.length/6), true);
                    for (i = 0; i < $scope.watchedList.length; i++) {
                        $scope.index.push(i);
                    }
                    //console.log($scope.index);
                    console.log($scope.watchedList[0])
                    console.log($scope.watchedList[1])
                    console.log($scope.watchedList[2])

					//console.log('Success: ', response.data)
					//$scope.toastMessege("Filme Adicionado a Lista de Vistos")
				},
				function (response) {
					console.log('Error: ', response)
				}
			);

    }

    $scope.getWatchedList();

    $scope.splitRecommendations = function (a, n, balanced) {

        if (n < 2)
            return [a];

        var len = a.length,
            out = [],
            i = 0,
            size;

        if (len % n === 0) {
            size = Math.floor(len / n);
            while (i < len) {
                out.push(a.slice(i, i += size));
            }
        }

        else if (balanced) {
            while (i < len) {
                size = Math.ceil((len - i) / n--);
                out.push(a.slice(i, i += size));
            }
        }

        else {

            n--;
            size = Math.floor(len / n);
            if (len % size === 0)
                size--;
            while (i < size * n) {
                out.push(a.slice(i, i += size));
            }
            out.push(a.slice(size * n));

        }

        return out;
    },

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
                    $scope.getWatchedList();
                    console.log('Success: ', response.data)
                    $scope.toastMessege("Nota Atualizada")
                },
                function (response) {
                    console.log('Error: ', response)
                }
                );

                


        }

    $scope.removeFromWatchedlist = function (movieID) {

        $http.post("removefromwatchedlist/", {
            "movie_id": movieID,
            "user_id": 1
        }, {
                'Content-Type': 'application/json; charset=utf-8'
            })
            .then(
            function (response) {
                console.log('Success: ', response.data)
                $scope.getWatchedList();
                $scope.toastMessege("Filme Removido da Lista de Assitidos")
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