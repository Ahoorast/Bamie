<script>
    import { userData } from "$lib/stores/userStore";
    import { logout } from "../utils/api/authentication";
    let username;
    let is_slidebar_open = false;
    $: username = $userData?.user?.username;
</script>
<header>
    <nav class=" border-gray-200 px-4 lg:px-6 py-2.5 bg-green-950">
        <div class="flex flex-wrap justify-between items-center mx-auto max-w-screen-xl">
            <div class="flex items-center">
                <a href="/">
                    <img src="/bamie_logo.svg" class="mr-3 h-6 sm:h-9" alt="Bamie Logo" />
                </a>
                <a href="/">
                    <span class="self-center text-xl font-semibold whitespace-nowrap text-white">Bamie</span>
                </a>
                <a href="https://discord.gg/XWtsKUqbMA">
                    <img src="/discord_logo.svg" class="mr-1 h-1 sm:h-9 px-3" alt="Discord Logo">
                </a>
                <a href="https://t.me/BamieAI">
                <img src="/telegram_logo.svg" class="mr-1 h-1 sm:h-9" alt="Telegram Logo">
                </a>
            </div>
            <div class="flex items-center lg:order-2">
                {#if username}
                    <div class="text-white focus:ring-4 font-medium rounded-lg text-sm px-4 lg:px-5 py-2 lg:py-2.5 mr-2 focus:outline-none focus:ring-gray-800">
                        {username}
                    </div>
                    <button on:click={() => {logout()}} class="text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-sm px-4 lg:px-5 py-2 lg:py-2.5 mr-2 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800">
                        Logout
                    </button>
                {:else}
                    <a href="/login" class="text-white  focus:ring-4 font-medium rounded-lg text-sm px-4 lg:px-5 py-2 lg:py-2.5 mr-2 hover:bg-gray-700 focus:outline-none focus:ring-gray-800">
                        Login
                    </a>
                    <a href="/signup" class="text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-sm px-4 lg:px-5 py-2 lg:py-2.5 mr-2 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800">
                        Sign up
                    </a>
                {/if}
                <!-- make this shit open slidbar for mobile having home anvas monitor about us and stuff -->
                <button on:click={() => {is_slidebar_open = true}} data-collapse-toggle="mobile-menu-2" type="button" class="inline-flex items-center p-2 ml-1 text-sm text-gray-500 rounded-lg lg:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600" aria-controls="mobile-menu-2" aria-expanded="false">
                    <span class="sr-only">Open main menu</span>
                    <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clip-rule="evenodd"></path></svg>
                    <svg class="hidden w-6 h-6" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
                </button>
                {#if is_slidebar_open === true}
                    <div class="bg-gray-800 opacity-50 w-full h-full"></div>
                    <div class="w-64 z-40 fixed overflow-y-auto top-0 bg-white shadow h-full flex-col justify-between pb-4 transition duration-150 ease-in-out">
                        <div class="px-6 h-full">
                            <div class="flex flex-col justify-between h-full w-full">
                                <div class="py-1">
                                    <div class="mb-5">
                                        <button on:click={() => {is_slidebar_open = false}} class="btn-icon variant-filled text-lg">&RightArrow;</button>
                                    </div>
                                    <div>
                                        <a href="/" class="block py-2 pr-4 pl-3 border-b   lg:border-0 lg:p-0 text-gray-400 lg:hover:text-white hover:bg-gray-700 hover:text-white lg:hover:bg-transparent border-gray-700">
                                            Home
                                        </a>
                                    </div>
                                    {#if username}
                                    <div>
                                        <a href="/canvas" class="block py-2 pr-4 pl-3 border-b   lg:border-0 lg:p-0 text-gray-400 lg:hover:text-white hover:bg-gray-700 hover:text-white lg:hover:bg-transparent border-gray-700">
                                            Canvas
                                        </a>
                                    </div>
                                    <div>
                                        <a href="/chatroom_playground" class="block py-2 pr-4 pl-3 border-b   lg:border-0 lg:p-0 text-gray-400 lg:hover:text-white hover:bg-gray-700 hover:text-white lg:hover:bg-transparent border-gray-700">
                                            Chatroom Playground
                                        </a>
                                    </div>
                                    <div>
                                        <a href="/monitor" class="block py-2 pr-4 pl-3 border-b   lg:border-0 lg:p-0 text-gray-400 lg:hover:text-white hover:bg-gray-700 hover:text-white lg:hover:bg-transparent border-gray-700">
                                            Monitor
                                        </a>
                                    </div>
                                    {/if}
                                    <div>
                                        <a href="/about-us" class="block py-2 pr-4 pl-3 border-b   lg:border-0 lg:p-0 text-gray-400 lg:hover:text-white hover:bg-gray-700 hover:text-white lg:hover:bg-transparent border-gray-700">
                                            About us
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                {/if}
            </div>
            <div class="hidden justify-between items-center w-full lg:flex lg:w-auto lg:order-1" id="mobile-menu-2">
                <ul class="flex flex-col mt-4 font-medium lg:flex-row lg:space-x-8 lg:mt-0">
                    <div>
                        <a href="/" class="block py-2 pr-4 pl-3 rounded bg-primary-700 lg:bg-transparent lg:text-primary-700 lg:p-0 text-white" aria-current="page">
                            Home
                        </a>
                    </div>
                    {#if username}
                    <div>
                        <a href="/canvas" class="block py-2 pr-4 pl-3 border-b   lg:border-0 lg:p-0 text-gray-400 lg:hover:text-white hover:bg-gray-700 hover:text-white lg:hover:bg-transparent border-gray-700">
                            Canvas
                        </a>
                    </div>
                    <div>
                        <a href="/chatroom_playground" class="block py-2 pr-4 pl-3 border-b   lg:border-0 lg:p-0 text-gray-400 lg:hover:text-white hover:bg-gray-700 hover:text-white lg:hover:bg-transparent border-gray-700">
                            Chatroom Playground
                        </a>
                    </div>
                    <div>
                        <a href="/monitor" class="block py-2 pr-4 pl-3 border-b   lg:border-0 lg:p-0 text-gray-400 lg:hover:text-white hover:bg-gray-700 hover:text-white lg:hover:bg-transparent border-gray-700">
                            Monitor
                        </a>
                    </div>
                    {/if}
                    <div>
                        <a href="/about-us" class="block py-2 pr-4 pl-3 border-b   lg:border-0 lg:p-0 text-gray-400 lg:hover:text-white hover:bg-gray-700 hover:text-white lg:hover:bg-transparent border-gray-700">
                            About us
                        </a>
                    </div>
                </ul>
            </div>
        </div>
    </nav>
</header>