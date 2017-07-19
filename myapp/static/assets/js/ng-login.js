/**
 * Created by chengle on 2017/7/12.
 */
var app = angular.module('loginApp',[])
app.controller('LoginController',function($scope, $http){
    $scope.r_password = "";
    $scope.r_name = "";
    $scope.r_email = "";
    $scope.count = 0;
    $scope.register = function(){
        var params = {
            "password":$scope.r_password,
            "email":$scope.r_email,
            "agent_name":$scope.r_name,
        }
        $http({
            method: "GET",
            url: "http://localhost:5050/register/",
            params:params,
        }).success(function(data) {
            console.log(data);
        })
        .error(function(){
            alert("Something is wrong!");
        })
    }
})