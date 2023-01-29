document.addEventListener('DOMContentLoaded', function() {
    console.log('loaded')
    document.querySelector('#spa-results').style.display = 'none';
    select_appointment_type()   
});


function select_appointment_type() {
    let upcoming = document.getElementById("upcoming-appointments")
    let history = document.getElementById("history-appointments")
    
    upcoming.addEventListener('click', function() {
            document.querySelector('#search-results').style.display = 'none';
            document.querySelector('#spa-results').style.display = 'block';
            upcoming.style.color = 'white';
            upcoming.style.backgroundColor = '#F39530';
            upcoming.style.padding = "10px 10px 10px 10px";
            upcoming.style.borderRadius = '5px'
            history.style.backgroundColor = null;
            history.style.color = 'black';
            get_appointment_values("upcoming-appointments")
        });

    history.addEventListener('click', function() {
            document.querySelector('#search-results').style.display = 'none';
            document.querySelector('#spa-results').style.display = 'block';
            history.style.color = 'white';
            history.style.backgroundColor = '#F39530';
            history.style.padding = "10px 10px 10px 10px";
            history.style.borderRadius = '5px'
            upcoming.style.backgroundColor = null;
            upcoming.style.color = 'black';
            get_appointment_values("history-appointments")
        });
}

function get_appointment_values(appointment){
    fetch(`/dashboard/${appointment}`)
    .then(response => {
        return response.json()
    })
    .then(appointments => {
        appointments.forEach(appointment => {
            let element = document.createElement('div');
            element.setAttribute("class", "element");
            element.setAttribute('id', `${appointment.id}`)
            // element.id = appointment.id;
            appoint_container = `
                <div class="search-results">
                    <div class="info">
                        <span class=""><strong>Patient's Name: </strong> ${appointment.patient}</span>
                    </div>
                    <div class="info">
                        <span class=""><strong>Doctor's Name: </strong></span>${appointment.doctor}
                    </div>
                    <div class="info">
                        <span class=""><strong>Appointment Date: </strong> </span>${appointment.appointment_date}
                    </div>
                    <div class="info">
                        <span class=""><strong>Time: </strong> </span>${appointment.appointment_time}
                    </div>
                </div>
            `
            element.innerHTML = appoint_container;
            element.addEventListener('click', function() {
                // console.log(appointment.report);
                    if (appointment.report !== null ){
                        let report_element = document.createElement('div');
                        report_element.setAttribute("class", "element");
                        report_element.id = `report-${appointment.id}`
                        report_container = `
                            <div>
                                <div class="report-result">
                                    <div class="info">
                                        <span class=""><strong>Report for </strong> ${appointment.patient}</span>
                                    </div>
                                    <div class="info">
                                        <span class=""><strong>Doctor's Name: </strong></span>${appointment.doctor}
                                    </div>
                                    <div class="info">
                                        <span class=""><strong>Appointment Date: </strong> </span>${appointment.appointment_date}
                                    </div>
                                    <div class="info">
                                        <span class=""><strong>Time: </strong> </span>${appointment.appointment_time}
                                    </div>
                                    <div class="">
                                        <textarea class="form-control" rows="3" readonly>${appointment.report}</textarea>
                                    </div>
                                </div>
                            </div>
                        `
                        element.innerHTML = report_container;
                    }
                    else {
                        alert("No reports found!");
                    }
                })
            document.querySelector('#spa-results').appendChild(element);
        });
        // console.log(appointments);   
    })
    .catch(e => console.log(e))
    document.querySelector('#spa-results').innerHTML='';
}

