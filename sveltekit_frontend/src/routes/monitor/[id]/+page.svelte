<script>
  import { onMount } from 'svelte';

    /** @type {import('./$types').PageData} */
    export let data;
    let messages = [];
    let suggested_message = "";
    function parseMessages() {
        for (let i = 0; i < data.recieved_messages.length; i++) {
            messages.push({
                message: data.recieved_messages[i],
                client: true,
                timestamp: data.recieved_messages_timestamp[i],
            });
        }
        for (let i = 0; i < data.sent_messages.length; i++) {
            messages.push({
                message: data.sent_messages[i],
                client: false,
                timestamp: data.sent_messages_timestamp[i],
            });
        }
        messages.sort((a, b) => (a.timestamp < b.timestamp? -1: +1));
    }
    $: {
        parseMessages();
    }
    onMount(async () => {
        await data;
        parseMessages();
        suggested_message = data.suggested_messages[data.suggested_messages.length - 1];
    });
    $: console.log(messages);
</script>

{#key messages}
{#each messages as message}
    {#if message.client}
    <div class="grid grid-cols-[1fr_auto] gap-2">
        <div class="card p-4 rounded-tr-none space-y-2">
            <header class="flex justify-between items-center">
                <p class="font-bold">{data.client}</p>
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
	<button class="variant-filled-primary" type="button">Send</button>
</div>

