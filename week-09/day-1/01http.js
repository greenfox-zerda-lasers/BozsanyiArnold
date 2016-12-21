var http = require('http');

var server = http.createServer(function server(req, res) {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end(Date() + req.method + req.url);
});


server.listen(8080, '127.0.0.1');
