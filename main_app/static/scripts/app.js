console.log("my script is connected")



// document.getElementById('toggle_login').addEventListener('click', 
// function(e){
//     e.preventDefault();
//     console.log('clickedd')
//     document.getElementById('hidden').style.display = 'flex';
//     document.getElementById('login').style.display = "none";
//     document.getElementById('register').style.display = 'flex';
//     document.getElementById('hidden2').style.display="none";
//     })

// document.getElementById('toggle_register').addEventListener('click', 
// function(e){
//     e.preventDefault();
//     console.log('clickedd!')
//     document.getElementById('hidden2').style.display = 'flex';
//     document.getElementById('login').style.display = "flex";
//     document.getElementById('register').style.display = 'none';
//     document.getElementById('hidden').style.display = "none";

//     })


let printButton = document.getElementById('print')
printButton.addEventListener('click', convertToPdf())
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
    


