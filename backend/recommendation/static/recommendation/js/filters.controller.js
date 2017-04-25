var app = angular.module('filtersApp', ['ngRateIt', 'rzModule']).config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

app.controller('filtersCtrl', ['$scope', '$http', '$routeParams', '$window', '$rootScope',function ($scope, $http, $routeParams, $window, $rootScope) {

    //--------------------------------------------Filter Box Handlers--------------------------------------------
    $scope.filterVisible = false;
    $scope.toggle = true;
    $rootScope.prop.menu = false;

    $scope.getGenres = function () {
        return ([
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
        ])
    }

    $scope.getLanguage = function () {
        return ([
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
        ])
    }

    $scope.genresSelector = $scope.getGenres();
    $scope.languages = $scope.getLanguage();

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
    }

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

    //--------------------------------------------Get Filters Result Handlers--------------------------------------------

    $scope.getFilterResult = function () {
        $scope.baseUrl = 'http://api.themoviedb.org/3/discover/movie?api_key=5880f597a9fab4f284178ffe0e1f0dba';
        $scope.baseParams = '&language=pt-BR&release_date.gte=' + $routeParams.yearMin +
            '&release_date.lte=' + $routeParams.yearMax + '&with_runtime.gte=' +
            $routeParams.runtimeMin + '&with_runtime.lte=' + $routeParams.runtimeMax;

        $scope.params = '';

        if ($routeParams.genres == 'null' && $routeParams.language == 'null') {
            $scope.params = $scope.baseParams;

        } else if ($routeParams.genres == 'null') {
            $scope.params = $scope.baseParams + '&with_original_language=' + $routeParams.language;
        } else if ($routeParams.language == 'null') {
            $scope.params = $scope.baseParams + '&with_genres=' + $routeParams.genres;
        } else {
            $scope.params = $scope.baseParams + '&with_genres=' + $routeParams.genres + '&with_original_language=' + $routeParams.language;
        }

        $scope.requestUrl = $scope.baseUrl + $scope.params;

        $scope.getList = $http.get($scope.requestUrl);

        $scope.getList.then(
            function (payload) {
                $scope.fullList = [];
                $scope.index = [];

                for (i = 0; i < payload.data.results.length; i++) {
                    $scope.fullList.push({
                        title: payload.data.results[i].title,
                        poster: 'https://image.tmdb.org/t/p/original/' + payload.data.results[i].poster_path,
                        tmdb_id: payload.data.results[i].id
                    });
                }
                $scope.chunk_size = 6;
                $scope.filteredList = $scope.fullList.map(function (e, i) {
                    return i % $scope.chunk_size === 0 ? $scope.fullList.slice(i, i + $scope.chunk_size) : null;
                })
                    .filter(function (e) { return e; });

                for (i = 0; i < $scope.filteredList.length; i++) {
                    $scope.index.push(i);
                }
                $scope.control = true;

            });
    }

    $scope.getFilterResult();

    $scope.getSelectedGenres = function () {
        $scope.genresSelector = $scope.getGenres();
        if ($routeParams.genres == 'null') {
            return ('Não Selecionado')
        } else {
            $scope.lgenres = [];
            $scope.rawGenres = $routeParams.genres.split(',');

            for (i = 0; i < $scope.rawGenres.length; i++) {
                for (k = 0; k < $scope.genresSelector.length; k++) {
                    if ($scope.genresSelector[k].id == $scope.rawGenres[i]) {
                        $scope.lgenres.push($scope.genresSelector[k].name)
                    }
                }
            }

            return ($scope.lgenres.join(", "));
        }

    }

    $scope.getSelectedLanguage = function () {
        if ($routeParams.language == 'pt') {
            $scope.lng = 'Português';
        }
        if ($routeParams.language == 'en') {
            $scope.lng = 'Inglês';
        }
        if ($routeParams.language == 'de') {
            $scope.lng = 'Alemão';
        }
        if ($routeParams.language == 'it') {
            $scope.lng = 'Italiano';
        }
        if ($routeParams.language == 'ja') {
            $scope.lng = 'Japonês';
        }
        if ($routeParams.language == 'fr') {
            $scope.lng = 'Francês';
        }

        if ($routeParams.language == 'null') {
            $scope.lng = 'Não Selecionado';
        }

        return ($scope.lng);
    }

    $scope.getSelectedFilters = function () {
        $scope.currentGenres = $scope.getSelectedGenres();
        $scope.currentLanguage = $scope.getSelectedLanguage();
        $scope.currentMinRuntime = $routeParams.runtimeMin + 'min';
        $scope.currentMaxRuntime = $routeParams.runtimeMax + 'min';
        $scope.currentMinYear = $routeParams.yearMin.split('-');
        $scope.currentMinYear = $scope.currentMinYear[0];
        $scope.currentMaxYear = $routeParams.yearMax.split('-');
        $scope.currentMaxYear = $scope.currentMaxYear[0];
    }

    $scope.getSelectedFilters();

    //--------------------------------------------Filter Request Handlers--------------------------------------------
    $scope.handleFilters = function (genres, yearMin, yearMax, runtimeMin, runtimeMax, languages) {
        $scope.selectedGenres = [];
        $scope.selectedLanguage = 'null';
        $scope.aux = 0;

        for (i = 0; i < genres.length; i++) {
            if (genres[i].selected) {
                $scope.selectedGenres.push(genres[i].id);
            }
        }

        if ($scope.selectedGenres == '') {
            $scope.selectedGenres = 'null';
        } else {
            $scope.selectedGenres = $scope.selectedGenres.join(",");
        }

        for (i = 0; i < languages.length; i++) {
            if (languages[i].selected) {
                $scope.selectedLanguage = languages[i].code;
            }
        }

        $scope.selectedMinYear = yearMin + '-' + '01' + '-' + '01';
        $scope.selectedMaxYear = yearMax + '-' + '12' + '-' + '31'

        $window.location.href = '#/filtersview/' + $scope.selectedGenres + '/' + $scope.selectedLanguage + '/' + $scope.selectedMinYear + '/' + $scope.selectedMaxYear + '/' + runtimeMin + '/' + runtimeMax;
    }

    //--------------------------------------------Rating Handler--------------------------------------------

    $scope.setUserRatingExternal = function (rating, poster, title, id) {

        $http.post("rateexternalmovie/", {
            "tmdb_movie_id": id,
            "rate_id": rating,
            "user_id": $rootScope.globals.currentUser.user_id,
            "movie_poster": poster,
            "movie_title": title
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