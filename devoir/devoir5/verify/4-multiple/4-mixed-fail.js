const axios = require ('axios');
const os = require ('os');

async function post1(){
    const config = {
        baseURL: 'http://localhost:8000/scripts/fail.sh',
        method: 'post',
        headers: {},
    };
    try{
        return await axios (config);
    }
    catch (e){
        return e.response;
    }
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
    const text = 'super cool message'+os.EOL+'super cool person';
    const config = {
        baseURL: 'http://localhost:8000/scripts/test/multiplelines.sh',
        method: 'post',
        headers: {
            'Content-Type': 'text/plain; charset=utf-8',
            'Content-length': text.length},
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
        baseURL: 'http://localhost:8000/scripts/forbidden.sh',
        method: 'get',
    };
    try{
        return await axios (config);
    }
    catch (e){
        return e.response;
    }
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