var app = angular.module('profileApp', []).config(function ($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

app.controller('profileCtrl', ['$scope', '$http', '$rootScope', function ($scope, $http, $rootScope) {

	$scope.init = function () {
		$scope.getProfile();
	}
	$scope.batata = 28

	$scope.genres = [{
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
		}
	];

	$scope.getGenreName = function (genreID) {
		for (i=0;i<$scope.genres.length; i++) {
			if($scope.genres[i].id == genreID) {
				return $scope.genres[i]
			}
		}
	}

	$scope.getProfile = function () {
		$http.post("getprofile/", {
			"user_id": $rootScope.globals.currentUser.user_id
		}, {
				'Content-Type': 'application/json; charset=utf-8'
			})
			.then(
			function (response) {
				$scope.name = response.data.name;
				$scope.email = response.data.email;
				$scope.newName = $scope.name;
				$scope.newEmail = $scope.email;
				$scope.firstG = $scope.getGenreName(response.data.genres[0]);
				$scope.secondG = $scope.getGenreName(response.data.genres[1]);
				$scope.thirdG = $scope.getGenreName(response.data.genres[2]);
			},
			function (response) {
				console.log('Error: ', response)
			});
	}
	$scope.firstG = $scope.genres[0].name


	$scope.updateGenres = function () {
		console.log('genre');
	}

	$scope.updateUser = function () {
		console.log('user');
	}

	$scope.validateEntry = function() {
       if ($scope.newPassword == $scope.confirmedPassword) {
			$http.post("authentication/", {
				"email": $scope.email,
				"password": $scope.currentPasswordUser
			}, {
				'Content-Type': 'application/json; charset=utf-8'
			})
			.then(
			function (response) {
				if (response.data != 'Erro') {
					$scope.updateUser($scope.newName, $scope.newEmail, $scope.newPassword)
				}else {
					$scope.toastMessege('Senha Incorreta');
				}
			},
			function (response) {
				console.log('Error: ', response)
				$scope.toastMessege('Senha Incorreta')
			});
	   }else {
		   $scope.toastMessege('Senhas não combinam')
	   }
    }

	 $scope.clearField = function(fieldID){
        $scope.nameID = document.getElementById(fieldID);
        $scope.nameID.style.borderColor  = '#7d7b7b';
    }

    $scope.invalidateField = function(fieldID){
        $scope.nameID = document.getElementById(fieldID);
        $scope.nameID.style.borderColor  = 'red';
    }

	$scope.validateGenres = function() {
		if ($scope.firstG.id == $scope.secondG.id || $scope.firstG.id == $scope.thirdG.id || $scope.secondG.id == $scope.thirdG.id) {
			if ($scope.firstG.id == $scope.secondG.id && $scope.firstG.id == $scope.thirdG.id && $scope.secondG.id == $scope.thirdG.id) {
				$scope.invalidateField('secondG');
				$scope.invalidateField('thirdG');
				$scope.invalidateField('firstG');
			} else if ($scope.firstG.id == $scope.thirdG.id) {
				$scope.invalidateField('firstG');
				$scope.invalidateField('thirdG');
				$scope.clearField('secondG');
			}else if ($scope.secondG.id == $scope.thirdG.id) {
				$scope.invalidateField('secondG');
				$scope.invalidateField('thirdG');
				$scope.clearField('firstG');
			}else if ($scope.firstG.id == $scope.secondG.id) {
				$scope.invalidateField('firstG');
				$scope.invalidateField('secondG');
				$scope.clearField('thirdG');
			}

		} else {
			$http.post("authentication/", {
				"email": $scope.email,
				"password": $scope.currentPasswordGenre
			}, {
				'Content-Type': 'application/json; charset=utf-8'
			})
			.then(
			function (response) {
				if (response.data != 'Erro') {
					$scope.updateGenres();
				} else {
					$scope.toastMessege('Senha Incorreta')
				}
			},
			function (response) {
				console.log('Error: ', response)
				$scope.toastMessege('Senha Incorreta')
			});
			
		}
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

	$scope.init();
}]);