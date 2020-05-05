const http = require ('http');

const text = 'super cool message';

const req = http.request({
    hostname: 'localhost',
    port: 8000,
    path: '/scripts/readnoheader.sh',
    agent: false,
    method: 'POST',
    headers:{
        'Content-Type': 'text/plain; charset=utf-8',
        'Content-length': text.length,
        'usr': 'a smart user'
        }
    }, (res) => {
        console.log (res.statusCode);
        console.log (res.statusMessage);
        console.log (res.headers);
        res.on ('data', (data) => {
            console.log (data.toString ('utf-8'));
        });
});
req.write (text);
req.end ();