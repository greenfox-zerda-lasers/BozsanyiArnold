var express = require('express');

var bodyParser = require('body-parser');

var mysql = require('mysql');

var connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'Kutule0915'
})

var app = express();

app.use(bodyParser.json());

app.get('/todos', function getTodos(req, res) {
  connection.query('SELECT * FROM The_Todos', function(error, rows) {
    if (error) {
      res.send(error.toString());
    }
    res.send(rows);
  });
});

app.get('/todos/:id', function getTodoById(req, res) {
  connection.query('SELECT * FROM The_Todos WHERE id = ' + req.params.id + ';', function(error, row) {
    if (error) {
      res.send(error.toString());
    }
    res.send(row);
  });
});

app.post('/todos', function addATodo(req, res) {
  connection.query('INSERT INTO The_Todos VALUES ('+ req.body.text + ')', function(error, row) {
    if (error) {
      res.send(error.toString());
    }
    res.send(row)
  });
});
