const http = require ('http');

http.get({
    hostname: 'localhost',
    port: 8000,
    path: '/scripts/fail.sh',
    agent: false,
    headers:{
        msg: 'super message',
        usr: 'a super student'
    },
    }, (res) => {
        console.log (res.statusCode);
        console.log (res.statusMessage);
        console.log (res.headers);
        res.on ('data', (data) => {
            console.log (data.toString ('utf-8'));
        });
});