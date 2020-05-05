const http = require ('http');

http.get({
    hostname: 'localhost',
    port: 8000,
    path: '/summertime.png',
    agent: false,
    headers:{},
    }, (res) => {
        console.log (res.headers);
        res.on ('data', (data) => {
            console.log (data.toString ('base64'));
        })
});
