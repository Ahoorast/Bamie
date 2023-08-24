import { userData } from "../../stores/userStore";
import axios from 'axios';
import { BASE_API_URL } from "../constants";
import { success, failure, warning } from "../toasts";
import { goto } from '$app/navigation';

function parseGuidanceTreeFromResponse(data) {
    console.log("HI");
    let position_array = [];
    console.log("HIAY");
    for (let i = 0; i < data.position_array_x_axis.length; i++) {
        position_array.push({
            x: data.position_array_x_axis[i],
            y: data.position_array_y_axis[i],
        });
    }
    console.log(position_array);
    return {
        id: data.id,
        owner: data.owner,
        position_array: position_array,
        example_input_array: data.example_input_array,
        example_output_array: data.example_output_array,
        parent_array: data.parent_array,
    };
}

function parseGuidanceTreeToRequest(data) {
    let position_array_x_axis = [];
    let position_array_y_axis = [];
    let example_input_array = [];
    let example_output_array = [];
    for (let i = 0; i < data.position_array.length; i++) {
        position_array_x_axis.push(data.position_array[i].x);
        position_array_y_axis.push(data.position_array[i].y);
        example_input_array.push(data.example_input_array[i] === ""? " ": data.example_input_array[i]);
        example_output_array.push(data.example_output_array[i] === ""? " ": data.example_output_array[i]);
    }
    return {
        id: data.id,
        owner: data.owner,
        position_array_x_axis: position_array_x_axis,
        position_array_y_axis: position_array_y_axis,
        example_input_array: example_input_array,
        example_output_array: example_output_array,
        parent_array: data.parent_array,
    };
}

export const list = async () => {
    try {
        const url = `${ BASE_API_URL }/guidance_tree/list/`;
        const response = await axios({
            method: 'get',
            url: url,
        });
        return response.data;
    } catch (e) {
        failure("there was an error please try again");
    }
};

export const retrieve = async () => {
    try {
        const url = `${ BASE_API_URL }/guidance_tree/retrieve/`;
        const response = await axios({
            method: 'get',
            url: url,
        });
        return parseGuidanceTreeFromResponse(response.data);
    } catch (e) {
        failure("there was an error please try again");
    }
};

// export const create = async (data) => {
//     try {
//         const url = `${ BASE_API_URL }/guidance_tree/create/`;
//         const response = await axios({
//             method: 'post',
//             url: url,
//             data: parseGuidanceTreeToRequest(data),
//         });
//     } catch (e) {
//         failure("failed to create please try again");
//     }
// };

export const update = async (data) => {
    try {
        const url = `${ BASE_API_URL }/guidance_tree/update/` + data.id + '/';
        const response = await axios({
            method: 'put',
            url: url,
            data: parseGuidanceTreeToRequest(data),
        });
        console.log(response);
    } catch (e) {
        console.log(e);
        failure("failed to save please try again");
    }
};