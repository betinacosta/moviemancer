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
            function(e){
                console.log(e)
            }, 
            function(e){
                console.log("Error: "+e)
            }   
        )
}

//$scope.init = function () {
		$scope.imagePath = 'https://image.tmdb.org/t/p/original/';

		$scope.test = ['oi', 'bye'];

		$scope.images = [
			{
				img: $scope.imagePath + '/14HTiOiLHYf3qYIuxO12FkbfWlA.jpg',
				title: 'Os Oito Odiados'
			},
			{
				img: $scope.imagePath + '/qrx3qxAV1BW3JWdsglLJvyYZS0m.jpg',
				title: 'Os Infratores'
			},
			{
				img: $scope.imagePath + '/14HTiOiLHYf3qYIuxO12FkbfWlA.jpg',
				title: 'Os Oito Odiados'
			},
			{
				img: $scope.imagePath + '/qrx3qxAV1BW3JWdsglLJvyYZS0m.jpg',
				title: 'Os Infratores'
			},
			{
				img: $scope.imagePath + '/14HTiOiLHYf3qYIuxO12FkbfWlA.jpg',
				title: 'Os Oito Odiados'
			},
			{
				img: $scope.imagePath + '/qrx3qxAV1BW3JWdsglLJvyYZS0m.jpg',
				title: 'Os Infratores'
			}
		];

	//};

}]);
