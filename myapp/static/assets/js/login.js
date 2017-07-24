$('#register-button').click(function(){
	pwd = $('#r_password').val();
	pwd_confirm = $('#r_password_confirm').val();
	if(pwd == pwd_confirm){
		$('#registerForm').submit();
	}
	else{
		alert('Please confirm your password correctly!')
		pwd_confirm = $('#r_password_confirm').val("");
	}
})