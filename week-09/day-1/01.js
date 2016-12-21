var express = require('express');

var app = express();

app.get('/', function getApp(req, res) {
  res.send(Date(), req.method, req.url);
});

app.get('*', function getApp(req, res) {
  res.send(Date() + req.method + req.url);
});

app.listen(3000);
