<script>
    import { Node, Svelvet, ThemeToggle, Anchor } from "svelvet";
    import ResponseNode from "$lib/components/ResponseNode.svelte";
    import { failure } from "$lib/utils/toasts";
    let screenSize;
    let position_array = [
        { x: 0, y: 0 },
    ];
    let parent_array = [-1];
    let example_input_array = [""];
    let example_output_array = [""];
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
</script>   

<svelte:window bind:innerWidth={screenSize} />
<Svelvet fitView controls minimap height={760}>
    {#key parent_array}
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
    {/key}
    <ThemeToggle main="light" alt="dark" slot="toggle" />
</Svelvet>
