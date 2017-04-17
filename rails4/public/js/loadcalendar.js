$(document).ready(function(){
    $('input[id="personal"]').click(function(){
        if($(this).is(":checked")){
            scheduler.load("./data/personal.xml", function() {
          });
        }
        else if($(this).is(":not(:checked)")){
            
        }
    });
    
    $('input[id="all_schedules"]').click(function(){
        if($(this).is(":checked")){
            scheduler.load("./data/all_schedules.xml", function() {
          });
        }
        else if($(this).is(":not(:checked)")){
            
        }
    });
    
    $('input[id="myschedule"]').click(function(){
        if($(this).is(":checked")){
            scheduler.load("./data/myschedule.xml", function() {
          });
        }
        else if($(this).is(":not(:checked)")){
            
        }
    });
});
