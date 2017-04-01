var students = [
    {
        sid: '13514068',
        name: 'Garmastewira',
        title: 'Scheduling Using Simulated Annealing',
        status: "failed"
    },
    {
        sid: '13514120',
        name: 'Donald Trump',
        title: 'Using Big Data to Defeat Clinton',
        status: ""
    },
    {
        sid: '13510911',
        name: 'Hillary Clinton',
        title: 'How to Delete E-mails',
        status: "completed"
    },
    {
        sid: '13514105',
        name: 'Painem Jackson',
        title: 'Algorithm XXX Implementation on Agriculture',
        status: ""
    },
    {
        sid: "13513304",
        name: 'Leo Ariesta',
        title: 'Neural Networks in Self Driving Car',
        status: ""
    },
    {
        sid: '13513104',
        name: 'Huwala Umba',
        title: 'XXX using Raspberry Pi',
        status: "completed"
    },
    {
        sid: '13513105',
        name: 'Lala Po',
        title: 'Event-Driven Programming Language',
        status: "completed"
    },
    {
        sid: '13514203',
        name: 'Roth Horowitz',
        title: 'Prediction of Market Using XXX Algorithm',
        status: "failed"
    },
    {
        sid: '13514205',
        name: 'Vina Nadya Putri',
        title: 'Decision Tree Algorithm: YYY',
        status: ""
    }
];

// First time
for (var i = 0; i < students.length; i++) {
    var html = '<li class="mdl-list__item">';
    html += '<span class="mdl-list__item-primary-content">';
    html += '<i class="material-icons" style="margin-right: 15px">person</i>';
    html += students[i].sid + ' - ' + students[i].name;
    html += '</span>';
    html += '<span class="mdl-list__item-secondary-action" style="font-size: 14px">';
    html += '"' + students[i].title + '"';
    html += '</span>';
    if (students[i].status == "completed") {
        html += '<img src="images/completed.png" style="width: 23px; height: 23px; padding-left: 17px;">'
    } else if (students[i].status == "failed") {
        html += '<img src="images/failed.png" style="width: 23px; height: 23px; padding-left: 17px;">'
    } else {
        html += '<i class="material-icons" style="margin-left: 15px">content_copy</i>'
    }
    html += '</li>';
    $('.verification-list').append(html);
}

$('.verification-list > li').click(function() {
    location = "tu-13514068.html";
});

$('#search').bind('input', function() {
    var key = $(this).val();
    $('.verification-list').empty();
    for (var i = 0; i < students.length; i++) {
        if (students[i].sid.indexOf(key) !== -1 || students[i].name.toLowerCase().indexOf(key.toLowerCase()) !== -1) {
            var html = '<li class="mdl-list__item">';
            html += '<span class="mdl-list__item-primary-content">';
            html += '<i class="material-icons" style="margin-right: 15px">person</i>';
            html += students[i].sid + ' - ' + students[i].name;
            html += '</span>';
            html += '<span class="mdl-list__item-secondary-action" style="font-size: 14px">';
            html += '"' + students[i].title + '"';
            html += '</span>';
            if (students[i].status == "completed") {
                html += '<img src="images/completed.png" style="width: 23px; height: 23px; padding-left: 17px;">'
            } else if (students[i].status == "failed") {
                html += '<img src="images/failed.png" style="width: 23px; height: 23px; padding-left: 17px;">'
            } else {
                html += '<i class="material-icons" style="margin-left: 15px">content_copy</i>'
            }
            html += '</li>';
            $('.verification-list').append(html);
        }
    }
    $('.verification-list li').click(function() {
        location = "tu-13514068.html";
    });
});
