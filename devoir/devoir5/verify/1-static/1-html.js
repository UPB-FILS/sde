const http = require ('http');

http.get({
    hostname: 'localhost',
    port: 8000,
    path: '/page.html',
    agent: false,
    headers:{},
    }, (res) => {
        console.log (res.headers);
        res.on ('data', (data) => {
            console.log (data.toString ('utf-8'));
        })
});
