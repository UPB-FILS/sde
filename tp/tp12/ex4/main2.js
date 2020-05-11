const child_process = require ('child_process');

const pwd = child_process.spawn ('pwd');

pwd.stdout.on ('data', function (data){
    console.log (data.toString());
});

pwd.on ('exit', function (){
    const ls = child_process.spawn ('ls', ['..']);
    
    ls.stdout.on ('data', function (data){
        console.log (data.toString());
    });
});