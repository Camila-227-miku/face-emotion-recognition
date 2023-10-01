$(function(){
	$('#btnRegister').click(function(){		
		$.ajax({
			url: '/registerPerson',
			data: $('form').serialize(),
			type: 'POST',
			success: function(responseService){
				var response = JSON.parse(responseService);
				console.log("success", response, response.code);
				if(response.code == 'success'){
					if(confirm(response.message)){
						window.location.href = "/";
					}					
				}
				else{
					alert("Error al crear persona " + response.error)
				}
			},
			error: function(error){
				console.log("error", error);
				alert("Error al crear la persona " + error)
			}
		});
	});
});
