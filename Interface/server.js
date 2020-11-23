const express = require('express');
const rutas = require('./src/routes/routes');
const app = express();
app.use(express.static("public"));
const PORT =8080;

// Routes
app.use('/', rutas );

// Starting server
app.listen( PORT, () => {
    console.log( 'Sever on port ', PORT);
})