const express = require ('express');

const app = express();

app.listen(3000, () => console.log('Server running!'));

app.get('/treatment', (req, res) => res.send("You're on treatment"));
