var express = require('express');

var bodyParser = require('body-parser');

var app = express();

app.use(bodyParser.json());

app.get('/todos', function getTodos(req, res) {
  connection.query('Select * FROM The_Todos', function(error, rows) {
    if (error) {
      console.log(error.toString());
    }
    res.send(rows);
  });
});
