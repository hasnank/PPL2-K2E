$(document).ready(function () {
    $(".status-undo").hide();
    
    $(".btn-confirm").click(function() {
        $("tr").has(this).animate({backgroundColor: "#8cff66"});
        $(".status-opt").has(this).siblings(".status-undo").children(".result").html("<b>CONFIRMED</b>");
         $(".status-opt").has(this).fadeOut();
         $(".status-opt").has(this).siblings(".status-undo").delay(500).fadeIn();
    });
    
    $(".btn-reject").click(function() {
        $("tr").has(this).animate({backgroundColor: "#ff8080"});
         $(".status-opt").has(this).siblings(".status-undo").children(".result").html("<b>REJECTED</b>");
         $(".status-opt").has(this).fadeOut();
         $(".status-opt").has(this).siblings(".status-undo").delay(500).fadeIn();
    });
    
    $(".undo").click(function() {
        $("tr").has(this).animate({backgroundColor: "#fff"});
        $(".status-undo").has(this).fadeOut();
        $(".status-undo").has(this).siblings(".status-opt").delay(500).fadeIn();
    });
    
    $(".status-close").click(function() {
        $("tr").has(this).fadeOut();
    });
});