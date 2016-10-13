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

$scope.formatDate = function (date) {
	$scope.day = date.getDate()
	$scope.month = date.getMonth()+1;
	$scope.year = date.getFullYear();

	if($scope.day<10){
		$scope.day='0'+$scope.day
	}
	if($scope.month<10){
		$scope.month='0'+$scope.month
	} 

	return $scope.year + '-' + $scope.month + '-' + $scope.day;
}

$scope.getEndDate = function (initialDate, days) {
	
    initialDate.setDate(initialDate.getDate() + days);
    return initialDate;
}

$scope.loadCommingSoon = function () {
	$scope.today = $scope.formatDate(new Date());
	$scope.endDate = $scope.getEndDate(new Date(), 15);
	$scope.endDate = $scope.formatDate($scope.endDate);
	oParams = 
        {
            "primary_release_date.gte": $scope.today,
			"primary_release_date.lte": $scope.endDate,
            "language": "pt-br"
        };

	$scope.commingSoon = [];
	$scope.imagePath = 'https://image.tmdb.org/t/p/original/';

        tmdb.call("/discover/movie", oParams,
            function(soon, commingSoon, imagePath){
                for (i = 0; i < 6; i++)  {
					$scope.commingSoon. push (
						{
							img:$scope.imagePath + soon.results[i].poster_path,
							title:soon.results[i].title
						}
					)
				}
				console.log($scope.commingSoon);
            }, 
            function(e){
                console.log("Error: "+e)
            }   
        );
}
$scope.loadCommingSoon();


$scope.loadRecommendation = function () {

	$scope.images = [];
	$scope.imagePath = 'https://image.tmdb.org/t/p/original/';
	$http.get('reco').success(function(data, images, imagePath) {
	
		oParams = {"language": "pt-br"};

		for (i = 0; i < data.length; i++) {

			tmdb.call("/movie/" + data[i].tmdb_movie_id, oParams,
            function(movies){
				
                $scope.images.push ( 
					{
						img: $scope.imagePath + movies.poster_path,
						title: movies.title
					})
            }, 
            function(e){
                console.log("Error: "+e)
            }   
        );
		}
	});
}

$scope.loadRecommendation();

$scope.showFilterBar = function() {

	filterBar = document.getElementById('filterBar');
	toggleUp = document.getElementById('toggleUp');
	toggleDown = document.getElementById('toggleDown');

       if(filterBar.style.display == 'block') {
          filterBar.style.display = 'none';
		  toggleUp.style.display = 'none';
		  toggleDown.style.display = 'inline-block';
	   }
       else {
		   filterBar.style.display = 'block';
			toggleUp.style.display = 'inline-block';
			toggleDown.style.display = 'none';
	   }
          
}


}]);
