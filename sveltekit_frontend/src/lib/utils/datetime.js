import { userData } from "../stores/userStore";
import { get } from "svelte/store";

export const tokenExpiryDateTimeValidator = () => {
    if (!get(userData).expiry) return;
    const tokenExpiryDateTime = new Date(get(userData).expiry)
    const currentDateTime = new Date();
    if (currentDateTime > tokenExpiryDateTime) {
        userData.update(() => {});
    }
    //console.log("TOKEN " + tokenExpiryDateTime.toString())
    //console.log("CURRENT " + currentDateTime.toString());
};