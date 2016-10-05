var app = angular.module('myApp', []).config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    });

app.controller('mainCtrl', ['$scope', '$http', function ($scope, $http) {

    (function() {
	window.tmdb = {
		"api_key": "5880f597a9fab4f284178ffe0e1f0dba",
		"base_uri": "http://api.themoviedb.org/3",
		"images_uri": "http://image.tmdb.org/t/p",
		"timeout": 5000,
		call: function(url, params, success, error){
			var params_str ="api_key="+tmdb.api_key;
			for (var key in params) {
				if (params.hasOwnProperty(key)) {
					params_str+="&"+key+"="+encodeURIComponent(params[key]);
				}
			}
			var xhr = new XMLHttpRequest();
			xhr.timeout = tmdb.timeout;
			xhr.ontimeout = function () {
				throw("Request timed out: " + url +" "+ params_str);
			};
			xhr.open("GET", tmdb.base_uri + url + "?" + params_str, true);
			xhr.setRequestHeader('Accept', 'application/json');
			xhr.responseType = "text";
			xhr.onreadystatechange = function () {
				if (this.readyState === 4) {
					if (this.status === 200){
						if (typeof success == "function") {
							success(JSON.parse(this.response));	
						}else{
							throw('No success callback, but the request gave results')
						}
					}else{
						if (typeof error == "function") {
							error(JSON.parse(this.response));
						}else{
							throw('No error callback')
						}
					}
				}
			};
			xhr.send();
		}
	}
})()

$scope.searchMovie = function (query) {
    oParams = 
        {
            "query": query,
            "language": "pt-br"
        };

        tmdb.call("/search/movie", oParams,
            function(searchResult){
                console.log(searchResult)
            }, 
            function(e){
                console.log("Error: "+e)
            }   
        );

}

$scope.loadCommingSoon = function () {
	commingsoon = 
        {
            "primary_release_date.gte": '2014-09-15',
			"primary_release_date.lte": '2014-10-22',
            "language": "pt-br"
        };

        tmdb.call("/discover/movie", commingsoon,
            function(soon){
                console.log(soon)
            }, 
            function(e){
                console.log("Error: "+e)
            }   
        );
}



	//tmdb.call("/movie/" + data[0].tmdb_movie_id, recoo,
       //     function(soon){
           //     console.log(soon)
           // }, 
           // function(e){
           //     console.log("Error: "+e)
          //  }   
       // );

$scope.loadRecommendation = function () {

	$scope.images = [];
	$scope.imagePath = 'https://image.tmdb.org/t/p/original/';
	$http.get('reco').success(function(data, images, imagePath) {
	
		oParams = {"language": "pt-br"};

		for (i = 0; i < data.length; i++) {

			tmdb.call("/movie/" + data[i].tmdb_movie_id, oParams,
            function(movies){
				
                $scope.images.push ( {img: $scope.imagePath + movies.poster_path})
            }, 
            function(e){
                console.log("Error: "+e)
            }   
        );
		}
	});
}

$scope.loadRecommendation();


}]);
