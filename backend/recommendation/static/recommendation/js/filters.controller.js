var app = angular.module('filtersApp', ['ngRateIt', 'rzModule']).config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

app.controller('filtersCtrl', ['$scope', '$http', '$routeParams', '$window', function ($scope, $http, $routeParams, $window) {

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

    $scope.genresSelector = [
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
    ];

    $scope.languages = [
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
    ]

    $scope.getSelectedGenres = function () {

        if ($routeParams.genres) {
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
        } else {
            return ('Não Selecionado')
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

        if ($routeParams.language == '') {
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

    $scope.getFilteredList = function () {
        $scope.index = [];
        $scope.fullList = []

        oParams = {
            "language": "pt-BR",
            "release_date.gte": $routeParams.yearMin,
            "release_date.lte": $routeParams.yearMax,
            "with_runtime.gte": $routeParams.runtimeMin,
            "with_runtime.lte": $routeParams.runtimeMax,
            "with_genres": $routeParams.genres,
            "with_original_language": $routeParams.language
        };

        tmdb.call('/discover/movie', oParams,
            function (discovered, fullList) {
                for (i = 0; i < discovered.results.length; i++) {
                    $scope.fullList.push({
                        title: discovered.results[i].title,
                        poster: 'https://image.tmdb.org/t/p/original/' + discovered.results[i].poster_path,
                        tmdb_id: discovered.results[i].id
                    });
                }

                $scope.chunk_size = 6;
                $scope.filteredList = $scope.fullList.map(function (e, i) {
                    return i % $scope.chunk_size === 0 ? $scope.fullList.slice(i, i + $scope.chunk_size) : null;
                })
                    .filter(function (e) { return e; });

                for (i = 0; i < $scope.fullList.length; i++) {
                    $scope.index.push(i);
                }

            },
            function (e) {
                console.log("Error: " + e)
            }
        );
    }

    $scope.getFilteredList();
    $scope.getSelectedFilters();

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

    $scope.genresSelector = [
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
    ];

    $scope.languages = [
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
    ]

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

    $scope.handleFilters = function (genres, yearMin, yearMax, runtimeMin, runtimeMax, languages) {
        $scope.selectedGenres = [];
        $scope.selectedLanguage = '';
        $scope.aux = 0;

        for (i = 0; i < genres.length; i++) {
            if (genres[i].selected) {
                $scope.selectedGenres.push(genres[i].id);
            }
        }

        $scope.selectedGenres = $scope.selectedGenres.join(",");

        for (i = 0; i < languages.length; i++) {
            if (languages[i].selected) {
                $scope.selectedLanguage = languages[i].code;
            }
        }

        $scope.selectedMinYear = yearMin + '-' + '01' + '-' + '01';
        $scope.selectedMaxYear = yearMax + '-' + '12' + '-' + '31'

        $window.location.href = '#/filtersview/' + $scope.selectedGenres + '/' + $scope.selectedLanguage + '/' + $scope.selectedMinYear + '/' + $scope.selectedMaxYear + '/' + runtimeMin + '/' + runtimeMax;
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

}]);