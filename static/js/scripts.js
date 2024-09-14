document.addEventListener('keydown', function(event) {
    if (event.key === 'Tab') {
        event.preventDefault();
        let inputs = document.querySelectorAll('.form-inputs input, button');
        let currentIndex = Array.prototype.indexOf.call(inputs, document.activeElement);
        let nextIndex = (currentIndex + 1) % inputs.length;
        inputs[nextIndex].focus();
    }
});
