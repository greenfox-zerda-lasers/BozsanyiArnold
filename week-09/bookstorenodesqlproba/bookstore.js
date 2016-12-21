var mysql = require('mysql');

var connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'Kutule0915',
  database: 'bookstore'
});

connection.connect(function(error) {
  if (error) {
    console.log('jaaaaaj', error);
  } else {
    console.log('orulok')
  }
});

connection.query('SELECT * FROM publisher;', function(error, rows) {
  if (error) {
    console.log(error.toString());
    return;
  } else {
    console.log('Data recived from DB \n')
    console.log(rows)
  }
})

connection.end();
