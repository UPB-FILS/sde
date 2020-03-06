const fs = require ('fs');

let dir = process.argv[2];

try{    
   files = fs.readdirSync (dir);
   for (file of files){
        if (!/^\./.test(file))
            console.log (file);
    }
}
catch (err){
    console.error (err);
    process.exit (1);
}