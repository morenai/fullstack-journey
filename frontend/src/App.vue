<script setup>
import { RouterView } from 'vue-router'
</script>

<template>
  <nav>
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/guests">Guests</RouterLink>
  </nav>
  <RouterView />
</template>

<style scoped>
nav {
  display: flex;
  gap: 16px;
  padding: 16px;
  background: #1a1a2e;
}

nav a {
  color: #32707c;
  text-decoration: none;
  font-weight: 600;
}

nav a:hover {
  color: #fff;
}
</style>