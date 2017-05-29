'use strict';

angular.module('Moviemancer')

    .factory('MoviemancerService', ['$http', '$rootScope', '$window', function ($http, $rootScope, $window) {
        var service = {};

        service.getGenres = function () {
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

        service.getLanguages = function () {
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

        service.handleFilters = function (genres, yearMin, yearMax, runtimeMin, runtimeMax, languages) {
            var selectedGenres = [];
            var selectedLanguage = 'null';
            var aux = 0;

            for (i = 0; i < genres.length; i++) {
                if (genres[i].selected) {
                    selectedGenres.push(genres[i].id);
                }
            }

            if (selectedGenres == '') {
                selectedGenres = 'null';
            } else {
                selectedGenres = selectedGenres.join(",");
            }

            for (i = 0; i < languages.length; i++) {
                if (languages[i].selected) {
                    selectedLanguage = languages[i].code;
                }
            }

            var selectedMinYear = yearMin + '-' + '01' + '-' + '01';
            var selectedMaxYear = yearMax + '-' + '12' + '-' + '31'

            $window.location.href = '#/filtersview/' + selectedGenres + '/' + selectedLanguage + '/' + selectedMinYear + '/' + selectedMaxYear + '/' + runtimeMin + '/' + runtimeMax;
        }

        function uncheckLanguage(index, id, languages) {
            languages[index].selected = false;
            document.getElementById(id).style.backgroundColor = '#7d7b7b';
            return languages;
        }

        function checkLanguage(index, id, languages) {
            languages[index].selected = !languages[index].selected;
            if (languages[index].selected) {
                document.getElementById(id).style.backgroundColor = '#9a2726';
            } else {
                document.getElementById(id).style.backgroundColor = '#7d7b7b';
            }
            return languages;
        }

        service.selectPT = function (lng) {
            //Selected
            lng = checkLanguage(0, 'pt', lng)
            //Outros
            lng = uncheckLanguage(1, 'en', lng);
            lng = uncheckLanguage(2, 'de', lng);
            lng = uncheckLanguage(3, 'it', lng);
            lng = uncheckLanguage(4, 'ja', lng);
            lng = uncheckLanguage(5, 'fr', lng);

            return lng;
        }

        service.selectEN = function (lng) {
            //Selected
            lng = checkLanguage(1, 'en', lng)
            //Outros
            lng = uncheckLanguage(0, 'pt', lng);
            lng = uncheckLanguage(2, 'de', lng);
            lng = uncheckLanguage(3, 'it', lng);
            lng = uncheckLanguage(4, 'ja', lng);
            lng = uncheckLanguage(5, 'fr', lng);

            return lng;
        }

        service.selectDE = function (lng) {
            //Selected
            lng = checkLanguage(2, 'de', lng)
            //Outros
            lng = uncheckLanguage(1, 'en', lng);
            lng = uncheckLanguage(0, 'pt', lng);
            lng = uncheckLanguage(3, 'it', lng);
            lng = uncheckLanguage(4, 'ja', lng);
            lng = uncheckLanguage(5, 'fr', lng);

            return lng;
        }

        service.selectIT = function (lng) {
            //Selected
            lng = checkLanguage(3, 'it', lng)
            //Outros
            lng = uncheckLanguage(1, 'en', lng);
            lng = uncheckLanguage(2, 'de', lng);
            lng = uncheckLanguage(0, 'pt', lng);
            lng = uncheckLanguage(4, 'ja', lng);
            lng = uncheckLanguage(5, 'fr', lng);

            return lng;
        }

        service.selectJA = function (lng) {
            //Selected
            lng = checkLanguage(4, 'ja', lng)
            //Outros
            lng = uncheckLanguage(1, 'en', lng);
            lng = uncheckLanguage(2, 'de', lng);
            lng = uncheckLanguage(3, 'it', lng);
            lng = uncheckLanguage(0, 'pt', lng);
            lng = uncheckLanguage(5, 'fr', lng);

            return lng;
        }

        service.selectFR = function (lng) {
            //Selected
            lng = checkLanguage(5, 'fr', lng)
            //Outros
            lng = uncheckLanguage(1, 'en', lng);
            lng = uncheckLanguage(2, 'de', lng);
            lng = uncheckLanguage(3, 'it', lng);
            lng = uncheckLanguage(4, 'ja', lng);
            lng = uncheckLanguage(0, 'pt', lng);

            return lng;
        }

        service.selectGenre = function (id, index, genresSelector) {
            genresSelector[index].selected = !genresSelector[index].selected;
            var btn = document.getElementById(id);

            if (genresSelector[index].selected) {
                btn.style.backgroundColor = '#9a2726';
                btn.style.color = '#fff';
            } else {
                btn.style.backgroundColor = '#7d7b7b';
                btn.style.color = '#fff';
            }

            return genresSelector

        }

        //---------------------------------------------------Rating---------------------------------------------------
        service.setUserRating = function (rating, movieID, userID, callback) {

            $http.post("ratemovie/", {
                "movie_id": movieID,
                "rate_id": rating,
                "user_id": userID
            }, {
                    'Content-Type': 'application/json; charset=utf-8'
                })
                .then(
                function (response) {
                    callback(response);
                },
                function (response) {
                    callback(response);
                }
                );
        }

        service.setUserRatingExternal = function (rating, poster, title, id, userID, callback) {

            $http.post("rateexternalmovie/", {
                "tmdb_movie_id": id,
                "rate_id": rating,
                "user_id": userID,
                "movie_poster": poster,
                "movie_title": title
            }, {
                    'Content-Type': 'application/json; charset=utf-8'
                })
                .then(
                function (response) {
                    callback(response);
                },
                function (response) {
                    callback(response);
                }
                );
        }

        //---------------------------------------------------Watchlist---------------------------------------------------
        service.addWatchlist = function (movieID, userID, callback) {

            $http.post("addwatchlist/", {
                "movie_id": movieID,
                "user_id": userID
            }, {
                    'Content-Type': 'application/json; charset=utf-8'
                })
                .then(
                function (response) {
                    callback(response);
                },
                function (response) {
                    callback(response);
                }
                );
        }

        service.addWatchlistExternal = function (tmdb_id, poster, title, userID, callback) {

            $http.post("addwatchlistexternal/", {
                "tmdb_movie_id": tmdb_id,
                "user_id": userID,
                "movie_poster": poster,
                "movie_title": title
            }, {
                    'Content-Type': 'application/json; charset=utf-8'
                })
                .then(
                function (response) {
                    callback(response);
                },
                function (response) {
                    callback(response);
                }
                );
        }


        return service;
    }])