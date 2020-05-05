const http = require ('http');
const os = require ('os');

const text = 'super cool message'+os.EOL+'super cool person'

const req = http.request({
    hostname: 'localhost',
    port: 8000,
    path: '/scripts/test/multiplelines.sh',
    agent: false,
    method: 'POST',
    headers:{
        'Content-Type': 'text/plain; charset=utf-8',
        'Content-length': text.length,
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