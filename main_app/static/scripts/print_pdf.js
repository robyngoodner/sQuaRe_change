console.log("my script is connected")

let printButton = document.getElementById('print')


function convertToPdf() {
    console.log('function working')
    const pdf_content = document.getElementById('donations')
    pdf_content.style.height='1100px';
    const options = {
        margin: 1,
        filename: 'sQuaRe change donations.pdf',
        image: {type: 'jpeg', quality: 0.98 },
        html2canvas: {scale: 2},thisjsPDF: {unit: 'in', format: 'letter', orientation: 'portrait'}
    }
    html2pdf(pdf_content, options);
}

printButton.addEventListener('click', convertToPdf()) 



