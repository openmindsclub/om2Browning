const firstName = document.getElementById('firstname'); // Get the first name input
const lastName = document.getElementById('lastname'); // Get the last name input
const email = document.getElementById('email'); // Get the email input

const button = document.getElementById('submit');   // Get the submit button


button.addEventListener('click', handleSubmit); // Add an event listener to the submit button

function handleSubmit(event){  // Function that handles the submit event
    event.preventDefault(); //to prevent the default action ( the default action will submit the form refresh the page)

    const data = { // Create an object to store the data
        firstName: firstName.value,
        lastName: lastName.value,
        email: email.value
    }

    const body = JSON.stringify(data); // Convert the object to a JSON string to send it to the server 

    const url = "http://localhost:3000/register";

    const options = {
        method: 'POST', // The method to use
        headers: { // The headers of the request containing the content type
            'Content-Type': 'application/json'
        },
        body: body // The body of the request containing the JSON string of the data
    }
    
    fetch(url, options) // Send the data to the server
    .then(function(response){ // Waits for the response from the server and convert it to JSON and return it
        return response.json();
    })
    .then(function(data){ //take the json data of the response and display it

        const msg = document.getElementById('msg'); // Get the message element
        msg.innerHTML = data.msg; // display the message from the server inside the message element

        if(data.err === false) { // clear the form if the registration was successful
            firstName.value = '';
            lastName.value = '';
            email.value = '';
        }
    });
}