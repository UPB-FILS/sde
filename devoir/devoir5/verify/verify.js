const child_process = require ('child_process');
const fs = require ('fs');

const testFile = process.argv[2];

const server = child_process.spawn ('node',['index.js']);

server.stdout.on ('data', (data)=>{
    console.log (data.toString('utf-8'));
});

setTimeout (()=>{
    let output = '';
    const req = child_process.spawn ('node', [testFile]);
    req.stdout.on ('data', (data)=>{
        output = output + data;
    });

    req.on ('exit', ()=>{
        server.kill ('SIGKILL');
        fs.writeFileSync ('output/'+testFile.split('/').pop(), output);
    });
}, 2000);