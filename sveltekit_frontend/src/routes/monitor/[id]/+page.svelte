<script>
    import { onMount } from 'svelte';
    import { detail as chatroomDetail, push_message } from "$lib/utils/api/chatroom";
    import WaitingButton from '$lib/components/WaitingButton.svelte';
    /** @type {import('./$types').PageData} */
    export let data;
    
    let messages = [];
    let suggested_message = "";
    let chatroom = [];
    function parseMessages(chatroom) {
        messages = [];
        for (let i = 0; i < chatroom.recieved_messages.length; i++) {
            messages.push({
                message: chatroom.recieved_messages[i],
                client: true,
                timestamp: chatroom.recieved_messages_timestamp[i],
            });
        }
        for (let i = 0; i < chatroom.sent_messages.length; i++) {
            messages.push({
                message: chatroom.sent_messages[i],
                client: false,
                timestamp: chatroom.sent_messages_timestamp[i],
            });
        }
        messages.sort((a, b) => (a.timestamp < b.timestamp? -1: +1));
    }
    $: {
        if (chatroom?.length > 0) {
            parseMessages(chatroom);
        }
    }
    let push_message_promise;
    async function handleMessageSend() {
        push_message_promise = await push_message({
            chatroom_id: data.id,
            message: suggested_message,
            type: 'sent',
        });
        chatroom = push_message_promise;
        messages = [...messages, {
            message: suggested_message,
            client: false,
            timestamp: (new Date()).toString(),
        }];
        suggested_message = chatroom.suggested_messages[chatroom.suggested_messages.length - 1]; 
    }
    onMount(async () => {
        chatroom = await chatroomDetail(data.id);
        parseMessages(chatroom);
        suggested_message = chatroom.suggested_messages[chatroom.suggested_messages.length - 1];
    });
</script>

<div class="flex flex-col items-center justify-center px-6 py-8 mt-3 mx-auto lg:py-0">
    <div class="w-full bg-white rounded-lg shadow md:mt-0 max-w-4xl xl:p-0 gap-y-4 max-h-screen overflow-auto">
        <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
            {#key messages}
            {#each messages as message}
            {#if message.client}
            <div class="grid grid-cols-[1fr_auto] gap-2">
                <div class="card p-4 rounded-tr-none space-y-2">
                    <header class="flex justify-between items-center">
                        <p class="font-bold">{chatroom.client}</p>
                        <small class="opacity-50">{message.timestamp}</small>
                    </header>
                    <p>{message.message}</p>
                </div>
            </div>
            {:else} 
            <div class="grid grid-cols-[auto_1fr] gap-2">
                <div class="card p-4 variant-soft rounded-tl-none space-y-2">
                    <header class="flex justify-between items-center">
                        <p class="font-bold">support</p>
                        <small class="opacity-50">{message.timestamp}</small>
                    </header>
                    <p>{message.message}</p>
                </div>
            </div>
            {/if}
            {/each}
            {/key}
        </div>
    </div>
</div>
<div class="flex flex-col items-center justify-center mt-3 mx-auto lg:py-0">
    <div class="w-full bg-white rounded-lg shadow md:mt-0 max-w-4xl xl:p-0 gap-y-4">
        <div class="space-y-4 md:space-y-6 sm:p-8">
            <div class="flex flex-col items-center justify-center px-6 py-8 mt-3 mx-auto lg:py-0">
                <div class="input-group input-group-divider grid-cols-[auto_1fr_auto] rounded-container-token">
                    <button class="input-group-shim">+</button>
                    <textarea
                    bind:value={suggested_message}
                    class="bg-transparent border-0 ring-0"
                    name="prompt"
                    id="prompt"
                    placeholder="Write a message..."
                    rows="4"
                    />
                    {#await push_message_promise}
                    <WaitingButton/>
                    {:then}
                    <button on:click={handleMessageSend} class="variant-filled-primary" type="button">Send</button>
                    {/await}
                </div>
            </div>
        </div>
    </div>
</div>