document.addEventListener('DOMContentLoaded', function () {
    const jobOpeningsContainer = document.getElementById('jobOpeningsContainer');

    fetch('https://emmviron.pythonanywhere.com/api/jobs/')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Process the data and update the HTML
            data.forEach(job => {
                const jobElement = document.createElement('div');
                jobElement.innerHTML = `
                    <div style="" class="job_modal_btn" data-toggle="modal" onclick="showForm()" data-target="#exampleModalLong${job.id}">
                    <div class="ob_modal_btn_txt">${job.name}</div> <img src="https://ik.imagekit.io/s3jkgwyie/Business%20and%20Sales%20Manager.png?updatedAt=1704555706468">
                    </div>

                    <div class="modal fade" id="exampleModalLong${job.id}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLongTitle" aria-hidden="true">
                        <div class="modal-dialog" role="document">
                        <div class="modal-content">
                            <div class="modal-header">
                            <h5 class="modal-title" id="exampleModalLongTitle">${job.name}</h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                            </button>
                            </div>
                            <div class="modal-body">
                                <p>${job.job_description}</p>
                                <p style="font-weight: bolder;">Duties, Responsibilities, & Functions:</p>
                                <ul>${job.duties.split('\n').map(item => `<li>${item.trim()}</li>`).join('')}</ul>
                                <p style="font-weight: bolder;">Qualifications:</p>
                                <ul>${job.qualification.split('\n').map(item => `<li>${item.trim()}</li>`).join('')}</ul>
                                <p><span style="font-weight: bolder;">Salary:</span> ${job.salary}</p>
                                

                            </div>
                            <div class="modal-footer d-flex justify-center" style="gap: 15px; justify-content:center;">
                            <button type="button" onclick="hideForm()" class="btn btn-danger px-5" data-dismiss="modal">Not interested <i class="fa-solid fa-rectangle-xmark"></i></button>
                            <a href="#application_form" onclick="RevealForm()" class="btn btn-primary px-5" data-dismiss="modal">Apply <i class="fa-solid fa-arrow-right-from-bracket"></i></a>
                            </div>
                        </div>
                        </div>
                    </div>
                `;
                jobOpeningsContainer.appendChild(jobElement);
            });
        })
        .catch(error => console.error('Error fetching job openings:', error));
});

const form = document.getElementById('application_form');

function showForm(){
    form.classList.remove('d-none');
}

function RevealForm() {

    form.scrollIntoView({
        behavior: 'smooth',
        block: 'start' 
    });
    form.classList.remove('d-none');
    alert('Please fill the form below correctly and our recruitment team will get back to you shortly.');

}

function hideForm() {
    form.classList.add('d-none');
}








// backup

// document.addEventListener('DOMContentLoaded', function () {
//     const jobOpeningsContainer = document.getElementById('jobOpeningsContainer');

//     fetch('http://127.0.0.1:8000/api/jobs/')
//         .then(response => {
//             if (!response.ok) {
//                 throw new Error('Network response was not ok');
//             }
//             return response.json();
//         })
//         .then(data => {
//             // Process the data and update the HTML
//             data.forEach(job => {
//                 const jobElement = document.createElement('div');
//                 jobElement.innerHTML = `
//                     <p class="btn btn-secondary">${job.name}</p>
//                     <p>${job.job_description}</p>
//                     <p>Qualifications:</p>
//                     <ul>${job.qualification.split('\n').map(item => `<li>${item.trim()}</li>`).join('')}</ul>
//                 `;
//                 jobOpeningsContainer.appendChild(jobElement);
//             });
//         })
//         .catch(error => console.error('Error fetching job openings:', error));
// });



