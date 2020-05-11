const fs = require ('fs');

//exercise 1
fs.readFile ('names', function (err, data){console.log (data.toString())});
fs.readFile ('shows', function (err, data){console.log (data.toString())});

//exercise 2
fs.readdir ('..', function (err, data){console.log (data);});