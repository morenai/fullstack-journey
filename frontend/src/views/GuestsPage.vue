<script setup>
import { ref, onMounted } from 'vue'

const guests = ref([])
const loading = ref(true)

onMounted(async () => {
  const res = await fetch('http://127.0.0.1:8000/guests')
  guests.value = await res.json()
  loading.value = false
})
</script>

<template>
  <div class="guests">
    <h1>🏨 Guest List</h1>

    <p v-if="loading">Loading guests...</p>

    <div v-else>
      <p v-if="guests.length === 0">No guests yet.</p>

      <div v-for="guest in guests" :key="guest.id" class="guest-card">
        <h3>{{ guest.name }}</h3>
        <p>Room: {{ guest.room }} — {{ guest.room_type }}</p>
        <p>Status: {{ guest.checked_in ? 'Checked in' : 'Not checked in' }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.guests {
  padding: 32px;
}
.guest-card {
  background: #f5f5f5;
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 12px;
}
h3 {
  margin: 0 0 8px;
  color: #1a1a2e;
}
p {
  margin: 4px 0;
  color: #555;
}
</style>