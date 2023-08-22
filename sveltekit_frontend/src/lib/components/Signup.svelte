<script>
    import { signup } from "$lib/utils/api/authentication";
    import { failure } from "$lib/utils/toasts";
    let data = {
        username: undefined,
        email: undefined,
        password: undefined,
    }
    let password;
    function handleSignup() {
        if (data.password !== password) {
            failure("passwords don't match");
        }
        else {
            signup(data);
        }
    }
</script>
<div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
    <div class="w-full bg-white rounded-lg shadow md:mt-0 sm:max-w-md xl:p-0 gap-y-4">
        <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
            <div>
                <span>username</span>
                <input bind:value={data.username} class="input" title="username" type="text" placeholder="username"/>
                
            </div>
            <div>
                <span>email</span>
                <input bind:value={data.email} class="input" title="email" type="email" placeholder="john@example.com" autocomplete="email"/>
            </div>
            <div>
                <span>password</span>
                <input bind:value={data.password} class="input" title="password" type="password" placeholder="••••••••"/>
            </div>
            <div>
                <span>repeat password</span>
                <input bind:value={password} class="input" title="password" type="password" placeholder="••••••••"/>
            </div>
            <button on:click={handleSignup} type="button" class="btn variant-filled">Signup</button>
        </div>
    </div>
</div>
