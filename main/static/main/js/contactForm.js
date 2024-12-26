document.addEventListener("DOMContentLoaded", function () {
    const modalOverlay = document.getElementById('modal-overlay');
    const closeButton = document.getElementById('close-button');

    if (modalOverlay) {
        modalOverlay.style.display = 'flex';

        const closeModal = () => {
            modalOverlay.style.display = 'none';
        };

        closeButton.addEventListener('click', closeModal);
        modalOverlay.addEventListener('click', (e) => {
            if (e.target === modalOverlay) closeModal();
        });

        setTimeout(closeModal, 5000);
    }
});