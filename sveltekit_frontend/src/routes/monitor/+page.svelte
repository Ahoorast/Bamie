<script>
    import { list as listChatrooms } from "$lib/utils/api/chatroom";
    import { Table } from '@skeletonlabs/skeleton';
    import { tableMapperValues } from '@skeletonlabs/skeleton';
    import { onMount } from "svelte";
    import { goto } from '$app/navigation';
    let chatroom_list = [];
    let table_rows = [];
    let tableSource = {
        head: ['Id', 'Client', 'Request', 'Suggested Response'],
        body: tableMapperValues(chatroom_list, ['id', 'client']),
    };
    onMount(async () => {
        chatroom_list = await listChatrooms();
        table_rows = chatroom_list.map((chatroom) => {
            const last_recieved_message = chatroom.recieved_messages[chatroom.recieved_messages.length - 1];
            const last_suggested_message = chatroom.suggested_messages[chatroom.suggested_messages.length - 1];
            const last_recieved_messages_timestamp = chatroom.recieved_messages_timestamp[chatroom.recieved_messages_timestamp.length - 1];
            return {
                id: chatroom.id,
                client: chatroom.client,
                last_recieved_message: last_recieved_message,
                last_suggested_message: last_suggested_message,
                last_recieved_messages_timestamp: last_recieved_messages_timestamp,
            };
        });
        tableSource = {
            head: ['Id', 'Client', 'Request', 'Suggested Response', 'Request Timestamp'],
            // The data visibly shown in your table body UI.
            body: tableMapperValues(table_rows, ['id', 'client', 'last_recieved_message', 'last_suggested_message', 'last_recieved_messages_timestamp']),
            // Optional: The data returned when interactive is enabled and a row is clicked.
            meta: tableMapperValues(table_rows, ['id']),
            // Optional: A list of footer labels.
            // foot: ['Total', '', '<code class="code">5</code>']
        };
    });
    function handleClick(e) {
        const id = e.detail[0];
        goto(`/monitor/${id}/`);
    }
</script>

{#key table_rows}
<Table source={tableSource} interactive={true} on:selected={handleClick}/>
{/key}