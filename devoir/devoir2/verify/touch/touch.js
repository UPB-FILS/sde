const fs = require ('fs');

const file = process.argv[2];
const check = process.argv[3];

const referenceDate = Date.now();
console.log (referenceDate);
try{
    let stat = fs.statSync (file);
    let accessTime = stat.atime;
    let modifiedTime = stat.mtime;

    let diffAccess = (referenceDate - accessTime)/1000;
    let diffModify = (referenceDate - modifiedTime)/1000;

    if ((check === 'a') && ((diffAccess < 1) && (diffModify > 2)))
            process.exit (0);
    else if ((check === 'm') && ((diffAccess > 2) && (diffModify < 1)))
        process.exit (0);
    else if ((diffAccess < 1) && (diffModify < 1))
        process.exit (0);
    
    process.exit (1);
}
catch (err){
    console.error (err);
    console.log ('Cannot get file details.');
    process.exit (1);
}