<script>
    import { Node, Anchor } from "svelvet";
    import pkey from "$lib/components/PKEY.svelte";
    import { createEventDispatcher } from "svelte";
    const dispatch = createEventDispatcher();
    export let id;
    export let parent;
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
                {#if id != 0}
                <textarea
                    bind:value={example_input}
                    type="text"
                    rows="5"
                    placeholder="User's Question "
                />
                {/if}
                <button
                    class="bg-[#56860F] w-5 h-auto ml-0.5 inline-block rounded bg-success text-xs font-medium uppercase leading-normal text-white shadow-[0_4px_9px_-4px_#14a44d] transition duration-150 ease-in-out hover:bg-success-600 hover:shadow-[0_8px_9px_-4px_rgba(20,164,77,0.3),0_4px_18px_0_rgba(20,164,77,0.2)] focus:bg-success-600 focus:shadow-[0_8px_9px_-4px_rgba(20,164,77,0.3),0_4px_18px_0_rgba(20,164,77,0.2) ] focus:outline-none focus:ring-0 active:bg-success-700 active:shadow-[0_8px_9px_-4px_rgba(20,164,77,0.3),0_4px_18px_0_rgba(20,164,77,0.2)] dark:shadow-[0_4px_9px_-4px_rgba(20,164,77,0.5)] dark:hover:shadow-[0_8px_9px_-4px_rgba(20,164,77,0.2),0_4px_18px_0_rgba(20,164,77,0.1)] dark:focus:shadow-[0_8px_9px_-4px_rgba(20,164,77,0.2),0_4px_18px_0_rgba(20,164,77,0.1)] dark:active:shadow-[0_8px_9px_-4px_rgba(20,164,77,0.2),0_4px_18px_0_rgba(20,164,77,0.1)]"
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
                            connections={[["_" + parent, "_" + parent + "o"]]}
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
                    class="bg-red-700 w-5 h-auto ml-0.5 inline-block rounded bg-danger text-xs font-medium uppercase leading-normal text-white shadow-[0_4px_9px_-4px_#dc4c64] transition duration-150 ease-in-out hover:bg-danger-600 hover:shadow-[0_8px_9px_-4px_rgba(220,76,100,0.3),0_4px_18px_0_rgba(220,76,100,0.2)] focus:bg-danger-600 focus:shadow-[0_8px_9px_-4px_rgba(220,76,100,0.3),0_4px_18px_0_rgba(220,76,100,0.2)] focus:outline-none focus:ring-0 active:bg-danger-700 active:shadow-[0_8px_9px_-4px_rgba(220,76,100,0.3),0_4px_18px_0_rgba(220,76,100,0.2)] dark:shadow-[0_4px_9px_-4px_rgba(220,76,100,0.5)] dark:hover:shadow-[0_8px_9px_-4px_rgba(220,76,100,0.2),0_4px_18px_0_rgba(220,76,100,0.1)] dark:focus:shadow-[0_8px_9px_-4px_rgba(220,76,100,0.2),0_4px_18px_0_rgba(220,76,100,0.1)] dark:active:shadow-[0_8px_9px_-4px_rgba(220,76,100,0.2),0_4px_18px_0_rgba(220,76,100,0.1)]"
                    on:click={removeNode}
                >
                    x
                </button>
            </div>
        </div>
    </div>
</Node>
