const http = require ('http');

const req = http.request({
    hostname: 'localhost',
    port: 8000,
    path: '/scripts/simple.sh',
    agent: false,
    headers:{},
    method: 'POST'
    }, (res) => {
        console.log (res.statusCode);
        console.log (res.statusMessage);
        console.log (res.headers);
        res.on ('data', (data) => {
            console.log (data.toString ('utf-8'));
        });
});

req.end();