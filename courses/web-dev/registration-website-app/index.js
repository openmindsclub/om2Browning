//importing the required modules
const express = require('express');
const path = require('path');
const mongoose = require('mongoose'); // mongoose for mongodb 

const User = require('./models/User'); // Import User Model

mongoose.connect('mongodb://localhost/omc_users'); // connect to the local mongodb database called omc_users

const app = express();

app.use(express.json()); // to parse the json data from the request body
app.use(express.static(path.resolve(__dirname, 'client'))); // to serve all the static files from the client folder


// Define the routes
app.post('/register', async (req, res) => { // to handle the post request to the /register route
    const result = await User.findOne({ email: req.body.email }); // find the user with the email provided in the request body
    if(result) {
        //if the email already exists, send back an error
        return res.json({err: true, msg: 'email already exists'});
    }
    
    //if the email doesn't exist, create a new user

    const newUser = new User({ // create a new user object
        firstname: req.body.firstName,
        lastname: req.body.lastName,
        email: req.body.email
    });
    await newUser.save(); // save the new user to the database 
    return res.json({err: false, msg: 'you have succefully registered'}); // send back a success message
});


app.listen(3000, function (){ // start the server on port 3000
    console.log('Server is running on port 3000');
})