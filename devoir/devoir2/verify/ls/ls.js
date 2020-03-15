const _ = require ('lodash');
const fs = require ('fs');

const referenceFile = process.argv[2];
const scriptFile = process.argv[3];

try{
    let referenceOutput = fs.readFileSync (referenceFile);
    let reference = referenceOutput.toString().split('\n');
    _.remove (reference, function (file){
        return file === '';
    });

    let scriptOutput = fs.readFileSync (scriptFile);
    let script = scriptOutput.toString().split('\n');
    _.remove (script, function (file){
        return file === '';
    });

    let extraScriptFiles = _.difference (script, reference);
    let minusScriptFiles = _.difference (reference, script);

    if (extraScriptFiles.length != 0){
        console.log ('ls prints extra files/directories');
        process.exit (1);
    }
    else if (minusScriptFiles.length != 0){
        console.log ('ls does not print all files/directories, missing');
        process.exit (1);
    }
}
catch (err){
    console.error (err);
    console.log ('Cannot read files');
    process.exit (1);
}