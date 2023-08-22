<script>
    export let data;
    import ResponseNode from "$lib/components/ResponseNode.svelte";
    let position_1 = {
        x : 0,
        y : 0,
    };
    let position_2 = {
        x : 5,
        y : 5,
    };
</script>

<ResponseNode position = {position_1}/>
<ResponseNode position = {position_2}/>