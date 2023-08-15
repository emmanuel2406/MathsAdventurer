document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    eventClick: function(info){
        alert(info.event.extendedProps.description);
    }
    });
    fetch('/get_events',{
        method :"GET"
    })
    .then(response => response.json())
    .then(result => {
        var events = JSON.parse(result.events);
        var competitions = JSON.parse(result.competitions);
        var comp_name;
        for (let i = 0; i < events.length; i ++){
            // search competitions for corresponding name
            for (let j = 0; j < competitions.length; j ++){
                if (competitions[j].pk == events[i].fields.competition){
                    comp_name = competitions[j].fields.name;
                }
            }
            let description =  `${comp_name} round ${events[i].fields.round} \n Written ${events[i].fields.written}`
            console.log(description);
            calendar.addEvent({
                title: comp_name,
                allDay: true,
                start: events[i].fields.date,
                description: description
            })
        }
        calendar.render();
    })
    .catch(err => handleError(err))
});

function handleError(err){
    console.log('There is an error:');
    console.log(err);
};