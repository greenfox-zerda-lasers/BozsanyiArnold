var express = require('express');

var bodyParser = require('body-parser');

var mysql = require('mysql');

var cors = require('cors');

var connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'Kutule0915',
  database: 'ToDo'
});

var app = express();

app.use(bodyParser.json());

app.use(cors());


app.get('/todos', function (req, res) {
  connection.query('SELECT * FROM The_Todos', function (error, rows) {
    if (error) {
      res.send(error.toString());
    }
    res.send(rows);
  });
});

app.get('/todos/:id', function getTodoById(req, res) {
  connection.query('SELECT * FROM The_Todos WHERE id = ' + req.params.id, function (error, row) {
    if (error) {
      res.send(error.toString());
    }
    res.send(row);
  });
});

app.post('/todos', function addATodo(req, res) {
  connection.query('INSERT INTO The_Todos (text) VALUES ("' + req.body.text + '")', function (error) {
    if (error) {
      res.send(error.toString());
    }
  });
  connection.query('SELECT * FROM The_Todos ORDER BY id desc LIMIT 1', function (error, row) {
    if (error) {
      res.send(error);
    }
    res.send(row[0]);
  });
});

app.put('/todos/:id', function changeCompleted(req, res) {
  connection.query('UPDATE The_Todos SET completed = NOT completed WHERE id =' + req.params.id, function (error, row) {
    if (error) {
      res.send(error);
    }
    res.send(row);
  });
});

app.delete('/todos/:id', function deleteATodo(req, res) {
  connection.query('SELECT * FROM The_Todos WHERE id =' + req.params.id, function (error, rows) {
    if (error) {
      res.send(error);
    }
    var row = rows[0];
    row.destroyed = true;
    res.send(row);
  });
  connection.query('DELETE FROM The_Todos WHERE id =' + req.params.id, function (error) {
    if (error) {
      res.send(error);
    }
  });
});

// app.filter('todos/completed')

app.listen(3000);
