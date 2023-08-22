<script>
    import { BASE_API_URL } from "$lib/utils/constants";
    import { userData } from "$lib/stores/userStore";
    import axios from 'axios';
    import '@skeletonlabs/skeleton/themes/theme-skeleton.css';
    import '@skeletonlabs/skeleton/styles/skeleton.css';
    import "../app.css";
    axios.defaults.xsrfCookieName = 'csrftoken';
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    axios.interceptors.request.use(config => {
        const token = $userData.token;
        if (token) {
            config.headers.Authorization = `Token ${token}`;
        }
        return config;
    });
</script>

<div>
    <main>
        <slot/>
    </main>
</div>