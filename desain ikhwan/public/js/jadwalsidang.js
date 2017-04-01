$(document).ready(function () {
    $(".date-list > a").click(function() {
        $(".selected").removeClass("selected");
        $(this).addClass("selected");
        
        if ($(this).hasClass("date2")) {
            $(".exam-desc-cell-8 > .date1").addClass("hidden");
            $(".exam-desc-cell-8 > .date2").removeClass("hidden");
        } else {
            $(".exam-desc-cell-8 > .date2").addClass("hidden");
            $(".exam-desc-cell-8 > .date1").removeClass("hidden");
        }
    });
});