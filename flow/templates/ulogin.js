//用户登录
function ulogin(){
	//获取用户名和密码,登录成功以后，把用户名存储在session里面，然后显示在首页里面
	var username=$("#uusername").val();
	var password=$("#password").val();
	$.ajax({
		method : 'post',
		url : "http://localhost:8080/LawerSys/user_l.action",
		dataType : "text",
		data : {
			username : username,
			password : password
		},
		success : function(ret) {
			//提示注册成功
			if(ret=="success"){
				//关闭模态框
				 $("#close_lo").click();
				 //把用户名密码存储在session里面，首页显示用户名称
				 localStorage.setItem("username",username);
				 load_data();
			}else{
				alert("用户名或者密码输入错误，请重新输入");
				$("#password").val('');
			}


		},
	})
}