document.addEventListener('DOMContentLoaded', function() {
    console.log('loaded')
    appointments()
});


function appointments() {
    let upcoming = document.getElementById("upcoming-appointments")
    let history = document.getElementById("history-appointments")
    upcoming.addEventListener('click', function() {
        // event.preventDefault();
        get_appointment_values("upcoming-appointments")
    }
    );

    history.addEventListener('click', function() {
        // event.preventDefault();
        get_appointment_values("history-appointments")
    }
    );

}



function get_appointment_values(appointment){
    fetch(`/dashboard/${appointment}`)
    .then(response => {
        return response.json()
    })
    .then(appointments => {
        console.log(appointments);    
    })
    .catch(e => console.log(e))

}


