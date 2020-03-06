const fs = require ('fs');

var args = process.argv.slice(2);

for (let arg of args){
    try {
        if (fs.existsSync(arg)){
            console.log ('Folder to be deleted exists.');
            process.exit (1);
        }
    } catch (err) {
        console.log('Cannot stat files.');
        console.error (err);
        process.exit (1);
    }
      
}