const child_process = require ('child_process');
const fs = require ('fs');

const proc = child_process.spawn ('./script.sh');

proc.stdout.on ('data', function (data) {
    process.stdout.write (data.toString());
});

proc.on ('error', function (err) {
    // console.log (err);
    console.log ('Cannot run script');
});

proc.on ('close', function (exitcode) {
    console.log (exitcode);
});

// const proc = child_process.exec ('./script.sh', function (err, stdout, stderr) {
//     if (err) console.log ('Error '+err.message);
//     console.log (stdout);
// });

// fs.readFile ('input', function (err, data){
//     if (err){
//         console.log ('There was an error reading the file');
//     }
//     else{
//         console.log (data);
//     }
//     //
// });

// fs.readFile ('input2', function (err, data){
//     if (err){
//         console.log ('There was an error reading the file');
//     }
//     else{
//         console.log (data);
//     }
//     //
// });


// console.log ('reading file');

/*
// event loop
while (has_callbacks ()) {
    let callback = wait_for_callback ();
    callback (...);
}
*/