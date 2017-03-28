$(document).ready(function() {
	$("#p2").hide();
});

function loading() {
	$("#p2").show();
	setTimeout(function() { window.location='tu-calendar.html';}, 3000);
}

function fillDetails() {
	$('#final-project').val("Event-Driven Programming with XXX");
	$('#topic').val("Programming");
	$('#supervisor').val("Riza Satria Perdana");
}

function assignExaminers() {
	$('#examiner1').val("Yudhis");
	$('#examiner2').val("Inge");
	$('#examiner3').val("Masayu");
}
