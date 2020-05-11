const child_process = require ('child_process');

child_process.execFile ('pwd', function (err, stdout, stderr){
    if (err){console.log ('pwd execution had an error');}
    console.log ('pwd');
    console.log (stdout);

    child_process.execFile ('ls', ['..'], function (err, stdout, stderr){
        if (err){console.log ('ls execution had an error');}
        console.log ('ls ..');
        console.log (stdout);
    });
});

