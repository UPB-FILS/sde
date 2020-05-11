const fs = require ('fs');

fs.writeFile ('myFile', 'my message', function (err){
  if (err){
    console.log ('There was an error writing the first file');
  }
  else{
    fs.writeFile ('mySecondFile', 'my second message', function (err){
        if (err){
            console.log ('There was an error writing the second file');
        }
        else{
            fs.readFile ('myFile', function (err, data){
                if (err){
                    console.log ('There was an error reading the first file');
                }
                else{
                    console.log (data.toString());
                }
            });
            fs.readFile ('mySecondFile', function (err, data){
                if (err){
                    console.log ('There was an error reading the second file');
                }
                else{
                    console.log (data.toString());
                }
            });
            fs.readdir('.', function (err, data){
                if (err){
                    console.log ('There was a problem reading the dir.');
                }
                else{
                    console.log (data);
                }
            });
        }
    });
  }
});