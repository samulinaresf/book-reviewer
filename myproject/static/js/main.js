function mostrar_resumen() {
    let bookSummary = document.getElementsByClassName('book-summary');
    let bookSummaryButton = document.getElementsByClassName('book-summary-button')
    if(bookSummary.style.display === 'none'){
        bookSummary.style.display = 'block'
        bookSummaryButton.innerHTML = 'Ocultar'
    }else{
        bookSummary.style.display = 'none'
        bookSummaryButton.innerHTML = 'Resumen'}
}

function mostrar_resumen(button) {

    const bookSummary = button.previousElementSibling;

    if (!bookSummary) return;

    const isHidden = window.getComputedStyle(bookSummary).display === 'none';

    if (isHidden) {
        bookSummary.style.display = 'block';
        button.textContent = 'Ocultar';
    } else {
        bookSummary.style.display = 'none';
        button.textContent = 'Descripción ⌵';
    }
}
