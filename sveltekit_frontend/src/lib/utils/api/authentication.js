import { userData } from "../../stores/userStore";
import axios from 'axios';
import { BASE_API_URL } from "../constants";
import { success, failure, warning } from "../toasts";
import { goto } from '$app/navigation';

export const signup = async (data) => {
    try {
        const url = BASE_API_URL + '/signup/';
        const response = await axios({
            method: 'post',
            url: url,
            data: data,
        });
        success('you have successfully signed up');
        goto('/login');
    } catch (e) {
        const errors = e.response.data.messages;
        errors.forEach((e) => {
            failure(e);
        });
    }
};

export const login = async (data) => {
    try {
        const url = `${ BASE_API_URL }/login/`;
        const response = await axios({
            method: 'post',
            url: url,
            data: data,
        });
        userData.update(() => response.data);
        console.log(response.data);
        success('you have successfully logged in');
    } catch (e) {
        console.log(e);
        failure('login failed check your username and password');
    }
};

export const logout = async () => {
    try {    
        const url = `${ BASE_API_URL }/logout/`;
        const response = await axios({
            method: 'post',
            url: url,
        });
        success('you have successfully logged out');
        userData.update(() => {});
    } catch (e) {
        failure('logout failed');
    }
};