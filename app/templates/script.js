$(document).ready(function() {

	$("form").on("submit", function(event) {

		$.ajax({
			data: {
				length: $("#charnum_id").val(),
				symbols: $("#symbols_id").val(),
				numbers: $("#numbers_id").val(),
				lowercase: $("#lowercase_id").val(),
				uppercase: $("#uppercase_id").val(),
				excludeSimilar: $("excludeSimilar_id").val(),
				excludeAmbiguous: $("excludeAmbiguous_id").val()
			},
			type: "POST",
			url: "/generate"
		})
		.done(function(data) {
			if(data.error) {
				$("#password_id").val(data.error);
			}
			else {
				$("#password_id").val(data.password);
			}
		})

		event.preventDefault()
	});
})






// var password = document.getElementById("password")
// var symbols_input = document.getElementById("symbols")
// var numbers_input = document.getElementById("numbers")
// var lowercase_input = document.getElementById("lowercase")
// var uppercase_input = document.getElementById("uppercase")
// var excludeSimilar_input = document.getElementById("excludeSimilar")
// var excludeAmbiguous_input = document.getElementById("excludeAmbiguous")