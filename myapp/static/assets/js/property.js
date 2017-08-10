property_id = ""
$('a.publish').click(function(){
	property_id = this.closest('tr').children[0].textContent;
	bootbox.confirm("Are you sure?", function(result){
		if(result){
			$.post("/property/publish", {"id":property_id}, function(data){
				alert(data.message)
				if(data.status){
					location.href = '/property'
				}
			})
		}
	})
})

$('a.edit').click(function(){
	property_id = this.closest('tr').children[0].textContent;
	location.href = '/property/form?id=' + property_id;
})

$('a.upload-image').click(function(){
	property_id = this.closest('tr').children[0].textContent;
	location.href = '/property/images?id=' + property_id;
})

$('a.preview').click(function(){
	property_id = this.closest('tr').children[0].textContent;
	window.open(
			'/property/preview?id=' + property_id,
			'_blank'
		)
	
})