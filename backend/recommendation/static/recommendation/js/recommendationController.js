var app = angular.module('myApp2', []).config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    });

app.controller('recoCtrl', ['$scope', '$http', function ($scope, $http) {

	$scope.init = function() {

		$scope.getRecommendation();
	},

$scope.getRecommendation = function (movies) {
	$scope.fullRecommendation = [];
    $scope.index = [];
	
	$http.get('reco').success(function(data) {

		for (i = 0; i < data.length; i++) {
			$scope.fullRecommendation.push ({   title: data[i].tmdb_title, 
                                                poster: data[i].tmdb_poster, 
                                                movie_id: data[i].movie_id, 
                                                tmdb_id: data[i].tmdb_movie_id});
		}

		$scope.chunk_size = 6;
		$scope.fullList = $scope.fullRecommendation.map( function(e,i){ 
			return i%$scope.chunk_size===0 ? $scope.fullRecommendation.slice(i,i+$scope.chunk_size) : null; 
		})
		.filter(function(e){ return e; });

        for (i = 0; i < $scope.fullList.length; i++) {
            $scope.index.push(i);
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

$scope.setUserRating = function (rating, movieID) {

		$http.post("ratemovie/", {
				"movie_id": movieID,
				"rate_id": rating,
				"user_id": 1
			}, {
				'Content-Type': 'application/json; charset=utf-8'
			})
			.then(
				function (response) {
					$scope.getRecommendation();
					console.log('Success: ', response.data)
					$scope.toastMessege("Filme Adicionado a Lista de Vistos")
				},
				function (response) {
					console.log('Error: ', response)
				}
			);

			
	}

	$scope.addWatchlist = function (movieID) {

		$http.post("addwatchlist/", {
				"movie_id": movieID,
				"user_id": 1
			}, {
				'Content-Type': 'application/json; charset=utf-8'
			})
			.then(
				function (response) {
					console.log('Success: ', response.data)
					$scope.getRecommendation();
					$scope.toastMessege("Filme Adicionado a Quero Ver")
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
		setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}

}]);
