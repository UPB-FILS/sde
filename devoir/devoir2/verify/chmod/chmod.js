const fs = require ('fs');

const file = process.argv[2];
const permissions = process.argv[3];

try{
    let stat = fs.statSync (file);
    let perm = ((stat.mode & parseInt ('777', 8)).toString(8));
    if (permissions === perm)
        process.exit (0);
    process.exit (1);
}
catch (err){
    console.error (err);
    console.log ('Cannot get file details.');
    process.exit (1);
}