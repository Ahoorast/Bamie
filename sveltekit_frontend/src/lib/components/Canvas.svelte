<script>
    import { Node, Svelvet, ThemeToggle, Anchor } from "svelvet";
        import ResponseNode from "$lib/components/ResponseNode.svelte";
    let screenSize;
    let position1 = {x: 0, y: 0};
    let position2 = {x: 400, y: 400};
    let position3 = {x: 800, y: 800};
    let position4 = {x: 0, y: 800};
</script>

<svelte:window bind:innerWidth={screenSize} />
<p>{position1.x} + {position1.y}</p>
<Svelvet fitView controls minimap height={760}>
    <ResponseNode id = {1} position={position1}/>
    <ResponseNode id = {2} father = {1} position={position2} />
    <ResponseNode id = {3} father = {1} position={position3} />
    <ResponseNode id = {4} father = {2} position={position4} />
    <ThemeToggle main="light" alt="dark" slot="toggle" />
</Svelvet>
