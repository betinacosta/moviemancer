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
	
	$http.get('reco').success(function(data) {

		for (i = 0; i < data.length; i++) {
			$scope.fullRecommendation.push ({title: data[i].tmdb_title, poster: data[i].tmdb_poster});
		}

        $scope.teste = $scope.splitRecommendations($scope.fullRecommendation, Math.ceil($scope.fullRecommendation.length/6), true);

	});
},

$scope.splitRecommendations = function (a, n, balanced) {
    
    if (n < 2)
        return [a];

    var len = a.length,
            out = [],
            i = 0,
            size;

    if (len % n === 0) {
        size = Math.floor(len / n);
        while (i < len) {
            out.push(a.slice(i, i += size));
        }
    }

    else if (balanced) {
        while (i < len) {
            size = Math.ceil((len - i) / n--);
            out.push(a.slice(i, i += size));
        }
    }

    else {

        n--;
        size = Math.floor(len / n);
        if (len % size === 0)
            size--;
        while (i < size * n) {
            out.push(a.slice(i, i += size));
        }
        out.push(a.slice(size * n));

    }

    return out;
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
