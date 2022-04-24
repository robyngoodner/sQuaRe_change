console.log("my script is connected")



document.getElementById('toggle_login').addEventListener('click', 
function(e){
    e.preventDefault();
    console.log('clickedd')
    document.getElementById('hidden').style.display = 'flex';
    document.getElementById('login').style.display = "none";
    document.getElementById('register').style.display = 'flex';
    document.getElementById('hidden2').style.display="none";
    })

document.getElementById('toggle_register').addEventListener('click', 
function(e){
    e.preventDefault();
    console.log('clickedd!')
    document.getElementById('hidden2').style.display = 'flex';
    document.getElementById('login').style.display = "flex";
    document.getElementById('register').style.display = 'none';
    document.getElementById('hidden').style.display = "none";

    })




