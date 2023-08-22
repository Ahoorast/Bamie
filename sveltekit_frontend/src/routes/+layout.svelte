<script>
    import { BASE_API_URL } from "$lib/utils/constants";
    import { userData } from "$lib/stores/userStore";
    import axios from 'axios';
    import '@skeletonlabs/skeleton/themes/theme-skeleton.css';
    import '@skeletonlabs/skeleton/styles/skeleton.css';
    import "../app.css";
    import { Toast, toastStore } from '@skeletonlabs/skeleton';
    import { onMount } from "svelte";
    axios.defaults.xsrfCookieName = 'csrftoken';
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    axios.interceptors.request.use(config => {
        const token = $userData.token;
        if (token) {
            config.headers.Authorization = `Token ${token}`;
        }
        return config;
    });
    onMount(() => {
        if (typeof localStorage !== 'undefined') {
            const unsubscribe = userData.subscribe(value => {
                localStorage.setItem('userData', JSON.stringify(value));
            });
        }
    });
</script>

<Toast/>
<div>
    <header>
        {#if $userData?.user?.username}
        <p>logged in as {$userData?.user?.username}</p>
        {/if}
    </header>
    <main>
        <slot/>
    </main>
</div>