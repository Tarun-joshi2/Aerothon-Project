
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
  setInterval(function() {
    
    document.getElementById('main-div').style.display='block';
    document.getElementsByClassName('loader')[0].style.display='none';
  
  }, 2000);
  
  }

function fromsubmit(){
   
  var myDiv = document.getElementById('from-div');
  myDiv.classList.add('hidden');

  document.getElementsByClassName('loader')[0].style.display='block';
 
  shownavbar();
   
}


const data={"DEL":[
        {"dest":"JFK","hours":"14.0"},
        {"dest": "IAD","hours":"15.30"},
        {"dest": "EWR","hours": "14.30"},
        {
          "dest": "ORD",
          "hours": "15.0"
        },
        {
          "dest": "SFO",
          "hours": "15:45"
        },
        {
          "dest": "EWR",
          "hours": "16:30"
        }
    ],
    
   "BoM":[{
      "dest": "EWR",
      "hours": "16.0"
    },
    {
      "dest": "SFO",
      "hours": "16.0"
    },
      {
        "dest": "SFO",
        "hours": "16.0"
      }
    ],
    "BLR":[
      {
        "dest": "SFO",
        "hours": "15.0"
      },

      {
        "dest": "SEA",
        "hours": "17.0"
      }
    ],
      "HYD":[
          {
            "dest": "ORD",
            "hours": "15:45"
          }
        ]
    }


