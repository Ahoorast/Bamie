import { userData } from "../../stores/userStore";
import axios from 'axios';
import { BASE_API_URL } from "../constants";
import { success, failure, warning } from "../toasts";
import { goto } from '$app/navigation';

export const list = async () => {
    try {
        const url = `${ BASE_API_URL }/chatroom/list/`;
        const response = await axios({
            method: 'get',
            url: url,
        });
        return response.data;
    } catch (e) {
        failure("there was an error please try again");
    }
};

export const detail = async (id) => {
    try {
        const url = `${ BASE_API_URL }/chatroom/retrieve/` + id + '/';
        const response = await axios({
            method: 'get',
            url: url,
        });
        return response.data;
    } catch (e) {
        failure("there was an error please try again");
    }
};

export const create = async (data) => {
    try {
        const url = `${ BASE_API_URL }/chatroom/create/`;
        const response = await axios({
            method: 'post',
            url: url,
            data: data,
        });
    } catch (e) {
        failure("failed to create a new chatroom please try again");
    }
};

export const push_message = async (data) => {
    try {
        const url = `${ BASE_API_URL }/chatroom/message/`;
        const response = await axios({
            method: 'put',
            url: url,
            data: data,
        });
        success('message was successfully pushed');
        return response.data;
    } catch (e) {
        failure('message failed');
    }
}

export const createPlaygroundChatroom = async () => {
    try {
        const url = `${ BASE_API_URL }/chatroom/create/playground/`;
        const response = await axios({
            method: 'post',
            url: url,
        });
        return response.data;
    } catch (e) {
        failure('failed to create playground chatroom please try again');
    }
}