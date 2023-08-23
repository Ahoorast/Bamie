<script>
    import { Node, Svelvet, ThemeToggle, Anchor } from "svelvet";
    import ResponseNode from "$lib/components/ResponseNode.svelte";
    let screenSize;
    let position_array = [{x: 0, y: 0},
                          {x: 400, y: 400},
                          {x: 800, y: 800},
                          {x: 0, y: 800}];
    let parent_array = [-1, 0, 0, 1];
    let example_input_array = ["", "", "", ""];
    let example_output_array = ["", "", "", ""];
    function handleAddChild(id) {

    }
    function handleRemoveChild(id) {
        
    }
</script>

<svelte:window bind:innerWidth={screenSize} />
<Svelvet fitView controls minimap height={760}>
    {#each parent_array as par, indx}
        <ResponseNode id={indx} father={par} 
        bind:position={position_array[indx]}
        bind:example_input={example_input_array[indx]}
        bind:example_output={example_output_array[indx]}
        on:add-child={()=> handleAddChild(indx)}
        on:remove-child={()=> handleRemoveChild(indx)}
        />
    {/each}
    <ThemeToggle main="light" alt="dark" slot="toggle" />
</Svelvet>
