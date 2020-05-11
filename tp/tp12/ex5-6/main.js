const child_process = require ('child_process');
const fs = require ('fs');

const proc = child_process.spawn ('./script.sh');

proc.stdout.on ('data', function (data){
    console.log (data.toString());
});


fs.readFile ('input', function (err, data){
    if (err){
        proc.stdin.write ('There was an error reading the file');
        proc.stdin.end();
    }
    else{
        proc.stdin.write (data);
        proc.stdin.end();
    }
});