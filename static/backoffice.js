$(document).ready(function() {
		$("#add-field").on("click", function() {
			$("#more").append("<div class='form-group mb-3'><input name='ingrediente' type='text' >&nbsp;<input name='quantita' type='text' >&nbsp;<input  name='misura' type='text' >&nbsp;<input  name='componente' type='text' ></div>");
		});
		$("#remove-field").on("click", function() {
			$("#more").children().last().remove();
		});

});

