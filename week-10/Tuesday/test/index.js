'use strict';

var test = require('tape');
var request = require('supertest');
var app = require('../server');

test('Playlists returned', function (t) {
  request(app)
    .get('/playlists')
    .expect('Content-Type', /json/)
    .expect(200)
    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();
    });
});

test('404 on lobab', function (t) {
  request(app)
    .get('/lobab')
    .expect(404)
    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();
    });
});

test('teapot', function (t) {
  request(app)
    .get('/teapot')
    .expect(418)
    .end(function (err, res) {
      t.error(err, 'No error');
      t.end();
    });
});

test('posting', function (t) {
  request(app)
  .post('/playlists')
  .type('json')
  .send({name: "xyz"})
  .expect(200)
  .end(function (err, res) {
    t.error(err, 'No error');
    t.end();
  });
});

test('wrong-deleting', function (t) {
  request(app)
  .delete('/playlists')
  .expect(404)
  .end(function (err, res) {
    t.error(err, 'No error');
    t.end();
  });
});

test('succesfull-delete', function (t) {
  request(app)
  .delete('/playlists/:id')
  .expect(200)
  .end(function (err, res) {
    t.error(err, 'No error');
    t.end();
  });
});

test('gettracks', function (t) {
  request(app)
  .get('/playlist-tracks')
  .expect(200)
  .end(function (err, res) {
    t.error(err, 'No error');
    t.end();
  });
});

test('getsingletrack', function (t) {
  request(app)
  .get('/playlist-tracks/:playlist_id')
  .expect(200)
  .end(function (err, res) {
    t.error(err, 'No error');
    t.end();
  });
});
