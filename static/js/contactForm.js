function submitForm() {
    const form = document.getElementById('contactForm');
    const formData = new FormData(form);

    fetch('https://emmviron.pythonanywhere.com/api/submit/', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        alert('Form submitted successfully');
        form.reset();
    })
    .catch(error => {
        console.error('There was an error!', error);
        alert('Failed to submit form. Please try again later.');
    });
}
