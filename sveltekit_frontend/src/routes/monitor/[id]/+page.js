import { detail } from "$lib/utils/api/chatroom";

/** @type {import('./$types').PageLoad} */
export async function load({params}){
	const data = await detail(params.id);
    return {...data};
}