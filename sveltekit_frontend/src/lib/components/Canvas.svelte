<script>
    import { Node, Svelvet, ThemeToggle, Anchor } from "svelvet";
    import ResponseNode from "$lib/components/ResponseNode.svelte";
    import { update as updateCanvas } from "$lib/utils/api/guidance_tree";
    import { failure } from "$lib/utils/toasts";
    import { onMount } from "svelte";
    import WaitingButton from "./WaitingButton.svelte";
    let screenSize;
    let screenHeight;
    onMount(() => {
        screenHeight = 750;
        if (typeof window !== "undefined") {
            screenHeight = window.screen.height;
        }
    });
    export let id;
    export let owner;
    export let position_array = [
        { x: 0, y: 0 },
    ];
    export let parent_array = [-1];
    export let example_input_array = [""];
    export let example_output_array = [""];
    function handleAddChild(id) {
        parent_array = [...parent_array, id];
        position_array = [...position_array, {x: position_array[id].x + 400, y: position_array[id].y}];
        example_input_array = [...example_input_array, ""];
        example_output_array = [...example_output_array, ""];
    }
    function handleRemoveNode(id) {
        let children = parent_array.filter((par) => par === id);
        if (children.length > 0) {
            //failure("can't remove a node that has more than one child");
            return;
        }
        parent_array.splice(id, 1);
        for (let i = 0; i < parent_array.length; i++) {
            if (parent_array[i] > id) {
                parent_array[i] -= 1;
            }
        }
        parent_array = parent_array;
        position_array.splice(id, 1);
        position_array = position_array;
        example_input_array.splice(id, 1);
        example_input_array = example_input_array;
        example_output_array.splice(id, 1);
        example_input_array = example_input_array;
    }
    let update_promise;
    function handleSave() {
        update_promise = updateCanvas({
            id: id,
            owner: owner,
            position_array: position_array,
            parent_array: parent_array,
            example_input_array: example_input_array,
            example_output_array: example_output_array,
        });
    }
</script>   

<svelte:window bind:innerWidth={screenSize} />
<Svelvet fitView controls minimap height={screenHeight}>
    {#key parent_array}
        {#each parent_array as par, indx}
            {#if indx > 0}
                <ResponseNode
                    id={indx}
                    parent={par}
                    bind:position={position_array[indx]}
                    bind:example_input={example_input_array[indx]}
                    bind:example_output={example_output_array[indx]}
                    on:add-child={() => handleAddChild(indx)}
                    on:remove-node={() => handleRemoveNode(indx)}
                />
            {:else}
                <ResponseNode
                    id={indx}
                    bind:position={position_array[indx]}
                    bind:example_input={example_input_array[indx]}
                    bind:example_output={example_output_array[indx]}
                    on:add-child={() => handleAddChild(indx)}
                />
            {/if}
        {/each}
    {/key}
    <ThemeToggle main="light" alt="dark" slot="toggle" />
</Svelvet>

{#await update_promise}
<WaitingButton/>
{:then}
<button type="button" on:click={handleSave} class="btn variant-filled m-2">save</button>
{/await}