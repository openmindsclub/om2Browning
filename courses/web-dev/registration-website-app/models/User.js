const mongoose = require('mongoose');

const Schema = mongoose.Schema;

const UserSchema = new Schema({
    firstname: {
        type: String,
        trim: true,
        required: true
    },
    lastname: {
        type: String,
        trim: true,
        required: true
    },
    email: {
        type: String,
        required: true
    }
});

module.exports = mongoose.model('User', UserSchema);