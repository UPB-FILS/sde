const fs = require ('fs');

var args = process.argv.slice(2);

for (let arg of args){
    try {
        fs.accessSync(arg);
        process.exit (0);
    } catch (err) {
        console.log('Directory ' + arg + ' does not exist.');
        console.error (err);
        process.exit (1);
    }
      
}