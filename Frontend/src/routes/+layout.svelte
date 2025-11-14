<script>
	import favicon from '$lib/assets/favicon.svg';
	import { isLoading } from 'svelte-i18n';
	import '../lib/i18n.js';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

{#if $isLoading}
	<div style="display: flex; justify-content: center; align-items: center; height: 100vh; font-family: Arial, sans-serif;">
		Cargando...
	</div>
{:else}
	{@render children?.()}
{/if}
