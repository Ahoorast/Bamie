<script>
    import { Node, Anchor } from "svelvet";
    import pkey from "$lib/components/PKEY.svelte";
    import { createEventDispatcher } from "svelte";
    const dispatch = createEventDispatcher();
    export let id;
    export let father;
    export let position = { x, y };
    export let example_input;
    export let example_output;
    let outputs;
    function addChild() {
        dispatch("add-child");
    }
    function removeNode() {
        dispatch("remove-node");
    }
</script>

<Node id={"_" + id } bind:position={position} bind:outputs={outputs}>
    <div class="nodeWrapper">
        <div
            class="row-auto shadow-orange-400 bg-slate-500 p-1 rounded-sm bg-opacity-40"
        >
            <div class="flex flex-row mb-1.5">
                <textarea
                    bind:value={example_input}
                    type="text"
                    rows="5"
                    placeholder="User's Question "
                />
                <button
                    class="bg-green-500 w-5 h-auto shadow-md ml-0.5"
                    on:click={addChild}
                >
                    +
                </button>
            </div>
            <div class="grid justify-items-stretch">
                {#if id != 0}
                    <div class="justify-self-start">
                        <Anchor
                            edge={pkey}
                            id={"_" + id + "i"}
                            locked={true}
                            direction="west"
                            connections={[["_" + father, "_" + father + "o"]]}
                        />
                    </div>
                {/if}
                <div class="justify-self-end">
                    <Anchor
                        nodeConnect={false}
                        locked={true}
                        direction="east"
                        id={"_" + id + "o"}
                    />
                </div>
            </div>
            <div class="flex flex-row mt-1.5">
                <textarea
                    bind:value={example_output}
                    type="text"
                    rows="5"
                    placeholder="Expected Answer {id}"
                />
                <button
                    class="bg-red-500 w-5 h-auto shadow-md ml-0.5"
                    on:click={removeNode}
                >
                    x
                </button>
            </div>
        </div>
    </div>
</Node>
