import axios from 'axios';
import qs from 'qs';

async function storeJWTToken(token) {

}

function isAuthenticated() {
    const token = localStorage.getItem('access_token');
    console.log("isAuth localstorage access_token", token);

    // axios.get('http://localhost:5001/whoami',
    //     {
    //         headers: { "Authorization": `Bearer ${token}` }
    //     }).then((response) => {
    //         console.log(response);
    //     }).catch((err) => {
    //         console.log(err);
    //     });

    // const payload = { 'access_token': token };
    // axios.post('http://localhost:5001/verify', token , { headers: { 'content-type': 'application/json' } }  )
    // .then((response) => {
    //     console.log("check jwt post");
    //     console.log(response);
    // }).catch((err) => {
    //     console.log(err);
    // });

    let auth = false;

    axios.get('http://localhost:5001/whoami',
        {
            headers: { "Authorization": `Bearer ${token}` , "Accept": 'application/json' , "Access-Control-Allow-Origin": '*' }
        }).then((response) => {
            console.log(response);
            auth = true;
        }).catch((err) => {
            console.log(err);
        });

    // const whoami = axios({
    //     method: 'GET',
    //     url: 'http://0.0.0.0:5001/verify',
    //     responseType: 'json', // responseType 也可以寫在 header 裡面
    //     headers: {
    //         Authorization: `Bearer ${token}` ,
    //         Accept: 'application/json',
    //         'Access-Control-Allow-Origin': '*',
    //     }
    // })
    // .then(function (response) {
    //     console.log("isAuth whoami response", response);
    // })
    // .catch(function (error) {
    //     console.log(error);
    // });

    return auth;
}

export { isAuthenticated };