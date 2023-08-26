<script>
    import { login } from "$lib/utils/api/authentication";
    import WaitingButton from "./WaitingButton.svelte";
    let data = {
        username: undefined,
        password: undefined,
    }
    let login_promise;
    function handleLogin() {
        login_promise = login(data);
    }
</script>
<div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
    <div class="w-full bg-white rounded-lg shadow md:mt-0 sm:max-w-md xl:p-0 gap-y-4">
        <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
            <div>
                <span>username</span>
                <input bind:value={data.username} class="input" type="text" placeholder="username"/>
            </div>
            <div>
                <span>password</span>
                <input bind:value={data.password} class="input" type="password" placeholder="••••••••"/>
            </div>
            {#await login_promise}
            <WaitingButton/>
            {:then}
            <button on:click={handleLogin} type="button" class="btn variant-filled">Login</button>
            {/await}
        </div>
    </div>
</div>
