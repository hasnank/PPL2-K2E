/**
 * Created by CXXXV on 09/04/2017.
 */
var initialize_calendar;

initialize_calendar = function(){
    $('.calendar').each(function () {
        var calendar = $(this);
        calendar.fullCalendar({});
    })
};
$(document).on('turbolinks:load', initialize_calendar);