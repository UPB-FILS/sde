const fs = require ('fs');

if (process.argv[2] === 'sym'){
    const source = process.argv[3];
    const dest = process.argv[4];

    try{
       // let sourceStat = fs.lstatSync (source);
        let destStat = fs.lstatSync (dest);
        if (destStat.isSymbolicLink()){
            if (fs.readlinkSync (dest) !== source){
                console.log ('Link file does not point to correct source file.');
                process.exit (1);
            }
        }
        else{
            console.log ('Target file is not link.');
            process.exit (1)
        }
    }
    catch (err){
        console.log ('Cannot read file information');
        console.error (err);
        process.exit (1);
    }
}
else{
    const source = process.argv[2];
    const dest = process.argv[3];

    try{
        let sourceStat = fs.statSync (source);
        let destStat = fs.statSync (dest);

        if (sourceStat.ino !== destStat.ino){
            console.log ('Link does not exist.');
            process.exit (1);
        }
    }
    catch (err){
        console.log ('Cannot read file information');
        console.error (err);
        process.exit (1);
    }
}