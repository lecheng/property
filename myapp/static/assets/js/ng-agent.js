var app = angular.module('agentApp',[])

app.controller('agentController',function($scope, $http){
	$scope.name = $('#name').val();
	$scope.license_num = $('#license_num').val();
	$scope.us_phone = $('#us_phone').val();
	$scope.chinese_phone = $('#chinese_phone').val();
	$scope.wechat = $('#wechat').val();
	$scope.email = $('#email').val();
	$scope.address = $('#address').val();
	$scope.qrcode = $('#qrcode').val();
	$scope.save = function(){
        var params = {
            "license_num":$scope.license_num,
            "us_phone":$scope.us_phone,
            "chinese_phone":$scope.chinese_phone,
            "wechat":$scope.wechat,
            "address":$scope.address,
            "email":$scope.email,
            "agent_name":$scope.name,
            "qrcode":$scope.qrcode
        }
        $http({
            method: "POST",
            url: "http://localhost:5050/agent/save",
            params:params,
        }).success(function(data) {
            alert("Save Successfully!");
            location.href = "/agent/"
        })
        .error(function(){
            alert("Something is wrong!");
        })
    }
})