const fs = require ('fs');

fs.readFile ('inexistentFile', function (err, data){
    if (err){
        console.log ('Full error');
        console.log (err);

        console.log ('error code');
        console.log (err.code);
    }
});