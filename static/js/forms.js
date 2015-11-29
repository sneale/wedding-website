$(function() {
	check = function() {
		if ($("#guest")[0].checked) {
			$(".plus_one").show();
		} else {
			$(".plus_one").hide();
		}
	}
	check()
});