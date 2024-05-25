
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





function myFunction(){

  console.log('iiii'+  document.getElementById('formselect'));
  document.getElementById('formselect').style.display='none';

}

