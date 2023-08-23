<script>
    import { Node, Svelvet, ThemeToggle, Anchor } from "svelvet";
    import ResponseNode from "$lib/components/ResponseNode.svelte";
    let screenSize;
    let position_array = [
        { x: 0, y: 0 },
        { x: 400, y: 0 },
        { x: 400, y: 400 },
        { x: 800, y: 0 },
    ];
    let parent_array = [-1, 0, 0, 1];
    let example_input_array = ["", "", "", ""];
    let example_output_array = ["", "", "", ""];
    $: console.log(position_array[0]);
    function handleAddChild(id) {
        parent_array = [...parent_array, id];
        position_array = [...position_array, {x: position_array[id].x + 400, y: position_array[id].y}];
        example_input_array = [...example_input_array, ""];
        example_output_array = [...example_output_array, ""];
    }
    function handleRemoveNode(id) {
        parent_array.splice(id, 1);
        parent_array = parent_array;
        position_array.splice(id, 1);
        position_array = position_array;
        example_input_array.splice(id, 1);
        example_input_array = example_input_array;
        example_output_array.splice(id, 1);
        example_input_array = example_input_array;
        console.log(parent_array);
    }
</script>

<svelte:window bind:innerWidth={screenSize} />
<Svelvet fitView controls minimap height={760}>
    {#each parent_array as par, indx}
        {#if indx > 0}
            <ResponseNode
                id={indx}
                father={par}
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
    <ThemeToggle main="light" alt="dark" slot="toggle" />
</Svelvet>
