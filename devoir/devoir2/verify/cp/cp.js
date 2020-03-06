const fs = require ('fs');

const sourceFile = process.argv[2];
const destFile = process.argv[3];
try{
    let source = fs.readFileSync (sourceFile);

    try{
        let dest = fs.readFileSync (destFile);
        if (source.toString() !== dest.toString()){
            console.log ('Source and destination file are not the same.');
            process.exit (1);
        }
    }
    catch (err){
        console.error (err);
        console.log ('Destination file does not exist.');
        process.exit (1);
    }
}

catch (err){
    console.error (err);
    console.log ("Cannot read source file. Internal problem.");
    process.exit (1);
}