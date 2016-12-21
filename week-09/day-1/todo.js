var express = require('express');
var bodyParser = require('body-parser');

var app = express();

app.use(bodyParser.json());

var todos = [{ completed: false, id: 1, text: 'Buy milk' },
            { completed: false, id: 2, text: 'Make dinner' },
            { completed: false, id: 3, text: 'Save the world' }];

var currentId = 3;

app.get('/todos', function getTodos(req, res) {
  res.send(todos);
});

app.get('/todos/:id', function getAtodo(req, res) {
  res.send(todos[req.params.id - 1]);
});

app.post('/todos', function postAtodo(req, res) {
  currentId += 1;
  todos.push({ completed: false, id: currentId, text: req.body.text });
  res.send({ completed: false, id: currentId, text: req.body.text });
});

app.put('/todos/:id', function putData(req, res) {
  todos.forEach(function each(e) {
    if (e.id == req.params.id) {
      e.completed = !e.completed;
    }
  });
  res.send(todos);
});

// app.delete('todos/:id', function deleteData(req, res){
//
// });

app.listen(3000);
