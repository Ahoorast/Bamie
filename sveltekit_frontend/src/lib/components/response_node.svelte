<script>
    import { draggable } from '@neodrag/svelte';
    export let position = {
    x : 0,
    y : 0,
};
</script>

<div  use:draggable={{ position: position, bounds: 'parent' }}
class="w-5 h-5 bg-gray-100 border border-gray-500 rounded-md">
    yo turns out we had a secret wepon
</div>
