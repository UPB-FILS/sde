const axios = require ('axios');

async function post1(){
    const config = {
        baseURL: 'http://localhost:8000/scripts/test/simple.sh',
        method: 'post',
        headers: {},
    };
    return await axios (config);
}

async function post2 (){
    const text = 'msg';
    const config = {
        baseURL: 'http://localhost:8000/scripts/read.sh',
        method: 'post',
        headers: {
            'Content-Type': 'text/plain; charset=utf-8',
            'Content-length': text.length},
        data: text
    };
    return await axios (config);
}

async function post3 (){
    const text = 'super cool message';
    const config = {
        baseURL: 'http://localhost:8000/scripts/readenv.sh',
        method: 'post',
        headers: {
            'Content-Type': 'text/plain; charset=utf-8',
            'Content-length': text.length,
            'usr': 'a foreign land.'},
        data: text
    };
    return await axios (config);
}

async function get1 (){
    const config = {
        baseURL: 'http://localhost:8000/scripts/test/simple.sh',
        method: 'get',
    };
    return await axios (config);
}

async function get2 (){
    const config = {
        baseURL: 'http://localhost:8000/scripts/simple.sh',
        method: 'get',
    };
    return await axios (config);
}

async function get3 (){
    const config = {
        baseURL: 'http://localhost:8000/scripts/env.sh',
        method: 'get',
        headers:{
            msg: 'Hello',
            usr: 'a friend'
        },
    };
    return await axios (config);
}

async function main ()
{

    try{
        const responses = await Promise.all ([get1(), get2(), get3(), post1(), post2(), post3()]);
        let data = '';
        for (let res of responses){
            data = data + res.status + '\n' + res.statusText + '\n' + JSON.stringify (res.headers) + '\n' + res.data + '\n';     
        }
        console.log (data);
    }
    catch (e){
        console.log ('error');
        console.log (e);
    }

}

main ();