var app = angular.module('myApp2', []).config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    });

app.controller('recoCtrl', ['$scope', '$http', function ($scope, $http) {

	$scope.init = function() {

		$scope.getRecommendation();
	},

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

},

$scope.getRecommendation = function (movies) {
	$scope.fullRecommendation = [];
	
	$http.get('reco').success(function(data) {

		for (i = 0; i < data.length; i++) {
			$scope.fullRecommendation.push ({title: data[i].tmdb_title, poster: data[i].tmdb_poster});
		}
	});
},

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
          
},
// Call init function
	$scope.init();

}]);
