$(document).ready(function() {
	$('.category').click(function() {
		alert("helo how can i be of help");
		$.ajax({
			url: "localhost:5000/api/v0/categories",
			type: 'GET'
			success: function(data) {
				console.log(data)
			},
			failure: function(message) {
				console.log(message);
			}
		});
	});
});

