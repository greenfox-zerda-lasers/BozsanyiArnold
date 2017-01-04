'use strict';

var express = require('express');
var app = express();
var playlists = ['John', 'Betty', 'Hal'];
var bodyParser = require('body-parser');

app.use(bodyParser.json());

app.get('/playlists', function (req, res) {
  res.json(playlists);
});

app.get('/teapot', function (req, res) {
  res.sendStatus(418);
});

app.post('/playlists', function (req, res) {
  res.status(200)
  .json({id: 450, name: "xyz"})
});

app.delete('/playlists/:id', function (req, res) {
  res.status(200)
  res.json({id: req.params.id})
});

app.get('/playlist-tracks', function (req, res) {
  res.sendStatus(200)
});

app.get('/playlist-tracks/:playlist_id', function (err, res) {
  res.sendStatus(200)
});

module.exports = app;
