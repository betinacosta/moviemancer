var app = angular.module('queroVerApp', ['ngRateIt']).config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

app.controller('watchlistCtrl', ['$scope', '$http', '$rootScope', '$location', 'MoviemancerService', function ($scope, $http, $rootScope, $location, MoviemancerService) {
    $rootScope.prop.menu = false;
    $scope.dataLoading = false;
	$scope.noResults = false;
    //--------------------------------------------Get Watchlist Handler--------------------------------------------

    $scope.getWatchlist = function () {
        $scope.dataLoading = true;

        $scope.fullList = [];
        $scope.index = [];

        $http.post("getwatchlist/", {
            "user_id": $rootScope.globals.currentUser.user_id
        }, {
                'Content-Type': 'application/json; charset=utf-8'
            })
            .then(
            function (response) {

                if(response.data.length < 1) {
                    $scope.noResults = true;
                }

                for (i = 0; i < response.data.length; i++) {
                    $scope.fullList.push({
                        title: response.data[i].title,
                        poster: response.data[i].poster,
                        movie_id: response.data[i].movie_id,
                        tmdb_id: response.data[i].tmdb_movie_id,
                        rating: response.data[i].tmdb_rating
                    });
                }

                $scope.chunk_size = 6;
                $scope.watchlist = $scope.fullList.map(function (e, i) {
                    return i % $scope.chunk_size === 0 ? $scope.fullList.slice(i, i + $scope.chunk_size) : null;
                })
                    .filter(function (e) {
                        return e;
                    });

                for (i = 0; i < $scope.watchlist.length; i++) {
                    $scope.index.push(i);
                }
                $scope.dataLoading = false;
            },
            function (response) {
                console.log('Error: ', response)
            }
            );

    }

    //--------------------------------------------Remove from List Handler--------------------------------------------

    $scope.removeFromWatchlist = function (movieID) {

        $http.post("removefromwatchlist/", {
            "movie_id": movieID,
            "user_id": $rootScope.globals.currentUser.user_id
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

    //--------------------------------------------Rating Handler--------------------------------------------

    $scope.setUserRating = function (rating, movieID) {
        MoviemancerService.setUserRating(rating, movieID, $rootScope.globals.currentUser.user_id, function (response) {
            if (response.status == 200) {
                $scope.getWatchlist();
                console.log('Success: ', response.data)
                $scope.toastMessege("Filme Adicionado a Lista de Vistos")

            } else {
                $scope.toastMessege("Erro ao Classificar Filme")
            }
        });
    }

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

    $scope.genresSelector = MoviemancerService.getGenres();
    $scope.languages = MoviemancerService.getLanguages();

    $scope.selectPT = function () {
        $scope.languages = MoviemancerService.selectPT($scope.languages);
    }

    $scope.selectEN = function () {
        $scope.languages = MoviemancerService.selectEN($scope.languages);
    }

    $scope.selectDE = function () {
        $scope.languages = MoviemancerService.selectDE($scope.languages);
    }

    $scope.selectIT = function () {
        $scope.languages = MoviemancerService.selectIT($scope.languages);
    }

    $scope.selectJA = function () {
        $scope.languages = MoviemancerService.selectJA($scope.languages);
    }

    $scope.selectFR = function () {
        $scope.languages = MoviemancerService.selectFR($scope.languages);
    }

    $scope.selectGenre = function (id, index) {
        $scope.genresSelector = MoviemancerService.selectGenre(id, index, $scope.genresSelector);
    }

    $scope.showFilterBar = function () {
        $scope.filterVisible = !$scope.filterVisible;
        $scope.toggle = !$scope.toggle;
    },
        //--------------------------------------------Filter Request Handlers--------------------------------------------

        $scope.handleFilters = function (genres, yearMin, yearMax, runtimeMin, runtimeMax, languages, discover, recommendation) {
            MoviemancerService.handleFilters(genres, yearMin, yearMax, runtimeMin, runtimeMax, languages, discover, recommendation);
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
        setTimeout(function () {
            x.className = x.className.replace("show", "");
        }, 3000);
    }

    //--------------------------------------------Init--------------------------------------------
    $scope.init = function () {

        $scope.getWatchlist();
    },

        $scope.init();
}]);