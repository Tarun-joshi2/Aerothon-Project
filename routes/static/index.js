
function getinfo(){


var myHeaders = new Headers();
myHeaders.append("X-API-Key", "a18ab1f2924d45698703419889");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.checkwx.com/metar/lat/40.72/lon/-73.99/decoded", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));

}

console.log('function call');

const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});



function shownavbar(){
  console.log('function call');
  setInterval(function() {
    

    document.getElementById('from-div').style.display='block';
    document.getElementById('main-div').style.display='block';
    document.getElementById('formselect').style.display='block';
    
    document.getElementsByClassName('loader')[0].style.display='none';
  
  }, 2000);
  
  }

function fromsubmit(){
  console.log('function call');
  var myDiv = document.getElementById('from-div');
  myDiv.classList.add('hidden');

  document.getElementsByClassName('loader')[0].style.display='block';

  document.getElementById('formselect').style.display='none';
 


 
  shownavbar();
   
}


