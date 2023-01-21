document.addEventListener('DOMContentLoaded', function() {
    console.log('booking appointment')

    let today = formatDate(new Date());
    let selected_date = document.querySelector('#select-date');
    selected_date.value = today; 
    let doc_id = document.querySelector('#doctor_id').innerHTML;

    console.log(doc_id);
    // console.log(document.querySelector('#select-date').value);
    
    selected_date.addEventListener('change', function() {
        console.log(selected_date.value)
        show_times(doc_id, selected_date.value);
    });
});

function formatDate(date_value) {
    let date = new Date(date_value),
        month = '' + (date.getMonth() + 1),
        day = '' + date.getDate(),
        year = date.getFullYear();

    if (month.length < 2) 
        month = '0' + month;
    if (day.length < 2) 
        day = '0' + day;

    return [year, month, day].join('-');
}


function show_times(doc_id, selected_date) {
    fetch(`appointments/${doc_id}/${selected_date}`)
    .then(response => response.json())
    .then(times => {
        console.log(times);
    })
}

 