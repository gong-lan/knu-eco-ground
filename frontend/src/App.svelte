<script>
  import Router from 'svelte-spa-router'
  import ComingSoon from "./routes/ComingSoon.svelte"

  const routes = {
    '/': ComingSoon,
  }
</script>

<Router {routes}/>