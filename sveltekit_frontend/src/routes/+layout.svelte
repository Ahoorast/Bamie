<script>
    import { BASE_API_URL } from "$lib/utils/constants";
    import { userData } from "$lib/stores/userStore";
    import axios from 'axios';
    import '@skeletonlabs/skeleton/themes/theme-crimson.css';
    import '@skeletonlabs/skeleton/styles/skeleton.css';
    import "../app.css";
    import { Toast, toastStore } from '@skeletonlabs/skeleton';
    import { onMount } from "svelte";
    import { tokenExpiryDateTimeValidator } from "$lib/utils/datetime";
    import Header from "$lib/components/Header.svelte";
    axios.defaults.xsrfCookieName = 'csrftoken';
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    axios.interceptors.request.use(config => {
        const token = $userData?.token;
        if (token) {
            config.headers.Authorization = `Token ${token}`;
        }
        return config;
    });
    onMount(async () => {
        if (typeof localStorage !== 'undefined') {
            const unsubscribe = userData.subscribe(value => {
                localStorage.setItem('userData', JSON.stringify(value));
            });
        }
        tokenExpiryDateTimeValidator();
    });
</script>

<div>
    <Header/>
    <div class="z-0">
        <Toast/>
    </div>
    <main>
        <slot/>
    </main>
</div>