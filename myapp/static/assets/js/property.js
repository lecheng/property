property_id = ""
$('a.delete').click(function(){
	property_id = this.closest('tr').children[0].textContent;
	bootbox.confirm("Are you sure?", function(result){
		if(result){
			$.post("/property/delete", {"id":property_id}, function(data){
				alert(data.message);
				location.href = '/property';
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
})

$('#upload-submit').click(function(){
	var action = '/property/upload?id=' + property_id;
	$('#upload-form').attr('action',action).submit();
})

$('a.preview').click(function(){
	property_id = this.closest('tr').children[0].textContent;
	window.open(
			'/property/preview?id=' + property_id,
			'_blank'
		)
	
})