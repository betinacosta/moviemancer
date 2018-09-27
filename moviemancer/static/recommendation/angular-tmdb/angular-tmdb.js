/* global angular */
var storage = angular.module('tmdb', [])

    .value('TMDB', {
    "API_KEY": undefined,
    "API_URL": 'http://api.themoviedb.org/3/',
    "IMG_URL": 'http://image.tmdb.org/'
})

    .service('tmdbMovie', ['TMDB', '$http', function (TMDB, $http) {
    this.search = function (title, params, onSuccess, onError) {
        var paramString = '';
        for (var p in params) {
            paramString = paramString + '&' + p + '=' + params[p];
        }
        var url = TMDB.API_URL + 'search/movie?api_key=' + TMDB.API_KEY + '&search_type=ngram&query=' + title + paramString;
        $http.get(url).
            success(function (data, status, headers, config) {
            if (onSuccess !== undefined)
                onSuccess(data, status, headers, config);
        }).
            error(function (data, status, headers, config) {
            if (onError !== undefined)
                onError(data, status, headers, config);
        });
    }

    this.details = function (id, params, onSuccess, onError) {
        var paramString = '';
        for (var p in params) {
            paramString = paramString + '&' + p + '=' + params[p];
        }
        var url = TMDB.API_URL + 'movie/' + id + '?api_key=' + TMDB.API_KEY + paramString;
        $http.get(url).
            success(function (data, status, headers, config) {
            if (onSuccess !== undefined)
                onSuccess(data, status, headers, config);
        }).
            error(function (data, status, headers, config) {
            if (onError !== undefined)
                onError(data, status, headers, config);
        });
    }

    this.images = function (id, params, onSuccess, onError) {
        var paramString = '';
        for (var p in params) {
            paramString = paramString + '&' + p + '=' + params[p];
        }
        var url = TMDB.API_URL + 'movie/' + id + '/images?api_key=' + TMDB.API_KEY + paramString;
        $http.get(url).
            success(function (data, status, headers, config) {
            if (onSuccess !== undefined)
                onSuccess(data, status, headers, config);
        }).
            error(function (data, status, headers, config) {
            if (onError !== undefined)
                onError(data, status, headers, config);
        });
    }

    this.discover = function (params, onSuccess, onError) {
        var paramString = '';
        for (var p in params) {
            paramString = paramString + '&' + p + '=' + params[p];
        }
        var url = TMDB.API_URL + 'discover/movie?api_key=' + TMDB.API_KEY + paramString;

        $http.get(url).
            success(function (data, status, headers, config) {
            if (onSuccess !== undefined)
                onSuccess(data, status, headers, config);
        }).
            error(function (data, status, headers, config) {
            if (onError !== undefined)
                onError(data, status, headers, config);
        });
    }

    this.alternativeTitles = function (id, params, onSuccess, onError) {
        var paramString = '';
        for (var p in params) {
            paramString = paramString + '&' + p + '=' + params[p];
        }
        var request = TMDB.API_URL + 'movie/' + id + '/alternative_titles?api_key=' + TMDB.API_KEY + paramString;

        $http.get(request).
            success(function (data, status, headers, config) {
            if (onSuccess !== undefined)
                onSuccess(data, status, headers, config);
        }).
            error(function (data, status, headers, config) {
            if (onError !== undefined)
                onError(data, status, headers, config);
        });
    }

    this.credits = function (id, params, onSuccess, onError) {
        var paramString = '';
        for (var p in params) {
            paramString = paramString + '&' + p + '=' + params[p];
        }
        var request = TMDB.API_URL + 'movie/' + id + '/credits?api_key=' + TMDB.API_KEY + paramString;
        $http.get(request).
            success(function (data, status, headers, config) {
            if (onSuccess !== undefined)
                onSuccess(data, status, headers, config);
        }).
            error(function (data, status, headers, config) {
            if (onError !== undefined)
                onError(data, status, headers, config);
        });
    }

    this.keywords = function (id, params, onSuccess, onError) {
        var paramString = '';
        for (var p in params) {
            paramString = paramString + '&' + p + '=' + params[p];
        }
        var request = TMDB.API_URL + 'movie/' + id + '/keywords?api_key=' + TMDB.API_KEY + paramString;
        $http.get(request).
            success(function (data, status, headers, config) {
            if (onSuccess !== undefined)
                onSuccess(data, status, headers, config);
        }).
            error(function (data, status, headers, config) {
            if (onError !== undefined)
                onError(data, status, headers, config);
        });
    }

    this.releases = function (id, params, onSuccess, onError) {
        var paramString = '';
        for (var p in params) {
            paramString = paramString + '&' + p + '=' + params[p];
        }
        var request = TMDB.API_URL + 'movie/' + id + '/releases?api_key=' + TMDB.API_KEY + paramString;
        $http.get(request).
            success(function (data, status, headers, config) {
            if (onSuccess !== undefined)
                onSuccess(data, status, headers, config);
        }).
            error(function (data, status, headers, config) {
            if (onError !== undefined)
                onError(data, status, headers, config);
        });
    }

    this.videos = function (id, params, onSuccess, onError) {
        var paramString = '';
        for (var p in params) {
            paramString = paramString + '&' + p + '=' + params[p];
        }
        var request = TMDB.API_URL + 'movie/' + id + '/videos?api_key=' + TMDB.API_KEY + paramString;
        $http.get(request).
            success(function (data, status, headers, config) {
            if (onSuccess !== undefined)
                onSuccess(data, status, headers, config);
        }).
            error(function (data, status, headers, config) {
            if (onError !== undefined)
                onError(data, status, headers, config);
        });
    }

    this.translations = function (id, params, onSuccess, onError) {
        var paramString = '';
        for (var p in params) {
            paramString = paramString + '&' + p + '=' + params[p];
        }
        var request = TMDB.API_URL + 'movie/' + id + '/translations?api_key=' + TMDB.API_KEY + paramString;
        $http.get(request).
            success(function (data, status, headers, config) {
            if (onSuccess !== undefined)
                onSuccess(data, status, headers, config);
        }).
            error(function (data, status, headers, config) {
            if (onError !== undefined)
                onError(data, status, headers, config);
        });
    }

    this.similar = function (id, params, onSuccess, onError) {
        var paramString = '';
        for (var p in params) {
            paramString = paramString + '&' + p + '=' + params[p];
        }
        var request = TMDB.API_URL + 'movie/' + id + '/similar?api_key=' + TMDB.API_KEY + paramString;
        $http.get(request).
            success(function (data, status, headers, config) {
            if (onSuccess !== undefined)
                onSuccess(data, status, headers, config);
        }).
            error(function (data, status, headers, config) {
            if (onError !== undefined)
                onError(data, status, headers, config);
        });
    }

    this.reviews = function (id, params, onSuccess, onError) {
        var paramString = '';
        for (var p in params) {
            paramString = paramString + '&' + p + '=' + params[p];
        }
        var request = TMDB.API_URL + 'movie/' + id + '/reviews?api_key=' + TMDB.API_KEY + paramString;
        $http.get(request).
            success(function (data, status, headers, config) {
            if (onSuccess !== undefined)
                onSuccess(data, status, headers, config);
        }).
            error(function (data, status, headers, config) {
            if (onError !== undefined)
                onError(data, status, headers, config);
        });
    }

    this.lists = function (id, params, onSuccess, onError) {
        var paramString = '';
        for (var p in params) {
            paramString = paramString + '&' + p + '=' + params[p];
        }
        var request = TMDB.API_URL + 'movie/' + id + '/lists?api_key=' + TMDB.API_KEY + paramString;
        $http.get(request).
            success(function (data, status, headers, config) {
            if (onSuccess !== undefined)
                onSuccess(data, status, headers, config);
        }).
            error(function (data, status, headers, config) {
            if (onError !== undefined)
                onError(data, status, headers, config);
        });
    }

    this.upcoming = function (params, onSuccess, onError) {
        var paramString = '';
        for (var p in params) {
            paramString = paramString + '&' + p + '=' + params[p];
        }
        var request = TMDB.API_URL + 'movie/upcoming?api_key=' + TMDB.API_KEY + paramString;
        $http.get(request).
            success(function (data, status, headers, config) {
            if (onSuccess !== undefined)
                onSuccess(data, status, headers, config);
        }).
            error(function (data, status, headers, config) {
            if (onError !== undefined)
                onError(data, status, headers, config);
        });
    }

    this.nowPlaying = function (params, onSuccess, onError) {
        var paramString = '';
        for (var p in params) {
            paramString = paramString + '&' + p + '=' + params[p];
        }
        var request = TMDB.API_URL + 'movie/now_playing?api_key=' + TMDB.API_KEY + paramString;
        $http.get(request).
            success(function (data, status, headers, config) {
            if (onSuccess !== undefined)
                onSuccess(data, status, headers, config);
        }).
            error(function (data, status, headers, config) {
            if (onError !== undefined)
                onError(data, status, headers, config);
        });
    }

    this.popular = function (params, onSuccess, onError) {
        var paramString = '';
        for (var p in params) {
            paramString = paramString + '&' + p + '=' + params[p];
        }
        var request = TMDB.API_URL + 'movie/popular?api_key=' + TMDB.API_KEY + paramString;
        $http.get(request).
            success(function (data, status, headers, config) {
            if (onSuccess !== undefined)
                onSuccess(data, status, headers, config);
        }).
            error(function (data, status, headers, config) {
            if (onError !== undefined)
                onError(data, status, headers, config);
        });
    }
    
    this.topRated = function (params, onSuccess, onError) {
        var paramString = '';
        for (var p in params) {
            paramString = paramString + '&' + p + '=' + params[p];
        }
        var request = TMDB.API_URL + 'movie/top_rated?api_key=' + TMDB.API_KEY + paramString;
        $http.get(request).
            success(function (data, status, headers, config) {
            if (onSuccess !== undefined)
                onSuccess(data, status, headers, config);
        }).
            error(function (data, status, headers, config) {
            if (onError !== undefined)
                onError(data, status, headers, config);
        });
    }

    this.setup = function (apiKey, useSSL) {
        TMDB.API_KEY = apiKey;
        if (useSSL) {
            TMDB.API_URL = 'https://api.themoviedb.org/3/';
            TMDB.IMG_URL = 'https://image.tmdb.org/';
        } else {
            TMDB.API_URL = 'http://api.themoviedb.org/3/';
            TMDB.IMG_URL = 'http://image.tmdb.org/';
        }
    }
}])

    .service('tmdbTV', ['TMDB', '$http', function (TMDB, $http) {
    this.setup = function (apiKey, useSSL) {
        TMDB.API_KEY = apiKey;
        if (useSSL) {
            TMDB.API_URL = 'https://api.themoviedb.org/3/';
            TMDB.IMG_URL = 'https://image.tmdb.org/';
        } else {
            TMDB.API_URL = 'http://api.themoviedb.org/3/';
            TMDB.IMG_URL = 'http://image.tmdb.org/';
        }
    }

    this.tv = {
        details: function (id, params, onSuccess, onError) {
            var paramString = '';
            for (var p in params) {
                paramString = paramString + '&' + p + '=' + params[p];
            }
            var request = TMDB.API_URL + 'tv/' + id + '?api_key=' + TMDB.API_KEY + paramString;
            $http.get(request).
                success(function (data, status, headers, config) {
                if (onSuccess !== undefined)
                    onSuccess(data, status, headers, config);
            }).
                error(function (data, status, headers, config) {
                if (onError !== undefined)
                    onError(data, status, headers, config);
            });
        },
        alternativeTitles: function (id, params, onSuccess, onError) {
            var paramString = '';
            for (var p in params) {
                paramString = paramString + '&' + p + '=' + params[p];
            }
            var request = TMDB.API_URL + 'tv/' + id + '/alternative_titles?api_key=' + TMDB.API_KEY + paramString;
            $http.get(request).
                success(function (data, status, headers, config) {
                if (onSuccess !== undefined)
                    onSuccess(data, status, headers, config);
            }).
                error(function (data, status, headers, config) {
                if (onError !== undefined)
                    onError(data, status, headers, config);
            });
        },
        credits: function (id, params, onSuccess, onError) {
            var paramString = '';
            for (var p in params) {
                paramString = paramString + '&' + p + '=' + params[p];
            }
            var request = TMDB.API_URL + 'tv/' + id + '/credits?api_key=' + TMDB.API_KEY + paramString;
            $http.get(request).
                success(function (data, status, headers, config) {
                if (onSuccess !== undefined)
                    onSuccess(data, status, headers, config);
            }).
                error(function (data, status, headers, config) {
                if (onError !== undefined)
                    onError(data, status, headers, config);
            });
        },
        externalIds: function (id, params, onSuccess, onError) {
            var paramString = '';
            for (var p in params) {
                paramString = paramString + '&' + p + '=' + params[p];
            }
            var request = TMDB.API_URL + 'tv/' + id + '/external_ids?api_key=' + TMDB.API_KEY + paramString;
            $http.get(request).
                success(function (data, status, headers, config) {
                if (onSuccess !== undefined)
                    onSuccess(data, status, headers, config);
            }).
                error(function (data, status, headers, config) {
                if (onError !== undefined)
                    onError(data, status, headers, config);
            });
        },
        images: function (id, params, onSuccess, onError) {
            var paramString = '';
            for (var p in params) {
                paramString = paramString + '&' + p + '=' + params[p];
            }
            var request = TMDB.API_URL + 'tv/' + id + '/images?api_key=' + TMDB.API_KEY + paramString;
            $http.get(request).
                success(function (data, status, headers, config) {
                if (onSuccess !== undefined)
                    onSuccess(data, status, headers, config);
            }).
                error(function (data, status, headers, config) {
                if (onError !== undefined)
                    onError(data, status, headers, config);
            });
        },
        keywords: function (id, params, onSuccess, onError) {
            var paramString = '';
            for (var p in params) {
                paramString = paramString + '&' + p + '=' + params[p];
            }
            var request = TMDB.API_URL + 'tv/' + id + '/keywords?api_key=' + TMDB.API_KEY + paramString;
            $http.get(request).
                success(function (data, status, headers, config) {
                if (onSuccess !== undefined)
                    onSuccess(data, status, headers, config);
            }).
                error(function (data, status, headers, config) {
                if (onError !== undefined)
                    onError(data, status, headers, config);
            });
        },
        translations: function (id, params, onSuccess, onError) {
            var paramString = '';
            for (var p in params) {
                paramString = paramString + '&' + p + '=' + params[p];
            }
            var request = TMDB.API_URL + 'tv/' + id + '/translations?api_key=' + TMDB.API_KEY + paramString;
            $http.get(request).
                success(function (data, status, headers, config) {
                if (onSuccess !== undefined)
                    onSuccess(data, status, headers, config);
            }).
                error(function (data, status, headers, config) {
                if (onError !== undefined)
                    onError(data, status, headers, config);
            });
        },
        similar: function (id, params, onSuccess, onError) {
            var paramString = '';
            for (var p in params) {
                paramString = paramString + '&' + p + '=' + params[p];
            }
            var request = TMDB.API_URL + 'tv/' + id + '/similar?api_key=' + TMDB.API_KEY + paramString;
            $http.get(request).
                success(function (data, status, headers, config) {
                if (onSuccess !== undefined)
                    onSuccess(data, status, headers, config);
            }).
                error(function (data, status, headers, config) {
                if (onError !== undefined)
                    onError(data, status, headers, config);
            });
        },
        videos: function (id, params, onSuccess, onError) {
            var paramString = '';
            for (var p in params) {
                paramString = paramString + '&' + p + '=' + params[p];
            }
            var request = TMDB.API_URL + 'tv/' + id + '/videos?api_key=' + TMDB.API_KEY + paramString;
            $http.get(request).
                success(function (data, status, headers, config) {
                if (onSuccess !== undefined)
                    onSuccess(data, status, headers, config);
            }).
                error(function (data, status, headers, config) {
                if (onError !== undefined)
                    onError(data, status, headers, config);
            });
        },
        onAir: function (params, onSuccess, onError) {
            var paramString = '';
            for (var p in params) {
                paramString = paramString + '&' + p + '=' + params[p];
            }
            var request = TMDB.API_URL + 'tv/on_the_air?api_key=' + TMDB.API_KEY + paramString;
            $http.get(request).
                success(function (data, status, headers, config) {
                if (onSuccess !== undefined)
                    onSuccess(data, status, headers, config);
            }).
                error(function (data, status, headers, config) {
                if (onError !== undefined)
                    onError(data, status, headers, config);
            });
        },
        onAirToday: function (params, onSuccess, onError) {
            var paramString = '';
            for (var p in params) {
                paramString = paramString + '&' + p + '=' + params[p];
            }
            var request = TMDB.API_URL + 'tv/airing_today?api_key=' + TMDB.API_KEY + paramString;
            $http.get(request).
                success(function (data, status, headers, config) {
                if (onSuccess !== undefined)
                    onSuccess(data, status, headers, config);
            }).
                error(function (data, status, headers, config) {
                if (onError !== undefined)
                    onError(data, status, headers, config);
            });
        },
        topRated: function (params, onSuccess, onError) {
            var paramString = '';
            for (var p in params) {
                paramString = paramString + '&' + p + '=' + params[p];
            }
            var request = TMDB.API_URL + 'tv/top_rated?api_key=' + TMDB.API_KEY + paramString;
            $http.get(request).
                success(function (data, status, headers, config) {
                if (onSuccess !== undefined)
                    onSuccess(data, status, headers, config);
            }).
                error(function (data, status, headers, config) {
                if (onError !== undefined)
                    onError(data, status, headers, config);
            });
        },
        popular: function (params, onSuccess, onError) {
            var paramString = '';
            for (var p in params) {
                paramString = paramString + '&' + p + '=' + params[p];
            }
            var request = TMDB.API_URL + 'tv/popular?api_key=' + TMDB.API_KEY + paramString;
            $http.get(request).
                success(function (data, status, headers, config) {
                if (onSuccess !== undefined)
                    onSuccess(data, status, headers, config);
            }).
                error(function (data, status, headers, config) {
                if (onError !== undefined)
                    onError(data, status, headers, config);
            });
        },
        discover: function (params, onSuccess, onError) {
            var paramString = '';
            for (var p in params) {
                paramString = paramString + '&' + p + '=' + params[p];
            }
            var url = TMDB.API_URL + 'discover/tv?api_key=' + TMDB.API_KEY + paramString;

            $http.get(url).
                success(function (data, status, headers, config) {
                if (onSuccess !== undefined)
                    onSuccess(data, status, headers, config);
            }).
                error(function (data, status, headers, config) {
                if (onError !== undefined)
                    onError(data, status, headers, config);

                console.log(data, status, headers, config);
            });
        }
    }
    this.seasons = {
        season: function (id, num, params, onSuccess, onError) {
            var paramString = '';
            for (var p in params) {
                paramString = paramString + '&' + p + '=' + params[p];
            }
            var request = TMDB.API_URL + 'tv/' + id + '/season/' + num + '?api_key=' + TMDB.API_KEY + paramString;
            $http.get(request).
                success(function (data, status, headers, config) {
                if (onSuccess !== undefined)
                    onSuccess(data, status, headers, config);
            }).
                error(function (data, status, headers, config) {
                if (onError !== undefined)
                    onError(data, status, headers, config);
            });
        },
        credits: function (id, num, params, onSuccess, onError) {
            var paramString = '';
            for (var p in params) {
                paramString = paramString + '&' + p + '=' + params[p];
            }
            var request = TMDB.API_URL + 'tv/' + id + '/season/' + num + '/credits?api_key=' + TMDB.API_KEY + paramString;
            $http.get(request).
                success(function (data, status, headers, config) {
                if (onSuccess !== undefined)
                    onSuccess(data, status, headers, config);
            }).
                error(function (data, status, headers, config) {
                if (onError !== undefined)
                    onError(data, status, headers, config);
            });
        },
        externalIds: function (id, num, params, onSuccess, onError) {
            var paramString = '';
            for (var p in params) {
                paramString = paramString + '&' + p + '=' + params[p];
            }
            var request = TMDB.API_URL + 'tv/' + id + '/season/' + num + '/external_ids?api_key=' + TMDB.API_KEY + paramString;
            $http.get(request).
                success(function (data, status, headers, config) {
                if (onSuccess !== undefined)
                    onSuccess(data, status, headers, config);
            }).
                error(function (data, status, headers, config) {
                if (onError !== undefined)
                    onError(data, status, headers, config);
            });
        },
        images: function (id, num, params, onSuccess, onError) {
            var paramString = '';
            for (var p in params) {
                paramString = paramString + '&' + p + '=' + params[p];
            }
            var request = TMDB.API_URL + 'tv/' + id + '/season/' + num + '/images?api_key=' + TMDB.API_KEY + paramString;
            $http.get(request).
                success(function (data, status, headers, config) {
                if (onSuccess !== undefined)
                    onSuccess(data, status, headers, config);
            }).
                error(function (data, status, headers, config) {
                if (onError !== undefined)
                    onError(data, status, headers, config);
            });
        },
        videos: function (id, num, params, onSuccess, onError) {
            var paramString = '';
            for (var p in params) {
                paramString = paramString + '&' + p + '=' + params[p];
            }
            var request = TMDB.API_URL + 'tv/' + id + '/season/' + num + '/videos?api_key=' + TMDB.API_KEY + paramString;
            $http.get(request).
                success(function (data, status, headers, config) {
                if (onSuccess !== undefined)
                    onSuccess(data, status, headers, config);
            }).
                error(function (data, status, headers, config) {
                if (onError !== undefined)
                    onError(data, status, headers, config);
            });
        }
    }
    this.episodes = {
        episode: function (id, sNumber, eNumber, params, onSuccess, onError) {            
            var paramString = '';
            for (var p in params) {
                paramString = paramString + '&' + p + '=' + params[p];
            }
            var request = TMDB.API_URL + 'tv/' + id + '/season/' + sNumber + '/episode/' + eNumber + '?api_key=' + TMDB.API_KEY + paramString;
            $http.get(request).
                success(function (data, status, headers, config) {
                if (onSuccess !== undefined)
                    onSuccess(data, status, headers, config);
            }).
                error(function (data, status, headers, config) {
                if (onError !== undefined)
                    onError(data, status, headers, config);
            });
        },
        credits: function (id, sNumber, eNumber, params, onSuccess, onError) {
            var paramString = '';
            for (var p in params) {
                paramString = paramString + '&' + p + '=' + params[p];
            }
            var request = TMDB.API_URL + 'tv/' + id + '/season/' + sNumber + '/episode/' + eNumber + '/credits?api_key=' + TMDB.API_KEY + paramString;
            $http.get(request).
                success(function (data, status, headers, config) {
                if (onSuccess !== undefined)
                    onSuccess(data, status, headers, config);
            }).
                error(function (data, status, headers, config) {
                if (onError !== undefined)
                    onError(data, status, headers, config);
            });
        },
        externalIds: function (id, sNumber, eNumber, params, onSuccess, onError) {
            var paramString = '';
            for (var p in params) {
                paramString = paramString + '&' + p + '=' + params[p];
            }
            var request = TMDB.API_URL + 'tv/' + id + '/season/' + sNumber + '/episode/' + eNumber + '/external_ids?api_key=' + TMDB.API_KEY + paramString;
            $http.get(request).
                success(function (data, status, headers, config) {
                if (onSuccess !== undefined)
                    onSuccess(data, status, headers, config);
            }).
                error(function (data, status, headers, config) {
                if (onError !== undefined)
                    onError(data, status, headers, config);
            });
        },
        images: function (id, sNumber, eNumber, params, onSuccess, onError) {
            var paramString = '';
            for (var p in params) {
                paramString = paramString + '&' + p + '=' + params[p];
            }
            var request = TMDB.API_URL + 'tv/' + id + '/season/' + sNumber + '/episode/' + eNumber + '/images?api_key=' + TMDB.API_KEY + paramString;
            $http.get(request).
                success(function (data, status, headers, config) {
                if (onSuccess !== undefined)
                    onSuccess(data, status, headers, config);
            }).
                error(function (data, status, headers, config) {
                if (onError !== undefined)
                    onError(data, status, headers, config);
            });
        },
        videos: function (id, sNumber, eNumber, params, onSuccess, onError) {
            var paramString = '';
            for (var p in params) {
                paramString = paramString + '&' + p + '=' + params[p];
            }
            var request = TMDB.API_URL + 'tv/' + id + '/season/' + sNumber + '/episode/' + eNumber + '/videos?api_key=' + TMDB.API_KEY + paramString;
            $http.get(request).
                success(function (data, status, headers, config) {
                if (onSuccess !== undefined)
                    onSuccess(data, status, headers, config);
            }).
                error(function (data, status, headers, config) {
                if (onError !== undefined)
                    onError(data, status, headers, config);
            });
        }
    }
}]);
