// STARTER CODE
for (var i = 2; i <= 4; i++) {
    $("#log" + i).hide();
}

function changeLog(id, logTitle) {
    for (var i = 1; i <= 4; i++) {
        $("#list" + i).removeClass("verification-selected");
    }
    $("#list" + id).addClass("verification-selected");
    var selected = $("#log" + id).css('display') != 'none';
    for (var i = 1; i <= 4; i++) {
        if (id != i) {
            $("#log" + i).hide();
        }
    }
    if (!selected) {
        $("#log" + id).fadeIn();
    }
    $("#log-title").text("LOG " + logTitle);
}
