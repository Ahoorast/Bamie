<script>
    import Canvas from "$lib/components/Canvas.svelte";
    import { retrieve as retrieveCanvas, update as updateCanvas } from "$lib/utils/api/guidance_tree";
    import { onMount } from "svelte";
    let canvas_data = {
        id: -1,
        position_array: [{ x: 0, y: 0 }], 
        parent_array: [-1],
        example_input_array: [""],
        example_output_array: [""],
    }
    onMount(async () => {
        const response = await retrieveCanvas();
        canvas_data = response;
    });
</script>

<Canvas 
    id={canvas_data.id}
    owner={canvas_data.owner}
    position_array={canvas_data.position_array}
    parent_array={canvas_data.parent_array}
    example_input_array={canvas_data.example_input_array}
    example_output_array={canvas_data.example_output_array}
/>
