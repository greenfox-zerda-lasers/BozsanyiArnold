var express = require('express');

var exampleApp = express();

exampleApp.get('/', function getApp(request, response) {
  response.send('hellobello');
});

exampleApp.post('/', function postApp(request, response) {
  response.send('posted nigga');
});

exampleApp.listen(3000);
