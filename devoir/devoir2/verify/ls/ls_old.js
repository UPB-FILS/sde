const fs = require ('fs');
const _ = require ('lodash');
const path = require ('path');


let dir = process.argv[2];
let outputfile = process.argv[3];



try{
    let output = fs.readFileSync (outputfile);
    let realContents = [];

    if (process.argv[4] === 'r')
    {
        if (process.argv[5] === 'a')
            realContents = readDir (dir, '', true);
        else
            realContents = readDir (dir, '', false);
    }
    else if (process.argv[4] === 'a'){
        realContents = fs.readdirSync (dir);
        realContents.push ('.', '..');
    }
    else{
        realContents = fs.readdirSync (dir);
        _.remove (realContents, function (file){
            return file.charAt(0) === '.';
        })
    }

    console.log (realContents);

    let scriptFiles = output.toString().split('\n');
    _.remove (scriptFiles, function (file){
        return file === '';
    });

    let extraScriptFiles = _.difference (scriptFiles, realContents);
    let minusScriptFiles = _.difference (realContents, scriptFiles);

    if (extraScriptFiles.length != 0){
        console.log ('ls prints extra files/directories: ' + extraScriptFiles);
        process.exit (1);
    }
    else if (minusScriptFiles.length != 0){
        console.log ('ls does not print all files/directories, missing: ' + minusScriptFiles);
        process.exit (1);
    }
}
catch (err){
    console.error (err);
    console.log ('Cannot read files');
    process.exit (1);
}

function readDir (dir, parent, all){
    let output = [];
    let files = fs.readdirSync (dir);
    if (all)
        output.push (parent+'.', parent+'..');
    for (file of files){
        if (all && !/^\./.test(file))
            output.push (parent+file);
        else if (!all)
            output.push (parent+file);
        let stat = fs.statSync (path.join (dir, file));
        if (stat.isDirectory())
            output = output.concat (readDir (path.join(dir, file), parent+file+'/', all));
    }
    return output;
}