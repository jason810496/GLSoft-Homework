import axios from 'axios';
import qs from 'qs';

async function storeJWTToken(token) {

}

function isAuthenticated() {
    const token = localStorage.getItem('access_token');
    console.log("isAuth localstorage access_token", token);

    let auth = false;

    let rep = axios.get('http://localhost:5001/whoami',
        {
            headers: { "Authorization": `Bearer ${token}` , "Accept": 'application/json' , "Access-Control-Allow-Origin": '*' }
        }).then((response) => {
            console.log(response);
            if (response.status === 200){
                auth = true;
            }
            auth = true;
        }).catch((err) => {
            console.log(err);
        });

    console.log("isAuth rep", rep);

    console.log("isAuth auth", auth);

    return auth;
}

export { isAuthenticated };