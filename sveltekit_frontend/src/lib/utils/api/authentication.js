import { userData } from "../../stores/userStore";
import axios from 'axios';
import { BASE_API_URL } from "../constants";

export const signup = async (data) => {
    try {
        const url = BASE_API_URL + '/signup/';
        const response = await axios({
            method: 'post',
            url: url,
            data: data,
        });
    } catch (e) {
        
    }
}

export const login = async (data) => {
    try {
        const url = `${ BASE_API_URL }/login/`;
        const response = await axios({
            method: 'post',
            url: url,
            data: data,
        });
        userData.update(() => response.data);
    } catch (e) {
        
    }
}

export const logout = async () => {
    try {    
        const url = `${ BASE_API_URL }/logout/`;
        const response = await axios({
            method: 'post',
            url: url,
        });
        console.log(response);
    } catch (e) {
    }
}